from google.cloud import storage
from telegram.ext import Dispatcher, CommandHandler, Filters, MessageHandler
from telegram import Update, Bot
from random import choices, randint
from time import sleep
import os

def start(bot, update):
    update.message.reply_text("Bot de teste do @Renangmc0504", quote=False)


def chatID(bot, update):
    nome = update.message.from_user
    nome = nome.first_name
    chat_id = update.message.chat_id
    update.message.reply_text(f"Chat ID: '{chat_id}'", quote=False)

def horario(bot, update):

    agora = datetime.datetime.now()
    hora_atual_formatada = agora.strftime("%H:%M:%S")
    update.message.reply_text(f"Horário atual: {hora_atual_formatada}", quote = False)

                         
def webhook(request):
    bot = Bot(token=os.environ["TELEGRAM_TOKEN"])
    
    dispatcher = Dispatcher(bot, None, 0)

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('panca', panca))
    dispatcher.add_handler(CommandHandler('id', chatID))

    if request.method == 'POST':
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return 'ok'