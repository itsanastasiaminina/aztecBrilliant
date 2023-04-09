import os
import telebot
from dotenv import load_dotenv

from main import start_generate


load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Hello, enter command /generate {arg}\narg - is the number of "
                                               "iterations")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "/generate {arg} - generate dimond img\narg - is the number of "
                                               "iterations")
    elif message.text.split()[0] == "/generate":
        start_generate(int(message.text.split()[1]), message.from_user.id)
        bot.send_message(message.from_user.id, "start generate")
        bot.send_message(message.from_user.id, "generate...")
        photo = open('images/save_image' + str(message.from_user.id) + '.JPG', 'rb')
        bot.send_photo(message.from_user.id, photo)
        os.remove('images/save_image' + str(message.from_user.id) + '.JPG')
    else:
        bot.send_message(message.from_user.id, "error message")


bot.polling(none_stop=True, interval=0)
