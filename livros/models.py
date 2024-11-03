from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Create your models here.
class Livro(models.Model):
    stream_choices = (('AK', 'Amazon Kindle'), ('F', 'Físico'), ('AU', 'Audiobook'))
    nome = models.CharField(max_length=100)
    streaming = models.CharField(max_length=2, choices=stream_choices)
    nota = models.IntegerField(null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)
    categorias = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.nome