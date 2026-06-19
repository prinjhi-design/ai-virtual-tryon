import shutil
import uuid
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

PERSON_DIR = INPUT_DIR / "person"
GARMENT_DIR = INPUT_DIR / "garment"
LOGO_DIR = INPUT_DIR / "logo"

PREVIEW_DIR = OUTPUT_DIR / "preview"
FINAL_DIR = OUTPUT_DIR / "final"


def save_upload(file, destination_folder: Path):
    destination_folder.mkdir(parents=True, exist_ok=True)

    file_id = str(uuid.uuid4())
    filename = f"{file_id}_{file.filename}"

    save_path = destination_folder / filename

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(save_path), file_id