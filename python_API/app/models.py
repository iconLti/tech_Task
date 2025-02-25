from pydantic import BaseModel


class PathRequest(BaseModel):
    target_id : str