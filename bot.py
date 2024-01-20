import logging

import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from deep_translator import GoogleTranslator
from dotenv import load_dotenv
from transformers import pipeline
from PIL import Image
import requests

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


load_dotenv()

TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
assert TELEGRAM_API_TOKEN, "Expected TELEGRAM_API_TOKEN to be set"


async def reply_text(update: Update, text: str):
    user = update.message.from_user
    target_language = user.language_code
    translated_text = GoogleTranslator(source="en", target=target_language).translate(
        text
    )
    logger.info(f"Reply {user.username=} {text=} {target_language=} {translated_text=}")
    await update.message.reply_text(translated_text)


image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")


async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Starting new chat")

    await reply_text(update, "Send me a photo and I'll respond with a caption!")


async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Received new image")

    photo = await update.message.photo[-1].get_file()

    raw_image = Image.open(requests.get(photo.file_path, stream=True).raw)

    response_message = image_to_text(raw_image, max_new_tokens=20)[0]
    await reply_text(update, response_message["generated_text"])


def main():
    application = Application.builder().token(TELEGRAM_API_TOKEN).build()

    application.add_handler(CommandHandler("start", handle_start))

    application.add_handler(MessageHandler(filters.PHOTO, handle_image))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
