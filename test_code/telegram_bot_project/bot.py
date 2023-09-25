import os
import django
from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, filters, CallbackContext
from django.contrib.auth.models import User
from telegram_bot_app.models import Message  # Import your Message model

# Initialize Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telegram_bot_project.settings")
django.setup()

# Initialize the bot with your bot token
bot_token = '5506660546:AAElaULaSwfil3ELY09bjwMLcimiAG0oBu0'
bot = Bot(token=bot_token)

# Define the function to handle incoming messages
def send_message_to_user(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    user_message = update.message.text

    # Retrieve the user based on the chat_id or token
    try:
        user = User.objects.get(username=str(user_id))
    except User.DoesNotExist:
        user = None

    # Create a Message object and save it to the database
    if user:
        message = Message(user=user, text=user_message)
        message.save()

    # Send a response to the user
    response_text = f"User {user_id}, I have received your message: {user_message}"
    bot.send_message(chat_id=user_id, text=response_text)

def main():
    # Initialize the Updater
    updater = Updater(token=bot_token, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register a message handler to respond to incoming text messages
    message_handler = MessageHandler(filters.text & ~filters.command, send_message_to_user)
    dispatcher.add_handler(message_handler)

    # Start polling for updates
    updater.start_polling()

    # Run the bot until Ctrl+C is pressed
    updater.idle()

if __name__ == '__main__':
    main()
