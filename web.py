from fastapi import FastAPI

from routers.lost import router as lost_router
from setting import settings
import db.db as db

app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(lost_router)
db.init_db()

@app.get("/health")
def health():
    return {
        "status": "ok"
    }