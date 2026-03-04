# ─────────────────────────────────────────────
#  NikeBot – Dil Dosyası  (10 dil)
# ─────────────────────────────────────────────

LANGUAGES = {

    # ── Türkçe ──────────────────────────────
    'tr': {
        'flag': '🇹🇷', 'name': 'Türkçe',
        'select_lang':      '🌍 Lütfen dilinizi seçin:',
        'lang_set':         '✅ Dil Türkçe olarak ayarlandı!',
        'welcome':          '👋 Merhaba *{name}*!\n\n🤖 Ben *NikeBot* — çok amaçlı Telegram botuyum!\n\n📥 Sosyal medya videolarını indir, grubu yönet.\n\n👇 Bir seçenek seç:',
        'main_menu':        '🏠 Ana Menü',
        'btn_download':     '📥 Video İndir',
        'btn_about':        'ℹ️ Bot Hakkında',
        'btn_lang':         '🌍 Dil Değiştir',
        'btn_help':         '❓ Yardım',
        'btn_ping':         '🏓 Ping',
        'btn_uptime':       '⏱ Uptime',
        'btn_back':         '🔙 Geri',
        'btn_platforms':    '📱 Platformlar',
        'download_prompt':  '📎 İndirmek istediğin video linkini gönder:\n\n📱 Desteklenen platformlar için /platforms yaz.',
        'downloading':      '⏳ İndiriliyor, lütfen bekle...',
        'download_success': '✅ Video başarıyla indirildi!',
        'download_fail':    '❌ İndirme başarısız!\nLink geçersiz veya desteklenmiyor.',
        'file_too_large':   '❌ Dosya 50MB sınırını aşıyor!',
        'spam_warn':        '⚠️ Lütfen 3 saniye bekle!',
        'ping_msg':         '🏓 Pong! `{ms}ms`',
        'uptime_msg':       '⏱ *Bot Uptime:* `{uptime}`',
        'about_msg':        (
            '🤖 *NikeBot Hakkında*\n'
            '━━━━━━━━━━━━━━━━━━━\n'
            '📌 *İsim:* NikeBot\n'
            '💡 *Versiyon:* 1.0.0\n'
            '👨‍💻 *Kurucu:* @nikecheatyeniden\n'
            '📢 *Kanal:* @nikestoretr\n'
            '━━━━━━━━━━━━━━━━━━━\n'
            '🔧 *Özellikler:*\n'
            '• 50+ platformdan video indirme\n'
            '• 10 dil desteği\n'
            '• Spam koruması (3sn)\n'
            '• Grup yönetim araçları\n'
            '• Log sistemi'
        ),
        'platforms_msg':    (
            '📱 *Desteklenen Platformlar (50+)*\n'
            '━━━━━━━━━━━━━━━━━━━\n'
            'TikTok • Instagram • YouTube • YouTube Shorts\n'
            'Twitter/X • Facebook • Reddit • Pinterest\n'
            'Vimeo • Dailymotion • Twitch • Kick\n'
            'SoundCloud • Spotify* • LinkedIn • Snapchat\n'
            'Bilibili • VK • OK.ru • Rumble • Odysee\n'
            'Triller • Likee • Kwai • Bigo Live • YY\n'
            'Niconico • Huya • Douyu • MX TakaTak\n'
            'Weibo • Moj • ShareChat • Chingari\n'
            'Meipai • Streamable • Gfycat • Imgur\n'
            'Telegram • Discord* • Mixcloud • Bandcamp\n'
            '━━━━━━━━━━━━━━━━━━━\n'
            '_* bazı kısıtlamalar olabilir_'
        ),
        'help_msg':         (
            '❓ *Yardım Menüsü*\n'
            '━━━━━━━━━━━━━━━━━━━\n'
            '📥 *Video İndir:* Link gönder, video gelsin!\n\n'
            '⚙️ *Komutlar:*\n'
            '/start — Botu başlat\n'
            '/ping — Ping/gecikme ölçümü\n'
            '/uptime — Bot çalışma süresi\n'
            '/bothakinda — Bot hakkında bilgi\n'
            '/platforms — Desteklenen platformlar'
        ),
        'admin_only': '⛔ Bu komut sadece adminlere özeldir!',
        'no_reply':   '⚠️ Lütfen bir kullanıcıya yanıt ver!',
        'user_banned':   '🔨 [{user}](tg://user?id={uid}) yasaklandı!',
        'user_unbanned': '✅ [{user}](tg://user?id={uid}) yasağı kaldırıldı!',
        'user_muted':    '🔇 [{user}](tg://user?id={uid}) susturuldu! `({dur})`',
        'user_unmuted':  '🔊 [{user}](tg://user?id={uid}) susturması kaldırıldı!',
    },

    # ── English ──────────────────────────────
    'en': {
        'flag': '🇺🇸', 'name': 'English',
        'select_lang':      '🌍 Please select your language:',
        'lang_set':         '✅ Language set to English!',
        'welcome':          '👋 Hello *{name}*!\n\n🤖 I am *NikeBot* — a multi-purpose Telegram bot!\n\n📥 Download social media videos & manage groups.\n\n👇 Choose an option:',
        'main_menu':        '🏠 Main Menu',
        'btn_download':     '📥 Download Video',
        'btn_about':        'ℹ️ About Bot',
        'btn_lang':         '🌍 Change Language',
        'btn_help':         '❓ Help',
        'btn_ping':         '🏓 Ping',
        'btn_uptime':       '⏱ Uptime',
        'btn_back':         '🔙 Back',
        'btn_platforms':    '📱 Platforms',
        'download_prompt':  '📎 Send the video link you want to download:\n\n📱 Type /platforms for supported sites.',
        'downloading':      '⏳ Downloading, please wait...',
        'download_success': '✅ Video downloaded successfully!',
        'download_fail':    '❌ Download failed!\nInvalid link or not supported.',
        'file_too_large':   '❌ File exceeds 50MB limit!',
        'spam_warn':        '⚠️ Please wait 3 seconds!',
        'ping_msg':         '🏓 Pong! `{ms}ms`',
        'uptime_msg':       '⏱ *Bot Uptime:* `{uptime}`',
        'about_msg':        (
            '🤖 *About NikeBot*\n'
            '━━━━━━━━━━━━━━━━━━━\n'
            '📌 *Name:* NikeBot\n'
            '💡 *Version:* 1.0.0\n'
            '👨‍💻 *Founder:* @nikecheatyeniden\n'
            '📢 *Channel:* @nikestoretr\n'
            '━━━━━━━━━━━━━━━━━━━\n'
            '🔧 *Features:*\n'
            '• 50+ platform video download\n'
            '• 10 language support\n'
            '• Spam protection (3s)\n'
            '• Group management tools\n'
            '• Log system'
        ),
        'platforms_msg':    (
            '📱 *Supported Platforms (50+)*\n'
            '━━━━━━━━━━━━━━━━━━━\n'
            'TikTok • Instagram • YouTube • YouTube Shorts\n'
            'Twitter/X • Facebook • Reddit • Pinterest\n'
            'Vimeo • Dailymotion • Twitch • Kick\n'
            'SoundCloud • LinkedIn • Snapchat • Bilibili\n'
            'VK • OK.ru • Rumble • Odysee • Triller\n'
            'Likee • Kwai • Bigo Live • Niconico\n'
            'Huya • Douyu • Weibo • Streamable • Gfycat\n'
            'Imgur • Mixcloud • Bandcamp • and more...\n'
            '━━━━━━━━━━━━━━━━━━━\n'
            '_* some restrictions may apply_'
        ),
        'help_msg':         (
            '❓ *Help Menu*\n'
            '━━━━━━━━━━━━━━━━━━━\n'
            '📥 *Download Video:* Send a link, get the video!\n\n'
            '⚙️ *Commands:*\n'
            '/start — Start the bot\n'
            '/ping — Ping/latency check\n'
            '/uptime — Bot uptime\n'
            '/bothakinda — About the bot\n'
            '/platforms — Supported platforms'
        ),
        'admin_only': '⛔ This command is admin only!',
        'no_reply':   '⚠️ Please reply to a user!',
        'user_banned':   '🔨 [{user}](tg://user?id={uid}) has been banned!',
        'user_unbanned': '✅ [{user}](tg://user?id={uid}) has been unbanned!',
        'user_muted':    '🔇 [{user}](tg://user?id={uid}) has been muted! `({dur})`',
        'user_unmuted':  '🔊 [{user}](tg://user?id={uid}) has been unmuted!',
    },

    # ── Español ──────────────────────────────
    'es': {
        'flag': '🇪🇸', 'name': 'Español',
        'select_lang':      '🌍 Por favor selecciona tu idioma:',
        'lang_set':         '✅ ¡Idioma configurado en Español!',
        'welcome':          '👋 ¡Hola *{name}*!\n\n🤖 Soy *NikeBot* — ¡un bot de Telegram multipropósito!\n\n📥 Descarga videos de redes sociales y gestiona grupos.\n\n👇 Elige una opción:',
        'main_menu':        '🏠 Menú Principal',
        'btn_download':     '📥 Descargar Video',
        'btn_about':        'ℹ️ Sobre el Bot',
        'btn_lang':         '🌍 Cambiar Idioma',
        'btn_help':         '❓ Ayuda',
        'btn_ping':         '🏓 Ping',
        'btn_uptime':       '⏱ Uptime',
        'btn_back':         '🔙 Volver',
        'btn_platforms':    '📱 Plataformas',
        'download_prompt':  '📎 Envía el enlace del video que quieres descargar:',
        'downloading':      '⏳ Descargando, por favor espera...',
        'download_success': '✅ ¡Video descargado con éxito!',
        'download_fail':    '❌ ¡Descarga fallida!\nEnlace inválido o no soportado.',
        'file_too_large':   '❌ ¡El archivo supera el límite de 50MB!',
        'spam_warn':        '⚠️ ¡Por favor espera 3 segundos!',
        'ping_msg':         '🏓 ¡Pong! `{ms}ms`',
        'uptime_msg':       '⏱ *Uptime del Bot:* `{uptime}`',
        'about_msg':        '🤖 *Sobre NikeBot*\n━━━━━━━━━━━━━━━━━━━\n📌 *Nombre:* NikeBot\n💡 *Versión:* 1.0.0\n👨‍💻 *Fundador:* @nikecheatyeniden\n📢 *Canal:* @nikestoretr\n━━━━━━━━━━━━━━━━━━━\n🔧 *Funciones:*\n• Descarga de 50+ plataformas\n• 10 idiomas\n• Protección anti-spam\n• Gestión de grupos\n• Sistema de logs',
        'platforms_msg':    '📱 *Plataformas Soportadas (50+)*\n━━━━━━━━━━━━━━━━━━━\nTikTok • Instagram • YouTube • Twitter/X\nFacebook • Reddit • Pinterest • Vimeo\nDailymotion • Twitch • Kick • SoundCloud\ny muchas más...',
        'help_msg':         '❓ *Ayuda*\n━━━━━━━━━━━━━━━━━━━\n📥 *Descargar Video:* ¡Envía un enlace!\n\n⚙️ *Comandos:*\n/start — Iniciar bot\n/ping — Verificar ping\n/uptime — Tiempo activo\n/bothakinda — Sobre el bot\n/platforms — Plataformas',
        'admin_only': '⛔ ¡Este comando es solo para admins!',
        'no_reply':   '⚠️ ¡Por favor responde a un usuario!',
        'user_banned':   '🔨 [{user}](tg://user?id={uid}) ha sido baneado!',
        'user_unbanned': '✅ [{user}](tg://user?id={uid}) ha sido desbaneado!',
        'user_muted':    '🔇 [{user}](tg://user?id={uid}) ha sido silenciado! `({dur})`',
        'user_unmuted':  '🔊 [{user}](tg://user?id={uid}) ha sido dessilenciado!',
    },

    # ── Français ──────────────────────────────
    'fr': {
        'flag': '🇫🇷', 'name': 'Français',
        'select_lang':      '🌍 Veuillez sélectionner votre langue:',
        'lang_set':         '✅ Langue définie en Français!',
        'welcome':          '👋 Bonjour *{name}*!\n\n🤖 Je suis *NikeBot* — un bot Telegram polyvalent!\n\n📥 Téléchargez des vidéos et gérez vos groupes.\n\n👇 Choisissez une option:',
        'main_menu':        '🏠 Menu Principal',
        'btn_download':     '📥 Télécharger Vidéo',
        'btn_about':        'ℹ️ À Propos',
        'btn_lang':         '🌍 Changer Langue',
        'btn_help':         '❓ Aide',
        'btn_ping':         '🏓 Ping',
        'btn_uptime':       '⏱ Uptime',
        'btn_back':         '🔙 Retour',
        'btn_platforms':    '📱 Plateformes',
        'download_prompt':  '📎 Envoyez le lien de la vidéo à télécharger:',
        'downloading':      '⏳ Téléchargement en cours...',
        'download_success': '✅ Vidéo téléchargée avec succès!',
        'download_fail':    '❌ Échec du téléchargement!\nLien invalide ou non supporté.',
        'file_too_large':   '❌ Fichier dépasse la limite de 50MB!',
        'spam_warn':        '⚠️ Veuillez attendre 3 secondes!',
        'ping_msg':         '🏓 Pong! `{ms}ms`',
        'uptime_msg':       '⏱ *Uptime du Bot:* `{uptime}`',
        'about_msg':        '🤖 *À Propos de NikeBot*\n━━━━━━━━━━━━━━━━━━━\n📌 *Nom:* NikeBot\n💡 *Version:* 1.0.0\n👨‍💻 *Fondateur:* @nikecheatyeniden\n📢 *Canal:* @nikestoretr\n━━━━━━━━━━━━━━━━━━━\n🔧 *Fonctionnalités:*\n• Téléchargement 50+ plateformes\n• 10 langues\n• Protection anti-spam\n• Gestion de groupe\n• Système de logs',
        'platforms_msg':    '📱 *Plateformes Supportées (50+)*\n━━━━━━━━━━━━━━━━━━━\nTikTok • Instagram • YouTube • Twitter/X\nFacebook • Reddit • Pinterest • Vimeo\nDailymotion • Twitch • Kick • SoundCloud\net bien plus...',
        'help_msg':         '❓ *Aide*\n━━━━━━━━━━━━━━━━━━━\n📥 *Télécharger Vidéo:* Envoyez un lien!\n\n⚙️ *Commandes:*\n/start — Démarrer le bot\n/ping — Vérifier le ping\n/uptime — Temps de fonctionnement\n/bothakinda — À propos\n/platforms — Plateformes',
        'admin_only': '⛔ Cette commande est réservée aux admins!',
        'no_reply':   '⚠️ Veuillez répondre à un utilisateur!',
        'user_banned':   '🔨 [{user}](tg://user?id={uid}) a été banni!',
        'user_unbanned': '✅ [{user}](tg://user?id={uid}) a été débanni!',
        'user_muted':    '🔇 [{user}](tg://user?id={uid}) mis en sourdine! `({dur})`',
        'user_unmuted':  '🔊 [{user}](tg://user?id={uid}) réactivé!',
    },

    # ── Deutsch ──────────────────────────────
    'de': {
        'flag': '🇩🇪', 'name': 'Deutsch',
        'select_lang':      '🌍 Bitte wähle deine Sprache:',
        'lang_set':         '✅ Sprache auf Deutsch eingestellt!',
        'welcome':          '👋 Hallo *{name}*!\n\n🤖 Ich bin *NikeBot* — ein vielseitiger Telegram-Bot!\n\n📥 Lade Videos herunter und verwalte Gruppen.\n\n👇 Wähle eine Option:',
        'main_menu':        '🏠 Hauptmenü',
        'btn_download':     '📥 Video herunterladen',
        'btn_about':        'ℹ️ Über den Bot',
        'btn_lang':         '🌍 Sprache ändern',
        'btn_help':         '❓ Hilfe',
        'btn_ping':         '🏓 Ping',
        'btn_uptime':       '⏱ Uptime',
        'btn_back':         '🔙 Zurück',
        'btn_platforms':    '📱 Plattformen',
        'download_prompt':  '📎 Sende den Video-Link zum Herunterladen:',
        'downloading':      '⏳ Wird heruntergeladen...',
        'download_success': '✅ Video erfolgreich heruntergeladen!',
        'download_fail':    '❌ Download fehlgeschlagen!\nLink ungültig oder nicht unterstützt.',
        'file_too_large':   '❌ Datei überschreitet 50MB Limit!',
        'spam_warn':        '⚠️ Bitte warte 3 Sekunden!',
        'ping_msg':         '🏓 Pong! `{ms}ms`',
        'uptime_msg':       '⏱ *Bot-Uptime:* `{uptime}`',
        'about_msg':        '🤖 *Über NikeBot*\n━━━━━━━━━━━━━━━━━━━\n📌 *Name:* NikeBot\n💡 *Version:* 1.0.0\n👨‍💻 *Gründer:* @nikecheatyeniden\n📢 *Kanal:* @nikestoretr\n━━━━━━━━━━━━━━━━━━━\n🔧 *Funktionen:*\n• 50+ Plattform-Downloads\n• 10 Sprachen\n• Spam-Schutz\n• Gruppenverwaltung\n• Log-System',
        'platforms_msg':    '📱 *Unterstützte Plattformen (50+)*\n━━━━━━━━━━━━━━━━━━━\nTikTok • Instagram • YouTube • Twitter/X\nFacebook • Reddit • Pinterest • Vimeo\nDailymotion • Twitch • Kick • SoundCloud\nund viele mehr...',
        'help_msg':         '❓ *Hilfe*\n━━━━━━━━━━━━━━━━━━━\n📥 *Video herunterladen:* Link senden!\n\n⚙️ *Befehle:*\n/start — Bot starten\n/ping — Ping prüfen\n/uptime — Laufzeit\n/bothakinda — Über den Bot\n/platforms — Plattformen',
        'admin_only': '⛔ Dieser Befehl ist nur für Admins!',
        'no_reply':   '⚠️ Bitte antworte einem Benutzer!',
        'user_banned':   '🔨 [{user}](tg://user?id={uid}) wurde gebannt!',
        'user_unbanned': '✅ [{user}](tg://user?id={uid}) wurde entbannt!',
        'user_muted':    '🔇 [{user}](tg://user?id={uid}) stummgeschaltet! `({dur})`',
        'user_unmuted':  '🔊 [{user}](tg://user?id={uid}) entstummgeschaltet!',
    },

    # ── Русский ──────────────────────────────
    'ru': {
        'flag': '🇷🇺', 'name': 'Русский',
        'select_lang':      '🌍 Пожалуйста, выберите язык:',
        'lang_set':         '✅ Язык установлен на Русский!',
        'welcome':          '👋 Привет *{name}*!\n\n🤖 Я *NikeBot* — многофункциональный Telegram бот!\n\n📥 Скачивай видео и управляй группами.\n\n👇 Выбери опцию:',
        'main_menu':        '🏠 Главное Меню',
        'btn_download':     '📥 Скачать Видео',
        'btn_about':        'ℹ️ О Боте',
        'btn_lang':         '🌍 Сменить Язык',
        'btn_help':         '❓ Помощь',
        'btn_ping':         '🏓 Пинг',
        'btn_uptime':       '⏱ Аптайм',
        'btn_back':         '🔙 Назад',
        'btn_platforms':    '📱 Платформы',
        'download_prompt':  '📎 Отправь ссылку на видео для скачивания:',
        'downloading':      '⏳ Скачивание, подожди...',
        'download_success': '✅ Видео успешно скачано!',
        'download_fail':    '❌ Ошибка загрузки!\nСсылка недействительна или не поддерживается.',
        'file_too_large':   '❌ Файл превышает лимит 50MB!',
        'spam_warn':        '⚠️ Подожди 3 секунды!',
        'ping_msg':         '🏓 Понг! `{ms}ms`',
        'uptime_msg':       '⏱ *Аптайм Бота:* `{uptime}`',
        'about_msg':        '🤖 *О NikeBot*\n━━━━━━━━━━━━━━━━━━━\n📌 *Имя:* NikeBot\n💡 *Версия:* 1.0.0\n👨‍💻 *Основатель:* @nikecheatyeniden\n📢 *Канал:* @nikestoretr\n━━━━━━━━━━━━━━━━━━━\n🔧 *Функции:*\n• Скачивание с 50+ платформ\n• 10 языков\n• Защита от спама\n• Управление группой\n• Система логов',
        'platforms_msg':    '📱 *Поддерживаемые Платформы (50+)*\n━━━━━━━━━━━━━━━━━━━\nTikTok • Instagram • YouTube • Twitter/X\nFacebook • Reddit • Pinterest • Vimeo\nDailymotion • Twitch • Kick • SoundCloud\nи многое другое...',
        'help_msg':         '❓ *Помощь*\n━━━━━━━━━━━━━━━━━━━\n📥 *Скачать Видео:* Отправь ссылку!\n\n⚙️ *Команды:*\n/start — Запустить бота\n/ping — Проверка пинга\n/uptime — Время работы\n/bothakinda — О боте\n/platforms — Платформы',
        'admin_only': '⛔ Эта команда только для администраторов!',
        'no_reply':   '⚠️ Пожалуйста, ответьте на сообщение!',
        'user_banned':   '🔨 [{user}](tg://user?id={uid}) заблокирован!',
        'user_unbanned': '✅ [{user}](tg://user?id={uid}) разблокирован!',
        'user_muted':    '🔇 [{user}](tg://user?id={uid}) замолчан! `({dur})`',
        'user_unmuted':  '🔊 [{user}](tg://user?id={uid}) размолчан!',
    },

    # ── Português ──────────────────────────────
    'pt': {
        'flag': '🇧🇷', 'name': 'Português',
        'select_lang':      '🌍 Por favor selecione seu idioma:',
        'lang_set':         '✅ Idioma definido para Português!',
        'welcome':          '👋 Olá *{name}*!\n\n🤖 Sou o *NikeBot* — um bot Telegram multifuncional!\n\n📥 Baixe vídeos de redes sociais e gerencie grupos.\n\n👇 Escolha uma opção:',
        'main_menu':        '🏠 Menu Principal',
        'btn_download':     '📥 Baixar Vídeo',
        'btn_about':        'ℹ️ Sobre o Bot',
        'btn_lang':         '🌍 Mudar Idioma',
        'btn_help':         '❓ Ajuda',
        'btn_ping':         '🏓 Ping',
        'btn_uptime':       '⏱ Uptime',
        'btn_back':         '🔙 Voltar',
        'btn_platforms':    '📱 Plataformas',
        'download_prompt':  '📎 Envie o link do vídeo para baixar:',
        'downloading':      '⏳ Baixando, aguarde...',
        'download_success': '✅ Vídeo baixado com sucesso!',
        'download_fail':    '❌ Falha no download!\nLink inválido ou não suportado.',
        'file_too_large':   '❌ Arquivo supera o limite de 50MB!',
        'spam_warn':        '⚠️ Por favor aguarde 3 segundos!',
        'ping_msg':         '🏓 Pong! `{ms}ms`',
        'uptime_msg':       '⏱ *Uptime do Bot:* `{uptime}`',
        'about_msg':        '🤖 *Sobre o NikeBot*\n━━━━━━━━━━━━━━━━━━━\n📌 *Nome:* NikeBot\n💡 *Versão:* 1.0.0\n👨‍💻 *Fundador:* @nikecheatyeniden\n📢 *Canal:* @nikestoretr\n━━━━━━━━━━━━━━━━━━━\n🔧 *Funcionalidades:*\n• Download de 50+ plataformas\n• 10 idiomas\n• Proteção anti-spam\n• Gestão de grupo\n• Sistema de logs',
        'platforms_msg':    '📱 *Plataformas Suportadas (50+)*\n━━━━━━━━━━━━━━━━━━━\nTikTok • Instagram • YouTube • Twitter/X\nFacebook • Reddit • Pinterest • Vimeo\nDailymotion • Twitch • Kick • SoundCloud\ne muito mais...',
        'help_msg':         '❓ *Ajuda*\n━━━━━━━━━━━━━━━━━━━\n📥 *Baixar Vídeo:* Envie um link!\n\n⚙️ *Comandos:*\n/start — Iniciar bot\n/ping — Verificar ping\n/uptime — Tempo ativo\n/bothakinda — Sobre o bot\n/platforms — Plataformas',
        'admin_only': '⛔ Este comando é apenas para admins!',
        'no_reply':   '⚠️ Por favor responda a um usuário!',
        'user_banned':   '🔨 [{user}](tg://user?id={uid}) foi banido!',
        'user_unbanned': '✅ [{user}](tg://user?id={uid}) foi desbanido!',
        'user_muted':    '🔇 [{user}](tg://user?id={uid}) silenciado! `({dur})`',
        'user_unmuted':  '🔊 [{user}](tg://user?id={uid}) dessilenciado!',
    },

    # ── العربية ──────────────────────────────
    'ar': {
        'flag': '🇸🇦', 'name': 'العربية',
        'select_lang':      '🌍 الرجاء اختيار لغتك:',
        'lang_set':         '✅ تم تعيين اللغة إلى العربية!',
        'welcome':          '👋 مرحباً *{name}*!\n\n🤖 أنا *NikeBot* — بوت تيليغرام متعدد الأغراض!\n\n📥 نزّل مقاطع الفيديو وأدر مجموعاتك.\n\n👇 اختر خياراً:',
        'main_menu':        '🏠 القائمة الرئيسية',
        'btn_download':     '📥 تنزيل فيديو',
        'btn_about':        'ℹ️ حول البوت',
        'btn_lang':         '🌍 تغيير اللغة',
        'btn_help':         '❓ مساعدة',
        'btn_ping':         '🏓 بينغ',
        'btn_uptime':       '⏱ وقت التشغيل',
        'btn_back':         '🔙 رجوع',
        'btn_platforms':    '📱 المنصات',
        'download_prompt':  '📎 أرسل رابط الفيديو للتنزيل:',
        'downloading':      '⏳ جارٍ التنزيل...',
        'download_success': '✅ تم تنزيل الفيديو بنجاح!',
        'download_fail':    '❌ فشل التنزيل!\nالرابط غير صالح أو غير مدعوم.',
        'file_too_large':   '❌ الملف يتجاوز حد 50MB!',
        'spam_warn':        '⚠️ الرجاء الانتظار 3 ثوانٍ!',
        'ping_msg':         '🏓 بونغ! `{ms}ms`',
        'uptime_msg':       '⏱ *وقت تشغيل البوت:* `{uptime}`',
        'about_msg':        '🤖 *حول NikeBot*\n━━━━━━━━━━━━━━━━━━━\n📌 *الاسم:* NikeBot\n💡 *الإصدار:* 1.0.0\n👨‍💻 *المؤسس:* @nikecheatyeniden\n📢 *القناة:* @nikestoretr\n━━━━━━━━━━━━━━━━━━━\n🔧 *المميزات:*\n• تنزيل من 50+ منصة\n• 10 لغات\n• حماية من السبام\n• إدارة المجموعات\n• نظام تسجيل',
        'platforms_msg':    '📱 *المنصات المدعومة (50+)*\n━━━━━━━━━━━━━━━━━━━\nTikTok • Instagram • YouTube • Twitter/X\nFacebook • Reddit • Pinterest • Vimeo\nDailymotion • Twitch • Kick • SoundCloud\nوالمزيد...',
        'help_msg':         '❓ *مساعدة*\n━━━━━━━━━━━━━━━━━━━\n📥 *تنزيل فيديو:* أرسل رابطاً!\n\n⚙️ *الأوامر:*\n/start — تشغيل البوت\n/ping — فحص البينغ\n/uptime — وقت التشغيل\n/bothakinda — حول البوت\n/platforms — المنصات',
        'admin_only': '⛔ هذا الأمر للمشرفين فقط!',
        'no_reply':   '⚠️ الرجاء الرد على رسالة مستخدم!',
        'user_banned':   '🔨 [{user}](tg://user?id={uid}) تم حظره!',
        'user_unbanned': '✅ [{user}](tg://user?id={uid}) تم رفع حظره!',
        'user_muted':    '🔇 [{user}](tg://user?id={uid}) تم كتمه! `({dur})`',
        'user_unmuted':  '🔊 [{user}](tg://user?id={uid}) تم إلغاء كتمه!',
    },

    # ── 日本語 ──────────────────────────────
    'ja': {
        'flag': '🇯🇵', 'name': '日本語',
        'select_lang':      '🌍 言語を選択してください:',
        'lang_set':         '✅ 言語を日本語に設定しました!',
        'welcome':          '👋 こんにちは *{name}*!\n\n🤖 私は *NikeBot* — 多目的Telegramボットです!\n\n📥 動画をダウンロードしてグループを管理しましょう。\n\n👇 オプションを選んでください:',
        'main_menu':        '🏠 メインメニュー',
        'btn_download':     '📥 動画ダウンロード',
        'btn_about':        'ℹ️ ボットについて',
        'btn_lang':         '🌍 言語変更',
        'btn_help':         '❓ ヘルプ',
        'btn_ping':         '🏓 ピング',
        'btn_uptime':       '⏱ 稼働時間',
        'btn_back':         '🔙 戻る',
        'btn_platforms':    '📱 プラットフォーム',
        'download_prompt':  '📎 動画リンクを送信してください:',
        'downloading':      '⏳ ダウンロード中...',
        'download_success': '✅ 動画のダウンロードに成功しました!',
        'download_fail':    '❌ ダウンロード失敗!\nリンクが無効またはサポートされていません。',
        'file_too_large':   '❌ ファイルが50MBを超えています!',
        'spam_warn':        '⚠️ 3秒お待ちください!',
        'ping_msg':         '🏓 ポン! `{ms}ms`',
        'uptime_msg':       '⏱ *ボット稼働時間:* `{uptime}`',
        'about_msg':        '🤖 *NikeBotについて*\n━━━━━━━━━━━━━━━━━━━\n📌 *名前:* NikeBot\n💡 *バージョン:* 1.0.0\n👨‍💻 *創設者:* @nikecheatyeniden\n📢 *チャンネル:* @nikestoretr\n━━━━━━━━━━━━━━━━━━━\n🔧 *機能:*\n• 50+プラットフォームからダウンロード\n• 10言語対応\n• スパム保護\n• グループ管理\n• ログシステム',
        'platforms_msg':    '📱 *対応プラットフォーム (50+)*\n━━━━━━━━━━━━━━━━━━━\nTikTok • Instagram • YouTube • Twitter/X\nFacebook • Reddit • Pinterest • Vimeo\nDailymotion • Twitch • Kick • SoundCloud\nその他多数...',
        'help_msg':         '❓ *ヘルプ*\n━━━━━━━━━━━━━━━━━━━\n📥 *動画ダウンロード:* リンクを送信!\n\n⚙️ *コマンド:*\n/start — ボット開始\n/ping — ピング確認\n/uptime — 稼働時間\n/bothakinda — ボットについて\n/platforms — プラットフォーム',
        'admin_only': '⛔ このコマンドは管理者専用です!',
        'no_reply':   '⚠️ ユーザーに返信してください!',
        'user_banned':   '🔨 [{user}](tg://user?id={uid}) がBANされました!',
        'user_unbanned': '✅ [{user}](tg://user?id={uid}) のBANが解除されました!',
        'user_muted':    '🔇 [{user}](tg://user?id={uid}) がミュートされました! `({dur})`',
        'user_unmuted':  '🔊 [{user}](tg://user?id={uid}) のミュートが解除されました!',
    },

    # ── 한국어 ──────────────────────────────
    'ko': {
        'flag': '🇰🇷', 'name': '한국어',
        'select_lang':      '🌍 언어를 선택하세요:',
        'lang_set':         '✅ 언어가 한국어로 설정되었습니다!',
        'welcome':          '👋 안녕하세요 *{name}*!\n\n🤖 저는 *NikeBot* — 다목적 Telegram 봇입니다!\n\n📥 소셜 미디어 동영상을 다운로드하고 그룹을 관리하세요.\n\n👇 옵션을 선택하세요:',
        'main_menu':        '🏠 메인 메뉴',
        'btn_download':     '📥 동영상 다운로드',
        'btn_about':        'ℹ️ 봇 정보',
        'btn_lang':         '🌍 언어 변경',
        'btn_help':         '❓ 도움말',
        'btn_ping':         '🏓 핑',
        'btn_uptime':       '⏱ 업타임',
        'btn_back':         '🔙 뒤로',
        'btn_platforms':    '📱 플랫폼',
        'download_prompt':  '📎 다운로드할 동영상 링크를 보내세요:',
        'downloading':      '⏳ 다운로드 중...',
        'download_success': '✅ 동영상이 성공적으로 다운로드되었습니다!',
        'download_fail':    '❌ 다운로드 실패!\n링크가 유효하지 않거나 지원되지 않습니다.',
        'file_too_large':   '❌ 파일이 50MB 제한을 초과합니다!',
        'spam_warn':        '⚠️ 3초 기다려주세요!',
        'ping_msg':         '🏓 퐁! `{ms}ms`',
        'uptime_msg':       '⏱ *봇 업타임:* `{uptime}`',
        'about_msg':        '🤖 *NikeBot 정보*\n━━━━━━━━━━━━━━━━━━━\n📌 *이름:* NikeBot\n💡 *버전:* 1.0.0\n👨‍💻 *창립자:* @nikecheatyeniden\n📢 *채널:* @nikestoretr\n━━━━━━━━━━━━━━━━━━━\n🔧 *기능:*\n• 50개 이상 플랫폼 다운로드\n• 10개 언어 지원\n• 스팸 방지\n• 그룹 관리\n• 로그 시스템',
        'platforms_msg':    '📱 *지원 플랫폼 (50+)*\n━━━━━━━━━━━━━━━━━━━\nTikTok • Instagram • YouTube • Twitter/X\nFacebook • Reddit • Pinterest • Vimeo\nDailymotion • Twitch • Kick • SoundCloud\n그 외 더...',
        'help_msg':         '❓ *도움말*\n━━━━━━━━━━━━━━━━━━━\n📥 *동영상 다운로드:* 링크를 보내세요!\n\n⚙️ *명령어:*\n/start — 봇 시작\n/ping — 핑 확인\n/uptime — 업타임\n/bothakinda — 봇 정보\n/platforms — 플랫폼',
        'admin_only': '⛔ 이 명령어는 관리자 전용입니다!',
        'no_reply':   '⚠️ 사용자에게 답장해주세요!',
        'user_banned':   '🔨 [{user}](tg://user?id={uid}) 차단되었습니다!',
        'user_unbanned': '✅ [{user}](tg://user?id={uid}) 차단이 해제되었습니다!',
        'user_muted':    '🔇 [{user}](tg://user?id={uid}) 음소거되었습니다! `({dur})`',
        'user_unmuted':  '🔊 [{user}](tg://user?id={uid}) 음소거가 해제되었습니다!',
    },
}

LANG_ORDER = ['tr','en','es','fr','de','ru','pt','ar','ja','ko']

def t(key: str, lang: str, **kwargs) -> str:
    """Translate a key into the given language."""
    lang_data = LANGUAGES.get(lang, LANGUAGES['tr'])
    text = lang_data.get(key, LANGUAGES['tr'].get(key, key))
    if kwargs:
        try:
            text = text.format(**kwargs)
        except KeyError:
            pass
    return text
