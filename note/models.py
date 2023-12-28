from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    subject = models.CharField(max_length = 255)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name = 'notes')

    class Meta:
        verbose_name_plural = "Notes"

# - In the Notes model, a ForeignKey field named 'user' is added, which establishes a relationship with the Users model.
# - The 'on_delete=models.CASCADE' option means that when a user is deleted, all associated notes will be deleted.
# - The 'related_name' attribute is set to 'notes' so that you can access a user's notes using 'user.notes.all()'.
