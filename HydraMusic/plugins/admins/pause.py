from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from HydraMusic import app
from HydraMusic.core.call import Hydra
from HydraMusic.utils.database import is_music_playing, music_off
from HydraMusic.utils.decorators import AdminRightsCheck
from strings import get_command

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(
    filters.command(PAUSE_COMMAND) & filters.group & ~filters.edited & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Hydra.pause_stream(chat_id)
    await message.reply_text(_["admin_2"].format(message.from_user.mention))
