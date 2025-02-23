#user_crud.py
from db import database
from db import models
from services import utils


class UserService:
    #@staticmethod
    #def create_user(username: str, email: str):
      #  while(find_user_by_username(create_unic_name(username)) != ''):
        #    create_unic_name(username)
        #user = User(name=username, email=email)
        #db.session.add(user)

        #return user
    

    def find_user_by_username(username: str) -> models.User:
        user = '' #; лишняя точка с запятой
        try:
            user = models.User.query.filter_by(name=username).first()
            return user
        except Exception as e:
            database.session.rollback()
            raise Exception(f"Ошибка поиска пользователя: {str(e)}")
