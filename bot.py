from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8542276438:AAER4o-QIUsZCubaeT6dyNun9T6BVlPOqeQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("Share phone", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("Hi! Verify first.\nShare your phone 👇", reply_markup=reply_markup)

async def got_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phone = update.message.contact.phone_number
    await update.message.reply_text(f"Phone: {phone}\n\nNow send ID photo.")

async def got_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Photo received.\nNow send product photo.")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.CONTACT, got_contact))
    app.add_handler(MessageHandler(filters.PHOTO | filters.Document.ALL, got_photo))
    
    print("Bot starting...")
    app.run_polling()

if __name__ == '__main__':
    main()
