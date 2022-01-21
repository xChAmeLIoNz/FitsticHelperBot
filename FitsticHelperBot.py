from requests import *
from telegram import *
from telegram.ext import *

updater = Updater(token="5160047465:AAFXJS1IkbT-Cr_4NuitOUhXrDvZ3W3ysE8")
dispatcher = updater.dispatcher

programmaText = "Programma"
informazioniText = "Informazioni"
  
def start(update: Update, context: CallbackContext):
    buttons=[[KeyboardButton("Programma")], [KeyboardButton("Informazioni")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ciao " + update.effective_user.first_name + "!" + "\nSeleziona un pulsante per iniziare",
    reply_markup=ReplyKeyboardMarkup(buttons))

def messageHandler(update: Update, context: CallbackContext):
    if programmaText in update.message.text:
        update.message.reply_text("Ecco il link del programma\nhttps://docs.google.com/spreadsheets/d/1kOQY13lzyX8CF9iBRnAZGr8Xz3hUtca6PmQV0_ZUsfE/edit#gid=537086263")
    if informazioniText in update.message.text:
        update.message.reply_text("Questo bot è stato creato da Alessandro Fogli Iseppe con Python, se avete in mente delle implementazioni"
        + " scrivetemi in privato")
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))

updater.start_polling()
hi