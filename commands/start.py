from core import bot


def _start():
    @bot.message_handler(commands=['start'])
    def __start(message):
        bot.reply_to(message, "Habar qabul qilindi!")
        print(message)

    pass
