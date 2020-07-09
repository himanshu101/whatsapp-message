from rest_framework import serializers

from .models import User, Message, GroupMessage, Group, GroupMembers


class MessageSerializer(serializers.ModelSerializer):

    sender = serializers.SerializerMethodField()
    receiver = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ('sender', 'receiver', 'message', 'created_at',)

    @staticmethod
    def get_sender(obj):
        return UserSerializer(obj.sender).data

    @staticmethod
    def get_receiver(obj):
        return UserSerializer(obj.receiver).data


class GroupMessageSerializer(serializers.ModelSerializer):

    sender = serializers.SerializerMethodField()

    class Meta:
        model = GroupMessage
        fields = ('sender', 'message', 'group_id', 'created_at')

    @staticmethod
    def get_sender(obj):
        return UserSerializer(obj.sender).data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'name')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class GroupMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupMembers
        fields = '__all__'
