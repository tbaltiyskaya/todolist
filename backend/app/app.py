#app.py
from flask import Flask

from .config import DB_CONFIG
from .database import db
from .services import user_crud

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'postgresql://{DB_CONFIG["user"]}:{DB_CONFIG["password"]}'
    f'@{DB_CONFIG["host"]}/{DB_CONFIG["database"]}'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def init_db():
    with app.app_context():
        db.init_app(app)
        try:
            db.session.execute('SELECT 1')
            db.session.commit()
            print("Подключение успешно!")
        except Exception as e:
            print(f"Ошибка подключения: {str(e)}")

if __name__ == '__main__':
    init_db()
    user_crud.find_user_by_username('kevin#000100')
    app.run(debug=True)
