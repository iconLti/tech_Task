from pydantic import BaseModel, Field


class PathRequest(BaseModel):
    target_id : str = Field(..., min_length=1, description="Non-empty string ID")