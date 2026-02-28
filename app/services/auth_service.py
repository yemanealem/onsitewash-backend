from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token

def create_user(db, username: str, password: str):
    user = User(
        username=username,
        password=hash_password(password)
    )
    db.add(user)
    db.commit()
    return user

def authenticate_user(db, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        return None
    return user

def generate_token(user):
    return create_access_token({"sub": user.username})
