from starlette.responses import JSONResponse
from typing_extensions import Annotated

from fastapi import APIRouter, Header, UploadFile, File
import db.db as db
from setting import settings
from utils.github_upload import upload_image
from utils.groq_ai import classify_lost_item

import time

router = APIRouter(
    prefix="/api/v1/lost",
    tags=["lost"]
)

@router.get("/")
def get_lost_items(query: str = "", page: int = 1, page_size: int = 10):
    items = db.get_lost_items(query=query, page=page, page_size=page_size)
    item_list = []
    for item in items:
        item_list.append({
            "id": item[0],
            "context": item[1],
            "image_link": item[2],
            "created_at": item[3]
        })
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "data": item_list
        }
    )

@router.delete("/{item_id}")
def delete_lost_item(
    item_id: int,
    Authorization: Annotated[str | None, Header()] = None
):
    if not Authorization or Authorization != settings.EMB_API_KEY:
        return JSONResponse(
            status_code=401,
            content={
                "status": "error",
                "data": {
                    "message": "Unauthorized"
                }
            }
        )
        
    if not db.is_exist_lost_item(item_id):
        return JSONResponse(
            status_code=404,
            content={
                "status": "error",
                "data": {
                    "message": "Item not found"
                }
            }
        )
        
    db.delete_lost_item(item_id)
    return JSONResponse(
        status_code=200,
        content= {
            "status": "ok",
            "data": {
                "message": "Item deleted successfully"
            }
        }
    )
    
ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp"
}

ALLOWED_CONTENT_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp"
}

MAX_FILE_SIZE = 30 * 1024 * 1024 # 30MB
    
@router.post("/")
async def insert_lost_item(
    image: Annotated[UploadFile, File()],
    Authorization: Annotated[str | None, Header()] = None
):
    if not Authorization or Authorization != settings.EMB_API_KEY:
        return JSONResponse(
            status_code=401,
            content={
                "status": "error",
                "data": {
                    "message": "Unauthorized"
                }
            }
        )
        
    content = await image.read()
    extension = image.filename.split(".")[-1].lower()
    
    if extension not in ALLOWED_EXTENSIONS:
        return JSONResponse(
            status_code=400,
            content={
                "status": "error",
                "data": {
                    "message": "Invalid file extension"
                }
            }
        )

    if image.content_type not in ALLOWED_CONTENT_TYPES:
        return JSONResponse(
            status_code=400,
            content={
                "status": "error",
                "data": {
                    "message": "Invalid file extension"
                }
            }
        )
    
    if len(content) > MAX_FILE_SIZE:
        return JSONResponse(
            status_code=400,
            content={
                "status": "error",
                "data": {
                    "message": "File size exceeds the limit"
                }
            }
        )
    
    path = upload_image(
        image_bytes=content,
        extension=extension
    )
    
    image_link = settings.GITHUB_RAW_URL + path
    
    # print(image_link)
    context = classify_lost_item(image_link)
    created_at = int(time.time())
    db.insert_lost_item(context, image_link, created_at)
    
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "data": {
                "message": "Item inserted successfully",
                "context": context,
                "image_link": image_link,
                "created_at": created_at
            }
        }
    )
