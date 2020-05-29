from core import bot


def _start():
    @bot.message_handler(commands=['start'])
    def __start(message):
        text = \
            "<b>Bizning botimizga xush kelibsiz!</b> \n" \
            f"<i>Hurmatli {message.from_user.first_name}, sizni ko'rib turganimizdan mamnunmiz!</i>"
        bot.reply_to(message, text, parse_mode="HTML")
        print(message)
    pass
