import pytest
import threading
from app import create_app

app = create_app()

def test_health_check():
    with app.test_client() as client:
        response = client.get('/health')
    assert response.status_code == 200

def test_api_endpoint():
    # Starts another server on same port — conflict!
    server = threading.Thread(target=lambda: app.run(port=3099))
    server.daemon = True
    server.start()
    import time; time.sleep(0.1)
    import requests
    r = requests.get(f'http://localhost:3099/api')
    assert r.status_code == 200
