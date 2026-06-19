from fastapi import FastAPI
from app.api.router import router

app = FastAPI(
    title="AI Virtual Try-On API",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Virtual Try-On API is running successfully!"}

@app.get("/health")
def health():
    return {"status": "healthy"}