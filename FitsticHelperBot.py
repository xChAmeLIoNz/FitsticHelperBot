from requests import *
from telegram import *
from telegram.ext import *

updater = Updater(token="5160047465:AAFXJS1IkbT-Cr_4NuitOUhXrDvZ3W3ysE8")
dispatcher = updater.dispatcher


programmaText="/programma"
informazioniText="/informazioni"
easterEggText="/easteregg"
fadText="/fad"

def start(update: Update, context: CallbackContext):
    buttons=[[InlineKeyboardButton("Programma", callback_data='1')], [InlineKeyboardButton(text="Informazioni", callback_data='2')], [InlineKeyboardButton(text="Crediti", callback_data='3')], [InlineKeyboardButton(text="FAD", callback_data='4')] ]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Seleziona un pulsante per iniziare",
    reply_markup=InlineKeyboardMarkup(buttons))

def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

  
    query.answer()
    if query.data=='1':
        query.edit_message_text(text=f"Ecco il link del programma\nhttps://docs.google.com/spreadsheets/d/1kOQY13lzyX8CF9iBRnAZGr8Xz3hUtca6PmQV0_ZUsfE/edit#gid=537086263")
    elif query.data=='2':
        query.edit_message_text(text=f"Questo bot è stato creato da Alessandro Fogli Iseppe con Python, se avete in mente delle implementazioni"
        + " scrivetemi in privato")
    elif query.data=='3':
        query.edit_message_text(text=f"Collaboratori: \nFrancesco Banzi @BanzF (InlineKeyboardButton)")
    elif query.data=='4':
        query.edit_message_text(text=f"Ecco il link del portale FAD: \nhttps://elearning.cfiformazione.it/")

def messageHandler(update: Update, context: CallbackContext):
    if programmaText in update.message.text:
        update.message.reply_text("Ecco il link del programma\nhttps://docs.google.com/spreadsheets/d/1kOQY13lzyX8CF9iBRnAZGr8Xz3hUtca6PmQV0_ZUsfE/edit#gid=537086263")
    if informazioniText in update.message.text:
        update.message.reply_text("Questo bot è stato creato da Alessandro Fogli Iseppe con Python, se avete in mente delle implementazioni"
        + " scrivetemi in privato")
    if easterEggText in update.message.text:
        update.message.reply_text("Israele è uno stato illegittimo, e chi sostiene il contrario è un rabbino.")
    if fadText in update.message.text:
        update.message.reply_text("Ecco il link del portale FAD: \nhttps://elearning.cfiformazione.it/")
    

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))

updater.start_polling()
updater.dispatcher.add_handler(CallbackQueryHandler(button))
