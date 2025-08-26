from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Sage School Bot!\n"
        "Use /help to see our information."
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Available commands:\n"
        "/schedule - View school schedule\n"
        "/contact - Get contact info\n"
        "/about - About our school\n"
        "/learnmore - Join our Telegram channel and social media"
    )

# /schedule command
async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕘 Classes: Mon-Fri, 8:00 AM - 3:00 PM.\n"
        "የስልጠና አሰጣጥ ስረአትአችን በቀን እንዲሁም በማታ ፣ በርቀት እና በቅናሜ እና እሁድ ነው።/about"
    )

# /contact command
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "☎️ Phone: +123456789\n"
        "🏫 Address: Megenanya, Tamages Building, Second Floor"
    )

# /about command
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏫 Trainings we provide in the technology sector:\n"
        "- Computer Programming and Database\n"
        "- Web Development and Full Stack Application\n"
        "- Machine Learning and others /learnmore"
    )

# /learnmore command with buttons
async def learn_more(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Telegram Channel", url="https://t.me/sagetraininginstitute")],
        [InlineKeyboardButton("Website", url="https://ephemeral-begonia-daa994.netlify.app")],
        [InlineKeyboardButton("Facebook", url="https://www.facebook.com/sagetraininginstitute")],
        [InlineKeyboardButton("LinkedIn", url="https://www.linkedin.com/company/sage-training-institute")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🌐 Join our social media:", reply_markup=reply_markup)

# Main function
def main():
    app = Application.builder().token("8274017951:AAEA5zU7MsL3BQ66uhGLAd4G1UwlZlgt_Mo").build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("schedule", schedule))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("learnmore", learn_more))

    print("✅ Sage School Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
