"""
from SimpleCV import Image, Camera
def picture():
	cam = Camera()
	img = cam.getImage()
	img.save('selfie.jpg')
"""
#
## from VideoCapture import Device
## cam = Device()
## cam.saveSnapshot('image.jpg')
#
#import pygame
#import pygame.camera
#
#pygame.camera.init()
## pygame.camera.list_camera() #Camera detected or not
#cam = pygame.camera.Camera("/dev/video0",(640,480))
#cam.start()
#
#def picture():
#    img = cam.get_image()
#    pygame.image.save(img,"selfie.jpg")

from cv2 import *
import time
def picture():
# initialize the camera
    cam = VideoCapture(0)   # 0 -> index of camera
    time.sleep(1)
    s, img = cam.read()
    if s:    # frame captured without any errors
        namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
        imshow("cam-test",img)
        destroyWindow("cam-test")
        imwrite("selfie.jpg",img) #save image
