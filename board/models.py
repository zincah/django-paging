from django.db import models
from django.db.models.fields import DateTimeField, TimeField

# Create your models here.

class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=50)
    contents = models.TextField()
    impo = models.BooleanField(default=False)
    bdate = DateTimeField()
    
    def __str__(self):
        return self.subject
    
    def summary(self):
        if len(self.contents) > 30:
            return self.contents[:30] + "..."
        return self.contents