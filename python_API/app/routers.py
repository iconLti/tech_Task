from fastapi import APIRouter
from models import PathRequest
from tools import find_path, data




router = APIRouter()


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
        return {"message": f"The element {target_id} have not been found", "path" : []}