import re
from unidecode import unidecode

def normalize_text(text: str) -> str:
    text = unidecode(text)               # quita tildes
    text = re.sub(r"\s+", " ", text)     # colapsa espacios
    return text.strip()

def extract_context(text: str, match_span: tuple[int, int], window_words: int = 200) -> str:
    words = text.split()
    start_char, end_char = match_span
    cumulative = 0
    start_idx = 0
    end_idx = len(words)

    for i, w in enumerate(words):
        cumulative += len(w) + 1
        if cumulative >= start_char:
            start_idx = max(0, i - window_words)
            break

    cumulative = 0
    for i, w in enumerate(words):
        cumulative += len(w) + 1
        if cumulative >= end_char:
            end_idx = min(len(words), i + window_words)
            break

    return " ".join(words[start_idx:end_idx])
