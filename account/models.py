from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            null=False, blank=False)

    def __str__(self):
        return self.name


class User(AbstractUser):
    ACCOUNT_TYPE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('STAFF', 'Staff'),
        ('EMPLOYEE', 'Employee'),
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    designation = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, null=False,
                              blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(
        max_length=10, choices=ACCOUNT_TYPE_CHOICES, default='EMPLOYEE')
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def get_full_name(self):
        return F"{self.pk}-{self.email}"
