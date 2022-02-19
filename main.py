from constants import TELEGRAM_TOKEN, MAX_INPUT
from utils.compute_primel_cache import compute_primel_cache
from commands.start import start
from commands.primel import primel
from commands.unknown import unknown

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

def main():
    compute_primel_cache(MAX_INPUT + 1)
    logging.basicConfig(format = '%(asctime)s - %(message)s', level = logging.INFO)
    updater = Updater(token = TELEGRAM_TOKEN, use_context = True)

    start_handler = CommandHandler('start', start)
    updater.dispatcher.add_handler(start_handler)
    primel_handler = CommandHandler('primel', primel)
    updater.dispatcher.add_handler(primel_handler)
    unknown_handler = MessageHandler(Filters.command, unknown)
    updater.dispatcher.add_handler(unknown_handler)

    updater.start_polling()

if __name__ == "__main__":
    main()