"""
admin_cmds.py — Gizli Admin Komutları
/adminlist /kban /banu /mute /umute /log
"""
import time
import config
import state
import languages as L
from log_helper import send_log
import telebot.types as types


# ─── Yardımcı fonksiyonlar ───────────────────────────────────────────────────

def _tr(key: str, user_id: int, **kw) -> str:
    return L.t(key, state.get(user_id), **kw)


def _target(message) -> object | None:
    """Reply yapılan mesajın sahibini döndür."""
    if message.reply_to_message:
        return message.reply_to_message.from_user
    return None


def _parse_dur(s: str) -> int:
    """'1h', '30m', '2d' → saniye cinsinden int"""
    if not s:
        return 3600
    unit_map = {'m': 60, 'h': 3600, 'd': 86400, 's': 1}
    try:
        unit  = s[-1].lower()
        value = int(s[:-1])
        return value * unit_map.get(unit, 60)
    except Exception:
        return 3600


def _dur_label(secs: int) -> str:
    if secs >= 86400:
        return f"{secs // 86400}g"
    if secs >= 3600:
        return f"{secs // 3600}s"
    return f"{secs // 60}d"


# ─── Kayıt fonksiyonu ─────────────────────────────────────────────────────────

def register(bot: telebot.TeleBot) -> None:  # type: ignore[name-defined]

    # ── /adminlist ──────────────────────────────────────────────────────────
    @bot.message_handler(commands=['adminlist'])
    def cmd_adminlist(message):
        uid = message.from_user.id
        if uid not in config.ADMIN_IDS:
            return  # sessizce yoksay

        text = (
            "🔐 *Gizli Admin Komutları*\n"
            "━━━━━━━━━━━━━━━━━━━\n"
            "🔨 `/kban` — Kullanıcıyı banla *(yanıtla)*\n"
            "✅ `/banu` — Ban kaldır *(yanıtla)*\n"
            "🔇 `/mute [süre]` — Sustur *(örn: /mute 1h)*\n"
            "🔊 `/umute` — Susturma kaldır *(yanıtla)*\n"
            "📋 `/log [mesaj]` — Kanala log gönder\n"
            "━━━━━━━━━━━━━━━━━━━\n"
            "_Süre formatları: 30m • 1h • 12h • 1d • 7d_\n\n"
            f"👨‍💻 Kurucu: {config.FOUNDER_USERNAME}\n"
            f"📢 Kanal: {config.CHANNEL_USERNAME}"
        )
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
        bot.reply_to(message, text, reply_markup=kb)

    # ── /kban ───────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['kban'])
    def cmd_kban(message):
        uid = message.from_user.id
        if uid not in config.ADMIN_IDS:
            return

        target = _target(message)
        if not target:
            bot.reply_to(message, _tr('no_reply', uid))
            return
        try:
            bot.ban_chat_member(message.chat.id, target.id)
            bot.reply_to(
                message,
                _tr('user_banned', uid, user=target.first_name, uid=target.id),
            )
            send_log(bot, 'kban', message.from_user,
                     state.get(uid), target=target)
        except Exception as e:
            bot.reply_to(message, f"❌ Hata: {str(e)[:150]}")

    # ── /banu ───────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['banu'])
    def cmd_banu(message):
        uid = message.from_user.id
        if uid not in config.ADMIN_IDS:
            return

        target = _target(message)
        if not target:
            bot.reply_to(message, _tr('no_reply', uid))
            return
        try:
            bot.unban_chat_member(message.chat.id, target.id)
            bot.reply_to(
                message,
                _tr('user_unbanned', uid, user=target.first_name, uid=target.id),
            )
            send_log(bot, 'banu', message.from_user,
                     state.get(uid), target=target)
        except Exception as e:
            bot.reply_to(message, f"❌ Hata: {str(e)[:150]}")

    # ── /mute ───────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['mute'])
    def cmd_mute(message):
        uid = message.from_user.id
        if uid not in config.ADMIN_IDS:
            return

        target = _target(message)
        if not target:
            bot.reply_to(message, _tr('no_reply', uid))
            return

        parts    = message.text.split()
        dur_str  = parts[1] if len(parts) > 1 else '1h'
        dur_secs = _parse_dur(dur_str)
        until    = int(time.time()) + dur_secs

        try:
            perms = types.ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_polls=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False,
            )
            bot.restrict_chat_member(
                message.chat.id, target.id, perms, until_date=until
            )
            label = _dur_label(dur_secs)
            bot.reply_to(
                message,
                _tr('user_muted', uid,
                    user=target.first_name, uid=target.id, dur=label),
            )
            send_log(bot, 'mute', message.from_user,
                     state.get(uid), target=target, extra=label)
        except Exception as e:
            bot.reply_to(message, f"❌ Hata: {str(e)[:150]}")

    # ── /umute ──────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['umute'])
    def cmd_umute(message):
        uid = message.from_user.id
        if uid not in config.ADMIN_IDS:
            return

        target = _target(message)
        if not target:
            bot.reply_to(message, _tr('no_reply', uid))
            return

        try:
            perms = types.ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_polls=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
            )
            bot.restrict_chat_member(message.chat.id, target.id, perms)
            bot.reply_to(
                message,
                _tr('user_unmuted', uid,
                    user=target.first_name, uid=target.id),
            )
            send_log(bot, 'umute', message.from_user,
                     state.get(uid), target=target)
        except Exception as e:
            bot.reply_to(message, f"❌ Hata: {str(e)[:150]}")

    # ── /log ────────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['log'])
    def cmd_log(message):
        uid = message.from_user.id
        if uid not in config.ADMIN_IDS:
            return

        text = message.text[4:].strip() or "Manuel log kaydı"
        send_log(
            bot, 'manual', message.from_user,
            state.get(uid), extra=text
        )
        bot.reply_to(message, "✅ Log kanalına gönderildi!")
