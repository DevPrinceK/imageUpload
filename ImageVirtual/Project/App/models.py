from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.


class Image(models.Model):
    name = CharField(max_length=50, default='img')
    image = ImageField(upload_to='imageUpload')

    def __str__(self) -> str:
        return str(self.id) + ' ' + self.name
