from django.db import models

class Greeting(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title