from telegram.ext import CallbackContext
from telegram import Update
import logging

def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = "Hi, I'm Primey! Use the command /primel to check whether your guess is valid in Primel."
    
    logging.log(level = logging.INFO, msg = f"Chat ID: '{chat_id}', Logged Message: '{text}'")
    context.bot.send_message(chat_id, text)