from django.db import models


class Iban(models.Model):
    value = models.CharField(max_length=22)
    is_valid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return f"{self.value} {self.is_valid=}"
