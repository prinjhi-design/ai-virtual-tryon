from fastapi import APIRouter, UploadFile, File
from typing import Optional

from app.services.tryon_service import (
    save_upload,
    PERSON_DIR,
    GARMENT_DIR,
    LOGO_DIR,
)

router = APIRouter(prefix="/api/v1", tags=["Virtual Try-On"])


@router.post("/generate")
async def generate_tryon(
    person_image: UploadFile = File(...),
    garment_image: UploadFile = File(...),
    logo_image: Optional[UploadFile] = File(None),
):
    person_path, job_id = save_upload(person_image, PERSON_DIR)
    garment_path, _ = save_upload(garment_image, GARMENT_DIR)

    logo_path = None
    if logo_image:
        logo_path, _ = save_upload(logo_image, LOGO_DIR)

    return {
        "job_id": job_id,
        "status": "pending",
        "person_image": person_path,
        "garment_image": garment_path,
        "logo_image": logo_path,
    }


@router.get("/status/{job_id}")
def status(job_id: str):
    return {
        "job_id": job_id,
        "status": "pending",
    }