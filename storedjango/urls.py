"""
URL configuration for tienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from storedjango import settings
from tienda.views import index, contact, product

'''
path: el contact/ es la url en el navegador, mientras
que se usa el name='contacto' se refiere al modo en el que se
llamara a ella en el archivo html
'''
urlpatterns = [
                  path('', index, name='index'),
                  path('items/', include('item.urls')),
                  path('contact/', contact, name='contacto'),
                  path('product/', product, name='product'),
                  path('admin/', admin.site.urls),
                  path('categorias/',include('categoriasMain.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
