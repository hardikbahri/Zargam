from django.shortcuts import render
from django.template import context

from .models import  *
chords=Song.objects.all()



def songlist(request, artist,abc=None):
    
    songlist=Song.objects.filter(full_name=artist)
    
    context={
        "songlist":songlist,
        "chords":chords,
        
        
        
    }
    if(abc==None):
        return render(request,'songlist.html',context)
    else:
        song=Song.objects.get(song_name=abc)
        context={
        "song":song,
        
        
        
    }
        return render(request,'song.html',context)
def search_song(request):
    searched=request.POST['searched']#__icontains is used for if the model contains even a part of the searched 
    
    results=Song.objects.filter(song_name__icontains=searched) or Song.objects.filter(full_name__icontains=searched) 
    context={
        "searched":searched,
        "results":results,
    }
    return render(request,'search.html',context)
# def song(request,abc,artist):
#     song=Song.objects.get(song_name=abc)
#     context={
#         "song":song,
        
#     }
    
#     return render(request,'song.html',context)

# # # Create your views here.
