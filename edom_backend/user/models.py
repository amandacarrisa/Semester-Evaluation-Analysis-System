from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

User = get_user_model


class Pengguna(AbstractUser):
    """
    This class overrides Django's default user naming system to better suit the EDOM-NG specifications.
    """

    first_name = None
    last_name = None
    full_name = models.CharField(max_length=255)

    def get_full_name(self) -> str:
        return self.full_name

    def get_short_name(self) -> str:
        return self.username

    def __str__(self) -> str:
        return f"{self.username} - {self.full_name}"

class EdomAdmin(models.Model):
    user = models.OneToOneField(Pengguna,on_delete=models.CASCADE,primary_key=True)
    id_admin = models.CharField(max_length=20)

    def get_full_name(self) -> str:
        return self.user.get_full_name()
    
    def get_short_name(self) -> str:
        return self.user.get_short_name()
    
    def get_id_admin(self) -> str:
        return self.id_admin
    
    def __str__(self) -> str:
        return f"{self.get_id_admin()} - {self.get_full_name()}"

class Mahasiswa(models.Model):
    user = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    npm = models.CharField(max_length=10)

    def get_full_name(self) -> str:
        return self.user.get_full_name()

    def get_short_name(self) -> str:
        return self.user.get_short_name()

    def get_npm(self) -> str:
        return self.npm

    def __str__(self) -> str:
        return f"{self.npm} - {self.get_full_name()}"


class Professor(models.Model):
    """
    This class overrides Django's default user naming system to better suit the EDOM-NG specifications.
    """

    user = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    npm = models.CharField(max_length=10)

    def get_full_name(self) -> str:
        return self.user.get_full_name()

    def get_short_name(self) -> str:
        return self.user.get_short_name()

    def get_npm(self) -> str:
        return self.npm

    def __str__(self) -> str:
        return f"{self.npm} - {self.get_full_name()}"
