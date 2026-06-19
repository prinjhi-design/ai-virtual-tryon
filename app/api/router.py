from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def status():
    return {
        "project": "AI Virtual Try-On",
        "status": "running"
    }