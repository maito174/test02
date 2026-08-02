from datetime import datetime

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_get_current_datetime_returns_iso_datetime() -> None:
    response = client.get("/now")

    assert response.status_code == 200
    payload = response.json()
    assert "current_datetime" in payload
    assert isinstance(payload["current_datetime"], str)
    datetime.fromisoformat(payload["current_datetime"])
