from dataclasses import fields
from rest_framework import serializers
from .models import Message

from django.contrib.auth.models import User


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.CharField()
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'subject', 'body', 'timestamp', 'read']
    
    # create new message
    def create(self, data):
        # get the sender & receiver input 
        sender = User.objects.get(username=data.pop('sender'))
        # get the sender & receiver from db
        try:
            receiver = User.objects.get(username=data.pop('receiver'))
        except User.DoesNotExist:
            raise serializers.ValidationError("receiver doesn't exist")
        # create new message
        message = Message.objects.create(sender=sender, receiver=receiver, **data)
        return message