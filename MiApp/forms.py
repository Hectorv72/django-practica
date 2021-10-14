from django.forms import ModelForm
from .models import imagen

class FormCargar(ModelForm):
	class Meta:
		model = imagen
		fields = ('titulo','Imagen', 'sonido')