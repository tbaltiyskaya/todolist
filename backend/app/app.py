#app.py
from flask import Flask
from flask_migrate import Migrate
from config import DB_CONFIG
from db.database import db, init_app
from services import user_crud
from services import list_crud
from sqlalchemy import text 
from routes.user_routes import routes
from flask_cors import CORS
from views import view_user, view_list, view_task
from services.list_crud import ListService
from services.user_crud import UserService
from services.task_crud import TaskService


def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": "http://localhost:60287"}}) 
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f'postgresql://{DB_CONFIG["user"]}:{DB_CONFIG["password"]}'
        f'@{DB_CONFIG["host"]}/{DB_CONFIG["database"]}'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_app(app)
    migrate = Migrate(app, db)

    return app


app = create_app()

app.register_blueprint(routes)


def init_db(app):
    with app.app_context():
        try:
            db.session.execute(text('SELECT 1')) 
            db.session.commit()
            print("Подключение успешно!")
        except Exception as e:
            print(f"Ошибка подключения к БД: {str(e)}")


if __name__ == '__main__':
    init_db(app)
    app.run(debug=True)
