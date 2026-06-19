from pathlib import Path
import shutil

BASE_DIR = Path.cwd()

INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

PERSON_DIR = INPUT_DIR / "person"
GARMENT_DIR = INPUT_DIR / "garment"
LOGO_DIR = INPUT_DIR / "logo"

PREVIEW_DIR = OUTPUT_DIR / "preview"
FINAL_DIR = OUTPUT_DIR / "final"


def ensure_directories():
    for d in [
        PERSON_DIR,
        GARMENT_DIR,
        LOGO_DIR,
        PREVIEW_DIR,
        FINAL_DIR,
    ]:
        d.mkdir(parents=True, exist_ok=True)


def save_file(src_path: str, dst_path: Path):
    shutil.copy(src_path, dst_path)