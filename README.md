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


###3. Run
Open your terminal in the folder and run:

Bash

> `npm install axios
node ovh-monitor.js`
Checks every 10 mins. Pings 5 times when stock is found.


### Why this is better:
* **No Git commands:** It assumes they just downloaded your file.
* **Code Blocks:** Using the \` \` \` symbols makes the commands look like real buttons/boxes instead of a mess.
* **Direct:** It tells them exactly where to paste the keys.

**Would you like me to make a `package.json` file for you?** It lets people just ty
