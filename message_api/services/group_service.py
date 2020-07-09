from django.db import DatabaseError

from ..models import Group, GroupMembers
from ..utils import log
from ..dto.error import Error


class GroupService:

    @classmethod
    def create_group(cls, data):
        try:
            group = Group()
            group.description = data.get('description')
            group.name = data.get('name')
            group.save()

            return group, None
        except DatabaseError as ex:
            log('Creating Group', format(ex), 'error')

            return None, Error(format(ex))

    @classmethod
    def add_member_in_group(cls, group_id, data):
        try:
            group_member = GroupMembers()
            group_member.group_id = group_id
            group_member.user_id = data.get('member_id')
            group_member.save()

            return group_member, None
        except DatabaseError as ex:
            log('Adding Group in Member', format(ex), 'error')

            return None, Error(format(ex))
