from django.db import models

# Create your models here.

class Filmes(models.Model):
	nome = models.CharField(max_length=50)
	diretor = models.CharField(max_length=100)
	elenco = models.CharField(max_length=100)
	genero = models.CharField(max_length=100)
	nacionalidade = models.CharField(max_length=30)
	datalancamento = models.DateField()
	sinopse = models.CharField(max_length=200)
	distribuidor = models.CharField(max_length=30)
	
	def __str__(self):
		return self.nome
