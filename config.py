import os
import time
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN         = os.getenv("BOT_TOKEN", "8796552651:AAGqUIttCQFmF6EoM4RyGkbf2oKsiCfhZMk")
ADMIN_IDS         = [int(x.strip()) for x in os.getenv("ADMIN_IDS", "5839948259").split(",") if x.strip().isdigit()]
LOG_CHANNEL       = os.getenv("LOG_CHANNEL", "@nikestoretr")
FOUNDER_USERNAME  = os.getenv("FOUNDER", "@nikecheatyeniden")
CHANNEL_USERNAME  = os.getenv("CHANNEL", "@nikestoretr")

BOT_NAME      = "NikeBot"
VERSION       = "1.0.0"
START_TIME    = time.time()
SPAM_COOLDOWN = 3            # saniye
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB
TEMP_DIR      = "/tmp/nikebot"
