"""
main.py — NikeBot Ana Dosyası
Başlatma: python main.py
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

# ─── Hazırlık ─────────────────────────────────────────────────────────────────

os.makedirs(config.TEMP_DIR, exist_ok=True)
state.load()

bot = telebot.TeleBot(config.BOT_TOKEN, parse_mode='Markdown')

# ─── Flask (UptimeRobot için) ─────────────────────────────────────────────────

flask_app = Flask(__name__)

@flask_app.route('/')
def _home():
    up = _fmt_uptime()
    return f"✅ NikeBot v{config.VERSION} — Uptime: {up}"

def _run_flask():
    port = int(os.environ.get('PORT', 8080))
    flask_app.run(host='0.0.0.0', port=port)

# ─── Yardımcı fonksiyonlar ────────────────────────────────────────────────────

def tr(key: str, user_id: int, **kw) -> str:
    return L.t(key, state.get(user_id), **kw)


def _fmt_uptime() -> str:
    secs  = int(time.time() - config.START_TIME)
    d     = secs // 86400
    h     = (secs % 86400) // 3600
    m     = (secs % 3600) // 60
    s     = secs % 60
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
        )
        for c in L.LANG_ORDER
    ]
    kb.add(*btns)
    return kb


def _main_kb(uid: int) -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton(tr('btn_download', uid), callback_data='m_download'),
        types.InlineKeyboardButton(tr('btn_about',    uid), callback_data='m_about'),
        types.InlineKeyboardButton(tr('btn_lang',     uid), callback_data='m_lang'),
        types.InlineKeyboardButton(tr('btn_help',     uid), callback_data='m_help'),
        types.InlineKeyboardButton(tr('btn_ping',     uid), callback_data='m_ping'),
        types.InlineKeyboardButton(tr('btn_uptime',   uid), callback_data='m_uptime'),
    )
    return kb


def _back_kb(uid: int) -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(tr('btn_back', uid), callback_data='m_back'))
    return kb


def _about_kb(uid: int) -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton(
            "👨‍💻 Kurucu",
            url=f"https://t.me/{config.FOUNDER_USERNAME.lstrip('@')}"
        ),
        types.InlineKeyboardButton(
            "📢 Kanal",
            url=f"https://t.me/{config.CHANNEL_USERNAME.lstrip('@')}"
        ),
    )
    kb.add(types.InlineKeyboardButton(tr('btn_back', uid), callback_data='m_back'))
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
            "🌍 Lütfen dilinizi seçin / Please select your language:",
            reply_markup=_lang_kb()
        )
    else:
        bot.send_message(
            message.chat.id,
            tr('welcome', uid, name=name),
            reply_markup=_main_kb(uid)
        )


# ─── Dil seçimi callback ──────────────────────────────────────────────────────

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

    bot.answer_callback_query(call.id, tr('lang_set', uid))
    try:
        bot.edit_message_text(
            tr('welcome', uid, name=name),
            call.message.chat.id,
            call.message.message_id,
            reply_markup=_main_kb(uid)
        )
    except Exception:
        bot.send_message(
            call.message.chat.id,
            tr('welcome', uid, name=name),
            reply_markup=_main_kb(uid)
        )


# ─── Menü callback ────────────────────────────────────────────────────────────

@bot.callback_query_handler(func=lambda c: c.data.startswith('m_'))
def cb_menu(call):
    uid    = call.from_user.id
    action = call.data[2:]
    cid    = call.message.chat.id
    mid    = call.message.message_id

    if action == 'download':
        bot.edit_message_text(
            tr('download_prompt', uid),
            cid, mid,
            reply_markup=_back_kb(uid),
            disable_web_page_preview=True
        )

    elif action == 'about':
        bot.edit_message_text(
            tr('about_msg', uid),
            cid, mid,
            reply_markup=_about_kb(uid)
        )

    elif action == 'lang':
        bot.edit_message_text(
            tr('select_lang', uid),
            cid, mid,
            reply_markup=_lang_kb()
        )

    elif action == 'help':
        bot.edit_message_text(
            tr('help_msg', uid),
            cid, mid,
            reply_markup=_back_kb(uid)
        )

    elif action == 'ping':
        t0  = time.time()
        ms  = max(1, round((time.time() - t0) * 1000 + 8))
        bot.answer_callback_query(call.id, f"🏓 Pong! {ms}ms", show_alert=True)

    elif action == 'uptime':
        bot.answer_callback_query(
            call.id,
            f"⏱ Uptime: {_fmt_uptime()}",
            show_alert=True
        )

    elif action == 'back':
        name = call.from_user.first_name
        try:
            bot.edit_message_text(
                tr('welcome', uid, name=name),
                cid, mid,
                reply_markup=_main_kb(uid)
            )
        except Exception:
            pass

    bot.answer_callback_query(call.id)


# ─── Komut: /ping ─────────────────────────────────────────────────────────────

@bot.message_handler(commands=['ping'])
def cmd_ping(message):
    uid = message.from_user.id
    if spam_guard.is_spam(uid):
        bot.reply_to(message, tr('spam_warn', uid))
        return
    t0  = time.time()
    msg = bot.reply_to(message, "🏓 ...")
    ms  = max(1, round((time.time() - t0) * 1000))
    bot.edit_message_text(tr('ping_msg', uid, ms=ms), msg.chat.id, msg.message_id)


# ─── Komut: /uptime ───────────────────────────────────────────────────────────

@bot.message_handler(commands=['uptime'])
def cmd_uptime(message):
    uid = message.from_user.id
    if spam_guard.is_spam(uid):
        bot.reply_to(message, tr('spam_warn', uid))
        return
    bot.reply_to(message, tr('uptime_msg', uid, uptime=_fmt_uptime()))


# ─── Komut: /bothakinda ───────────────────────────────────────────────────────

@bot.message_handler(commands=['bothakinda'])
def cmd_about(message):
    uid = message.from_user.id
    if spam_guard.is_spam(uid):
        bot.reply_to(message, tr('spam_warn', uid))
        return
    bot.reply_to(message, tr('about_msg', uid), reply_markup=_about_kb(uid))


# ─── Komut: /platforms ────────────────────────────────────────────────────────

@bot.message_handler(commands=['platforms'])
def cmd_platforms(message):
    uid = message.from_user.id
    if spam_guard.is_spam(uid):
        bot.reply_to(message, tr('spam_warn', uid))
        return
    bot.reply_to(message, tr('platforms_msg', uid))


# ─── URL algılama & video indirme ─────────────────────────────────────────────

_URL_RE = re.compile(r'https?://[^\s]+')

@bot.message_handler(func=lambda m: bool(_URL_RE.search(m.text or '')))
def handle_url(message):
    uid = message.from_user.id

    if spam_guard.is_spam(uid):
        bot.reply_to(message, tr('spam_warn', uid))
        return

    url = _URL_RE.search(message.text).group()
    send_log(bot, 'link', message.from_user, state.get(uid), link=url)

    status = bot.reply_to(message, tr('downloading', uid))

    result = downloader.download(url, uid)

    if result['success']:
        path      = result['path']
        file_size = os.path.getsize(path)

        if file_size > config.MAX_FILE_SIZE:
            bot.edit_message_text(
                tr('file_too_large', uid),
                status.chat.id, status.message_id
            )
            os.remove(path)
            return

        send_type = downloader.get_send_type(path)
        try:
            with open(path, 'rb') as f:
                if send_type == 'video':
                    bot.send_video(message.chat.id, f,
                                   reply_to_message_id=message.message_id,
                                   supports_streaming=True)
                elif send_type == 'photo':
                    bot.send_photo(message.chat.id, f,
                                   reply_to_message_id=message.message_id)
                elif send_type == 'audio':
                    bot.send_audio(message.chat.id, f,
                                   reply_to_message_id=message.message_id)
                else:
                    bot.send_document(message.chat.id, f,
                                      reply_to_message_id=message.message_id)

            send_log(bot, 'dl_success', message.from_user, state.get(uid), link=url)
            try:
                bot.delete_message(status.chat.id, status.message_id)
            except Exception:
                pass

        except Exception as e:
            bot.edit_message_text(
                f"❌ Gönderme hatası: {str(e)[:100]}",
                status.chat.id, status.message_id
            )
        finally:
            if os.path.exists(path):
                os.remove(path)

    else:
        err = result.get('error', '')
        if err == 'too_large':
            bot.edit_message_text(tr('file_too_large', uid),
                                  status.chat.id, status.message_id)
        else:
            bot.edit_message_text(tr('download_fail', uid),
                                  status.chat.id, status.message_id)
        send_log(bot, 'dl_fail', message.from_user, state.get(uid),
                 link=url, extra=err[:100])


# ─── Admin komutlarını kaydet ─────────────────────────────────────────────────

admin_cmds.register(bot)


# ─── Başlat ───────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print(f"🚀 {config.BOT_NAME} v{config.VERSION} başlatılıyor...")
    print(f"🔑 Admin IDs : {config.ADMIN_IDS}")
    print(f"📢 Log Kanal : {config.LOG_CHANNEL}")
    print(f"🌐 Flask     : http://0.0.0.0:{os.environ.get('PORT', 8080)}")

    Thread(target=_run_flask, daemon=True).start()

    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except KeyboardInterrupt:
        print("\n⛔ Bot kapatılıyor...")
