from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_summary_endpoint() -> None:
    response = client.get("/reports/summary")
    assert response.status_code == 200
