# Don't Remove Credit @Spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @Spideyofficial_777
# Ask Doubt on telegram @hacker_x_official_777

# Clone Code Credit : YT - @Spidey_official_777 / TG - @hacker_x_official_777/ GitHub - @Spideyofficial777

from pyrogram import Client, filters

@Client.on_message(filters.command("stickerid") & filters.private)
async def stickerid(bot, message):
    s_msg = await bot.ask(chat_id = message.from_user.id, text = "Now Send Me Your Sticker")
    if s_msg.sticker:
        await s_msg.reply_text(f"**Sticker ID is**  \n `{s_msg.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{s_msg.sticker.file_unique_id}`")
    else: 
        await s_msg.reply_text("Oops !! Not a sticker file")
