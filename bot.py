import os
import telebot
from telebot import types
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start', 'menu'])
def start_handler(message):


    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="зміна розкладу", callback_data='task')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton(text="новий клієнт", callback_data='new_client')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton(text="список на сьогодні", callback_data='today')
    markup.row(btn3)
    btn4 = types.InlineKeyboardButton(text="знайти клієнта", callback_data='client')
    markup.row(btn4)
    btn5 = types.InlineKeyboardButton(text="Прайс", callback_data='price')
    markup.row(btn5)

    bot.send_message(
        message.chat.id,
        f"Привіт {message.chat.first_name} {message.chat.last_name}, натисни кнопку!",
        reply_markup=markup
    )


@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
