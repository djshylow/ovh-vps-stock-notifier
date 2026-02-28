# ovh-vps-stock-notifier
A Node.js script that monitors OVH Singapore VPS availability and sends 5x alerts via Telegram when Linux instances are in stock.


🛠️ Setup Guide
1. Create your Telegram Bot
Message @BotFather on Telegram and create a new bot.

Save the API Token it provides.

2. Find your Telegram Chat ID
Open a chat with your new bot and click Start.

Open your web browser and go to this URL (replace YOUR_TOKEN_HERE with your actual bot token):
https://api.telegram.org/botYOUR_TOKEN_HERE/getUpdates

Look for a section in the text that says "chat":{"id":123456789}.

The number (e.g., 123456789) is your Chat ID.

3. Local Installation
Clone this repository:

Bash

git clone https://github.com/yourusername/ovh-vps-stock-notifier.git
cd ovh-vps-stock-notifier
Install Dependencies:

Bash

npm install axios
Configure the script:
Open ovh-monitor.js and fill in your credentials:

JavaScript

const TELEGRAM_TOKEN = "your_bot_token_here";
const CHAT_ID = "your_chat_id_here";
4. Run the Monitor
Bash

node ovh-monitor.js
The script will now check the OVH API every 10 minutes. If it finds a Singapore VPS, it will ping you 5 times with a 30-second delay between alerts.
