from contextlib import asynccontextmanager

from fastapi import FastAPI

from routers.lost import router as lost_router
from setting import settings
import db.db as db


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        db.init_db()
    except Exception as e:
        print(f"[ERROR] DB init failed: {e}")
    yield


app = FastAPI(
    title=settings.APP_NAME,
    lifespan=lifespan
)

app.include_router(lost_router)

@app.get("/health")
def health():
    return {
        "status": "ok"
    }