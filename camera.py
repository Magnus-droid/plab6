import os
import camera
from PIL import Image


class Camera():

    def __init__(self, img_width=64, img_height=64, img_rot=0):
        self.value = None
        self.img_width = img_width
        self.img_height = img_height
        self.img_rot = img_rot

    def get_value(self):  return self.value

    def update(self):
        self.sensor_get_value()
        return self.value

    def reset(self):
        self.value = None

    def sensor_get_value(self):
        # This is a OS call that takes a image and makes it accessible to PIL operations in the same directory
        os.system('raspistill --nopreview -t 1 -o image.png -w "' + str(self.img_width) + '" -h "' + str(self.img_height) + '"')
        # Open the image just taken by raspicam
        # Stores the RGB array in the value field
        self.value = Image.open('image.png').convert('RGB')

# Just testing the camera in python

# os.system('raspistill -n -t 1 -o image.png -w "' + str(64) + '" -h "' + str(64) + '" -rot "' + str(0) + '"')
