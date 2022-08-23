from django.db import models

class Message(models.Model):
    sender = models.ForeignKey("auth.User", on_delete=models.PROTECT, related_name="messages_sent")
    receiver = models.ForeignKey("auth.User", on_delete=models.CASCADE,related_name="messages_received")
    subject = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.sender.username + ' sent to ' + self.receiver.username
