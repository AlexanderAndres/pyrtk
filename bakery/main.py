from fastapi import FastAPI
from app.middleware import apply_middlewares
from app.routers import health

app = FastAPI()

apply_middlewares(app)

app.include_router(health.router)

@app.get("/health")
async def health():
    return {"status": "ok"}
