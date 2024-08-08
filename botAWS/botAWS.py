import json
import os
import logging
from os.path import join, dirname
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler,MessageHandler, filters, ContextTypes
import asyncio




# Carregar o nosso TOKEN - boa prática
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
TOKEN = os.environ.get("TOKEN")
# Configurar o Logging, irá ajudar
# quando o bot tiver rodando no lambda
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)




## Funções para TELEGRAM:

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
	name = update.message.from_user.first_name
	await update.message.reply_text(f"Olá, eu sou um bot! Como posso te ajudar, {name}?")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text("Esse comando não existe.")
	
	
## Fim das funções


# Quando subimos a aplicação no lambda
# a função é chamada VÁRIAS vezes, então temos um problema:
# se a aplicação for inicializada como fazemos com run_polling(),
# o lambda irá tentar inicializar NOVAMENTE uma aplicação
# inicializada, isso dá B.O. Para contornar isso, em um primeiro
# definimos que a aplicação não está inicializada.
application = None
async def initialize_application():
	global application
# essa verificação é vital para contornar o problema anterior
# se a aplicação não foi inicializada, inicialize sentando nossos
# comandos .
# caso for, pule.
	if application is None:
		application = ApplicationBuilder().token(TOKEN).build()
		application.add_handler(CommandHandler("start", start))
		application.add_handler(MessageHandler(filters.COMMAND, unknown))
		await application.initialize()

# Função que vai cuidar de realizar a comunicação com o webhook
async def handle_request(event):
	try:
		logging.info("Processing request")
		update = Update.de_json(json.loads(event['body']), application.bot)
		await application.process_update(update)
		logging.info("Request processed successfully")
	except Exception as e:
		logging.error(f"Error processing update: {e}")
		raise
def lambda_handler(event, context):
	# Inicializar nossa aplicação caso não tenha
	asyncio.run(initialize_application())
	# Burocracia do lambda
	# para se comunicar com nossa API
	asyncio.run(handle_request(event))
	# Retornar uma mensagem de sucesso.
	return {
	'statusCode': 200,
	'body': json.dumps('Request processed successfully')
	}
