import random
from moviepy.editor import *
from moviepy.video.fx.all import crop
import pickle
filename = 'Info\\mypickle.pk'

with open(filename, 'rb') as fi:
    cuurent_video = pickle.load(fi)

import os
audiolist=[]
def Breakingclip(cuurent_video):
    path = "C:\\Users\\avina\\Desktop\\Output"
    for x in os.listdir(path):
        if x.endswith('.mp4'):
            clip_path=path+'\\'+x
            print(clip_path)
            
            with open(filename, 'wb') as fi:
                pickle.dump(cuurent_video, fi)
            clip_duration=VideoFileClip(path+'\\'+x).duration
            for i in range(0,int(clip_duration/58)):
                cuurent_video = cuurent_video+1
                print("Total Number of Video : %i "%(clip_duration/58)+"Current Video : %i"%(i)+" short# :   "+ str(cuurent_video))
                Clip=VideoFileClip(clip_path).subclip(i*58,58*(i+1))
                Clip.write_videofile("Video\\Short  #"+str(cuurent_video)+".mp4")
            
def extractingaudio():
         
         path="E:\\python\\Movieeditor\\Audio"
         for x in os.listdir(path):
                a_clip_path=path+"\\"+x
                music_audio=AudioFileClip(a_clip_path).subclip(0,58)
                music_audio.write_audiofile(a_clip_path)
                audiolist.append(a_clip_path)
         print(audiolist)      
                
def addingaudio():
        
            path="E:\\python\\Movieeditor\\Video"
            for x in os.listdir(path):
                music_audio=AudioFileClip(random.choice(audiolist))
                video = VideoFileClip(path+"\\"+x)
                clip_v2 = video.set_audio(music_audio)
                final_clip =CompositeVideoClip([video,clip_v2])     
                final_clip.write_videofile("OutputFile//"+x)


def cropping():
    path="E:\\python\\Movieeditor\\Video"
    for x in os.listdir(path):
        video = VideoFileClip(path+"\\"+x)
        (w,h) = video.size
        video2=crop(video,width=1080,height=1920,x_center=w,y_center=h)
        video2.write_videofile("Cropped\\"+x)
        



Breakingclip(cuurent_video)
#extractingaudio()
#addingaudio()
#cropping()