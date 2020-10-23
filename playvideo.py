#!/usr/bin/python

import pygame
import time
import subprocess
import threading
import os
import sys
from moviepy.editor import *
from os import listdir
from os.path import isfile, join
import random
from datetime import datetime



def createFileList(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

def startFromBlack():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    logging("Current Time is: "+ current_time + "\n")
    pygame.font.init()
    logging("turn on black screen" + "\n")
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.NOFRAME)
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    bgimage = "black.jpg"
    screen.fill(0)
   
   

def playVideo(videofile, dur):
    x = 1
    logging("Starting video: "  + videofile + "\n")
    
    playProcess=subprocess.Popen(['omxplayer','-b',videofile],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
    #logging("playProcess.pid: "  + playProcess.pid + "\n")
    
    time.sleep(dur)
    
    #os.system("killall omxplayer.bin")


def exitProgram():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    logging("Current Time is: "+ current_time + "\n")
    logging("exit program" + "\n")
    f.close()
    os.system("killall omxplayer.bin")
    sys.exit(0)

f = open("logger.txt", "w")

def logging(logtext):
    f.write(logtext)

def getVideoLength(video):
    clip = VideoFileClip(video)
    video_duration = int(clip.duration)
    f.write("Clip is " +  str(video_duration) + " seconds." + "\n")
    return video_duration

#video=threading.Thread(target=playVideo, args=["/home/pi/Documents/video/bh.mp4", 1])
#video.start()

files = createFileList("./video")
f.write("Files: " +  str(files) + "\n")
#background=threading.Thread(target=startFromBlack)
#background.start()

startFromBlack()

for i in range(3000):
    rand = random.randint(1, len(files)-1)
    try:
        dur = getVideoLength("/home/pi/Documents/videoplayer/video/"+ files[rand])
        playVideo("/home/pi/Documents/videoplayer/video/"+ files[rand], dur)
    except:
        f.write("Error on playback, random :" +  str(rand) + " ... " + "\n")
    
exitProgram()

