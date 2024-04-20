from app.database import db
from app import create_app

app = create_app()
with app.app_context() as ctx:
    db.drop_all()
    db.create_all()
    db.session.commit()

