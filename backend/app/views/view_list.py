from flask import jsonify
from services.list_crud import ListService
from services.notice_crud import NoticeService
from typing import Dict
from werkzeug.exceptions import BadRequest

import logging

logging.basicConfig(level=logging.DEBUG)


def create_list(user_id: int, name: str, isDated: bool, isGroup: bool):
    try:
        if user_id is None or name is None or isDated is None or isGroup is None:
            return BadRequest("User id, name, isDated and isGroup are required")
        new_list_id = ListService.create_new_list(user_id, name, isDated, isGroup)
        if new_list_id is None:
            return jsonify({'status': 'error', 'message': 'List is not created'}), 401
        return jsonify({'status': 'success', 'data': new_list_id}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def get_list_name(list_id: int):
    try:
        if list_id is None:
            return BadRequest("User id, name, isDated and isGroup are required")
        list_name = ListService.get_list_name(list_id)
        if list_name is None:
            return jsonify({'status': 'error', 'message': 'List is not created'}), 401
        return jsonify({'status': 'success', 'data': list_name}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def rename_list(list_id: int, name: str):
    try:
        if list_id is None or name is None:
            return BadRequest("User id, name, isDated and isGroup are required")
        rename_status = ListService.update_list_name(list_id, name)
        if rename_status is False:
            return jsonify({'status': 'error', 'message': 'List is not renamed'}), 401
        return jsonify({'status': 'success', 'data': rename_status}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def delete_list(list_id: int, user_id: int):
    try:
        if list_id is None or user_id is None:
            return BadRequest("User id, name, isDated and isGroup are required")
        deleted_list = ListService.delete_list(user_id, list_id)
        if deleted_list is False:
            return jsonify({'status': 'error', 'message': 'List is not deleted'}), 401
        return jsonify({'status': 'success', 'data': deleted_list}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def show_all_lists(user_id: int):
    try:
        if user_id is None:
            return BadRequest("User id is required")
        all_lists = ListService.show_all_lists(user_id)
        return jsonify({'status': 'success', 'data': all_lists}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500

 
def show_own_lists(user_id: int):
    try:
        if user_id is None:
            return BadRequest("User id is required")
        own_lists = ListService.show_own_lists(user_id)
        return jsonify({'status': 'success', 'data': own_lists}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def show_group_lists(user_id: int):
    try:
        if user_id is None:
            return BadRequest("User id is required")
        group_lists = ListService.show_group_lists(user_id)
        return jsonify({'status': 'success', 'data': group_lists}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def show_author_lists(user_id: int):
    try:
        if user_id is None:
            return BadRequest("User id is required")
        author_lists = ListService.show_author_lists(user_id)
        return jsonify({'status': 'success', 'data': author_lists}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def show_list_cover(list_id: int):
    try:
        if list_id is None:
            return BadRequest("User id is required")
        this_list = ListService.get_list(list_id)
        if this_list is None:
            return BadRequest("List is not found")
        response = {'list_name': this_list.name, 'author': this_list.author, 'datetype': this_list.datetype, 'grouptype': this_list.grouptype}
        return jsonify({'status': 'success', 'data': response}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def show_list_members(user_id: int, list_id: int):
    try:
        if user_id is None or list_id is None:
            return BadRequest("User id is required")
        members = ListService.show_list_users(user_id, list_id)
        if members is None:
            return jsonify({'status': 'error', 'message': 'No access'}), 401
        return jsonify({'status': 'success', 'data': members}), 201

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    

def show_possible_list_members(user_id: int, list_id: int):
    try:
        if user_id is None or list_id is None:
            return BadRequest("User id is required")
        members = ListService.show_possible_members(user_id, list_id)
        if members is None:
            return jsonify({'status': 'error', 'message': 'No access'}), 401
        return jsonify({'status': 'success', 'data': members}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500 


def check_list(list_id: int):
    try:
        if list_id is None:
            return BadRequest("User id is required")
        type = ListService.check_list_type(list_id)
        if type is None:
            return jsonify({'status': 'error', 'message': 'No access'}), 401
        responce = { 
                'list_datetype': type.get('datetype'),
                'list_grouptype': type.get('grouptype')
            }
        return jsonify({'status': 'success', 'data': responce}), 201
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500 
    

def req_add_member(user_id: int, member_id: int, list_id: int):
    try:
        if user_id is None or member_id is None or list_id is None:
            return BadRequest("UserIds are required")
        notice = NoticeService.create_list_notice(user_id, member_id, list_id)
        if notice:
            return jsonify({'status': 'success', 'data': True}), 201
        return jsonify({'status': 'error', 'message': 'Friendship error'}), 401
    except Exception as e:
        logging.error(f"Error find_user_by_name: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
    


def resp_add_member(notice_id: int, status: bool):
    try:
        if notice_id is None or status is None:
            return BadRequest("UserIds are required")
        notice = NoticeService.get_list_notice(notice_id)
        if notice is None:
            return jsonify({'status': 'error', 'message': 'notice error'}), 401
        if status:
            author = notice.sender
            user = notice.getter
            list = notice.list
            adding = ListService.add_user_to_list(list, author, user)
            if adding:
                NoticeService.delete_list_notice(notice_id)
                return jsonify({'status': 'success', 'data': True}), 201
        else:
            NoticeService.delete_list_notice(notice_id)
            return jsonify({'status': 'success', 'data': True}), 201
        
    except Exception as e:
        logging.error(f"Error find_user_by_name: {e}")
        return jsonify({'status': 'error', 'message': 'Server error'}), 500
