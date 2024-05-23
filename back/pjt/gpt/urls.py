from django.contrib import admin 
from django.urls import path 
from . import views 

app_name = 'gpt'

urlpatterns = [ 
	path('', views.query_view, name='query_view'), 
] 