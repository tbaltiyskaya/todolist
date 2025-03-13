from services.user_crud import UserService
from services.list_crud import ListService
from werkzeug.exceptions import BadRequest
from flask import jsonify
from typing import Dict

#войти в аккаунт 
def sign_in(username: str, password: str):
    if UserService.check_password(username, password):
        return jsonify({'status': 'success', 'message': 'Login successful'}), 200
    else: 
        return jsonify({'status': 'error', 'message': 'Invalid username or password'}), 401

#зарегистрироваться  
def sign_up(username: str, email: str, password: str):
    try:
        if not username or not email or not password:
            raise BadRequest("Username, email, and password are required.")
        UserService.create_new_user(username, email, password)
        return jsonify({'status': 'success', 'message': 'Sign up successful'}), 200
    except:
        return jsonify({'status': 'error', 'message': 'Registration error'}), 401

  
#создать лист
def create_list(params: Dict[str, any]):
    user_id=params.get('user_id')
    name=params.get('name')
    isDated=params.get('Isdated')
    isGroup=params.get('IsGroup')
    if(name == None):
        return jsonify({'status': 'error', 'message': 'Name of list must be not null'}), 401
    try:
        ListService.create_new_list(user_id, name, isDated, isGroup)
        return jsonify({'status': 'success', 'message': 'List created successful'}), 200
    except:
        return jsonify({'status': 'error', 'message': 'Unknown Error'}), 401
    

#переименовать лист
def rename_list(list_id: int, name: str):
    if list_id is None or not name:
        return jsonify({'status': 'error', 'message': 'List ID and name are required'}), 400
    try:
        ListService.update_list_name(list_id, name)
        return jsonify({'status': 'success', 'message': 'List renamed successful'}), 200
    except:
        return jsonify({'status': 'error', 'message': 'Unknown Error'}), 500
    

#Удалить лист
def delete_list(user_id: int, list_id: int):
    if(user_id is None or list_id is None):
        return jsonify({'status': 'error', 'message': 'params are None'}), 400
    try:
        ListService.delete_list(user_id, list_id)
        return jsonify({'status': 'success', 'message': 'List deleted successful'}), 200
    except:
        return jsonify({'status': 'error', 'message': 'Unknown Error'}), 500


#Показать листы пользователя
def show_lists(user_id: int, type: str):
    if user_id is None or not type:
        return jsonify({'status': 'error', 'message': 'User is None'}), 400
    if (type!= 'all' and type!= 'own' and type!= 'group' and type!= 'author'):
        return jsonify({'status': 'error', 'message': 'Uncorrect type'}), 400
    try:
        if type == 'all':
            all_lists = ListService.show_all_lists(user_id)
        elif type == 'own':
            all_lists = ListService.show_own_lists(user_id)
        elif type == 'group':
            all_lists = ListService.show_group_lists(user_id)
        elif type == 'author':
            all_lists = ListService.show_author_lists(user_id)
        return jsonify({'status': 'success', 'data': all_lists}), 200
    except:
        return jsonify({'status': 'error', 'message': 'Unknown Error'}), 500


#открыть лист    
def open_list( user_id: int, list_id: int):
    if user_id is None or list_id is None:
        return jsonify({'status': 'error', 'message': 'params are None'}), 400
    try:
        type = ListService.check_list_type(list_id)
    except:
        return jsonify({'status': 'error', 'message': 'Unknown Error'}), 500




    

    

    


