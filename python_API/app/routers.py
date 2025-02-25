from fastapi import APIRouter
from models import PathRequest
from tools import find_path, data




router = APIRouter()


@router.post("/get_path")
async def get_path(request: PathRequest):
    target_id = request.target_id
    path = find_path(data, target_id)
    
    if path is not None:
        return {"path" : path}
    else:
        return {"message": "The element does not exist", "path" : []}