import telebot
import requests
import json
from ioconverter import IOConverter
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_reply(message: telebot.types.Message):
    text = 'Привет! Я - бот, который переводит из одной валюты в другую\n'
    text += IOConverter.get_help()
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def help_reply(message: telebot.types.Message):
    bot.reply_to(message, IOConverter.get_help())


@bot.message_handler(commands=['list'])
def list_reply(message: telebot.types.Message):
    bot.reply_to(message, IOConverter.get_list())


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        text = IOConverter.convert(message.text)
    except Exception as e:
        text = e
    bot.send_message(message.chat.id, text)


bot.polling()
