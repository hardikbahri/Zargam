from django.shortcuts import render

from .models import  Artist
dests=Artist.objects.all()
def artist(request):
    return render(request,'index.html',{'dests':dests})



# Create your views here.
