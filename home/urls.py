from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('put', views.get_email, name="get_email")
]