from django.db import models

# Create your models here.


class Data(models.Model):
    day = models.CharField(max_length=2)
    value = models.CharField(max_length=10)
    month = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.day} - {self.value} - {self.month}'

    data = models.Manager()

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Datas'



