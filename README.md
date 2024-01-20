# telegram-bot-image-caption

Simple Telegram bot that returns the caption of an image.

This bot makes use of [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base) for generation captions of the images.

Also, it detects the language of the user and translates with [deep-translator](https://pypi.org/project/deep-translator/).


## How to start

Create a new Telegram bot by talking to BotFather.

Copy the bot token and paste into `.env`, like this:

```
echo "TELEGRAM_API_TOKEN=your-token" > .env
```

Make sure you have python 3.10 installed. If you're using pyenv you can do:

```
pyenv install 3.10.9
```

Then to install dependencies do:

```
pip install -r requirements.txt
```

Finally start the bot by executing:

```
python bot.py
```

# LICENSE

[MIT](/LICENSE)
