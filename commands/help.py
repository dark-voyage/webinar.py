from core import bot


def _help():
    @bot.message_handler(commands=['help'])
    def __help(message):
        bot.reply_to(message, "Habar qabul qilindi!")
        print(message)
    pass
