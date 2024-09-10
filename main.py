import logging
from pyrogram import Client, filters
import asyncio

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Pyrogram setup
api_id = "your_api_id" 
api_hash = "your_api_hash"
phone_number = "telegram_number"
# Destination Locations. Here 2 different locations, u can add more
d_logs = chat_ID    # add destination chat_ID
d_ulp = chat_ID     # add destination chat_ID

# List of chat IDs
logs_chat = [chat_ID]  # add destination chat_ID
ulp_chat = [chat_ID]   # add destination chat_ID

# Set to track forwarded document file IDs (to prevent duplicates)
forwarded_files = set()

# Initialize Pyrogram client
user_client = Client("telegram_username", api_id=api_id, api_hash=api_hash, phone_number=phone_number)   # add your telegram_username

@user_client.on_message(filters.chat(logs_chat + ulp_chat) & filters.document)
async def forward_file(_, message):
    try:
        # Log that the message handler was triggered
        logger.info(f"Received a document from chat {message.chat.id}")

        # Check if the document has already been forwarded
        if message.document.file_id in forwarded_files:
            logger.info(f"Duplicate document '{message.document.file_name}' from chat {message.chat.id}, skipping")
            return
        
        # Determine destination based on chat ID
        if message.chat.id in logs_chat:
            destination_chat = d_logs
        elif message.chat.id in ulp_chat:
            destination_chat = d_ulp
        else:
            logger.warning(f"Message from unexpected chat: {message.chat.id}, skipping")
            return

        # Log document information
        logger.info(f"Forwarding document '{message.document.file_name}' from {message.chat.id} to {destination_chat}")
        
        # Forward the document
        await user_client.copy_message(chat_id=destination_chat, from_chat_id=message.chat.id, message_id=message.id)
        logger.info(f"Message {message.id} forwarded successfully from {message.chat.id} to {destination_chat}")
        
        # Mark the document as forwarded by adding its file_id to the set
        forwarded_files.add(message.document.file_id)

        # Optional delay to avoid hitting rate limits
        await asyncio.sleep(1)

    except Exception as e:
        logger.error(f"Failed to forward message {message.id} from {message.chat.id} to {destination_chat}: {e}")

# Run the client
user_client.run()
