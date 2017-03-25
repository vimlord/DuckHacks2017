from SimpleCV import Image, Camera

def picture():
	cam = Camera()
	img = cam.getImage()
	img.save('selfie.jpg')

# from VideoCapture import Device
# cam = Device()
# cam.saveSnapshot('image.jpg')

# import pygame
# import pygame.camera

# pygame.camera.init()
# pygame.camera.list_camera() #Camera detected or not
# cam = pygame.camera.Camera("/dev/video0",(640,480))
# cam.start()
# img = cam.get_image()
# pygame.image.save(img,"filename.jpg")