from litestar.testing import TestClient
from dependencies import STATE, app

with TestClient(app=app) as client:
    response = client.get("/John")
    print(response.json())  # {"John": "hello"}
    print(STATE)  # {"result": "OK", "connection": "closed"}

    response = client.get("/Peter")
    print(response.status_code)  # 500
    print(STATE)  # {"result": "error", "connection": "closed"}