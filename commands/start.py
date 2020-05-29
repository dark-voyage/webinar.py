from core import bot


def _start():
    @bot.message_handler(commands=['start'])
    def __start(message):
        text = \
            "<b>Bizning botimizga xush kelibsiz!</b> \n" \
            f"<i>Hurmatli {message.message_from.first_name}, sizni ko'rib turganimizdan mamnunmiz!"
        bot.reply_to(message, text, parse_mode="HTML")
        print(message)
    pass
