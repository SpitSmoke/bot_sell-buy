import telebot
from generate_code import save_code_to_file  # Gera uma nova chave

TOKEN = "SEU_TELEGRAM_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Digite /chave para receber sua chave de ativação.")

@bot.message_handler(commands=['chave'])
def send_key(message):
    key = save_code_to_file()  # Gera um novo código
    bot.reply_to(message, f"Sua chave de ativação: {key}")

print("🤖 Bot do Telegram rodando...")
bot.polling()
