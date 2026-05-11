import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Твои три крутые песни
songs = {
    "petlyura": {
        "url": "http://tmpfiles.org/dl/11693421/petlyura_-_gitara_semistrunnaya_48105061.mp3",
        "title": "Юрий Петлюра – Гитара семиструнная",
        "performer": "Юрий Петлюра"
    },
    "nirvana": {
        "url": "http://tmpfiles.org/dl/11704971/nirvana_-_something_in_the_way_47829460.mp3",
        "title": "Nirvana – Something In The Way",
        "performer": "Nirvana"
    },
    "imagine": {
        "url": "http://tmpfiles.org/dl/11705288/imagine_dragons_-_bones_73949726.mp3",
        "title": "Imagine Dragons – Bones",
        "performer": "Imagine Dragons"
    }
}

def main_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🎸 Юрий Петлюра – Гитара семиструнная", callback_data="petlyura"),
        InlineKeyboardButton("🎸 Nirvana – Something In The Way", callback_data="nirvana"),
        InlineKeyboardButton("🔥 Imagine Dragons – Bones", callback_data="imagine")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🎧 *Welcome to LoveBEnglish Bot!*\n\n"
        "This is my English project 2025 🎉\n"
        "Choose and download your favorite song for free:",
        parse_mode="Markdown",
        reply_markup=main_keyboard()
    )

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data in songs:
        song = songs[call.data]
        bot.send_audio(
            chat_id=call.message.chat.id,
            audio=song["url"],
            title=song["title"],
            performer=song["performer"]
        )
        bot.answer_callback_query(call.id, "Downloading…")

print("LoveBEnglish_bot успешно запущен! 3 песни готовы!")
bot.polling(none_stop=True)
