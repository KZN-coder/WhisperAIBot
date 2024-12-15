# WhisperAI integration for Telegram Bots

Bot is simple for usage and upgrading by yourself

## Installation
Clone the repo to your pc/server.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries.

```bash
pip install -r "requirements.txt"
```
Insert your key and token into the main.py
```python
API_TOKEN = '<your API token here>'
bot = telebot.TeleBot(API_TOKEN)
telebot.apihelper.CONNECT_TIMEOUT = 120
telebot.apihelper.READ_TIMEOUT = 120
API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3-turbo"
headers = {"Authorization": "Bearer <your HuggingFace access token here>"}
```
## Usage

Run the programm
```python
python3 main.py
```

## Authors

@dragunov_tt (Telegram)
