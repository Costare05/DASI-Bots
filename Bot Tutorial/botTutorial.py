from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import Update
import datetime # Biblioteca para a função horario


"""
Como gerar o TOKEN do seu primeiro bot:
obs: NUNCA divulgue (Em github ou qualquer outra coisa) o TOKEN do seu bot e seu ID .


1) Entre no seu telegram e fale com o @BotFather
2) Digite /start e veja os comandos [Apenas por curiosidade]
3) Digite /newbots
5) Escolha o arroba de seu bot [Siga os passos que o bot irá falar]
6) Digite /setinline
7) Digite o arromba de seu bot [Ex: @dasibot]


BOT CRIADO!!!

Agora digite o arroba dele na barra de pesquisa, subsitua o TOKEN que o @BotFather gerou pelo TOKEN aqui em baixo

DIVIRTA-SE!

"""


# Primeiro Contato com o usuário
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    # Fornece os seguintes parametros: User(first_name='Renan', id=<NUNCA DIVULGUE SEU ID>, is_bot=False, language_code='pt-br', username='Renangmc0504')
    nome = update.message.from_user
    nome = nome.first_name
    chat_id = update.message.chat_id
    #await update.message.reply_text(f"Bem vindo ao melhor setor, {nome}!", quote=False)
    await update.message.reply_text(f"Chat ID:, {chat_id}!", quote=False)


# Função que qualquer coisa que eu falar ele vai responder com uma mensagem automática
async def echo(update:Update, context: ContextTypes.DEFAULT_TYPE):
    texto_usuario = update.message.text
    texto_usuario = texto_usuario.upper() 
    await update.message.reply_text(texto_usuario)


async def horario(update:Update, context: ContextTypes.DEFAULT_TYPE):
    # Obtendo a data e hora atuais
    agora = datetime.datetime.now()

    # Formatando a hora atual no formato desejado
    hora_atual_formatada = agora.strftime("%H:%M:%S")

    # Imprimindo a hora atual formatada
    await update.message.reply_text(f"Horário atual: {hora_atual_formatada}")



if __name__ == "__main__":
    # Pegando o token e contruindo o bot

    TOKEN = "seuTokenAqui"

    bot = ApplicationBuilder().token(TOKEN).build()

    # Adicionando a função /start
    start_handler = CommandHandler("start",start)
    bot.add_handler(start_handler)

    # Adicionando echo
    #echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    #bot.add_handler(echo_handler)

    # Adicionando o horario
    #horario_handler = CommandHandler("horario",horario)
    #Wbot.add_handler(horario_handler)


    # Rodando o bot
    bot.run_polling()

