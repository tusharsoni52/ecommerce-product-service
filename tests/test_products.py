from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "UP",
        "service": "product-service"
    }


def test_create_product():
    payload = {
        "name": "Samsung Galaxy S25",
        "description": "512 GB",
        "price": 89999,
        "stock": 5
    }

    response = client.post("/products", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["id"] is not None
    assert data["name"] == payload["name"]
    assert data["description"] == payload["description"]
    assert float(data["price"]) == float(payload["price"])
    assert data["stock"] == payload["stock"]


def test_get_all_products():
    response = client.get("/products")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 1


def test_get_product_by_id():
    products_response = client.get("/products")

    assert products_response.status_code == 200

    products = products_response.json()

    assert len(products) >= 1

    product_id = products[0]["id"]

    response = client.get(f"/products/{product_id}")

    assert response.status_code == 200

    product = response.json()

    assert product["id"] == product_id
    assert "name" in product
    assert "price" in product