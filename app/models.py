from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        if self.completed == True:
            comp = 'is Completed'
        else:
            comp = 'is not Completed'
        return self.item + ' ' + comp


