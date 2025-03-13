from flask import jsonify
from services.task_crud import TaskService
from typing import Dict
from werkzeug.exceptions import BadRequest

import logging

logging.basicConfig(level=logging.DEBUG)


def show_task(task_id: int):
    try:
        if task_id is None:
            return BadRequest("User id, name, isDated and isGroup are required")
        task = TaskService.show_task_by_id(task_id)
        if task is None:
            return jsonify({'status': 'error', 'message': 'Task is not found'}), 401
        if task.time is not None:
            task_time = task.time.strftime("%H:%M")
        else: task_time = task.time
        if task.date is not None:
            task_date = task.date.strftime("%Y-%m-%d")
        else: task_date = task.date
        name = str(task.name) if task.name is not None else ''
        desc = str(task.desc) if task.desc is not None else ''
        responce = {'list': task.list,
                    'author': task.author,
                    'executor': task.executor,
                    'name': name,
                    'desc': desc,
                    'date': task_date,
                    'time': task_time,
                    'priority': task.priority,
                    'status': task.status
                    }
        return jsonify({'status': 'success', 'data': responce}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    


def create_task(params: Dict[str, any]):
    try:
        if params.get('list') is None or params.get('author') is None or params.get('executor') is None or params.get('name') is None:
            return BadRequest("User id, name, isDated and isGroup are required")
        created = TaskService.create_new_task(params)
        if created:
            return jsonify({'status': 'success'}), 201
        return jsonify({'status': 'error', 'message': 'Task is not created'}), 401
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

#сменить статус задачи 
def change_task_status(task_id: int, status: int):
    try:
        if task_id is None or status is None:
            return BadRequest("Task id and task name are required")
        updated_status = TaskService.update_task_status(task_id, status)
        if updated_status:
            return jsonify({'status': 'success', 'data': updated_status }), 200
        return jsonify({'status': 'error', 'message': 'Task is not updated'}), 401
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500

    

def delete_task(user_id: int,  task_id: int):
    try:
        if task_id is None or user_id is None:
            return BadRequest("Task id and task name are required")
        is_deleted = TaskService.delete_task(task_id, user_id)
        if is_deleted: 
            return jsonify({'status': 'success', 'data': True}), 200
        else:
            return jsonify({'status': 'error', 'message': 'task is not deleted'}), 401
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def archive_task(user_id: int,  task_id: int):
    try:
        if task_id is None or user_id is None:
            return BadRequest("Task id and task name are required")
        is_archived = TaskService.archive_task(task_id, user_id)
        if is_archived: 
            return jsonify({'status': 'success', 'data': True}), 200
        return jsonify({'status': 'error', 'message': 'task is not archived'}), 401
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    


def unzip_task(task_id: int, task_list: int):
    try:
        if task_id is None or task_list is None:
            return BadRequest("Task id and task name are required")
        is_unziped = TaskService.push_task_to_list(task_id, task_list)
        if is_unziped: 
            return jsonify({'status': 'success', 'data': True}), 200
        return jsonify({'status': 'error', 'message': 'task is not unziped'}), 401
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    
    

def update_task(task_id: int, params: Dict[str, any]):
    try:
        if task_id is None or params.get('name') is None or params.get('executor') is None:
            return BadRequest("Task id and task name are required")
        updated_task = TaskService.update_task(task_id, params)
        if updated_task:
            return jsonify({'status': 'success', 'data': updated_task }), 200
        return jsonify({'status': 'error', 'message': 'Task is not updated'}), 401
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def show_own_list_tasks(user_id: int, list_id: int, list_datetype: bool, task_date: str):
    try:
        if user_id is None or list_id is None or list_datetype is None or task_date is None:
            return BadRequest("User_id, list_id, list_datetype and task_date are required")
        tasks = TaskService.show_own_list_tasks(user_id, list_id, list_datetype, task_date)
        return jsonify({'status': 'success', 'data': tasks}), 200
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def show_authored_list_tasks(user_id: int, list_id: int, list_datetype: bool, task_date: str):
    try:
        if user_id is None or list_id is None or list_datetype is None or task_date is None:
            return BadRequest("User_id, list_id, list_datetype and task_date are required")
        tasks = TaskService.show_authored_list_tasks(user_id, list_id, list_datetype, task_date)
        return jsonify({'status': 'success', 'data': tasks}), 200
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500


def show_all_list_tasks(user_id: int, list_id: int, list_datetype: bool, task_date: str):
    try:
        if user_id is None or list_id is None or list_datetype is None or task_date is None:
            return BadRequest("User_id, list_id, list_datetype and task_date are required")
        tasks = TaskService.show_all_list_tasks(user_id, list_id, list_datetype, task_date)
        return jsonify({'status': 'success', 'data': tasks}), 200
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def show_day_tasks(user_id: int, task_date: str):
    try:
        if user_id is None or task_date is None:
            return BadRequest("User_id, list_id, list_datetype and task_date are required")
        tasks = TaskService.show_day_tasks(user_id, task_date)
        return jsonify({'status': 'success', 'data': tasks}), 200
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def show_archived_tasks(user_id: int):
    try:
        if user_id is None:
            return BadRequest("User_id, list_id, list_datetype and task_date are required")
        tasks = TaskService.show_archived_tasks(user_id)
        return jsonify({'status': 'success', 'data': tasks}), 200
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def get_progress(list_id: int, user_id: int, task_date: str):
    try:
        if list_id is None or user_id is None:
            return BadRequest("User_id, list_id, list_datetype and task_date are required")
        progress = TaskService.count_progress(list_id, user_id, task_date)
        return jsonify({'status': 'success', 'data': progress}), 200
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500







    
