import serial, os, thread
from time import sleep
from win32gui import *
from win32api import *
from win32con import *
from config_ir_values import *  # Do open this to understand how everything is working

ser= serial.Serial("COM10", 9600)

def read_serial():
    while 1:
        data =0
        #get the data
        data = int(ser.readline())

        if(data in Mute):
            keybd_event(VK_VOLUME_MUTE, 0,0,0)
        elif(data in Vol_up):
            keybd_event(VK_VOLUME_UP,0,0,0)
        elif(data in Vol_down):
            keybd_event(VK_VOLUME_DOWN,0,0,0)
        elif(data  in Back):
            keybd_event(VK_BROWSER_BACK, 0,0,0) #Back
        elif(data  in Play):
            keybd_event(VK_MEDIA_PLAY_PAUSE, 0,0,0) #Play/Pause
        elif(data  in My_media):
            os.system('start D:\DC++Share\Songs') #My Media
        elif(data  in Up):
            keybd_event(VK_UP, 0,0,0) #Up
        elif(data  in Right):
            keybd_event(VK_RIGHT, 0,0,0) #Right
        elif(data  in Down):
            keybd_event(VK_DOWN, 0,0,0) #Down
        elif(data  in Left):
            keybd_event(VK_LEFT, 0,0,0) #Left
        elif(data  in OK):
            keybd_event(VK_RETURN, 0,0,0) #OK
        elif(data in Close):
            keybd_event(0x12,0,0,0) # Code for Alt
            keybd_event(VK_F4, 0,0,0)
            keybd_event(0x12,0 ,KEYEVENTF_KEYUP ,0)
        elif data in Forward:
            keybd_event(0x12,0,0,0) # Code for Alt
            keybd_event(VK_RIGHT, 0,0,0)
            keybd_event(0x12,0 ,KEYEVENTF_KEYUP ,0)
        elif data in Backward:
            keybd_event(0x12,0,0,0) # Code for Alt
            keybd_event(VK_LEFT, 0,0,0)
            keybd_event(0x12,0 ,KEYEVENTF_KEYUP ,0)
        else:
            pass

read_serial()
ser.close()
