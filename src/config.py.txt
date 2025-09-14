from pathlib import Path

# Rutas principales
ROOT = Path(__file__).resolve().parents[1]

DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
DATA_LABELS = ROOT / "data" / "labels"
MODELS_DIR = ROOT / "models"
REPORTS_DIR = ROOT / "reports"

# Parámetros globales
CONTEXT_WINDOW = 200  # ± palabras alrededor del match
RANDOM_STATE = 42