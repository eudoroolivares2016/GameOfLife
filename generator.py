import pygame 
import os 
os.environ["SDL_VIDEO_CENTERED"] = '1'

width, height = 1920,1000 #screen size
size = (width,height)
pygame.init()
pygame.display.set_caption("Welcome to Ed's version of Conways game of life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 55

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)