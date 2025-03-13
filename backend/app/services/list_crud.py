from db import database
from db import models
from services import utils
from .task_crud import TaskService


class ListService:

    #Создать новый лист
    @staticmethod
    def create_new_list(user_id: int, name: str, isDated: bool, isGroup: bool):
        new_list = models.List( author=user_id, name=name, datetype=isDated, grouptype=isGroup)
        models.db.session.add(new_list)
        models.db.session.commit()
        if isGroup:
             access = models.Access(list=new_list.id, author=new_list.author, user=new_list.author)
             models.db.session.add(access)
             models.db.session.commit()
        return new_list.id


    @staticmethod
    def check_list_type(list: int):
        type = {'datetype': False, 'grouptype': False}
        this_list = models.List.query.filter_by(id=list).first()
        if this_list.datetype and this_list.grouptype:
            type['datetype'] = True
            type['grouptype'] = True
        elif this_list.datetype:
            type['datetype'] = True
        elif this_list.grouptype:
            type['grouptype'] = True
        return type


    #Изменить название листа
    @staticmethod
    def update_list_name(id: int, name: str):
        this_list = models.List.query.filter_by(id=id).first()
        this_list.name = name
        models.db.session.commit()
        return True


    @staticmethod
    def get_list_name(id: int):
        this_list = models.List.query.filter_by(id=id).first()
        name = this_list.name
        return name
    
    #Пригласить в групповой лист пользователя
    @staticmethod
    def add_user_to_list(list: int, author: int, user: int):
        this_list = models.List.query.filter_by(id=list, author=author, grouptype=True).first()
        if this_list is None:
            return False
        access = models.Access.query.filter_by(list=list, user=user).first()
        if access is None:
            new_access = models.Access(list=list, author=author, user=user)
            models.db.session.add(new_access)
            models.db.session.commit()
            return True
        return False


    #Удалить из группового листа пользователя
    @staticmethod
    def delete_user_from_list(list: int, author: int, user: int):
        this_list = models.List.query.filter_by(id=list, author=author, grouptype=True).first()
        access = models.Access.query.filter_by(list=this_list.id, user=user).first()
        models.db.session.delete(access)
        models.db.session.commit()
        return True
    
    
    #Удалить лист
    @staticmethod
    def delete_list(user: int, id: int):
        #Находим лист по id и правам управления
        this_list = models.List.query.filter_by(id=id, author=user).first()
        #Если прав на лист нет (он групповой но без управления)
        if this_list is None:
            #Удаляем связь пользователя с этим листом 
            access = models.Access.query.filter_by(list=id, user=user).first()
            if access:
                models.db.session.delete(access)
            #Удаляем все задачи пользователя в групповом листе
            tasks = TaskService.show_list_tasks(id, user)
            for task in tasks:
                models.db.session.delete(task)
        else:
            # удалить все таски с этим листом
            tasks = models.Task.query.filter_by(list=this_list.id).all()
            for task in tasks:
                models.db.session.delete(task) 
            #удалить лист из отношений если он групповой
            if(this_list.grouptype == True):
                accesses = models.Access.query.filter_by(list=id).all()
                for access in accesses:
                    models.db.session.delete(access)
            models.db.session.delete(this_list)
        models.db.session.commit()
        return True
    

    #Показать личные листы
    @staticmethod
    def show_own_lists(id: int):
        own_lists = models.List.query.filter_by(author=id, grouptype=False).all()
        list_ids = [own_list.id for own_list in own_lists]
        return list_ids
    

    #Показать групповые листы
    @staticmethod
    def show_group_lists(id: int):
        group_lists = models.Access.query.filter_by(user=id).all()
        list_ids = [group_list.list for group_list in group_lists]
        return list_ids
    

    #Показать управляемые листы
    @staticmethod
    def show_author_lists(id: int):
        author_lists = models.Access.query.filter_by(author=id, user=id).all()
        list_ids = [author_list.list for author_list in author_lists]
        return list_ids
    

    #показать все листы
    @staticmethod
    def show_all_lists(id: int):
         own_lists = ListService.show_own_lists(id)
         group_lists = ListService.show_group_lists(id)
         author_lists = ListService.show_author_lists(id)
         all_lists = own_lists + group_lists + author_lists
         unique_lists = list(set(all_lists))
         return unique_lists
    

    #показать лист по id
    @staticmethod
    def get_list(list_id: int):
        this_list = models.List.query.filter_by(id=list_id).first()
        return this_list


    #показать пользователей листа
    @staticmethod
    def show_list_users(user: int, list: int):
        if ListService.check_list_member(user, list):
            accesses = models.Access.query.filter_by(list=list).all()
            user_ids = [access.user for access in accesses]
            return user_ids
    

    #Проверить есть ли пользователь в листе
    @staticmethod
    def check_list_member(user: int, list: int):
        access = models.Access.query.filter_by(list=list, user=user).first()
        if access is None:
            return False
        return True
    

    @staticmethod
    def show_possible_members(user: int, list: int):
        from .user_crud import UserService
        if models.Access.query.filter_by(list=list, author=user).first():
            friends = UserService.show_friends(user)
            result_ids = []
            for friend in friends:
                inlist = ListService.check_list_member(friend, list)
                if not inlist:
                    result_ids.append(friend)
            return result_ids




