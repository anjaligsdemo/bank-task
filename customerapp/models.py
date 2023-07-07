from django.contrib.auth.models import AbstractUser
from django.db import models


class District(models.Model):
    name = models.CharField(max_length=100)
    wikipedia_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    ACCOUNT_TYPE_CHOICES = (
        ('CA', 'Checking'),
        ('SA', 'Saving'),
        ('CD', 'Certificate of Deposit'),
        ('MMA', 'Money Market Account'),
    )

    first_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    bank_account_type = models.CharField(max_length=3, choices=ACCOUNT_TYPE_CHOICES, null=True, blank=True)

    class Meta:
        default_related_name = 'custom_users'


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserMaterials(models.Model):
    user_profile = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_profile.username} - {self.material.name}"

