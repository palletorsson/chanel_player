#!/usr/bin/python

import pygame
import time
import subprocess
import thread
import os
import sys
from moviepy.editor import *
from os import listdir
from os.path import isfile, join
import random
from datetime import datetime


videoPath = "/home/pi/Documents/video/videoplayer/video/"
num = 0 
 
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

def playVideo(videofile, dur, display):
    x = 1
    logging("Starting video: "  + videofile + "\n")
    disp_string = '--display='+str(display)
    print(disp_string)
    
    playProcess=subprocess.Popen(['omxplayer', disp_string,'-b', videofile],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)

    time.sleep(dur)
    
    if display == 2: 
        thread.start_new_thread(newset_2,( ))
    else:
        thread.start_new_thread(newset_7, ( ))
    
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


def get_duration(file):
    """Get the duration of a video using ffprobe."""
    cmd = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(file)
    output = subprocess.check_output(
        cmd,
        shell=True, # Let this run in the shell
        stderr=subprocess.STDOUT
    )
    # return round(float(output))  # ugly, but rounds your seconds up or down
    return float(output)


files = createFileList("./video")
f.write("Files: " +  str(files) + "\n")

startFromBlack()

def newset_7():
    rand_7 = random.randint(1, len(files)-1)
    next_video_7 = videoPath + files[rand_7]
    dur_7 = get_duration(next_video_7)
    playVideo(next_video_7, dur_7, 7)


def newset_2():
    rand_2 = random.randint(1, len(files)-1)
    next_video_2 = videoPath + files[rand_2]
    dur_2 = get_duration(next_video_2)
    playVideo(next_video_2, dur_2, 2)
   
    
thread.start_new_thread(newset_7, ( ))
thread.start_new_thread(newset_2, ( ))

time.sleep(30000)    
exitProgram()
