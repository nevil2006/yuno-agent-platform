import telebot
import requests
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def reply(message):

    user_text = message.text

    response = requests.post(
        "http://127.0.0.1:8000/multi-agent",
        params={
            "query": user_text
        }
    )

    data = response.json()

    bot.reply_to(
        message,
        data["summary"]
    )


print("Bot running...")

bot.infinity_polling()