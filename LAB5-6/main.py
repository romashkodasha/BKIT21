import os

import telebot
from telebot import types

import config
from dbworker import *
import random

# Создание бота
bot = telebot.TeleBot(config.TOKEN)

# путь к текущему каталогу
cur_path = os.path.dirname(os.path.abspath(__file__))

def find_path(a, b, c):
    if a=="Длинные": res='0'
    else: res='1'
    if b=="Яркие": res+='0'
    else: res+='1'
    if c=="С дизайном": res+='0'
    else: res+='1'
    path = "C:/Users/ASUS/PycharmProjects/Lab5/%s"%res
    return path


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    ans = "Даа"
    markup.add(ans)
    bot.send_message(message.chat.id,"Йоу! Я бот by d_romashhh, давай посоветую тебе💅 Ты готова?",reply_markup=markup)
    set(make_key(message.chat.id, config.CURRENT_STATE),config.States.STATE_FIRST.value)


@bot.message_handler(commands=["restart"])
def start(message):
    bot.send_message(message.chat.id,"Произошел перезапуск")
    set(make_key(message.chat.id, config.CURRENT_STATE),config.States.STATE_FIRST.value)

@bot.message_handler(func=lambda message:get(make_key(message.chat.id,config.CURRENT_STATE))==config.States.STATE_FIRST.value)
def state_first(message): #message- хранит информацию введенную пользователем
    text=message.text
    markup=types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True) #то что выводятся кнопки
    but1=types.KeyboardButton("Короткие")
    but2 = types.KeyboardButton("Длинные")
    markup.add(but1,but2)
    bot.send_message(message.chat.id,"Для начала выбери длину ногтей💃",reply_markup=markup)
    #markup = types.ReplyKeyboardRemove(selective=False)
    #bot.send_message(message.chat.id, "Первый выводимый текст", reply_markup=markup)
    set(make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_SECOND.value)#переход в следующее состояние по ключу

@bot.message_handler(func=lambda message:get(make_key(message.chat.id,config.CURRENT_STATE))==config.States.STATE_SECOND.value)
def state_second(message): #message- хранит информацию введенную пользователем
    text=message.text
    set(make_key(message.chat.id, config.States.STATE_FIRST), text)
    markup=types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True) #то что выводятся кнопки
    but1=types.KeyboardButton("Нюдовые")
    but2 = types.KeyboardButton("Яркие")
    markup.add(but1,but2)
    bot.send_message(message.chat.id,"Теперь выбери стиль😎",reply_markup=markup)
    #markup = types.ReplyKeyboardRemove(selective=False)
    #bot.send_message(message.chat.id, "Пр", reply_markup=markup)
    set(make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_THIRD.value)


@bot.message_handler(func=lambda message:get(make_key(message.chat.id,config.CURRENT_STATE))==config.States.STATE_THIRD.value)
def state_third(message): #message- хранит информацию введенную пользователем
    text=message.text
    set(make_key(message.chat.id, config.States.STATE_SECOND), text)
    markup=types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True) #то что выводятся кнопки
    but1=types.KeyboardButton("С дизайном")
    but2 = types.KeyboardButton("Без дизайна")
    markup.add(but1,but2)
    bot.send_message(message.chat.id,"И последний вопрос❤",reply_markup=markup)
    set(make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_OPERATION.value)


@bot.message_handler(func=lambda message:get(make_key(message.chat.id,config.CURRENT_STATE))==config.States.STATE_OPERATION.value)
def state_operation(message): #message- хранит информацию введенную пользователем
    design=message.text
    length=get(make_key(message.chat.id,config.States.STATE_FIRST))
    bright = get(make_key(message.chat.id, config.States.STATE_SECOND))
    path=find_path(length, bright, design)
    photo = open(path+"/" + random.choice(os.listdir(path)), 'rb')
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, "Надеюсь тебе понравилось🌼",reply_markup=markup)
    set(make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_FIRST.value)
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    ans = "Даа"
    markup.add(ans)
    bot.send_message(message.chat.id, "Йоу! Я бот by d_romashhh, давай посоветую тебе💅 Ты готова?", reply_markup=markup)


if __name__ == '__main__':
    bot.infinity_polling() #зацикливает бот и вызывает его отдельно для каждого пользователя