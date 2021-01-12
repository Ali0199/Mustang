from django.urls import path
from . import views


urlpatterns=[
   path('login', views.login, name="login"),
   path('', views.Home, name="Home"),
   path('Karobka', views.Karobka, name="Karobka"),
   path('Kraska', views.Kraska, name="Kraska"),
   path('Idish', views.Idish, name="Idish"),
   path('Etiketika', views.Etiketika, name="Etiketika"),


]