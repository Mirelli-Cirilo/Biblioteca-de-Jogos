from django.db import models

# Create your models here.

class Game(models.Model):
    titulo = models.CharField(max_length=200)
    completo = models.BooleanField(default=False)
    resenha = models.TextField(null=True, blank=True)
  


    def __str__(self):
        return self.titulo