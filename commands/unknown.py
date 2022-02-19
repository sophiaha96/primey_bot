from telegram.ext import CallbackContext
from telegram import Update
import logging

def unknown(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = "Sorry, I didn't understand that command."
    
    logging.log(level = logging.INFO, msg = f"Chat ID: '{chat_id}', Logged Message: '{text}'")
    context.bot.send_message(chat_id, text)