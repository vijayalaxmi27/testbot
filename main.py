import telebot
from bardapi import Bard
import os
import json

os.environ['_BARD_API_KEY']="Wgh1-Q4dgayAkpOp3gRSKOObp5YuDAJ4dGZV2Erik6Q5K3sP_Ei2gXQfH0HeCClnGHIcqQ."

API_TOKEN = '5666879763:AAErm3K6VF56y7PCDlW2cjslyfN0r3dKM98'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'hello', 'hi'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    
@bot.message_handler(func=lambda msg: True)
def get_query(message):
  quest = message.text
  response = Bard().get_answer(quest)['content']
  bot.send_message(message.chat.id, response)

bot.infinity_polling()
