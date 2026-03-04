
"""
downloader.py — yt-dlp ile 50+ platformdan video/foto/ses indirme
• YouTube uzun video desteği (480p ile boyut düşürülür)
• Fotoğraf desteği (Instagram, Pinterest vb.)
• Detaylı hata mesajları
"""
import os
import glob
import config

try:
    import yt_dlp
    YT_DLP_AVAILABLE = True
except ImportError:
    YT_DLP_AVAILABLE = False
    print("[downloader] yt-dlp yüklü değil! pip install yt-dlp")

ERROR_MAP = {
    'Video unavailable':           '🚫 Video mevcut değil veya gizli',
    'Private video':               '🔒 Bu video gizli',
    'age-restricted':              '🔞 Yaş kısıtlı video (indirilemez)',
    'copyright':                   '©️ Telif hakkı nedeniyle kaldırılmış',
    'not available in your':       '🌍 Bölge kısıtlaması var',
    'Unable to extract':           '🔍 Link ayrıştırılamadı, geçerli mi?',
    'No video formats found':      '📭 Video formatı bulunamadı',
    'HTTP Error 403':              '🚫 Erişim reddedildi (403)',
    'HTTP Error 404':              '🔍 Sayfa bulunamadı (404)',
    'Sign in to confirm your age': '🔞 Yaş doğrulaması gerekiyor',
    'members-only':                '👥 Sadece üyelere özel içerik',
    'This live event will begin':  '🔴 Yayın henüz başlamadı',
    'is not a valid URL':          '🔗 Geçersiz URL formatı',
    'Unsupported URL':             '❌ Bu platform desteklenmiyor',
}


def _friendly_error(raw: str) -> str:
    raw_lower = raw.lower()
    for key, msg in ERROR_MAP.items():
        if key.lower() in raw_lower:
            return msg
    return '❌ İndirme başarısız!\n`' + raw[:120] + '`'


def download(url: str, user_id: int) -> dict:
    if not YT_DLP_AVAILABLE:
        return {'success': False, 'path': None, 'error': 'yt-dlp yüklü değil', 'is_photo': False}

    os.makedirs(config.TEMP_DIR, exist_ok=True)
    _cleanup_user(user_id)

    output_tmpl = os.path.join(config.TEMP_DIR, f'{user_id}_%(id)s.%(ext)s')

    try:
        with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True}) as ydl:
            info_only = ydl.extract_info(url, download=False)
    except Exception as e:
        return {'success': False, 'path': None, 'error': _friendly_error(str(e)), 'is_photo': False}

    is_photo = _check_photo(info_only)
    ydl_opts = _photo_opts(output_tmpl) if is_photo else _video_opts(output_tmpl)

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info     = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        filename = _find_file(filename, user_id)

        if filename and os.path.exists(filename):
            size = os.path.getsize(filename)
            if size > config.MAX_FILE_SIZE:
                os.remove(filename)
                return {'success': False, 'path': None, 'error': 'too_large', 'is_photo': False}
            return {'success': True, 'path': filename, 'error': None, 'is_photo': is_photo}

        return {'success': False, 'path': None, 'error': '📁 Dosya kaydedilemedi', 'is_photo': False}

    except yt_dlp.utils.DownloadError as e:
        return {'success': False, 'path': None, 'error': _friendly_error(str(e)), 'is_photo': False}
    except Exception as e:
        return {'success': False, 'path': None, 'error': _friendly_error(str(e)), 'is_photo': False}


def _check_photo(info: dict) -> bool:
    if not info:
        return False
    url = info.get('url', '') or info.get('webpage_url', '')
    if any(url.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp']):
        return True
    ext = info.get('extractor', '').lower()
    if 'photo' in ext or 'image' in ext:
        return True
    formats = info.get('formats', [])
    if not formats and not info.get('duration'):
        return True
    return False


def _video_opts(output_tmpl: str) -> dict:
    return {
        'format': (
            'bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/'
            'bestvideo[height<=480]+bestaudio/'
            'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/'
            'bestvideo[height<=720]+bestaudio/'
            'best[height<=720]/best'
        ),
        'outtmpl':             output_tmpl,
        'quiet':               True,
        'no_warnings':         True,
        'noplaylist':          True,
        'merge_output_format': 'mp4',
        'socket_timeout':      60,
        'retries':             5,
        'fragment_retries':    10,
        'concurrent_fragment_downloads': 4,
        'http_headers': {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/124.0.0.0 Safari/537.36'
            ),
            'Accept-Language': 'en-US,en;q=0.9',
        },
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }


def _photo_opts(output_tmpl: str) -> dict:
    return {
        'outtmpl':        output_tmpl,
        'quiet':          True,
        'no_warnings':    True,
        'noplaylist':     True,
        'socket_timeout': 30,
        'retries':        3,
        'http_headers': {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/124.0.0.0 Safari/537.36'
            ),
        },
    }


def _find_file(filename: str, user_id: int):
    if os.path.exists(filename):
        return filename
    base = os.path.splitext(filename)[0]
    for ext in ['.mp4', '.mkv', '.webm', '.mov', '.avi',
                '.mp3', '.m4a', '.ogg', '.flac', '.wav',
                '.jpg', '.jpeg', '.png', '.webp', '.gif']:
        candidate = base + ext
        if os.path.exists(candidate):
            return candidate
    pattern = os.path.join(config.TEMP_DIR, f'{user_id}_*')
    files   = glob.glob(pattern)
    if files:
        return max(files, key=os.path.getmtime)
    return None


def _cleanup_user(user_id: int) -> None:
    pattern = os.path.join(config.TEMP_DIR, f'{user_id}_*')
    for f in glob.glob(pattern):
        try:
            os.remove(f)
        except OSError:
            pass


def get_send_type(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    if ext in {'.mp4', '.mkv', '.webm', '.mov', '.avi', '.3gp', '.flv'}:
        return 'video'
    if ext in {'.jpg', '.jpeg', '.png', '.webp', '.gif'}:
        return 'photo'
    if ext in {'.mp3', '.m4a', '.ogg', '.flac', '.wav', '.aac'}:
        return 'audio'
    return 'document'
