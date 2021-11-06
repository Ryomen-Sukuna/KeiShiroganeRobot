import requests
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async
from tg_bot.modules.helper_funcs.decorators import keicmd


@keicmd(command=["ud", "urban"])
def ud(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text[len("/ud "):]
    results = requests.get(
        f"https://api.urbandictionary.com/v0/define?term={text}"
    ).json()
    try:
        reply_text = f'*{text}*\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
    except BaseException:
        reply_text = "No results found."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)
