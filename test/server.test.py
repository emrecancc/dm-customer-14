import http.server
import socketserver
import threading
import requests
import pytest

# Use a random available port instead of the hard‑coded 3079
PORT = 0

class Handler(http.server.SimpleHTTPRequestHandler):
    pass

@pytest.fixture(scope="module")
def server():
    httpd = socketserver.TCPServer(("localhost", PORT), Handler)
    thread = threading.Thread(target=httpd.serve_forever)
    thread.daemon = True
    thread.start()
    yield httpd
    httpd.shutdown()
    httpd.server_close()
    thread.join()

def test_server(server):
    # Retrieve the actual port assigned by the OS
    port = server.server_address[1]
    r = requests.get(f"http://localhost:{port}")
    assert r.status_code == 200
