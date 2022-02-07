from silverbots.telegram import TelegramBot

bot = TelegramBot("<YOUR_TOKEN>")


@bot.handle_message()
def handle_message(message):
    chat_id = message.chat.id
    msg_text = message.text.lower()
    if "hello" in msg_text or "hi" in msg_text:
        bot.send_message(chat_id, "Hi, I'm a sample Bot!")
    elif "buy" in msg_text:
        bot.send_message(chat_id, "Buy! Hope to see you again!")
    else:
        bot.send_message(chat_id, "I can't understand you.")


bot.run(debug=True)
