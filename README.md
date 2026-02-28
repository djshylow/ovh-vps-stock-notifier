# 📡 OVH Singapore VPS Stock Notifier

A Node.js script that monitors OVH Singapore VPS availability and sends 5x alerts via Telegram when Linux instances are in stock.

---

## 🛠️ Setup Guide

### 1. Create your Telegram Bot
* Message [@BotFather](https://t.me/botfather) on Telegram and create a new bot.
* Save the **API Token** it provides.

### 2. Find your Telegram Chat ID
1. Open a chat with your new bot and click **Start**.
2. Go to this URL in your browser (replace `YOUR_TOKEN_HERE` with your actual token):
   > `https://api.telegram.org/botYOUR_TOKEN_HERE/getUpdates`
3. Look for the section: `"chat":{"id":123456789}`.
4. The number **123456789** is your Chat ID.

### 3. Local Installation
**Clone the repository:**
```bash
git clone [https://github.com/djshylow/ovh-vps-stock-notifier.git](https://github.com/djshylow/ovh-vps-stock-notifier.git)
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
The script checks the OVH API every 10 minutes. If a Singapore VPS is found, it will ping you 5 times with a 30-second delay.
