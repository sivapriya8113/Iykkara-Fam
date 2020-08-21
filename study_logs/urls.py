from django.urls import path
from . import views

app_name = 'study_logs'

urlpatterns = [
    path('',views.index,name='index'),
    path('base/', views.base, name='base'),
    path('history/', views.history, name='history'),
    path('gallery/', views.gallery, name='gallery'),
    path('familytree/', views.familytree, name='familytree'),
    path('news/', views.news, name='news')


]
