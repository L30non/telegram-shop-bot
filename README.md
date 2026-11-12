# 🛒 Shop Bot

Telegram bot that lets Cambodian shop owners log sales in Khmer or English.
The AI parses messages → database → daily summaries.

## Status
🚧 Week 1: echo bot (Telegram plumbing works, no AI yet)

## Stack
Python · python-telegram-bot · Claude API (planned) · Postgres on Supabase (planned)

## Run locally
Requires Python 3.11+.

1. Create a bot with @BotFather and copy the token.
2. `cp .env.example .env` and paste the token.
3. `python -m venv .venv && source .venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python bot.py`
6. Message your bot on Telegram.

## Roadmap
- [x] Week 1: echo bot
- [ ] Week 2: Claude parses sales into structured JSON
- [ ] Week 3: save to database, `/today` command
- [ ] Week 4: deploy + daily summary
- [ ] Week 5: first real users
- [ ] Week 6: fixes + `/undo`
