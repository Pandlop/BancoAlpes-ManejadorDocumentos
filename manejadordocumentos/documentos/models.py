from django.db import models

# Create your models here.
class DocumentoCarga(models.Model):
    score = models.FloatField(null=True)
    archivo = models.FileField(null=False,default=None)
    estado = models.IntegerField(null=False, default=1)
    tipo = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '{}'.format(self.archivo)