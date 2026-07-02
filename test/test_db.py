import pytest
from app.models import User, db

def test_create_user():
    user = User(email='test@example.com', name='Test')
    db.session.add(user)
    db.session.commit()
    assert User.query.count() == 1  # No cleanup!

def test_user_count_empty():
    # Fails if test_create_user ran first
    assert User.query.count() == 0
