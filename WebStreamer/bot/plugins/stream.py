

from pyrogram import filters
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot
from pyrogram.types.messages_and_media import message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

def detect_type(m: Message):
    if m.document:
        return m.document
    elif m.video:
        return m.video
    elif m.audio:
        return m.audio
    else:
        return
    

@StreamBot.on_message(filters.private & (filters.document | filters.video | filters.audio), group=4)
async def media_receive_handler(_, m: Message):
    file = detect_type(m)
    file_name = ''
    if file:
        file_name = file.file_name
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    stream_link = Var.URL + str(log_msg.message_id) + '/' +quote_plus(file_name) if file_name else ''
    await m.reply_photo(
        photo="https://telegra.ph/file/9bdbff69e26b370e392e6.jpg",
        caption=f" <b><u>𝗬𝗼𝘂𝗿 𝗹𝗶𝗻𝗸 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱! 👍</u></b>\n\n<b><u>𝗪𝗮𝘁𝗰𝗵 𝗢𝗻𝗹𝗶𝗻𝗲 👇</u></b>\n\nhttps://stream.url2go.in/st?api=af5e38dfaf8b900b45335173d279b44d7ae4b2e9&url={stream_link}\n\n📝<b><u> 𝗡𝗢𝗧𝗘 </u></b>:\t𝑳𝑰𝑵𝑲 𝑾𝑶𝑵'𝑻 𝑬𝑿𝑷𝑰𝑹𝑬 𝑻𝑰𝑳𝑳 𝑰 𝑫𝑬𝑳𝑬𝑻𝑬\n\n🍃 Bᴏᴛ Made Bʏ : @MD_OWNER\n\n┈┈┈••✿ @MD_BOTZ ✿••┈┈┈",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
             [
              InlineKeyboardButton("📥 𝔻𝕆𝕎ℕ𝕃𝕆𝔸𝔻 📥", url=stream_link),
              InlineKeyboardButton('🍬 ℙℝ𝕆𝕁𝔼ℂ𝕋 🍬', url='tg://resolve?domain=MD_BOTZ')
             ]
            ]
        ),
    )
