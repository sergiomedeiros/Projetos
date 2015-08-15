from django.shortcuts import render, redirect  
from django.core.urlresolvers import reverse    # import para pode usar o name da url.
from .forms import ContatoForm
from .models import Contato
# Create your views here.

def add_contato(request):
	# formularios HTML tem dois tipos de submissao POST ou GET
	# POST : submissao mais segura
	# GET  : menos segura
	# verificando se a requisiçao e POST
	if request.method == 'POST':
		form_contato = ContatoForm(request.POST)
		if form_contato.is_valid():  # verifica se as informaçoes sao texto puro, seguranca
			form_contato.save()
			#return render(request,'sucesso.html')
			return redirect(reverse('sucesso'))
		else:
			print(form_contato.errors)
	else:
		form_contato = ContatoForm()

	return render(request,'add_contato.html',{'form_contato': form_contato})


def cadastro_sucesso(request):
	return render(request,'sucesso.html')

def lista_contatos(request):
	# select * from arquivo, [:3] para listar uma determina quantidade de registros
	contatos = Contato.objects.all()  
	return render(request,'lista_contatos.html',{'contatos' : contatos})
	