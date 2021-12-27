from django.db import models
import os
from twilio.rest import Client

# Create your models here.


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def save(self , *args, **kwargs):
        if self.score >= 70:
            message = client.messages.create(
            body=f"Congratulations {self.name} , your score is {self.score}",
            from_='',#my number by twilio site
            to=''#number to which you want to send
            )
        else:
            message = client.messages.create(
            body=f"Sorry, {self.name} , your score is {self.score}.Try again",
            from_='',#my number by twilio site
            to=''#number to which you want to sendn
            )
        return super().save(*args, **kwargs)
    