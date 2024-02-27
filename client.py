import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath
import time
from ftplib import FTP
from tkinter import filedialog
from pathlib import Path
from playsound import playsound
import pygame
from pygame import mixer

PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096
name = None
listbox =  None
filePathLabel=None
global song_counter
song_counter = 0

def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text="Now Playing: " +song_selected)
    else:
       infoLabel.configure(text="")

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")

def browseFiles():
    global textarea
    global filePathLabel

    try:
        fileName=filedialog.askopenfilename()
        filePathLabel.configure(text=fileName)
        HOSTNAME="127.0.0.1"
        USERNAME="lftpd"
        PASSWORD="lftpd"
        ftp_server= FTP(HOSTNAME,USERNAME,PASSWORD)
        ftp_server.encoding="utf-8"
        ftp_server.cwd("shared_files")
        f_name=ntpath.basename(fileName)
        with open(fileName,"rb") as file:
            ftp_server.storbinary(f"STOR {f_name}",file)
        ftp_server.dir()
        ftp_server.quit()          
    except FileNotFoundError:
        print("cancle button press")

def openChatWindow():
    global song_counter
    global filePathLabel
    global listbox
    global infoLabel
   
    print("\n\t\t\t\tIP MESSENGER")
    window=Tk()
    window.title('Music 🎵🎵🎵')
    window.geometry("500x350")
    window.config(bg="cyan")
    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel
    namelabel = Label(window, text= "🎵 Play Music! 🎵", font = ("Calibri",30),bg="green")
    namelabel.place(x=10, y=8)
    listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font = ("Calibri",10),bg="red")
    listbox.place(x=10, y=70)
    playButton=Button(window,text="Play",font=("Calibri",10),bg="orange",command=play)
    playButton.place(x=400,y=180)
    stopButton=Button(window,text="Stop",font=("Calibri",10),bg="orange",command=stop)
    stopButton.place(x=20,y=180)
    upButton=Button(window,text="Upload",font=("Calibri",10),bg="orange")
    upButton.place(x=20,y=280)
    downButton=Button(window,text="Download",font=("Calibri",10),bg="orange", command=browseFiles)
    downButton.place(x=90,y=190)                  
    ResumeButton=Button(window, text="Resume",bg="orange",bd=1,font=("Calibri",10),command=resume)
    ResumeButton.place(x=200,y=250)
    infoLabel = Label(window, text= "",fg= "blue",bg='pink', font = ("Calibri",8))
    infoLabel.place(x=4, y=330)
    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    openChatWindow()


def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()


setup()