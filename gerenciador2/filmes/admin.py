from django.contrib import admin

# Register your models here.

from .models import filme

#class ContatoAdmin(admin.ModelAdmin):
#	pass

admin.site.register(filme)
