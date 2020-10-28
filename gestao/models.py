from django.db import models


class Categoria(models.Model):
    nome = models.CharField(null=False, unique=False, max_length=100)
    categoria = models.ForeignKey('self', on_delete=models.CASCADE,
                                  null=True, blank=True,
                                   related_name='categorias')

    def __str__(self):
        return self.nome
