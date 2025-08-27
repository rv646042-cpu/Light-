import telebot

# Bot token
TOKEN = "8339848307:AAHDgHZ3pwaZXxbs_2Ry4YPEVJXP9W1oKGE"
bot = telebot.TeleBot(TOKEN)

# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! ✅ Bot is working.")

# Echo handler (jo message bhejoge wahi reply karega)
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("🤖 Bot started...")
bot.polling()
