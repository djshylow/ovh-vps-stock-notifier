const axios = require("axios");
const https = require("https");

// ---------------- SETTINGS ----------------
const sleepTime = 600000; // 10 minutes
const planCode = "vps-2025-model1";
const datacenterCode = "ap-southeast-sgp";

const TELEGRAM_TOKEN = "";
const CHAT_ID = ""; // your personal user ID

// ---------------- FORCE IPV4 ----------------
const agent = new https.Agent({
    family: 4
});

// ---------------- HELPERS ----------------
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function sendTelegram(message) {
    try {
        const url = `https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage`;

        const response = await axios.post(
            url,
            {
                chat_id: CHAT_ID,
                text: message
            },
            {
                httpsAgent: agent,
                timeout: 10000
            }
        );

        console.log("Telegram sent:", response.data.ok);

    } catch (err) {
        console.log("Telegram error:", err.response?.data || err.message);
    }
}

// ---------------- MAIN CHECK ----------------
async function checkVPS() {
    try {
        console.log("Checking OVH SG VPS...");
        const now = new Date().toLocaleString();
        console.log("Time:", now);
        console.log("----------------------------------");

        const url = `https://ca.api.ovh.com/v1/vps/order/rule/datacenter?ovhSubsidiary=SG&planCode=${planCode}`;

        const response = await axios.get(url, {
            timeout: 10000
        });

        const datacenters = response.data.datacenters;

        const sg = datacenters.find(
            dc => dc.code === datacenterCode || dc.datacenter === "SGP"
        );

        if (!sg) {
            await sendTelegram(`⚠️ SG datacenter not found at ${now}`);
            return;
        }

        const linuxStatus = sg.linuxStatus;
        const windowsStatus = sg.windowsStatus;

        console.log("Linux:", linuxStatus);
        console.log("Windows:", windowsStatus);

        const baseMessage =
`📡 OVH SG VPS Check
🕒 ${now}

Linux: ${linuxStatus}
Windows: ${windowsStatus}`;

        // 🚨 ALERT MODE
        if (linuxStatus === "available") {

            console.log("🚨 LINUX AVAILABLE — STARTING ALERT SPAM");

            for (let i = 1; i <= 5; i++) {

                await sendTelegram(
`🚨🚨 LINUX VPS AVAILABLE 🚨🚨

Alert ${i}/5

${baseMessage}`
                );

                if (i < 5) {
                    await sleep(30000); // 30 seconds
                }
            }

        } else {
            // Normal update
            await sendTelegram(baseMessage);
        }

    } catch (err) {
        console.log("Main error:", err.message);
    }
}

// ---------------- SAFE LOOP ----------------
async function startMonitor() {
    await checkVPS();
    setTimeout(startMonitor, sleepTime);
}

startMonitor();
