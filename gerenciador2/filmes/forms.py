from django import forms

from .models import filme

class filmeForm(forms.ModelForm):
	class Meta:
		model = filme
		fields = ('nome','diretor','elenco','genero','nacionalidade','datalancamento','sinopse','distribuidor')