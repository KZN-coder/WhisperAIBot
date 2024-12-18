import telebot
import os
import requests


API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)
telebot.apihelper.CONNECT_TIMEOUT = 120
telebot.apihelper.READ_TIMEOUT = 120
API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3-turbo"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

@bot.message_handler(commands=['start'])
def start_answer(message):
    bot.send_message(message.chat.id, "Я бот для расшифровки")

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    try:
        file_info = bot.get_file(message.voice.file_id)
        file_path = file_info.file_path

        downloaded_file = bot.download_file(file_path)

        with open('./data/voice_message.ogg', 'wb') as new_file:
            new_file.write(downloaded_file)

        q = query('./data/voice_message.ogg')
        q = q["text"]
        bot.reply_to(message, f"{q}")

        os.remove("./data/voice_message.ogg")

    except Exception as e:
        bot.reply_to(message, f"Ошибка при скачивании голосового сообщения: {e}")

bot.infinity_polling()