## About
This is a Telegram bot that validates whether a number is acceptable for the game Primel. If the guess does not follow the below conditions, a message will be sent back to the user detailing that the entry was invalid:
- Contain 5 digits
- Contain no special characters
- Have no leading 0s
- Be positive

Example: `10007` is the first valid Primel entry

## Installation
Requires Python 3.6 - 4

On Telegram, create a bot using [BotFather](https://t.me/botfather).

In `constants.py`, change `TELEGRAM_TOKEN` to your Telegram bot token.

```
$ pip install -r requirements.txt
```

## Usage

```
$ python main.py
```
After running, use the command `/primel <number>` to send a guess to your Telegram bot!