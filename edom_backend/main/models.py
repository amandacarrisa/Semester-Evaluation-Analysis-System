from django.db import models


class Developer(models.Model):
    """
    Models for developers
    """

    nama = models.CharField(max_length=255)
    npm = models.CharField(max_length=10)

    def angkatan(self):
        return f"20{self.npm[:2]}"

    def __str__(self) -> str:
        return f"{self.nama} - {self.npm}"
