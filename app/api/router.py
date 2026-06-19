from fastapi import APIRouter
from app.services.tryon_service import run_virtual_tryon

router = APIRouter()

@router.get("/status")
def status():
    return {
        "project": "AI Virtual Try-On",
        "status": "running"
    }

@router.get("/tryon")
def tryon():
    result = run_virtual_tryon(
        person_image="Input/person/sample_person.jpg",
        garment_image="Input/garment/sample_garment.jpg"
    )
    return result