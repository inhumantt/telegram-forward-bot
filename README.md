# Telegram Auto-Forward Bot

This Python script uses the [Pyrogram](https://docs.pyrogram.org/) library to automatically forward documents from specific Telegram groups or channels to predefined destination chats. The bot prevents forwarding duplicate files by checking for the same document `file_id` before forwarding.

## Features

- **Automatic Forwarding**: The script listens to incoming document messages from specified chats (`logs_chat` and `ulp_chat`) and forwards them to the corresponding destination chats (`d_logs` or `d_ulp`).
  
- **Duplicate Document Detection**: The bot uses the `file_id` assigned by Telegram to detect duplicates and skips forwarding documents that have already been processed.

- **Logging**: Logs messages and errors to the console, providing insights into actions such as received documents, forwarded files, and detected duplicates.

- **Rate Limiting**: Includes an optional delay between forwarding actions to avoid hitting Telegram’s rate limits.

## How It Works

1. **Chat Configuration**: You specify two lists of chat IDs (`logs_chat` and `ulp_chat`) from which the bot will listen for incoming document messages.
2. **Destination Setup**: Documents from `logs_chat` are forwarded to `d_logs`, and documents from `ulp_chat` are forwarded to `d_ulp`.
3. **Duplicate Check**: Before forwarding a document, the bot checks its `file_id` against previously forwarded documents. If a document has been forwarded before, it will skip it.
4. **Forwarding**: If the document is unique, it is forwarded to the appropriate destination channel or group.

## Requirements

- Python 3.x
- [Pyrogram](https://docs.pyrogram.org/) library
- Telegram API credentials (API ID and API Hash)

Install the necessary libraries using:

```bash
pip install pyrogram
