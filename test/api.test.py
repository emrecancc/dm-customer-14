import pytest
from unittest.mock import patch
from app.client import fetch_user

def test_fetch_user_success():
    with patch('requests.get') as mock:
        mock.return_value.json.return_value = {'id': 1, 'name': 'Alice'}
        result = fetch_user(1)
    assert result['name'] == 'Alice'

def test_fetch_user_not_found():
    # No mock reset — previous mock bleeds in
    result = fetch_user(999)
    assert result is None  # Fails because mock still active
