from django.db import models

# Create your models here.

class users(models.Model):
    user_key = models.CharField(max_length=30, primary_key=True)
    user_email = models.EmailField(unique=True,max_length=200)
    # user_name = models.CharField(default=None,max_length=100)
    # user_phone_number = models.CharField(default=None,max_length=10)
    # user_employee_id = models.CharField(default=None,max_length=20)

    # token = models.CharField(unique=True,blank=True,max_length=2000)
    def __str__(self):
        return self.user_email
