from models import User, db
from app import app

with app.app_context():
    # Cria um novo usuário
    new_user = User(username="admin", email="admin@example.com")
    new_user.set_password("admin123")  # Criptografa a senha
    db.session.add(new_user)
    db.session.commit()

    