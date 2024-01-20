import os
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
assert TELEGRAM_BOT_TOKEN, "Expected TELEGRAM_BOT_TOKEN to be set"

def start(update, context):
    update.message.reply_text("Send me a photo with a message and I'll respond with a caption!")

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
