import random
from datetime import datetime

import telegram
from telegram.ext import ContextTypes, filters, MessageHandler, ApplicationBuilder

from g3sta import G3STA_PATH

TOKEN = ""
WHITELIST = []


async def echo(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message is not None:
        print( f"[{datetime.strftime(message.date, '%Y-%m-%d %H:%M:%S')}] " + message.from_user.name + ": " + message.text)
        if not WHITELIST or message.from_user in WHITELIST:
            with open(G3STA_PATH, "r", encoding="utf-8") as f:
                await message.reply_text(random.choice(f.read().split("\n")))
        elif WHITELIST:
            await message.reply_text("Not whitelisted.")


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    application.run_polling()
