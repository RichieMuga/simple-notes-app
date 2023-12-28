from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(
        max_length=255,
        validators=[
            MinLengthValidator(
                limit_value=8, message="Password must be at least 8 characters."
            ),
            RegexValidator(
                regex=r"^(?=.*[a-zA-Z])(?=.*\d).+$",
                message="Password must contain at least one letter and one number.",
            ),
        ],
    )

    createdAt = models.DateTimeField(
        verbose_name="The time the user field was created", auto_now_add=True
    )
    updatedAt = models.DateTimeField(verbose_name="The time the user field was updated")
