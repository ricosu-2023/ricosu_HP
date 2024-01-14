from django.urls import path,include
from .views import ricosu

urlpatterns = [
  
  path("ricosu/"   ,ricosu, name="ricosu"),
  
]