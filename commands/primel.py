from constants import MAX_DIGITS
from utils.compute_primel_cache import primel_cache
from utils.parse_input import parse_input

from telegram.ext import CallbackContext
from telegram import Update
import logging

def primel(update: Update, context: CallbackContext):
    primel_input = parse_input(context.args)
    padded_primel_input = f'{primel_input:0{MAX_DIGITS}}'
    is_valid_primel = primel_input in primel_cache

    if primel_input == -1:
        text = "Invalid entry. Please input a positive, five-digit integer as your Primel guess."

    elif not is_valid_primel:
        closest_prime = min(primel_cache, key = lambda x: abs(x - primel_input))
        padded_closest_prime = f'{closest_prime:05}'
        text = f"{padded_primel_input} is not a valid Primel guess.\nThe next closest prime number is: `{padded_closest_prime}`."

    else:
        text = f"`{padded_primel_input}` is a valid Primel guess!"

    chat_id = update.effective_chat.id
    log_message = text.replace('\n', ' ').replace('`', '')
    
    logging.log(level = logging.INFO, msg = f"Chat ID: '{chat_id}', Logged Message: '{log_message}'")
    context.bot.send_message(chat_id, text, parse_mode = 'Markdown')