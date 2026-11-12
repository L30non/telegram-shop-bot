import os
import sys

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

load_dotenv()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! Send me a sale like: sold 3 bags coffee $12"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"you said: {update.message.text}")


def main():
    token = os.environ.get("TELEGRAM_TOKEN", "").strip()
    if not token:
        print(
            "TELEGRAM_TOKEN is missing. Copy .env.example to .env "
            "and paste your token from @BotFather.",
            file=sys.stderr,
        )
        sys.exit(1)

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()


if __name__ == "__main__":
    main()
