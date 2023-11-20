from django.db import models

# Create your models here.


class Data(models.Model):
    date = models.CharField(max_length=50)
    uf = models.CharField(max_length=10)
    utm = models.CharField(max_length=10)
    dolar_obs = models.CharField(max_length=10)
    euro = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.date} - {self.uf} - {self.utm} - {self.dolar_obs} - {self.euro}'

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Data'




