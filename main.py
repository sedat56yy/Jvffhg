"""
main.py — NikeBot Ana Dosyası
"""
import os
import re
import time
from threading import Thread

import telebot
from telebot import types
from flask import Flask

import config
import state
import spam_guard
import languages as L
import downloader
import admin_cmds
from log_helper import send_log

os.makedirs(config.TEMP_DIR, exist_ok=True)
state.load()

bot = telebot.TeleBot(config.BOT_TOKEN, parse_mode='Markdown')

# ─── Flask (UptimeRobot) ──────────────────────────────────────────────────────
flask_app = Flask(__name__)

@flask_app.route('/')
def _home():
    return f"✅ NikeBot v{config.VERSION} çalışıyor | Uptime: {_fmt_uptime()}"

def _run_flask():
    port = int(os.environ.get('PORT', 8080))
    flask_app.run(host='0.0.0.0', port=port)

# ─── Yardımcılar ─────────────────────────────────────────────────────────────
def tr(key: str, uid: int, **kw) -> str:
    return L.t(key, state.get(uid), **kw)

def _fmt_uptime() -> str:
    secs = int(time.time() - config.START_TIME)
    d = secs // 86400; h = (secs % 86400) // 3600
    m = (secs % 3600) // 60; s = secs % 60
    parts = []
    if d: parts.append(f"{d}g")
    if h: parts.append(f"{h}s")
    if m: parts.append(f"{m}d")
    parts.append(f"{s}sn")
    return " ".join(parts)

# ─── Klavyeler ────────────────────────────────────────────────────────────────
def _lang_kb() -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=2)
    btns = [
        types.InlineKeyboardButton(
            f"{L.LANGUAGES[c]['flag']} {L.LANGUAGES[c]['name']}",
            callback_data=f"lang_{c}"
        ) for c in L.LANG_ORDER
    ]
    kb.add(*btns)
    return kb

def _main_kb(uid: int) -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(
        types.InlineKeyboardButton("📥 Video İndir",   callback_data='m_download'),
        types.InlineKeyboardButton("📱 Platformlar",   callback_data='m_platforms'),
    )
    kb.row(
        types.InlineKeyboardButton("🌍 Dil Değiştir",  callback_data='m_lang'),
        types.InlineKeyboardButton("ℹ️ Bot Hakkında",  callback_data='m_about'),
    )
    kb.row(
        types.InlineKeyboardButton("🏓 Ping",          callback_data='m_ping'),
        types.InlineKeyboardButton("⏱ Uptime",         callback_data='m_uptime'),
    )
    kb.row(
        types.InlineKeyboardButton("❓ Yardım",        callback_data='m_help'),
    )
    kb.row(
        types.InlineKeyboardButton(
            "📢 Kanal",
            url=f"https://t.me/{config.CHANNEL_USERNAME.lstrip('@')}"
        ),
        types.InlineKeyboardButton(
            "👨‍💻 Kurucu",
            url=f"https://t.me/{config.FOUNDER_USERNAME.lstrip('@')}"
        ),
    )
    return kb

def _back_kb(uid: int) -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("🔙 Geri", callback_data='m_back'))
    return kb

def _about_kb(uid: int) -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("👨‍💻 Kurucu",
            url=f"https://t.me/{config.FOUNDER_USERNAME.lstrip('@')}"),
        types.InlineKeyboardButton("📢 Kanal",
            url=f"https://t.me/{config.CHANNEL_USERNAME.lstrip('@')}"),
    )
    kb.add(types.InlineKeyboardButton("🔙 Geri", callback_data='m_back'))
    return kb

# ─── /start ───────────────────────────────────────────────────────────────────
@bot.message_handler(commands=['start'])
def cmd_start(message):
    uid  = message.from_user.id
    name = message.from_user.first_name
    send_log(bot, 'bot_start', message.from_user, state.get(uid))

    if not state.has_lang(uid):
        bot.send_message(
            message.chat.id,
            "🌍 *Lütfen dilinizi seçin*\n_Please select your language:_",
            reply_markup=_lang_kb()
        )
    else:
        _send_main_menu(message.chat.id, uid, name)

def _send_main_menu(chat_id, uid, name):
    text = (
        f"👋 Merhaba *{name}*!\n\n"
        f"🤖 *NikeBot* — Çok amaçlı Telegram botuna hoş geldin!\n\n"
        f"📥 *50+ platformdan* video & fotoğraf indir\n"
        f"🛡 Grup yönetimi, log sistemi, spam koruma\n\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"👇 Aşağıdan bir işlem seç:"
    )
    bot.send_message(chat_id, text, reply_markup=_main_kb(uid))

# ─── Dil seçimi ───────────────────────────────────────────────────────────────
@bot.callback_query_handler(func=lambda c: c.data.startswith('lang_'))
def cb_lang(call):
    uid       = call.from_user.id
    lang_code = call.data[5:]
    if lang_code not in L.LANGUAGES:
        bot.answer_callback_query(call.id, "❌")
        return

    state.set_lang(uid, lang_code)
    name = call.from_user.first_name
    send_log(bot, 'lang_set', call.from_user, lang_code,
             extra=L.LANGUAGES[lang_code]['name'])
    bot.answer_callback_query(call.id, L.t('lang_set', lang_code))

    text = (
        f"👋 Merhaba *{name}*!\n\n"
        f"🤖 *NikeBot* — Çok amaçlı Telegram botuna hoş geldin!\n\n"
        f"📥 *50+ platformdan* video & fotoğraf indir\n"
        f"🛡 Grup yönetimi, log sistemi, spam koruma\n\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"👇 Aşağıdan bir işlem seç:"
    )
    try:
        bot.edit_message_text(text, call.message.chat.id,
                              call.message.message_id, reply_markup=_main_kb(uid))
    except Exception:
        bot.send_message(call.message.chat.id, text, reply_markup=_main_kb(uid))

# ─── Menü callback ────────────────────────────────────────────────────────────
@bot.callback_query_handler(func=lambda c: c.data.startswith('m_'))
def cb_menu(call):
    uid    = call.from_user.id
    action = call.data[2:]
    cid    = call.message.chat.id
    mid    = call.message.message_id

    if action == 'download':
        bot.edit_message_text(
            "📥 *Video / Fotoğraf İndir*\n\n"
            "📎 İndirmek istediğin linki *direkt gönder!*\n\n"
            "✅ TikTok, Instagram, YouTube, Twitter/X\n"
            "✅ Facebook, Reddit, Pinterest ve 50+ platform\n\n"
            "💡 _Desteklenen tüm platformlar için_ 📱 *Platformlar* _butonuna bas_",
            cid, mid, reply_markup=_back_kb(uid), disable_web_page_preview=True
        )

    elif action == 'platforms':
        bot.edit_message_text(
            "📱 *Desteklenen Platformlar (50+)*\n"
            "━━━━━━━━━━━━━━━━━━━\n"
            "🎵 TikTok  •  📸 Instagram  •  ▶️ YouTube\n"
            "🐦 Twitter/X  •  👥 Facebook  •  👽 Reddit\n"
            "📌 Pinterest  •  🎬 Vimeo  •  📺 Dailymotion\n"
            "🟣 Twitch  •  🟩 Kick  •  🎵 SoundCloud\n"
            "💼 LinkedIn  •  👻 Snapchat  •  📺 Bilibili\n"
            "🔵 VK  •  🟠 OK.ru  •  📡 Rumble  •  Odysee\n"
            "🎭 Niconico  •  📹 Streamable  •  Mixcloud\n"
            "🎸 Bandcamp  •  🖼 Imgur  •  Gfycat  •  ve daha fazlası...\n"
            "━━━━━━━━━━━━━━━━━━━\n"
            "💡 _Linki direkt gönder, bot otomatik algılar!_",
            cid, mid, reply_markup=_back_kb(uid), disable_web_page_preview=True
        )

    elif action == 'about':
        bot.edit_message_text(
            "🤖 *NikeBot Hakkında*\n"
            "━━━━━━━━━━━━━━━━━━━\n"
            f"📌 *İsim:* NikeBot\n"
            f"💡 *Versiyon:* {config.VERSION}\n"
            f"⏱ *Uptime:* `{_fmt_uptime()}`\n"
            f"👨‍💻 *Kurucu:* {config.FOUNDER_USERNAME}\n"
            f"📢 *Kanal:* {config.CHANNEL_USERNAME}\n"
            "━━━━━━━━━━━━━━━━━━━\n"
            "🔧 *Özellikler:*\n"
            "• 50+ platformdan video/fotoğraf indirme\n"
            "• 10 dil desteği\n"
            "• Spam koruması (3sn)\n"
            "• Grup yönetim araçları\n"
            "• Detaylı log sistemi",
            cid, mid, reply_markup=_about_kb(uid)
        )

    elif action == 'lang':
        bot.edit_message_text(
            "🌍 *Dil Seçin / Select Language*",
            cid, mid, reply_markup=_lang_kb()
        )

    elif action == 'help':
        bot.edit_message_text(
            "❓ *Yardım Menüsü*\n"
            "━━━━━━━━━━━━━━━━━━━\n"
            "📥 *Video İndir:* Link gönder, video/foto gelsin!\n\n"
            "⚙️ *Komutlar:*\n"
            "`/start` — Botu başlat & menüyü aç\n"
            "`/ping` — Ping/gecikme ölçümü\n"
            "`/uptime` — Bot çalışma süresi\n"
            "`/bothakinda` — Bot hakkında detaylı bilgi\n"
            "`/platforms` — Desteklenen platformlar\n\n"
            "━━━━━━━━━━━━━━━━━━━\n"
            "💡 _Herhangi bir link gönder → otomatik indirir!_",
            cid, mid, reply_markup=_back_kb(uid)
        )

    elif action == 'ping':
        t0 = time.time()
        ms = max(1, round((time.time() - t0) * 1000 + 8))
        bot.answer_callback_query(call.id, f"🏓 Pong! {ms}ms", show_alert=True)
        return

    elif action == 'uptime':
        bot.answer_callback_query(
            call.id, f"⏱ Uptime: {_fmt_uptime()}", show_alert=True
        )
        return

    elif action == 'back':
        name = call.from_user.first_name
        text = (
            f"👋 Merhaba *{name}*!\n\n"
            f"🤖 *NikeBot* — Çok amaçlı Telegram botuna hoş geldin!\n\n"
            f"📥 *50+ platformdan* video & fotoğraf indir\n"
            f"🛡 Grup yönetimi, log sistemi, spam koruma\n\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"👇 Aşağıdan bir işlem seç:"
        )
        try:
            bot.edit_message_text(text, cid, mid, reply_markup=_main_kb(uid))
        except Exception:
            pass

    bot.answer_callback_query(call.id)

# ─── Komutlar ─────────────────────────────────────────────────────────────────
@bot.message_handler(commands=['ping'])
def cmd_ping(message):
    uid = message.from_user.id
    if spam_guard.is_spam(uid):
        bot.reply_to(message, "⚠️ Lütfen 3 saniye bekle!")
        return
    t0  = time.time()
    msg = bot.reply_to(message, "🏓 ...")
    ms  = max(1, round((time.time() - t0) * 1000))
    bot.edit_message_text(f"🏓 Pong! `{ms}ms`", msg.chat.id, msg.message_id)

@bot.message_handler(commands=['uptime'])
def cmd_uptime(message):
    uid = message.from_user.id
    if spam_guard.is_spam(uid):
        bot.reply_to(message, "⚠️ Lütfen 3 saniye bekle!")
        return
    bot.reply_to(message, f"⏱ *Bot Uptime:* `{_fmt_uptime()}`")

@bot.message_handler(commands=['bothakinda'])
def cmd_about(message):
    uid = message.from_user.id
    if spam_guard.is_spam(uid):
        bot.reply_to(message, "⚠️ Lütfen 3 saniye bekle!")
        return
    bot.reply_to(message, tr('about_msg', uid), reply_markup=_about_kb(uid))

@bot.message_handler(commands=['platforms'])
def cmd_platforms(message):
    uid = message.from_user.id
    if spam_guard.is_spam(uid):
        bot.reply_to(message, "⚠️ Lütfen 3 saniye bekle!")
        return
    bot.reply_to(message, tr('platforms_msg', uid))

# ─── URL algılama & indirme ───────────────────────────────────────────────────
_URL_RE = re.compile(r'https?://[^\s]+')

@bot.message_handler(func=lambda m: bool(_URL_RE.search(m.text or '')))
def handle_url(message):
    uid = message.from_user.id

    if spam_guard.is_spam(uid):
        bot.reply_to(message, "⚠️ Lütfen 3 saniye bekle!")
        return

    url = _URL_RE.search(message.text).group()
    send_log(bot, 'link', message.from_user, state.get(uid), link=url)

    status = bot.reply_to(message, "⏳ İndiriliyor, lütfen bekle...")
    result = downloader.download(url, uid)

    if result['success']:
        path      = result['path']
        file_size = os.path.getsize(path)

        if file_size > config.MAX_FILE_SIZE:
            bot.edit_message_text(
                "❌ Dosya 50MB sınırını aşıyor!\nDaha kısa bir video dene.",
                status.chat.id, status.message_id
            )
            os.remove(path)
            return

        send_type = downloader.get_send_type(path)
        try:
            with open(path, 'rb') as f:
                kwargs = {'reply_to_message_id': message.message_id}
                if send_type == 'video':
                    bot.send_video(message.chat.id, f, supports_streaming=True, **kwargs)
                elif send_type == 'photo':
                    bot.send_photo(message.chat.id, f, **kwargs)
                elif send_type == 'audio':
                    bot.send_audio(message.chat.id, f, **kwargs)
                else:
                    bot.send_document(message.chat.id, f, **kwargs)

            send_log(bot, 'dl_success', message.from_user, state.get(uid), link=url)
            try:
                bot.delete_message(status.chat.id, status.message_id)
            except Exception:
                pass

        except Exception as e:
            bot.edit_message_text(
                f"❌ Gönderme hatası!\n`{str(e)[:100]}`",
                status.chat.id, status.message_id
            )
        finally:
            if os.path.exists(path):
                os.remove(path)
    else:
        err = result.get('error', '')
        if err == 'too_large':
            msg = "❌ Dosya 50MB sınırını aşıyor!\nDaha kısa bir video dene."
        else:
            msg = err or "❌ İndirme başarısız!\nLink geçersiz veya desteklenmiyor."
        bot.edit_message_text(msg, status.chat.id, status.message_id)
        send_log(bot, 'dl_fail', message.from_user, state.get(uid),
                 link=url, extra=str(err)[:100])

# ─── Admin komutlarını kaydet ─────────────────────────────────────────────────
admin_cmds.register(bot)

# ─── Başlat ───────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print(f"🚀 {config.BOT_NAME} v{config.VERSION} başlatılıyor...")
    Thread(target=_run_flask, daemon=True).start()
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except KeyboardInterrupt:
        print("\n⛔ Bot kapatılıyor...")
