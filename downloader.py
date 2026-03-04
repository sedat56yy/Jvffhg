"""
downloader.py — yt-dlp ile 50+ platformdan video/ses indirme
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


def download(url: str, user_id: int) -> dict:
    """
    Verilen URL'yi indirir.
    Döndürür: {'success': bool, 'path': str | None, 'error': str | None}
    """
    if not YT_DLP_AVAILABLE:
        return {'success': False, 'path': None, 'error': 'yt-dlp yüklü değil'}

    os.makedirs(config.TEMP_DIR, exist_ok=True)

    # Önce kullanıcıya ait eski dosyaları temizle
    _cleanup_user(user_id)

    output_tmpl = os.path.join(config.TEMP_DIR, f'{user_id}_%(id)s.%(ext)s')

    ydl_opts = {
        'format': (
            'bestvideo[ext=mp4][filesize<48M]+bestaudio[ext=m4a]/'
            'bestvideo[filesize<48M]+bestaudio/'
            'best[filesize<48M]/best'
        ),
        'outtmpl':              output_tmpl,
        'quiet':                True,
        'no_warnings':          True,
        'noplaylist':           True,
        'merge_output_format':  'mp4',
        'max_filesize':         config.MAX_FILE_SIZE,
        'socket_timeout':       30,
        'retries':              3,
        # TikTok / Instagram için gerekli
        'http_headers': {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/120.0.0.0 Safari/537.36'
            ),
        },
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info     = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        # Merged mp4 kontrolü
        if not os.path.exists(filename):
            base    = os.path.splitext(filename)[0]
            for ext in ['.mp4', '.mkv', '.webm', '.mov', '.avi', '.mp3', '.m4a', '.ogg']:
                candidate = base + ext
                if os.path.exists(candidate):
                    filename = candidate
                    break

        # Hâlâ bulunamadıysa glob ile tara
        if not os.path.exists(filename):
            pattern = os.path.join(config.TEMP_DIR, f'{user_id}_*')
            files   = glob.glob(pattern)
            if files:
                filename = max(files, key=os.path.getmtime)

        if os.path.exists(filename):
            size = os.path.getsize(filename)
            if size > config.MAX_FILE_SIZE:
                os.remove(filename)
                return {'success': False, 'path': None, 'error': 'too_large'}
            return {'success': True, 'path': filename, 'error': None}

        return {'success': False, 'path': None, 'error': 'Dosya bulunamadı'}

    except yt_dlp.utils.DownloadError as e:
        return {'success': False, 'path': None, 'error': str(e)[:200]}
    except Exception as e:
        return {'success': False, 'path': None, 'error': str(e)[:200]}


def _cleanup_user(user_id: int) -> None:
    """Kullanıcının önceki geçici dosyalarını sil."""
    pattern = os.path.join(config.TEMP_DIR, f'{user_id}_*')
    for f in glob.glob(pattern):
        try:
            os.remove(f)
        except OSError:
            pass


def get_send_type(path: str) -> str:
    """Dosya uzantısına göre gönderim tipini belirle."""
    ext = os.path.splitext(path)[1].lower()
    if ext in {'.mp4', '.mkv', '.webm', '.mov', '.avi', '.3gp', '.flv'}:
        return 'video'
    if ext in {'.jpg', '.jpeg', '.png', '.webp', '.gif'}:
        return 'photo'
    if ext in {'.mp3', '.m4a', '.ogg', '.flac', '.wav', '.aac'}:
        return 'audio'
    return 'document'
