from constants import MAX_DIGITS
from utils.compute_primel_cache import primel_cache
from utils.parse_input import parse_input

from telegram.ext import CallbackContext
from telegram import Update
import logging

def primel(update: Update, context: CallbackContext):
    primel_input = parse_input(context.args)
    is_valid_primel = primel_input in primel_cache

    if primel_input == -1:
        text = f"Invalid Primel Entry.\nPlease input a positive, {MAX_DIGITS}-digit integer with no leading 0s. For example, the first valid Primel number is: `10007`"

    elif not is_valid_primel:
        closest_prime = min(primel_cache, key = lambda x: abs(x - primel_input))
        primel_input = f'{primel_input:0{MAX_DIGITS}}'
        text = f"{primel_input} is not a valid Primel guess.\nThe next closest, valid Primel number is: `{closest_prime}`."

    else:
        text = f"`{primel_input}` is a valid guess in Primel! ✨"

    chat_id = update.effective_chat.id
    log_message = text.replace('\n', ' ').replace('`', '')
    logging.log(level = logging.INFO, msg = f"Chat ID: '{chat_id}', Logged Message: '{log_message}'")
    context.bot.send_message(chat_id, text, parse_mode = 'Markdown')