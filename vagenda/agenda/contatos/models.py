from django.db import models

# Create your models here.
class Contato(models.Model):
	nome     = models.CharField(max_length=100)
	email    = models.CharField(max_length=100)
	telefone = models.CharField(max_length=14)
	sexo     = models.CharField(max_length=1)
	cidade   = models.CharField(max_length=50,default="Teresina")

	#  metodo para retorna o nome do contato
	#  metodo reservado, (__metodo__ = Criar metodo resevado)
	def __str__(self):
		return self.nome
