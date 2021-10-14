from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.hola_mundo, name="home"),
    path('index/', views.llamar_index, name="index"),
    path('cargar/', views.prueba_get, name="cargar"),
    path('post/', views.cargar, name="post"),
    path('accounts/', include('django.contrib.auth.urls'), name="login"),
    path('gui/', views.gui, name="gui")]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
