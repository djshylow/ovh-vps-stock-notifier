import requests
import time
import os
from datetime import datetime

# ---------------- SETTINGS ----------------
SLEEP_TIME = 600  # 10 minutes in seconds
PLAN_CODE = "vps-2025-model1"
DATACENTER_CODE = "ap-southeast-sgp"

# Use environment variables for security
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
CHAT_ID = os.getenv("CHAT_ID", "")

def send_telegram(message):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("Error: Missing Telegram credentials.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    try:
        # family=4 equivalent: most modern systems handle this, 
        # but you can use a custom adapter if you strictly need IPv4 forcing.
        response = requests.post(url, json=payload, timeout=10)
        print(f"Telegram sent: {response.json().get('ok')}")
    except Exception as e:
        print(f"Telegram error: {e}")

def check_vps():
    try:
        print("Checking OVH SG VPS...")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Time: {now}")
        print("-" * 34)

        url = f"https://ca.api.ovh.com/v1/vps/order/rule/datacenter?ovhSubsidiary=SG&planCode={PLAN_CODE}"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        datacenters = response.json().get("datacenters", [])
        
        # Find Singapore datacenter
        sg = next((dc for dc in datacenters if dc.get("code") == DATACENTER_CODE or dc.get("datacenter") == "SGP"), None)

        if not sg:
            send_telegram(f"⚠️ SG datacenter not found at {now}")
            return

        linux_status = sg.get("linuxStatus")
        windows_status = sg.get("windowsStatus")

        print(f"Linux: {linux_status}")
        print(f"Windows: {windows_status}")

        base_message = (
            f"📡 OVH SG VPS Check\n"
            f"🕒 {now}\n\n"
            f"Linux: {linux_status}\n"
            f"Windows: {windows_status}"
        )

        # 🚨 ALERT MODE
        if linux_status == "available":
            print("🚨 LINUX AVAILABLE — STARTING ALERT SPAM")
            for i in range(1, 6):
                alert_msg = f"🚨🚨 LINUX VPS AVAILABLE 🚨🚨\n\nAlert {i}/5\n\n{base_message}"
                send_telegram(alert_msg)
                
                if i < 5:
                    time.sleep(30)  # 30 seconds
        else:
            # Normal update
            send_telegram(base_message)

    except Exception as e:
        print(f"Main error: {e}")

def start_monitor():
    while True:
        check_vps()
        print(f"Waiting {SLEEP_TIME//60} minutes for next check...")
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    start_monitor()
