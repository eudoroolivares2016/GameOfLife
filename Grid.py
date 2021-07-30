import pygame 
import numpy as np
import random

class Grid:
    def __init__(self,width,height,scale,offset):
        self.scale = scale
        self.columns = int(height/2)
        self.rows = int(width/2)
        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size)) # defines the grid array as a 2D array the shpae of the Grids size 
        self.offset = offset


    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)
                
