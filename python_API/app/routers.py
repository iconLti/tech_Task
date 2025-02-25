from fastapi import APIRouter
from app.models import PathRequest
from app.tools import find_path, data




router = APIRouter()


@router.get("/")
async def show_root():
    return {"message" : "better go to docs ^_^"}


@router.post("/get_path")
async def get_path(request: PathRequest):
    if not data:
        return {
            "message": "No data available for search.",
            "path": []
        }
    
    target_id = request.target_id
    path = find_path(data, target_id)
    
    if path is not None:
        return {"path" : path}
    else:
        return {"message": f"The element {target_id} has not been found", "path" : []}