import telebot
import config


bot = telebot.TeleBot(config.token)


def launch():
    bot.polling(none_stop=True)
