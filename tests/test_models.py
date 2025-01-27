from app.models import User

def test_user_model():
    user = User(id=1, username="testuser", email="test@example.com")
    assert user.id == 1
    assert user.username == "testuser"
    assert user.email == "test@example.com"
