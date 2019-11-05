import os
from PIL import Image
import socket
import sys
import subprocess
import time

class Camera:

    def __init__(self, img_width=50, img_height=30, img_rot=0):
        self.value = None
        self.img_width = img_width
        self.img_height = img_height
        self.img_rot = img_rot
        
        """ 
        subprocess.Popen(["python3", "camera-daemon.py"])
        time.sleep(2) 

        HOST = '127.0.0.1'
        PORT = 9000
        self.s = socket.socket()
        self.s.connect((HOST, PORT))
        print("connected to camera daemon")
        self.s.send(b'ack')
        """ 

    def get_value(self):  
        return self.value

    def update(self):
        #self.sensor_get_value()
        #self.s.send(b'snap')
        #self.value = Image.open('image.png').convert('RGB')
        self.value = self.sensor_get_value()
        return self.value

    def reset(self):
        self.value = None

    def sensor_get_value(self):
        # This is a OS call that takes a image and makes it accessible to PIL operations in the same directory
        os.system('raspistill -t 1 -o image.png -w "' + str(self.img_width) + '" -h "' + str(self.img_height) + '" -rot "' + str(self.img_rot) + '"')
        # Open the image just taken by raspicam
        # Stores the RGB array in the value field
        self.value = Image.open('image.png').convert('RGB')

# Just testing the camera in python

#os.system('raspistill -t 1 -o image.png -w "' + str(200) + '" -h "' + str(200) + '" -rot "' + str(0) + '"')
