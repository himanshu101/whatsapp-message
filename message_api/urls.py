from django.conf.urls import url

from .views import GroupMessageList, MessageList, GroupList, AddMember

urlpatterns = [

    url('^groups/(?P<group_id>[\d]+)/add?', AddMember.as_view(), name='add_group_member'),

    url('^groups', GroupList.as_view(), name='groups_list'),

    url('^messages/groups/(?P<group_id>[\d]+)?', GroupMessageList.as_view(), name='group_messages_list'),

    url('^messages/(?P<receiver_id>[\d]+)?', MessageList.as_view(), name='p2p_messages_list')
]
