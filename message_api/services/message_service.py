from django.db import DatabaseError

from ..models import Message, GroupMessage, GroupMembers
from ..utils import log
from ..dto.error import Error


class MessageService:

    @classmethod
    def save_group_message(cls, group_id,  data):
        if not GroupMembers.objects.filter(group_id=group_id, user_id=data.get('sender_id')).exists():
            return None, Error('Sender is not part of the group')
        try:
            message = GroupMessage()
            message.sender_id = data.get('sender_id')
            message.message = data.get('message')
            message.group_id = group_id
            message.save()

            return message, None
        except DatabaseError as ex:
            log('Saving Group message', format(ex), 'error')

            return None, Error(format(ex))

    @classmethod
    def save_p2p_message(cls, receiver_id,  data):
        try:
            message = Message()
            message.sender_id = data.get('sender_id')
            message.receiver_id = receiver_id
            message.message = data.get('message')
            message.save()

            return message, None
        except DatabaseError as ex:
            log('Saving P2P message', format(ex), 'error')

            return None, Error(format(ex))