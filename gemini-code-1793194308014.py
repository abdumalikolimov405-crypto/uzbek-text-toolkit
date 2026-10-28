import re

LATIN_TO_CYRILLIC = {
    "o'": "ў", "O'": "Ў", "g'": "ғ", "G'": "Ғ",
    "sh": "ш", "Sh": "Ш", "SH": "Ш",
    "ch": "ч", "Ch": "Ч", "CH": "Ч",
    "yo": "ё", "Yo": "Ё", "yu": "ю", "Yu": "Ю",
    "ya": "я", "Ya": "Я", "ye": "е", "Ye": "Е",
    "a": "а", "b": "б", "d": "д", "e": "э", "f": "ф",
    "g": "г", "h": "ҳ", "i": "и", "j": "ж", "k": "к",
    "l": "л", "m": "м", "n": "н", "o": "о", "p": "п",
    "q": "қ", "r": "р", "s": "с", "t": "т", "u": "у",
    "v": "в", "x": "х", "y": "й", "z": "з", "'": "ъ"
}

def to_cyrillic(text: str) -> str:
    """Lotin yozuvidagi o'zbekcha matnni kirill yozuviga o'giradi."""
    result = text
    # Avval birikmali harflarni almashtiramiz
    for lat in sorted(LATIN_TO_CYRILLIC.keys(), key=len, reverse=True):
        result = result.replace(lat, LATIN_TO_CYRILLIC[lat])
        result = result.replace(lat.capitalize(), LATIN_TO_CYRILLIC[lat].capitalize())
    return result

def validate_uz_phone(phone: str) -> bool:
    """O'zbekiston telefon raqamini (+998XXXXXXXXX) tekshiradi."""
    cleaned = re.sub(r"[\s\-\(\)]", "", phone)
    return bool(re.match(r"^\+?998(90|91|93|94|95|97|98|99|33|88|77|50)\d{7}$", cleaned))

def validate_pinfl(pinfl: str) -> bool:
    """14 xonali JSHSHIR (PINFL) raqamini tekshiradi."""
    return bool(re.match(r"^\d{14}$", str(pinfl).strip()))