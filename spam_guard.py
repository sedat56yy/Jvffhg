"""
spam_guard.py — 3 saniyelik spam koruması
"""
import time
import config

_last: dict[int, float] = {}


def is_spam(user_id: int) -> bool:
    """True dönerse kullanıcı spam yapıyor (mesajı reddet)."""
    now = time.time()
    last = _last.get(user_id, 0.0)
    if now - last < config.SPAM_COOLDOWN:
        return True
    _last[user_id] = now
    return False


def reset(user_id: int) -> None:
    """Admin işlemlerinden sonra cooldown'u sıfırla."""
    _last.pop(user_id, None)
