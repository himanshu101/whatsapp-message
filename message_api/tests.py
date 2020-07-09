from django.test import TestCase

from django.urls import reverse


from rest_framework.test import APIClient, APITransactionTestCase
from rest_framework import status

from .models import Group, GroupMembers, GroupMessage, User
from .serializers import GroupSerializer

# Create your tests here.

client = APIClient()
client.credentials()


class SendGroupMessage(TestCase):

    def setUp(self):

        self.group_data = {
            'name': 'Group 1',
            'description': 'Group Description'
        }

        user = User.objects.create(username='abc', name='ABC', phone='8292337777', email='abc@xyz.com',
                                   password='qweeee')

        self.group_member_data = {
            'member_id': user.id
        }

        self.group_message_data = {
            'sender_id': user.id,
            'message': 'Hello'
        }

    def test_send_group_message(self):
        response = client.post(reverse('groups_list'), self.group_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        group = Group.objects.filter(id=response.data['id']).first()
        self.assertEqual(response.data, GroupSerializer(group).data)

        response = client.post(reverse('add_group_member', kwargs={'group_id': group.id}),
                               self.group_member_data,
                               format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        group_member_count = GroupMembers.objects.filter(group_id=group.id).count()
        self.assertEqual(group_member_count, 1)

        response = client.post(reverse('group_messages_list', kwargs={'group_id': group.id}), self.group_message_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = client.get(reverse('group_messages_list', kwargs={'group_id': group.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 1)
