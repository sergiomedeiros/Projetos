from django.shortcuts import render

from .forms import filmeForm

# Create your views here.

def filme(request):
	if request.method == 'POST':
		form = filmeForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'sucesso.html')
		else:
			print(form.errors)
	else:
		form = filmeForm()
	return render(request, 'filme.html', {'form': form})
