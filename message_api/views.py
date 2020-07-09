
# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response

from .models import GroupMessage, Message, Group
from .serializers import MessageSerializer, GroupMessageSerializer, GroupSerializer, GroupMemberSerializer
from .pagination import CustomPagination
from .services.group_service import GroupService
from .services.message_service import MessageService


class GroupMessageList(generics.ListAPIView):

    serializer_class = GroupMessageSerializer
    pagination_class = CustomPagination
    ordering = ('-created_at',)

    def get_queryset(self):
        return GroupMessage.objects.filter(group_id=self.kwargs.get('group_id'))

    def post(self, request, *args, **kwargs):
        group_id = kwargs.get('group_id')
        message, error = MessageService.save_group_message(group_id, request.data)

        if error is not None:
            return Response({'detail': error.message}, status=error.status)

        return Response(self.serializer_class(message).data, status=status.HTTP_201_CREATED)


class MessageList(generics.ListCreateAPIView):

    serializer_class = MessageSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        receiver_id = self.kwargs.get('receiver_id')
        sender_id = self.request.query_params.get('sender_id')
        messages = (Message.objects.filter(sender_id=sender_id, receiver_id=receiver_id)
                    .select_related('sender', 'receiver')
                    )

        return messages

    def post(self, request, *args, **kwargs):
        receiver_id = kwargs.get('receiver_id')
        message, error = MessageService.save_p2p_message(receiver_id, request.data)
        if error is not None:
            return Response({'detail': error.message}, status=error.status)

        return Response(self.serializer_class(message).data, status=status.HTTP_201_CREATED)


class GroupList(generics.ListCreateAPIView):

    serializer_class = GroupSerializer
    pagination_class = CustomPagination
    ordering = ('-created_at',)

    def get_queryset(self):

        return Group.objects.all()

    def post(self, request, *args, **kwargs):
        group, error = GroupService.create_group(request.data)
        if error is not None:
            return Response({'detail': error.message}, status=error.status)

        return Response(self.serializer_class(group).data, status=status.HTTP_201_CREATED)


class AddMember(generics.CreateAPIView):
    serializer_class = GroupMemberSerializer

    def post(self, request, *args, **kwargs):
        group_id = kwargs.get('group_id')
        group_member, error = GroupService.add_member_in_group(group_id, request.data)
        if error is not None:
            return Response({'detail': error.message}, status=error.status)

        return Response(self.serializer_class(group_member).data, status=status.HTTP_200_OK)