from telebot import types
import telebot
import random
from translate import *
import json


# with open(r"/bot_alpa_0_3/data_base.json", "r") as db:
#     contacts = json.load(db)


API = "7284552120:AAFURt9NuH_7f52Tv_dhaHb_bJ2VLtlzf_A"
translate_lang = Translator(from_lang="Russian", to_lang="English")
hello_list = ["ОЙ, приветик красотка😍", "Йоу. братуха"]
bot = telebot.TeleBot(API)


# команда старт
@bot.message_handler(commands=["start"])
def start(message):
    num = round(random.uniform(0, len(hello_list)-1))
    # kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # button1 = types.KeyboardButton("Отдать свою душу", request_contact=True)
    # button2 = types.KeyboardButton("Не отдать свою душу", request_contact=True)
    # kb.add(button1, button2)
    bot.send_message(message.chat.id, hello_list[num]) #, reply_markup=kb)


# # БАЗА ДАННЫХ
# @bot.message_handler(content_types=["contact"])
# def contact_steal(message):
#     data = {
#         "chat_id": message.chat.id,
#         "user_id": message.from_user.id,
#         "first_name": message.from_user.first_name,
#         "username": message.from_user.username,
#         "phone_number": message.contact.phone_number
#     }
#     if data not in contacts:
#         contacts.append(data)
#     with open(r"C:\Users\badyk\PycharmProjects\pythonProject\bot_alpa_0_3\data_base.json", "w") as db:
#         json.dump(contacts, db)
#
#
# @bot.message_handler(commands=["world"])
# def world(message):
#     if message.chat.id == 1222621403:
#         for contact in contacts:
#             a = contact["chat_id"]
#             bot.send_message(a, 'РАСПРОДАЖА ПРЯМО ВОН ТАМ!!, СРОЧНО ПЕРЕХОДИ ПО ССЫЛКЕ И ЛУТАЙ БОНУСЫ https://www.youtube.com/watch?v=dQw4w9WgXcQ')
#     else:
#         bot.send_message(message.chat.id, "ИШ КУДОЙ ПАЛЕЗ, СОРВАНЕЦ, НЕДОУМОК")

# Переводчик сообщения


@bot.message_handler(commands=["translate"])
def translator(message):
    send = bot.send_message(message.chat.id, "Введите текст для перевода")
    bot.register_next_step_handler(send, transl)


def transl(message):
    message_text = message.text
    try:
        go = translate_lang.translate(message_text)
        bot.send_message(message.chat.id, go)
    except:
        alf = bot.send_message(message.chat.id,"Не точный текст перевода, повторите попытку")
        bot.register_next_step_handler(alf, transl)


bot.polling()
