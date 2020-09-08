from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('admin', views.admin, name='admin'),
    path('basket', views.basket, name='basket')
]
