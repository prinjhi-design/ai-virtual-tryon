from fastapi import FastAPI, UploadFile, File
from uuid import uuid4
from pathlib import Path
import shutil

app = FastAPI(
    title="AI Virtual Try-On API",
    version="1.0.0",
)

jobs = {}

# Create directories if they don't exist
PERSON_DIR = Path("input/person")
GARMENT_DIR = Path("input/garment")
LOGO_DIR = Path("input/logo")

PERSON_DIR.mkdir(parents=True, exist_ok=True)
GARMENT_DIR.mkdir(parents=True, exist_ok=True)
LOGO_DIR.mkdir(parents=True, exist_ok=True)


@app.get("/")
def root():
    return {"message": "AI Virtual Try-On API is running successfully!"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/api/v1/generate")
async def generate(
    person_image: UploadFile = File(...),
    garment_image: UploadFile = File(...),
    logo_image: UploadFile | None = File(default=None),
):
    job_id = str(uuid4())

    person_path = PERSON_DIR / f"{job_id}_{person_image.filename}"
    garment_path = GARMENT_DIR / f"{job_id}_{garment_image.filename}"

    with open(person_path, "wb") as buffer:
        shutil.copyfileobj(person_image.file, buffer)

    with open(garment_path, "wb") as buffer:
        shutil.copyfileobj(garment_image.file, buffer)

    logo_path = None

    if logo_image is not None:
        logo_path = LOGO_DIR / f"{job_id}_{logo_image.filename}"
        with open(logo_path, "wb") as buffer:
            shutil.copyfileobj(logo_image.file, buffer)

    jobs[job_id] = {
        "status": "uploaded",
        "person_image": str(person_path),
        "garment_image": str(garment_path),
        "logo_image": str(logo_path) if logo_path else None,
    }

    return {
        "job_id": job_id,
        "status": "uploaded",
    }


@app.get("/api/v1/status/{job_id}")
def status(job_id: str):
    if job_id not in jobs:
        return {"error": "Job not found"}

    return {
        "job_id": job_id,
        "status": jobs[job_id]["status"],
    }


@app.get("/api/v1/result/{job_id}")
def result(job_id: str):
    if job_id not in jobs:
        return {"error": "Job not found"}

    return jobs[job_id]