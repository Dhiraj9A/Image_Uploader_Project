from django.db import models

# Create your models here.
class img_uploder(models.Model):
    image=models.ImageField()
    title=models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
        