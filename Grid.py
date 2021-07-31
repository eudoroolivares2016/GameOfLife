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

    def Conway(self,off_color,on_color,surface)::
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(surface,on_color,[x_pos,y_pos,self.scale - self.offset, self.scale - self.offset])
            next = np.ndarray(shape = (self.size))
            for x in range(self.rows):
                for y in range(self.columns):
                    state = state.grid_array[x][y]
                    neighbors = self.get_neighbors(x,y)
                    if state == 0 and neighbors == 3: #Any dead cell with 3 live neighbors becomes a live cell
                        next[x][y] = 1
                    elif state == 1 and (neighbors == 3 or neighbors == 2)
                        next[x][y] == 1
                    elif state == 1 and (neighbors > 3):
                        next[x][y] == 0
                    elif state == 1 and (neighbors < 2):
                        next[x][y] == 0
                    else:
                        next[x][y] == state
            self.next.grid_array = next
    def get_neighbors(self, x_pos,y_pos):
        #TODO


