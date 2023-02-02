import os
import openai
import telebot

openai.api_key = "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"
bot = telebot.TeleBot("5880229817:AAHuBQ4kv2I1F15PMu6JU7KUPu6w_uPYims")

@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
  )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])

bot.polling()
# print(response['choices'][0]['text'])