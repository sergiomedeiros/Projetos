from django.shortcuts import render

from .forms import ContatoForm
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
			return render(request,'sucesso.html')
		else:
			print(form_contato.errors)
	else:
		form_contato = ContatoForm()

	return render(request,'add_contato.html',{'form_contato': form_contato})


