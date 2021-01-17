import pytube
from moviepy.editor import *
from tkinter import *

path = "C:/Users/pavan/Desktop/Downloads/Video/"

def download_video():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.get_highest_resolution()
        video.download(path)
        notif.config(fg="green",text="Video Download complete")
    except Exception as e:
        print(e)
        notif.config(fg="red",text="Video could not be downloaded")

def convert():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        mp4_file = path + youtube.title + ".mp4"
        mp3_file = path + youtube.title + ".mp3"
        VideoClip = VideoFileClip(mp4_file)
        AudioClip = VideoClip.audio
        AudioClip.write_audiofile(mp3_file)
        AudioClip.close()
        VideoClip.close()
        notif.config(fg="green",text="Audio conversion complete")
    except Exception as e:
        print(e)
        notif.config(fg="red",text="Audio could not be converted, try downloading video first")

        
        
#GUI
main_screen = Tk()
main_screen.title("YouTube Converter")

#Labels
Label(main_screen, text="YouTube Converter", fg="red", font=("Helvetica", 20)).grid(sticky=N,padx=100, row=0)
Label(main_screen, text="Enter YouTube URL: ", font=("Helvetica", 12)).grid(sticky=N,pady=15, row=1)
notif = Label(main_screen,font=("Calibri",12))
notif.grid(sticky=N,pady=1,row=6)

#Variables
url = StringVar()
#Entry bar
Entry(main_screen,width=50,textvariable=url).grid(sticky=N,row=2)
#Button
Button(main_screen,width=20,text="Download Video",font=("Helvetica", 12),command=download_video).grid(sticky=N,row=4,pady=10)
Button(main_screen,width=20,text="Convert to audio",font=("Helvetica", 12),command=convert).grid(sticky=N,row=5,pady=10)
main_screen.mainloop()