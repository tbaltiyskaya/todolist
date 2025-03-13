#user_crud.py
from db import database
from db import models
from services import utils
from .list_crud import ListService
from .task_crud import TaskService
from sqlalchemy import or_


class UserService:

    #Проверка пароля
    @staticmethod
    def check_password(username: str, password: str) -> bool:
        user = models.User.query.filter_by(name=username).first()
        if user is None:
            return False 
        user_password = models.Password.query.filter_by(id=user.id).first()
        if user_password is None:
            return False
        if password == user_password.password:
            return True 
        return False 

    
    #Поиск пользователя по имени
    @staticmethod
    def find_user_by_username(username: str):
        user = models.User.query.filter_by(name=username).first()
        if user is None:
            return None
        return user.id
    

    #найти пользователя по id
    @staticmethod
    def get_user_by_id(id: int):
        user = models.User.query.get(id)
        return user
    

    #Создать нового пользователя
    @staticmethod
    def create_new_user(username: str, email: str, password: str):
        user_uniq_name = utils.create_unic_name(username)
        while UserService.find_user_by_username(user_uniq_name) is not None:
            user_uniq_name = utils.create_unic_name(username)
        new_user = models.User(name=user_uniq_name, email=email)
        models.db.session.add(new_user)
        models.db.session.commit() 
        user = models.User.query.filter_by(name=user_uniq_name).first()
        if user is None:
            return 'Пользователь не найден после создания'
        new_password = models.Password(id=user.id, password=password)
        models.db.session.add(new_password)
        models.db.session.commit() 
        return user.id


    #Удалить пользователя по id пользователя 
    @staticmethod
    def delete_user(id: int):
        user = models.User.query.get(id)
        models.db.session.delete(user)
        #удалить все листы пользователя (личные и управляемые)
        own_lists = ListService.show_own_lists(id)
        for own_list in own_lists:
            ListService.delete_list(id, own_list.id)
        author_lists = ListService.show_author_lists(id)
        for author_list in author_lists:
            ListService.delete_list(id, author_list.id)
        #разорвать связи с групповыми листами 
        accesses = models.Access.query.filter_by(user=id).all()
        for access in accesses:
                  models.db.session.delete(access)
        #удалить таски с пользователем в групповых листах  
        group_lists = ListService.show_group_lists(id)
        for group_list in group_lists:
            user_tasks = TaskService.show_list_tasks(group_list.id, id)
            for user_task in user_tasks:
                models.db.session.delete(user_task)
        #удалить все дружбы пользователя
        friendships = models.Friend.query.filter(
                (models.Friend.friend_1 == id) | (models.Friend.friend_2 == id)
            ).all()
        for friendship in friendships:
            models.db.session.delete(friendship)
        models.db.session.commit()


    #подружить пользователей
    @staticmethod
    def create_friendship(user_1: int, user_2: int):
        friendship = models.Friend(friend_1=user_1, friend_2=user_2)
        models.db.session.add(friendship)
        models.db.session.commit()
        return True


    #убрать из друзей пользователя
    @staticmethod
    def delete_friendship(user_1: int, user_2: int):
        friendship = models.Friend.query.filter(
        or_(
            (models.Friend.friend_1 == user_1) & (models.Friend.friend_2 == user_2),
            (models.Friend.friend_1 == user_2) & (models.Friend.friend_2 == user_1)
        )
        ).first()
        if friendship:
            models.db.session.delete(friendship)
            models.db.session.commit()
            return True
        return False


    #Вывести друзей
    @staticmethod
    def show_friends(user: int):
        friendships_1 = models.Friend.query.filter_by(friend_1=user).all()
        friendships_2 = models.Friend.query.filter_by(friend_2=user).all()
        friend_1_ids = [friendship_1.friend_2 for friendship_1 in friendships_1]
        friend_2_ids = [friendship_2.friend_1 for friendship_2 in friendships_2]
        friendships = friend_1_ids + friend_2_ids
        return friendships
    

    #Проверить дружбу
    @staticmethod
    def check_friendship(user_1: int, user_2: int):
        friendship = models.Friend.query.filter(
        or_(
            (models.Friend.friend_1 == user_1) & (models.Friend.friend_2 == user_2),
            (models.Friend.friend_1 == user_2) & (models.Friend.friend_2 == user_1)
        )
        ).first()
        if friendship:
            return True
        else:
            return False


        



        


