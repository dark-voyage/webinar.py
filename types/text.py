from core import bot
from config import confession


def _text():
    @bot.message_handler(content_types=['text'])
    def __text(message):
        bot.send_message(confession, message.text)
    pass

