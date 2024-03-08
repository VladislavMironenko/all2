import telebot
from bott import get_first_news , get_first_news_1


token = '6167770624:AAFsFS4fHZS6JsWYsa4Q86NGP2RSgJfsmXE'
channel_id = '@ukrinfo123'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def func(message):
    bot.send_message(channel_id , message.text)

bot.polling()