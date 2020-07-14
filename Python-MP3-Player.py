import os
from tkinter.filedialog import askdirectory 
import pygame
from mutagen.id3 import ID3
from tkinter import *

listofsongs = []
realnames = []

root = Tk()
root.minsize(300,300)
v = StringVar()
songlabel = Label(root, textvariable = v, width = 35)
index = 0

def directorychooser():
	directory = askdirectory()
	os.chdir(directory)
	for file in os.listdir(directory):
		if file.endswith(".mp3"):
			audio = ID3(file)
			realnames.append(audio['TIT2'])
			listofsongs.append(file)

	for i in range(len(realnames)):
		listbox.insert(END,realnames[i])

	pygame.mixer.init()
	pygame.mixer.music.load(listofsongs[0])
	updatelabel()
	pygame.mixer.music.play()

def updatelabel():
	global index
	global songname
	v.set(realnames[index])

def nextsong():
    global index 
    index += 1 
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong():
   global index
   index -= 1
   pygame.mixer.music.load(listofsongs[index])
   pygame.mixer.music.play()
   updatelabel()

def stopsong():
	if stopbutton['text']== 'Stop Music':
		pygame.mixer.music.pause()
		v.set("")
		stopbutton['text'] = 'Play Music'
	else:
		pygame.mixer.music.unpause()
		updatelabel()
		stopbutton['text'] = 'Stop Music'


label = Label(root,text='Music Player') 
label.pack()
listbox = Listbox(root)
listbox.pack()

addbutton = Button(root, text = "Add Song", command = directorychooser)
addbutton.pack()
nextbutton = Button(root,text = 'Next Song', command = nextsong)
nextbutton.pack()
previousbutton = Button(root,text = 'Previous Song', command = prevsong)
previousbutton.pack()
stopbutton = Button(root,text='Stop Music', command = stopsong)
stopbutton.pack()

songlabel.pack()
root.mainloop()