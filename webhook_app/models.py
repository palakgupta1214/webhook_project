from django.db import models

# Create your models here.

class Webhook(models.Model):
    webhook_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    data = models.TextField(default='')

    def __str__(self):
        return self.webhook_id


    
