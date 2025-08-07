from django.db import models

class Item(models.Model):
    firstName = models.CharField(max_length=30)
    secondName = models.CharField(max_length=45)
    position = models.CharField(max_length=15, choices=[('tl', 'Tl'), ('sd1', 'Sd1'), ('sd2', 'Sd2'), ('sd3', 'Sd3'), ('sd4', 'Sd4')], default='sd1')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName + ' ' + self.secondName
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2560)
    estimate = models.IntegerField()
    dueDate = models.DateTimeField()
    createdBy = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='created_tasks')
    assigned = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
