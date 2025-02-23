#user_crud.py
from app.database import db
from app.models import User
from app.services.utils import create_unic_name


class UserService:
    #@staticmethod
    #def create_user(username: str, email: str):
      #  while(find_user_by_username(create_unic_name(username)) != ''):
        #    create_unic_name(username)
        #user = User(name=username, email=email)
        #db.session.add(user)

        #return user
    

    def find_user_by_username(username: str) -> User:
        user = '';
        try:
            user = User.query.filter_by(name=username).first()
            return user
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Ошибка поиска пользователя: {str(e)}")
