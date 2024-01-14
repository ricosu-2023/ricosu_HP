from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import (ListView 
                                  ,DetailView 
                                  ,FormView
                                 )
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import NippoModel
from .forms  import NippoFormClass, NippoModelForm
from django.urls import reverse, reverse_lazy,path
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .filters import  NippoModelFilter
from accounts.models import Profile



def ricosu(request): #クラス作成
    return render(request,"nippo/ricosu.html")    
    
