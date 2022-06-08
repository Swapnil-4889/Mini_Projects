#!/usr/bin/python3
# coding: utf-8

# In[10]:


#Please go through the comments get the working of the program
#I was not able to create a live simulation of the Ant moving 
#This codes give output of the pattern after a particular number of steps

from enum import Enum          # For implementing Enumerations
from enum import IntEnum       # For implementing Enumerations

class Direction(IntEnum):   #This Class is an enumeration that stores direction in the form of number
    UP=0                    #The directions are encoded in number for easy operation
    RIGHT=1   
    DOWN=2
    LEFT=3

class Colour(Enum):    # This class stores Colours
    WHITE=" "          #ANTVAL represents the ant on the pattern
    BLACK="*"
    ANTVAL="A"

def flip_colour(grid,x,y):     # This function flips the colour of a cell according to the rule
    if(grid[y][x] == Colour.BLACK):
        grid[y][x] = Colour.WHITE
    elif(grid[y][x] == Colour.WHITE):
        grid[y][x] = Colour.BLACK

def update_Direction(grid,x,y,direction):  # This function updates the direction and returns the new direction
    if(grid[y][x] == Colour.BLACK):
        turn_RIGHT = False
    else:
        turn_RIGHT = True
    direction_index = direction.value
    if turn_RIGHT:
        direction_index = (direction_index +1)%4
    else:
        direction_index =(direction_index - 1)%4
    directions=[Direction.UP, Direction.RIGHT, Direction.DOWN , Direction.LEFT]
    direction=directions[direction_index]
    return direction

def update_position(x,y,direction): #This function updates the posisition  and returns the new position
    if(direction == Direction.UP):
        y-=1
    elif(direction == Direction.RIGHT):
        x-=1
    elif(direction == Direction.DOWN):
        y+=1
    elif(direction == Direction.LEFT):
        x+=1
    return x,y

def print_grid_array(grid,x,y):   # This function prints the grid/pattern traced by the ant
    print(50 * "-")
    print("\n".join("".join(v.value for v in row) for row in grid))


def ANT_MOVE(width,height,steps):   # This is the function that simulates the motion of ant and calls all the other functions
    grid = [[Colour.WHITE] * width for _ in range(height)]
    x = width // 2
    y = height // 2
    direction = Direction.UP
    i=0
    j=0
    while (i<steps and 0<= x <width and 0<= y <height):
        flip_colour(grid,x,y)
        direction=update_Direction(grid,x,y,direction)
        x,y = update_position(x,y,direction)
        if(False and i==j):   #This condition can be made true and then  this program prints the pattern after every 100 steps
            print("STEP = "+str(j))
            print_grid_array(grid,x,y)
            j+=100
        i+=1
    print("FINAL PATTERN")
    val=grid[y][x]      # Only the final print of the pattern consists of the location of the ant
    grid[y][x]=Colour.ANTVAL
    print_grid_array(grid,x,y)
    grid[y][x]=val


if __name__ == "__main__":
    ANT_MOVE(width=64,height=64,steps=12300) #width and height are the width and height of the box respectively (64 x 64)for the problem
                                          
        # Steps is the number of steps for ant to trace
        # A represents the final posisiotn of the ant
# The steps argument for the ANT_MOVE function is the total number of steps the ant shall move 
#The ANT_MOVE function has a while loop


# In[ ]:




