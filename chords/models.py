from django.db import models

class Song(models.Model):
    song_name=models.CharField(max_length=50)
    song_chords=models.TextField()
    full_name = models.CharField(max_length=15)
    
    
    
    def __str__(self):
        return self.song_name



# Create your models here.
