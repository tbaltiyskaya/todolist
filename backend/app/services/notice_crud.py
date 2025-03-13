from db import database
from db import models
from services import utils
from typing import Dict 
from datetime import datetime


class NoticeService:

    @staticmethod
    def create_friend_notice(user_id: int, friend_id: int):
        new_notice = models.FriendNotice(sender=user_id, getter=friend_id)
        models.db.session.add(new_notice)
        models.db.session.commit()
        return True
    

    @staticmethod
    def delete_friend_notice(id: int):
        notice = models.FriendNotice.query.get(id)
        if notice is None:
            return False
        models.db.session.delete(notice)
        models.db.session.commit()
        return True
    

    @staticmethod
    def delete_list_notice(id: int):
        notice = models.ListNotice.query.get(id)
        if notice is None:
            return False
        models.db.session.delete(notice)
        models.db.session.commit()
        return True


    @staticmethod
    def create_list_notice(user_id: int, member_id: int, list_id: int):
        new_notice = models.ListNotice(sender=user_id, getter=member_id, list=list_id)
        models.db.session.add(new_notice)
        models.db.session.commit()
        return True


    @staticmethod
    def show_friend_notices(user_id: int):
        friend_notices = models.FriendNotice.query.filter_by(getter=user_id).all()
        f_notices_ids = [notice.id for notice in friend_notices]
        return f_notices_ids
    

    @staticmethod
    def show_list_notices(user_id: int):
        list_notices = models.ListNotice.query.filter_by(getter=user_id).all()
        l_notices_ids = [notice.id for notice in list_notices]
        return l_notices_ids
    

    @staticmethod
    def get_friend_notice(id: int):
        friend_notice = models.FriendNotice.query.filter_by(id=id).first()
        if friend_notice is not None:
            return friend_notice
        return None
        
    @staticmethod
    def get_list_notice(id: int):
        list_notice = models.ListNotice.query.filter_by(id=id).first()
        if list_notice is not None:
            return list_notice
        return None


    




    