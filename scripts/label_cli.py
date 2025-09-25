from __future__ import annotations
import argparse, sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PROCESSED = ROOT / "data" / "processed"
DATA_LABELS = ROOT / "data" / "labels"

def main():
    p = argparse.ArgumentParser(description="Etiquetador simple 0/1 sobre candidatos.csv")
    p.add_argument("--src", type=Path, default=DATA_PROCESSED/"candidatos.csv",
                   help="CSV fuente (por defecto: data/processed/candidatos.csv)")
    p.add_argument("--out", type=Path, default=DATA_LABELS/"etiquetas.csv",
                   help="CSV de salida con etiquetas")
    p.add_argument("--start", type=int, default=0, help="fila inicial (offset)")
    p.add_argument("--limit", type=int, default=0, help="máx. filas a etiquetar (0 = sin límite)")
    p.add_argument("--only-has-action", action="store_true", help="filtrar has_action == 1")
    args = p.parse_args()

    args.out.parent.mkdir(parents=True, exist_ok=True)

    # cargar candidatos
    if not args.src.exists():
        print(f"ERROR: no existe {args.src}")
        sys.exit(1)

    df = pd.read_csv(args.src)
    if args.only_has_action:
        df = df[df["has_action"] == 1].copy()

    df = df.reset_index(drop=True)
    if args.start > 0:
        df = df.iloc[args.start:].reset_index(drop=True)
    if args.limit > 0:
        df = df.iloc[:args.limit].reset_index(drop=True)

    # cargar etiquetas previas si existen (para no perder progreso)
    if args.out.exists():
        prev = pd.read_csv(args.out)
        prev_ids = set(prev["context_hash"])
    else:
        prev = pd.DataFrame(columns=["context_hash","label","rationale"])
        prev_ids = set()

    rows = []
    print("\n=== Etiquetador 0/1 ===")
    print("Instrucciones: 1=Pertinente, 0=No pertinente, s=saltear, q=salir\n")

    for i, row in df.iterrows():
        ch = row["context_hash"]
        if ch in prev_ids:
            continue

        print("-"*80)
        print(f"[{i}] PDF: {row.get('pdf')} | keyword: {row.get('keyword')} | has_action: {row.get('has_action')}")
        print("-"*80)
        print(row["context"])
        print("-"*80)
        ans = input("Etiqueta (1/0/s/q) > ").strip().lower()

        if ans == "q":
            break
        if ans == "s":
            continue
        if ans not in {"0","1"}:
            print("Valor inválido. Use 1/0/s/q.")
            continue

        rat = input("Rationale (opcional, Enter para omitir) > ").strip()
        rows.append({"context_hash": ch, "label": int(ans), "rationale": rat})

        # guardado incremental
        out_df = pd.concat([prev, pd.DataFrame(rows)], ignore_index=True)
        out_df.to_csv(args.out, index=False)

    print(f"\nGuardado: {args.out}")

if __name__ == "__main__":
    main()