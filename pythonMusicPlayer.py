#BouCo- Bouchan Ramirez Abraham
#Reproductor de música básico con python.

import os
#Va a preguntar en que folder se encuentra la musica que queremos reproducir, por lo tanto 
#usamos os, ya que nos permit navegar con el control de usuario y sus datos en la pc.
from tkinter.filedialog import askdirectory
 #Preguntar directorio
import pygame
from mutagen.id3 import ID3
#De mutagen hará extraibles los metadatos del tipo mp3 mp3 
from tkinter import *
 
root = Tk()
root.minsize(450,450)
#Los dos comandos pasados nos permiten abrir una ventaa de tk cuando se interpreta

 
listofsongs = []
realnames = []
 
v = StringVar()
songlabel = Label(root,textvariable=v,width=50)
 
index = 0
 
def directorychooser():
 
    directory = askdirectory()
    os.chdir(directory)
 
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
           # realnames.append(audio['TIT2'].text[0])
            print(files)
 
            listofsongs.append(files)

 
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()




directorychooser()
 
def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    #return songname
 
 
 
def nextsong(event):
    global index
    if (index + 1) == None:
        index -= 5
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    else:    
        index += 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        updatelabel()
 
def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
 
 
def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    #return songname

def playsong(event):
#pygame.mixer.music.play()
    pygame.mixer.music.unpause()
    

def pausesong(event):
    pygame.mixer.music.pause()

def rewindSong(event):
    pygame.mixer.music.rewind()


#def repeatPlaylist():
 #   if index+1 == null:
       # index -= 5
    #return index

   
    
 
label = Label(root,text='Reproductor MP3')
label.pack()
 

listbox = Listbox(root)
listbox.pack()

realnames.reverse()
for items in listofsongs:
    listbox.insert(0,items)
    
for items in realnames:
    listbox.insert(0,items)
 
realnames.reverse()

 
playbutton = Button(root, text = 'Play')
root.anchor = W
pygame.mixer.music.play()
playbutton.pack()

pausebutton = Button(root, text = 'Pause')
pygame.mixer.music.pause()
pausebutton.pack()
 
nextbutton = Button(root,text = 'Next Song')
nextbutton.pack()
 
previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()
 
stopbutton = Button(root,text='Stop Music')
stopbutton.pack()
 
rewindButton = Button(root,text='Rewind song')
rewindButton.pack()
 
nextbutton.bind("<Button-1>",nextsong)
pausebutton.bind("<Button-1>",pausesong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
playbutton.bind("<Button-1>",playsong) 
rewindButton.bind("<Button-1>", rewindSong)

songlabel.pack()
root.mainloop()
#repeatPlaylist()





