import pytest

from fastapi.testclient import TestClient
from app.main import app



client = TestClient(app)

@pytest.mark.parametrize(
    "existing_id",
    [
        "zesty-utopia-jostle",
        "zinc-utopia-ignite",
        "zenith-wistful-invent"
    ]
)
def test_get_path_if_found(existing_id):
    """
    /get_path should return 200 if UUID exists;
    in the end must be target UUID
    """
    response = client.post("/get_path", json={"target_id": existing_id})
    assert response.status_code == 200
    data = response.json()
    
    assert "path" in data
    assert len(data["path"]) > 0
    assert data["path"][-1] == existing_id
    

def test_get_path_if_not_found():
    """
    /get_path returns err message
    """
    fake_id = "why-are-u-here"
    response = client.post("/get_path", json={"target_id": fake_id})
    assert response.status_code == 200, f"message: The element {fake_id} has not been found"
    data = response.json()
    
    assert "path" in data
    assert data["path"] == []
    assert data.get("message")
    
    
def test_empty_target_id():
    """
    if target_id is empty string, return 422 error (Field(..., min_lenght=1))
    """
    response = client.post("/get_path", json={"target_id": ""})
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data
    
    