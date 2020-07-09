from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, unique=True, null=False)
    phone = models.CharField(max_length=10, unique=True, null=False)
    email = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)


class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)


class GroupMembers(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='member')


class GroupMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_sender')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_receiver')
    message = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
