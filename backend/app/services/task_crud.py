from db import database
from db import models
from services import utils
from typing import Dict 
from datetime import datetime


class TaskService:

    #Вывести задачу
    @staticmethod
    def show_task_by_id(id: int):
        task = models.Task.query.filter_by(id=id).first()
        return task


    #Создать новую заметку
    @staticmethod
    def create_new_task(params: Dict[str, any]):
        date_str = params.get('date')
        time_str = params.get('time')
        if date_str and time_str:
            datetime_str = f"{date_str} {time_str}"
            task_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
            date_str = task_datetime.date()
            time_str = task_datetime.time()
        elif date_str:
            date_str = datetime.strptime(date_str, '%Y-%m-%d').date()
        new_task = models.Task(
            list=params.get('list'),
            author=params.get('author'),
            executor=params.get('executor'),
            name=params.get('name'),
            desc=params.get('desc'),
            date=date_str,
            time=time_str,
            priority=params.get('priority'),
            status=1
        )
        models.db.session.add(new_task)
        models.db.session.commit()
        return True


    #удалить заметку
    @staticmethod
    def delete_task(id: int, user: int):
        task = models.Task.query.get(id)
        if task.author == user and task is not None:
            models.db.session.delete(task)
            models.db.session.commit()
            return True
        else:
            return False


    #редактировать заметку
    @staticmethod
    def update_task(id: int, params: Dict[str, any]):
        task = models.Task.query.filter_by(id=id).first()
        if task is None:
            return False
        date_str = params.get('date')
        time_str = params.get('time')
        if date_str and time_str:
            datetime_str = f"{date_str} {time_str}"
            task_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
            date_str = task_datetime.date()
            time_str = task_datetime.time()
        elif date_str:
            date_str = datetime.strptime(date_str, '%Y-%m-%d').date()
        task.executor = params.get('executor')
        task.name = params.get('name')
        task.desc = params.get('desc')
        task.date = date_str
        task.time = time_str
        task.priority = params.get('priority')
        models.db.session.commit()
        return True


    @staticmethod
    def update_task_status(id: int, status: int):
        task = models.Task.query.filter_by(id=id).first()
        if task is None:
            return False
        task.status = status
        models.db.session.commit()
        return True
    

    #архивировать заметку
    @staticmethod
    def archive_task(task_id: int, user_id: int):
        task = models.Task.query.filter_by(id=task_id, author=user_id).first()
        if task is not None: 
            task.list = None
            task.date = None
            task.time = None
            task.priority = 2
            task.status = 0
            models.db.session.commit()
            return True
        return False


    #Перенести заметку из архива в лист
    @staticmethod
    def push_task_to_list(id: int, list: int):
        task = models.Task.query.get(id)
        if(task.list is None):
            this_list = models.List.query.filter_by(id=list).first()
            if(this_list.datetype == False and this_list.grouptype == False):
                task.list = list
                task.status = 1
                models.db.session.commit()
                return True
            elif (this_list.datetype == True and this_list.grouptype == False):
                current_date = datetime.now()
                task.date = current_date.date()
                task.list = list
                task.status = 1
                models.db.session.commit()
                return True
            else:
                return False
        return False
            
            


    @staticmethod
    def show_own_list_tasks(user_id: int, list_id: int, list_datetype: bool, task_date: str):
        if list_datetype:
            date_object = datetime.strptime(task_date, '%Y-%m-%d')
            date = date_object.date()
            tasks = models.Task.query.filter_by(list=list_id, date=date, executor=user_id).all()
            tasks_ids = [task.id for task in tasks]
            return tasks_ids
        else:
            tasks = models.Task.query.filter_by(list=list_id, executor=user_id).all()
            tasks_ids = [task.id for task in tasks]
            return tasks_ids


    @staticmethod 
    def show_authored_list_tasks(user_id: int, list_id: int, list_datetype: bool, task_date: str):
        if list_datetype:
            date_object = datetime.strptime(task_date, '%Y-%m-%d')
            date = date_object.date()
            tasks = models.Task.query.filter_by(list=list_id, date=date, author=user_id).all()
            tasks_del = models.Task.query.filter_by(list=list_id, date=date, author=user_id, executor=user_id).all()
            tasks_ids = [task.id for task in tasks]
            task_ids_del = [task.id for task in tasks_del]
            filtered_tasks_ids = [task_id for task_id in tasks_ids if task_id not in task_ids_del]
            return filtered_tasks_ids
        else:
            tasks = models.Task.query.filter_by(list=list_id, author=user_id).all()
            tasks_del = models.Task.query.filter_by(list=list_id, author=user_id, executor=user_id).all()
            tasks_ids = [task.id for task in tasks]
            task_ids_del = [task.id for task in tasks_del]
            filtered_tasks_ids = [task_id for task_id in tasks_ids if task_id not in task_ids_del]
            return filtered_tasks_ids


    @staticmethod
    def show_all_list_tasks(user_id: int, list_id: int, list_datetype: bool, task_date: str):
        this_list = models.List.query.filter_by(id=list_id).first()
        if this_list.author == user_id:
            if list_datetype:
                date_object = datetime.strptime(task_date, '%Y-%m-%d')
                date = date_object.date()
                tasks = models.Task.query.filter_by(list=list_id, date=date).all()
                tasks_ids = [task.id for task in tasks]
                return tasks_ids
            else:
                tasks = models.Task.query.filter_by(list=list_id).all()
                tasks_ids = [task.id for task in tasks]
                return tasks_ids


    @staticmethod
    def show_day_tasks(user_id: int, task_date: str):
        date_object = datetime.strptime(task_date, '%Y-%m-%d')
        date = date_object.date()
        tasks = models.Task.query.filter_by(executor=user_id, date=date).all()
        tasks_ids = [task.id for task in tasks]
        return tasks_ids
    

    @staticmethod
    def show_archived_tasks(user_id: int):
        tasks = models.Task.query.filter_by(author=user_id, status=0).all()
        tasks_ids = [task.id for task in tasks]
        return tasks_ids
    

    @staticmethod
    def count_progress(list_id: int, user_id: int, task_date: str):
        this_list = models.List.query.filter_by(id=list_id).first()
        if this_list.datetype:
            date_object = datetime.strptime(task_date, '%Y-%m-%d')
            date = date_object.date()
            if this_list.grouptype:
                tasks = models.Task.query.filter_by(list=list_id, date=date).all()
                user_tasks = models.Task.query.filter_by(list=list_id, executor=user_id, date=date).all()
                statuses = [task.status for task in tasks]
                statuses = list(filter(lambda x: x != 4, statuses))
                user_statuses = [task.status for task in user_tasks]
                user_statuses = list(filter(lambda x: x != 4, user_statuses))
                wish_progress = len(statuses) * 3
                progress = sum(statuses)
                user_progress = sum(user_statuses)
                return {'wish_progress': wish_progress, 'progress': progress, 'user_progress': user_progress}

            else:
                user_tasks = models.Task.query.filter_by(list=list_id, executor=user_id, date=date).all()
                user_statuses = [task.status for task in user_tasks]
                user_statuses = list(filter(lambda x: x != 4, user_statuses))
                wish_progress = len(user_statuses) * 3
                user_progress = sum(user_statuses)
                return {'wish_progress': wish_progress, 'progress': user_progress, 'user_progress': user_progress}
        else:
            if this_list.grouptype:
                tasks = models.Task.query.filter_by(list=list_id).all()
                user_tasks = models.Task.query.filter_by(list=list_id, executor=user_id).all()
                statuses = [task.status for task in tasks]
                statuses = list(filter(lambda x: x != 4, statuses))
                user_statuses = [task.status for task in user_tasks]
                user_statuses = list(filter(lambda x: x != 4, user_statuses))

                wish_progress = len(statuses) * 3
                progress = sum(statuses)
                user_progress = sum(user_statuses)
                return {'wish_progress': wish_progress, 'progress': progress, 'user_progress': user_progress}
            else:
                user_tasks = models.Task.query.filter_by(list=list_id, executor=user_id).all()
                user_statuses = [task.status for task in user_tasks]
                user_statuses = list(filter(lambda x: x != 4, user_statuses))
                wish_progress = len(user_statuses) * 3
                user_progress = sum(user_statuses)
                return {'wish_progress': wish_progress, 'progress': user_progress, 'user_progress': user_progress}

    




    
    

    

                







