import telebot
TOKEN='1601219821:AAFxAyq5nC7HvU7Q93ETWkWq3SfiSyjUXfY'
bot=telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id,'Привет!')
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower()=='стикер':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBR99gm-tMJ5xRBCKWNeIcQYUGhgq2JQAC4gADDcr9LhnUyRhffXXyHwQ')
    elif message.text.lower()=='привет':
        bot.send_message(message.chat.id, 'Привет, друг')
    elif message.text.lower()=='пока':
        bot.send_message(message.chat.id, 'Пока, друг')
    elif message.text.lower()=='как дела?':
        bot.send_message(message.chat.id, 'Хорошо')
    else:
        bot.send_message(message.chat.id, 'я не понимаю')
bot.polling()