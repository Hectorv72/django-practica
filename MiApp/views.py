# -*- conding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from .forms import FormCargar
import random
from django.contrib.auth.decorators import login_required

def hola_mundo(request):
	html = []
	for letra in 'Python':
		html.append("<p>%s</p>"%letra)

	return HttpResponse(html)

def llamar_index(request):
	return render(request, 'MiApp/casa.html')

def prueba_get(request):
	entrada = request.GET.get('q', '')
	return render(request, 'MiApp/get.html', {'dato':entrada})


def cargar(request):
	if request.method == "POST":
		form = FormCargar(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
	else:
		form = FormCargar()
	return render(request, "MiApp/post.html",{'formulario':form})


def gui(request):
	imagen_selec = []
	for obj in range(4):
		imagen_selec.append(random.choice(imagen.objects.all()))

	#modelo = imagen.objects.all()
	return render(request, 'MiApp/gui.html', {'base': imagen_selec})
