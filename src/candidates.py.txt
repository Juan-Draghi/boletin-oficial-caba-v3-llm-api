from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Iterable, Iterator, Tuple, List

import pandas as pd

from .config import DATA_PROCESSED, CONTEXT_WINDOW
from .io_pdf import extract_text_from_pdf
from .preprocess import normalize_text, extract_context
from .rules import KEYWORDS, ACTION_VERBS


# =============== Utilidades internas ===============

def _normalize_spec(spec: str) -> tuple[str, bool]:
    """
    Interpreta un patrón con convención 'regex:'.
    Devuelve (pattern, is_regex).
    """
    if spec.startswith("regex:"):
        return spec[len("regex:"):], True
    return spec, False


def _iter_matches(text: str, pattern: str, is_regex: bool) -> Iterator[re.Match]:
    """
    Itera coincidencias en 'text'.
    - Si is_regex=True: usa el patrón tal cual.
    - Si is_regex=False: trata 'pattern' como literal y aplica \b...\b.
    """
    if is_regex:
        compiled = re.compile(pattern, flags=re.IGNORECASE)
    else:
        compiled = re.compile(rf"\b{re.escape(pattern)}\b", flags=re.IGNORECASE)
    yield from compiled.finditer(text)


def _ctx_hash(s: str) -> str:
    """Hash estable del contexto para deduplicar filas casi idénticas."""
    return hashlib.md5(s.encode("utf-8")).hexdigest()


# =============== Búsqueda de keywords y verbos ===============

def find_keyword_spans(text: str, patterns: List[str]) -> Iterator[tuple[str, tuple[int, int]]]:
    """
    Devuelve tuplas (pattern_original, span) para cada keyword encontrada.
    Acepta literales y regex con convención 'regex:'.
    """
    for pat in patterns:
        patt, is_rx = _normalize_spec(pat)
        for m in _iter_matches(text, patt, is_rx):
            yield pat, (m.start(), m.end())


def context_action_hits(context: str, verbs: List[str]) -> List[str]:
    """
    Devuelve la lista de verbos/expresiones de acción normativa encontrados en 'context'.
    Acepta literales y regex con convención 'regex:'.
    """
    hits: List[str] = []
    for v in verbs:
        patt, is_rx = _normalize_spec(v)
        # si hay al menos un match, guardamos el 'v' tal cual aparece en rules.py
        if any(True for _ in _iter_matches(context, patt, is_rx)):
            hits.append(v)
    return hits


# =============== Generación de candidatos ===============

def generate_candidates_from_pdf(pdf_path: Path) -> pd.DataFrame:
    """
    Lee un PDF, normaliza texto, busca KEYWORDS y extrae contexto ±N palabras.
    Marca si el contexto contiene ACTION_VERBS y agrega metadatos.
    Deduplica por hash de contexto.
    """
    raw = extract_text_from_pdf(pdf_path)
    norm = normalize_text(raw)

    rows = []
    for kw, span in find_keyword_spans(norm, KEYWORDS):
        ctx = extract_context(norm, span, CONTEXT_WINDOW)
        hits = context_action_hits(ctx, ACTION_VERBS)
        rows.append({
            "pdf": pdf_path.name,
            "pdf_path": str(pdf_path),
            "keyword": kw,                               # conserva el patrón tal cual (incluye 'regex:' si aplica)
            "keyword_is_regex": int(kw.startswith("regex:")),
            "start": span[0],
            "end": span[1],
            "context": ctx,
            "context_hash": _ctx_hash(ctx),
            "has_action": int(len(hits) > 0),
            "action_hits": ";".join(hits),              # verbos/regex que matchearon en el contexto
        })

    df = pd.DataFrame(rows)
    if not df.empty:
        df = df.drop_duplicates(subset=["context_hash"])

    return df


def export_candidates(df: pd.DataFrame, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)


def run_batch(
    input_dir: Path,
    out_csv: Path,
    filter_has_action: bool = False,
    master_csv: Path | None = None,
) -> None:
    """
    Procesa todos los PDFs en 'input_dir' y guarda:
      - 'out_csv' con los candidatos de esta corrida
      - (opcional) 'master_csv' acumulando históricos (sin duplicar contextos)

    Parámetros:
      - filter_has_action: si True, solo conserva filas con has_action == 1
      - master_csv: ruta al CSV maestro para append + deduplicación
    """
    all_rows: List[pd.DataFrame] = []

    for pdf in input_dir.glob("*.pdf"):
        df = generate_candidates_from_pdf(pdf)
        if df.empty:
            continue
        if filter_has_action:
            df = df[df["has_action"] == 1]
        if not df.empty:
            all_rows.append(df)

    full = pd.concat(all_rows, ignore_index=True) if all_rows else pd.DataFrame()
    export_candidates(full, out_csv)

    if master_csv is not None and not full.empty:
        master_csv.parent.mkdir(parents=True, exist_ok=True)
        try:
            prev = pd.read_csv(master_csv)
            merged = pd.concat([prev, full], ignore_index=True)
            merged = merged.drop_duplicates(subset=["context_hash"])
        except FileNotFoundError:
            merged = full
        merged.to_csv(master_csv, index=False)
