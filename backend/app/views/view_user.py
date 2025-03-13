from services.user_crud import UserService
from services.list_crud import ListService
from werkzeug.exceptions import BadRequest
from services.notice_crud import NoticeService
from flask import jsonify
from typing import Dict

import logging

#войти в аккаунт 
def sign_in(username: str, password: str):
    try:           
        if UserService.check_password(username, password):
            user_id = UserService.find_user_by_username(username)
            return jsonify({'status': 'success', 'data': user_id}), 200
        else: 
            return jsonify({'status': 'error', 'message': 'Invalid username or password'}), 401
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500


#зарегистрироваться  
def sign_up(username: str, email: str, password: str):
    try:
        if not username or not email or not password:
            return BadRequest("Username, email, and password are required.")
        new_user_id = UserService.create_new_user(username, email, password)
        if new_user_id is None:
            return jsonify({'status': 'error', 'message': 'Registration error'}), 401
        return jsonify({'status': 'success', 'data': new_user_id}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500


#Получить данные пользователя по id 
def get_user_by_id(user_id: int):
    try:
        user = UserService.get_user_by_id(user_id)
        if user is not None:
            username = user.name
            email = user.email
            responce = {'username': username, 'email': email}
            return jsonify({'status': 'success', 'data': responce}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

#Вывести друзей пользователя
def get_user_friends(user_id: int):
    try:
        if user_id is None:
            return BadRequest("User id is required")
        friendlist = UserService.show_friends(user_id)
        return jsonify({'status': 'success', 'data': friendlist}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def find_user_by_name(finder: int, username: str):
    try:
        if finder is None or username is None:
            return BadRequest("Username is required")
        user_id = UserService.find_user_by_username(username)
        if user_id is None:
            responce = {'user_id': 0, 'add': False}
            return jsonify({'status': 'success', 'data': responce }), 201
        if UserService.check_friendship(finder, user_id):
            responce = {'user_id': user_id, 'add': False}
            return jsonify({'status': 'success', 'data': responce }), 201
        responce = {'user_id': user_id, 'add': True}
        return jsonify({'status': 'success', 'data': responce }), 201
    except Exception as e:
        logging.error(f"Error find_user_by_name: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def delete_friend(user_id: int, friend_id: int):
    try:
        if user_id is None or friend_id is None:
            return BadRequest("UserIds are required")
        friendship = UserService.delete_friendship(user_id, friend_id)
        if friendship:
            return jsonify({'status': 'success', 'data': True}), 201
        return jsonify({'status': 'success', 'data': False }), 201
    except Exception as e:
        logging.error(f"Error find_user_by_name: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500


def req_add_friend(user_id: int, friend_id: int):
    try:
        if user_id is None or friend_id is None:
            return BadRequest("UserIds are required")
        notice = NoticeService.create_friend_notice(user_id, friend_id)
        if notice:
            return jsonify({'status': 'success', 'data': True}), 201
        return jsonify({'status': 'error', 'message': 'Friendship error'}), 401
    except Exception as e:
        logging.error(f"Error find_user_by_name: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    


def resp_add_friend(notice_id: int, status: bool):
    try:
        if notice_id is None or status is None:
            return BadRequest("UserIds are required")
        notice = NoticeService.get_friend_notice(notice_id)
        if notice is None:
            return jsonify({'status': 'error', 'message': 'notice error'}), 401
        if status:
            user_1 = notice.sender
            user_2 = notice.getter
            friendship = UserService.create_friendship(user_1, user_2)
            if friendship:
                NoticeService.delete_friend_notice(notice_id)
                return jsonify({'status': 'success', 'data': True}), 201
        else:
            NoticeService.delete_friend_notice(notice_id)
            return jsonify({'status': 'success', 'data': True}), 201
        
    except Exception as e:
        logging.error(f"Error find_user_by_name: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    


def show_friend_notices(user_id: int):
    try:
        if user_id is None:
            return BadRequest("UserIds are required")
        notices = NoticeService.show_friend_notices(user_id)
        return jsonify({'status': 'success', 'data': notices}), 201
    except Exception as e:
        logging.error(f"Error find_user_by_name: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def show_list_notices(user_id: int):
    try:
        if user_id is None:
            return BadRequest("UserIds are required")
        notices = NoticeService.show_list_notices(user_id)
        return jsonify({'status': 'success', 'data': notices}), 201
    except Exception as e:
        logging.error(f"Error find_user_by_name: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def get_friend_notice(notice_id: int):
    try:
        if notice_id is None:
            return BadRequest("UserIds are required")
        notice = NoticeService.get_friend_notice(notice_id)
        responce = {'sender': notice.sender, 'getter': notice.getter}
        return jsonify({'status': 'success', 'data': responce}), 201
    except Exception as e:
        logging.error(f"Error find_user_by_name: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500


def get_list_notice(notice_id: int):
    try:
        if notice_id is None:
            return BadRequest("UserIds are required")
        notice = NoticeService.get_list_notice(notice_id)
        list_name = ListService.get_list_name(notice.list)
        responce = {'sender': notice.sender, 'getter': notice.getter,
                     'list': notice.list, 'list_name': list_name }
        return jsonify({'status': 'success', 'data': responce}), 201
    except Exception as e:
        logging.error(f"Error find_user_by_name: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500


    



