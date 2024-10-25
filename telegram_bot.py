from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final ='Enter yout token here'
Bot_USERNAME: Final ='@faceDGod_bot'

#Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Yo! Thanks for chatting. Im the faceDGod bot.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Yo! Type something so I can help you out!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Yo! This is a custom command.')
#Responses

def handle_response(text:str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey There!'
        
    if 'how are you' in processed:
        return 'I am good'


