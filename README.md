# 📡 OVH Singapore VPS Stock Notifier

A lightweight monitoring script that checks **OVH Singapore VPS (Linux)** availability and sends **5 instant Telegram alerts** when stock becomes available.

Available in both **Node.js** and **Python** versions.

---

## 🚀 Features

- ✅ Monitors OVH Singapore VPS Linux stock
- 🔔 Sends 5 repeated Telegram alerts when stock is detected
- 🔁 Continuous automatic monitoring
- 🟢 Lightweight & fast
- 🖥️ Works on Windows, macOS, and Linux
- ⚡ Available in JavaScript (Node.js) and Python

---

## 🛠 Setup Guide

### 1️⃣ Create a Telegram Bot

1. Open Telegram
2. Message **@BotFather**
3. Run the command:

```
/newbot
```

4. Follow instructions and copy your **Bot Token**

---

### 2️⃣ Get Your Chat ID

1. Send any message to your new bot
2. Open this link in your browser (replace YOUR_TOKEN):

```
https://api.telegram.org/botYOUR_TOKEN/getUpdates
```

3. Look for:

```
"chat": {
    "id": 123456789,
```

4. Copy that number — this is your **CHAT_ID**

---

### 3️⃣ Configure the Script

Open one of these files:

- `ovh-monitor.js` (Node.js version)
- `ovh_monitor.py` (Python version)

Replace the credentials inside the file.

#### Node.js

```javascript
const TELEGRAM_TOKEN = "your_token_here";
const CHAT_ID = "your_chat_id_here";
```

#### Python

```python
TELEGRAM_TOKEN = "your_token_here"
CHAT_ID = "your_chat_id_here"
```

---

## ▶️ How to Run

---

## 🟢 Option A: Node.js Version

### Install dependency

```bash
npm install axios
```

### Run the script

```bash
node ovh-monitor.js
```

---

## 🟢 Option B: Python Version

### Install dependency

```bash
pip install requests
```

### Run the script

**Windows**
```bash
py ovh_monitor.py
```
or
```bash
python ovh_monitor.py
```

**Mac / Linux**
```bash
python3 ovh_monitor.py
```

---

## 🔄 Running 24/7 (Recommended for VPS)

If you are running this on a VPS, use a process manager.

---

### Using PM2 (Recommended for Node.js)

```bash
npm install -g pm2
pm2 start ovh-monitor.js --name ovh-monitor
pm2 save
pm2 startup
```

Check logs:

```bash
pm2 logs ovh-monitor
```

---

### Using Screen (Linux – Python or Node)

```bash
screen -S ovh-monitor
python3 ovh_monitor.py
```

Detach safely:

```
CTRL + A + D
```

Reattach:

```bash
screen -r ovh-monitor
```

---

## 📂 Project Structure

```
.
├── ovh-monitor.js      # Node.js version
├── ovh_monitor.py      # Python version
└── README.md
```

---

## 🧠 How It Works

1. Script checks OVH Singapore VPS stock endpoint
2. Detects Linux VPS availability
3. If stock is available:
   - Sends 5 Telegram alert messages
4. Continues monitoring automatically

---

## ⚠️ Important Notes

- This script monitors **Singapore region only**
- Designed specifically for **Linux VPS instances**
- Avoid very aggressive intervals to prevent rate limiting
- Make sure your server clock/timezone is correct

---

## 💡 Use Cases

- Developers waiting for OVH restock
- Hosting resellers
- Infrastructure buyers
- Anyone tired of manually refreshing the OVH website

---

## 📜 License

MIT License — free to use, modify, and distribute.
