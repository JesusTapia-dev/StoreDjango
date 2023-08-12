from django.urls import path
from . import views

app_name='category'#esto es necesario para el ciclo for del template
urlpatterns=[
    path('<int:pk>/', views.categoriasDetail, name='categoriasDetail'),
]