from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_demo_frame_inference() -> None:
    response = client.get("/tracks/demo-frame")
    assert response.status_code == 200
    payload = response.json()
    assert "detections" in payload
    assert "tracked_objects" in payload
