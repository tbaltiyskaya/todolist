from flask import Flask, request
from views import view_user, view_list, view_task
from flask import Blueprint
from services import utils
from flask import jsonify


routes = Blueprint('user_routes', __name__)

#Операции с пользователями

@routes.route('/sign_in', methods=['POST'])
def sign_in_route():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    return view_user.sign_in(username, password)


@routes.route('/sign_up', methods=['POST'])
def sign_up_route():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    new_user_id = view_user.sign_up(username, email, password)
    return new_user_id


@routes.route('/show_user_by_id', methods=['POST'])
def show_user_by_id_route():
    data = request.get_json()
    user_id = data.get('user_id')
    return view_user.get_user_by_id(user_id)


@routes.route('/show_user_friends', methods=['POST'])
def show_user_friends_route():
    data = request.get_json()
    user_id = data.get('watcher_id')
    return view_user.get_user_friends(user_id)


@routes.route('/find_friend', methods=['POST'])
def find_friend_route():
    data = request.get_json()
    user_id = data.get('user_id')
    username = data.get('find_username')
    return view_user.find_user_by_name(user_id, username)


@routes.route('/delete_friend', methods=['POST'])
def delete_friend_route():
    data = request.get_json()
    user_id = data.get('user_id')
    friend_id = data.get('friend_id')
    return view_user.delete_friend(user_id, friend_id)

#Заявка в друзья
@routes.route('/req_add_friend', methods=['POST'])
def req_add_friend_route():
    data = request.get_json()
    user_id = data.get('user_id')
    friend_id = data.get('friend_id')
    return view_user.req_add_friend(user_id, friend_id)

#Просмотр заявок в друзья
@routes.route('/show_friend_notices', methods=['POST'])
def show_friend_notices_route():
    data = request.get_json()
    user_id = data.get('user_id')
    return view_user.show_friend_notices(user_id)


#Принятие или отказ заявки в друзья
@routes.route('/resp_add_friend', methods=['POST'])
def resp_add_friend_route():
    data = request.get_json()
    notice_id = data.get('notice_id')
    status = data.get('status')
    return view_user.resp_add_friend(notice_id, status)


@routes.route('/req_add_member', methods=['POST'])
def req_add_member_route():
    data = request.get_json()
    user_id = data.get('author_id')
    member_id = data.get('member_id')
    list_id = data.get('list_id')
    return view_list.req_add_member(user_id, member_id, list_id)


@routes.route('/resp_add_member', methods=['POST'])
def resp_add_member_route():
    data = request.get_json()
    notice_id = data.get('notice_id')
    status = data.get('status')
    return view_list.resp_add_member(notice_id, status)



@routes.route('/show_list_notices', methods=['POST'])
def show_list_notices_route():
    data = request.get_json()
    user_id = data.get('user_id')
    return view_user.show_list_notices(user_id)


@routes.route('/get_friend_notice', methods=['POST'])
def get_friend_notice_route():
    data = request.get_json()
    notice_id = data.get('notice_id')
    return view_user.get_friend_notice(notice_id)


@routes.route('/get_list_notice', methods=['POST'])
def get_list_notice_route():
    data = request.get_json()
    notice_id = data.get('notice_id')
    return view_user.get_list_notice(notice_id)



#Операции с листами
@routes.route('/create_list', methods=['POST'])
def create_list_route():
    data = request.get_json()
    user_id = data.get('user_id')
    name = data.get('tempName')
    groupType = data.get('groupType')
    dateType = data.get('dateType')
    return view_list.create_list(user_id, name, dateType, groupType)


@routes.route('/rename_list', methods=['POST'])
def rename_list_route():
    data = request.get_json()
    list_id = data.get('list_id')
    name = data.get('tempName')
    return view_list.rename_list(list_id, name)


@routes.route('/delete_list', methods=['POST'])
def delete_list_route():
    data = request.get_json()
    list_id = data.get('list_id')
    user_id = data.get('user_id')
    return view_list.delete_list(list_id, user_id)


@routes.route('/show_all_lists', methods=['POST'])
def show_all_lists_route():
    data = request.get_json()
    user_id = data.get('user_id')
    return view_list.show_all_lists(user_id)


@routes.route('/show_own_lists', methods=['POST'])
def show_own_lists_route():
    data = request.get_json()
    user_id = data.get('user_id')
    return view_list.show_own_lists(user_id)


@routes.route('/show_group_lists', methods=['POST'])
def show_group_lists_route():
    data = request.get_json()
    user_id = data.get('user_id')
    return view_list.show_group_lists(user_id)


@routes.route('/show_author_lists', methods=['POST'])
def show_author_lists_route():
    data = request.get_json()
    user_id = data.get('user_id')
    return view_list.show_author_lists(user_id)


@routes.route('/show_list_cover', methods=['POST'])
def show_list_cover_route():
    data = request.get_json()
    list_id = data.get('list_id')
    return view_list.show_list_cover(list_id)


@routes.route('/show_list_members', methods=['POST'])
def show_list_members_route():
    data = request.get_json()
    user_id = data.get('watcher_id')
    list_id = data.get('subject_id')
    return view_list.show_list_members(user_id, list_id)


@routes.route('/show_possible_list_members', methods=['POST'])
def show_possible_list_members_route():
    data = request.get_json()
    user_id = data.get('watcher_id')
    list_id = data.get('subject_id')
    return view_list.show_possible_list_members(user_id, list_id)


@routes.route('/get_list_name', methods=['POST'])
def get_list_name_route():
    data = request.get_json()
    list_id = data.get('list_id')
    return view_list.get_list_name(list_id)

#Операции с задачами

@routes.route('/show_task', methods=['POST'])
def show_task_route():
    data = request.get_json()
    task_id = data.get('task_id')
    return view_task.show_task(task_id)


@routes.route('/create_task', methods=['POST'])
def create_task_route():
    data = request.get_json()
    task_props = {
    'list': data.get('task_list'),
    'author': data.get('task_author'),
    'executor': data.get('task_executor'),
    'name': data.get('task_name'),
    'desc': data.get('task_desc'),
    'date': data.get('task_date'),
    'time': data.get('task_time'),
    'priority': data.get('task_priority')}
    return view_task.create_task(task_props)


@routes.route('/update_task', methods=['POST'])
def update_task_route():
    data = request.get_json()
    task_id = data.get('task_id')
    task_props = {
    'executor': data.get('task_executor'),
    'name': data.get('task_name'),
    'desc': data.get('task_desc'),
    'date': data.get('task_date'),
    'time': data.get('task_time'),
    'priority': data.get('task_priority')}
    return view_task.update_task(task_id, task_props)


@routes.route('/change_task_status', methods=['POST'])
def change_task_status_route():
    data = request.get_json()
    task_id = data.get('task_id')
    status = data.get('task_status')
    return view_task.change_task_status(task_id, status)


@routes.route('/show_own_list_tasks', methods=['POST'])
def show_own_list_tasks_route():
    data = request.get_json()
    user_id = data.get('user_id')
    list_id = data.get('list_id')
    list_datetype = data.get('list_datetype')
    task_date = data.get('task_date')
    return view_task.show_own_list_tasks(user_id, list_id, list_datetype, task_date)


@routes.route('/show_authored_list_tasks', methods=['POST'])
def show_authored_list_tasks_route():
    data = request.get_json()
    user_id = data.get('user_id')
    list_id = data.get('list_id')
    list_datetype = data.get('list_datetype')
    task_date = data.get('task_date')
    return view_task.show_authored_list_tasks(user_id, list_id, list_datetype, task_date)


@routes.route('/show_all_list_tasks', methods=['POST'])
def show_all_list_tasks_route():
    data = request.get_json()
    user_id = data.get('user_id')
    list_id = data.get('list_id')
    list_datetype = data.get('list_datetype')
    task_date = data.get('task_date')
    return view_task.show_all_list_tasks(user_id, list_id, list_datetype, task_date)


@routes.route('/show_day_tasks', methods=['POST'])
def show_day_tasks_route():
    data = request.get_json()
    user_id = data.get('user_id')
    task_date = data.get('task_date')
    return view_task.show_day_tasks(user_id, task_date)


@routes.route('/check_list', methods=['POST'])
def check_lists_route():
    data = request.get_json()
    list_id = data.get('list_id')
    return view_list.check_list(list_id)


@routes.route('/delete_task', methods=['POST'])
def delete_task_route():
    data = request.get_json()
    user_id = data.get('user_id')
    task_id = data.get('task_id')
    return view_task.delete_task(user_id, task_id)


@routes.route('/show_archived_tasks', methods=['POST'])
def show_archived_tasks_route():
    data = request.get_json()
    user_id = data.get('user_id')
    return view_task.show_archived_tasks(user_id)


@routes.route('/archive_task', methods=['POST'])
def archive_task_route():
    data = request.get_json()
    user_id = data.get('user_id')
    task_id = data.get('task_id')
    return view_task.archive_task(user_id, task_id)


@routes.route('/unzip_task', methods=['POST'])
def unzip_task_route():
    data = request.get_json()
    task_id = data.get('task_id')
    task_list = data.get('task_list')
    return view_task.unzip_task(task_id, task_list)


@routes.route('/get_progress', methods=['POST'])
def get_progress_route():
    data = request.get_json()
    list_id = data.get('list_id')
    user_id = data.get('user_id')
    task_date = data.get('task_date')
    return view_task.get_progress(list_id, user_id, task_date)






