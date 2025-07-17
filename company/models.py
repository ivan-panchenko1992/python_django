from django.db import models

class Item(models.Model):
    firstName = models.CharField(max_length=30)
    secondName = models.CharField(max_length=45)
    position = models.CharField(max_length=15, choices=[('tl', 'Tl'), ('sd1', 'Sd1'), ('sd2', 'Sd2'), ('sd3', 'Sd3'), ('sd4', 'Sd4')], default='sd1')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName + self.secondName
