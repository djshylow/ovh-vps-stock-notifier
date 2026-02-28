# 📡 OVH SG VPS Notifier

Simple script to monitor Singapore VPS stock on OVH and alert via Telegram.

### 🛠️ 1. Setup Telegram
1. Message **@BotFather** for a Token.
2. Message your bot, then open this link (replace with your token) to find your **Chat ID**:  
`https://api.telegram.org/botYOUR_TOKEN_HERE/getUpdates`

### ⚙️ 2. Setup Script
1. Open `ovh-monitor.js` and paste your IDs:
   - `const TELEGRAM_TOKEN = "your_token";`
   - `const CHAT_ID = "your_id";`

### 🚀 3. How to Run
Open your terminal in the folder and run:

```bash
npm install axios
node ovh-monitor.js
