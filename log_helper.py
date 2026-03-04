"""
log_helper.py — Log kanalına detaylı mesaj gönderir
"""
from datetime import datetime
import config

# Dil kodundan ülke tahmini
LANG_COUNTRY = {
    'tr': '🇹🇷 Türkiye',
    'en': '🇺🇸 Global/USA',
    'es': '🇪🇸 İspanya/Güney Amerika',
    'fr': '🇫🇷 Fransa',
    'de': '🇩🇪 Almanya',
    'ru': '🇷🇺 Rusya',
    'pt': '🇧🇷 Brezilya/Portekiz',
    'ar': '🇸🇦 Arap Bölgesi',
    'ja': '🇯🇵 Japonya',
    'ko': '🇰🇷 Kore',
}

LOG_ICONS = {
    'bot_start':   '🟢 Bot Başlatıldı',
    'bot_stop':    '🔴 Bot Kapatıldı',
    'lang_set':    '🌍 Dil Seçildi',
    'link':        '🔗 Link Gönderildi',
    'dl_success':  '✅ İndirme Başarılı',
    'dl_fail':     '❌ İndirme Başarısız',
    'kban':        '🔨 Kullanıcı Banlandı',
    'banu':        '✅ Ban Kaldırıldı',
    'mute':        '🔇 Kullanıcı Susturuldu',
    'umute':       '🔊 Susturma Kaldırıldı',
    'manual':      '📋 Manuel Log',
    'channel_add': '📢 Kanala Eklendi',
}


def send_log(
    bot,
    action: str,
    user,
    lang: str = 'tr',
    link: str = None,
    target=None,
    extra: str = None,
) -> None:
    """Log kanalına formatlı mesaj gönderir."""
    try:
        now     = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        country = LANG_COUNTRY.get(lang, '🌍 Bilinmiyor')
        title   = LOG_ICONS.get(action, '📋 Log')
        uname   = f"@{user.username}" if getattr(user, 'username', None) else "—"
        lname   = getattr(user, 'last_name', '') or ''

        text = (
            f"{title}\n"
            f"{'─' * 32}\n"
            f"👤 *Kim:* [{user.first_name}](tg://user?id={user.id})\n"
            f"📝 *İsim:* {user.first_name} {lname}".strip() + "\n"
            f"🆔 *ID:* `{user.id}`\n"
            f"📱 *Username:* {uname}\n"
            f"🌍 *Dil:* `{lang.upper()}`\n"
            f"🗺️ *Ülke:* {country}\n"
            f"⏰ *Zaman:* `{now}`\n"
        )

        if link:
            short_link = link[:120] + ('...' if len(link) > 120 else '')
            text += f"🔗 *Link:* `{short_link}`\n"

        if target:
            tname = getattr(target, 'first_name', '?')
            text += f"🎯 *Hedef:* [{tname}](tg://user?id={target.id}) (`{target.id}`)\n"

        if extra:
            text += f"ℹ️ *Detay:* {extra}\n"

        text += f"{'─' * 32}"

        bot.send_message(
            config.LOG_CHANNEL,
            text,
            parse_mode='Markdown',
            disable_web_page_preview=True,
        )
    except Exception as e:
        print(f"[log] Gönderilemedi: {e}")
