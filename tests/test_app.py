from app import app


def test_health_returns_ok():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json()["status"] == "ok"


def test_products_returns_json_list():
    client = app.test_client()
    response = client.get("/products")
    assert response.status_code == 200
    assert response.content_type.startswith("application/json")
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "id" in data[0]
    assert "name" in data[0]
    assert "price" in data[0]
