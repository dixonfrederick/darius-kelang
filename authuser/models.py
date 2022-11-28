from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=30)
    role_choice = (
        ("Premium", "Premium User"),
        ("Normal", "Normal User"),
    )
    role = models.CharField(
        max_length=20, choices=role_choice, default="Normal")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Transaksi(models.Model):
    jenisTransaksi = models.CharField(max_length=30, null=True)
    nominal = models.BigIntegerField(null=True)
    tanggalTransaksi = models.DateField(auto_now=True)
    users = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.jenisTransaksi
