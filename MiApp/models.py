from django.db import models
from django.forms import ModelForm

def subir_imagen(instance, filename):
	return 'imagenes/%s'% filename

def subir_sonido(instance, filename):
	return 'sonidos/%s'% filename 

class imagen(models.Model):
	titulo = models.CharField(max_length=35)
	Imagen = models.FileField(upload_to=subir_imagen, blank=True, null=True)
	sonido = models.FileField(upload_to=subir_sonido, blank=True, null=True)

	def __unicode__ (self):
		return str(titulo)


