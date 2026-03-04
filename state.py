"""
state.py — Kullanıcı dil tercihleri (JSON dosyasına kalıcı kayıt)
"""
import json
import os

_FILE = "user_langs.json"
user_langs: dict[int, str] = {}


def load() -> None:
    global user_langs
    if os.path.exists(_FILE):
        try:
            with open(_FILE, "r", encoding="utf-8") as f:
                raw = json.load(f)
                user_langs = {int(k): v for k, v in raw.items()}
        except Exception:
            user_langs = {}


def save() -> None:
    try:
        with open(_FILE, "w", encoding="utf-8") as f:
            json.dump({str(k): v for k, v in user_langs.items()}, f, ensure_ascii=False)
    except Exception as e:
        print(f"[state] Kaydetme hatası: {e}")


def get(user_id: int) -> str:
    return user_langs.get(user_id, "tr")


def set_lang(user_id: int, lang: str) -> None:
    user_langs[user_id] = lang
    save()


def has_lang(user_id: int) -> bool:
    return user_id in user_langs
