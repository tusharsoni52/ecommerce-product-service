# ecommerce-product-service

A FastAPI microservice that manages the e-commerce product catalogue, including product details, pricing, and stock.

## Overview

This service provides product CRUD endpoints and persists data in a MySQL database.

## Endpoints

* `GET /api/v1/products/health`
* `GET /api/v1/products`
* `GET /api/v1/products/{product_id}`
* `POST /api/v1/products`

## Database

* MySQL 8.4
* Database: `product_db`
* Container: `product-mysql`
* Host port: `3307`
* Container port: `3306`

## Environment Variables

This service loads variables from `.env`.

* `MYSQL_HOST` - MySQL host (default: `localhost`)
* `MYSQL_PORT` - MySQL port (default: `3306`)
* `MYSQL_DATABASE` - database name (default: `product_db`)
* `MYSQL_USER` - database user (default: `product_user`)
* `MYSQL_PASSWORD` - database password (default: `product_password`)

## Run with Docker Compose

1. Ensure Docker Desktop is running.
2. Create the shared network if needed:

   ```powershell
   docker network create ecommerce-network
   ```

3. Start the service:

   ```powershell
   docker compose up --build -d
   ```

4. Verify the health endpoint:

   ```text
   http://localhost:8000/api/v1/products/health
   ```

## Run All Services

1. Ensure Docker Desktop is running.
2. Create the shared network if it does not already exist:

   ```powershell
   docker network create ecommerce-network
   ```

3. Start all services in order:

   ```powershell
   cd repo\ecommerce-product-service
   docker compose up --build -d

   cd ..\ecommerce-cart-service
   docker compose up --build -d

   cd ..\ecommerce-order-service
   docker compose up --build -d

   cd ..\ecommerce-api-gateway
   docker compose up --build -d
   ```

4. Verify:

   * Product Service: `http://localhost:8000/api/v1/products/health`
   * Cart Service: `http://localhost:8001/health`
   * Order Service: `http://localhost:8002/health`
   * API Gateway: `http://localhost:8080/health`

## Cleanup

To stop and remove all containers for the full stack:

```powershell
cd repo\ecommerce-product-service
docker compose down

cd ..\ecommerce-cart-service
docker compose down

cd ..\ecommerce-order-service
docker compose down

cd ..\ecommerce-api-gateway
docker compose down
```

If the shared network is no longer needed:

```powershell
docker network rm ecommerce-network
```

## Dependencies

* fastapi
* uvicorn[standard]
* sqlalchemy
* pymysql
* python-dotenv
* pydantic
* pytest
* httpx

## Project Structure

* `app/main.py`
* `app/api/products.py`
* `app/config.py`
* `app/db/database.py`
* `app/models/`
* `app/schemas/`
* `app/services/`

