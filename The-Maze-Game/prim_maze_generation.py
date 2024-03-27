# Aabjosh Singh
# The Maze Game - Open End Project
# File that generates mazes

# X AND Y VARIABLES MEAN X-LENGHT, Y-HEIGHT

# Random is imported to have random generation
import random

# Start with an empty 2D array for the maze
maze = []

# prints maze for debugging in console using ASCII string blocks
def output(maze):
    for i in range(len(maze)):
        rowstr = ""
        for j in range(len(maze[0])):
            if maze[i][j] == "w":
                rowstr += ("\033[1;44m" + "  " + "\033[0m")
            elif maze[i][j] == "p":
                rowstr += ("  " + "\033[0m")
            else:
                rowstr += ("\033[1;42m" + "  " + "\033[0m")
        print(rowstr)

# Check and return adjacent cells to randompos
def adjacent(randompos):
  	adjacentpaths = 0
  	if maze[randompos[0]-1][randompos[1]] == 'p':
    		adjacentpaths += 1
  	if maze[randompos[0]+1][randompos[1]] == 'p':
  		  adjacentpaths += 1
  	if maze[randompos[0]][randompos[1]-1] == 'p':
  		  adjacentpaths +=1
  	if maze[randompos[0]][randompos[1]+1] == 'p':
  		  adjacentpaths += 1
  
  	return adjacentpaths

# Set a random starting point and ensure it is not on an edge
def random_start(height, width):
    initial_y = int(random.random()*height)
    initial_x = int(random.random()*width)
    if initial_y == 0:
        initial_y += 1
    elif initial_y == height-1:
        initial_y -= 1
      
    if initial_x == 0:
        initial_x += 1
    elif initial_x == width-1:
        initial_x -= 1

    return [initial_y, initial_x]

# Most important function, that creates the maze of the given size
def initialize(y, x):
    global maze
    maze = []
    print('GENERATING MAZE, AREA = ' + str(y*x))
  
    for i in range(y):
      	row = []
      	for j in range(x):
      		  row.append(' ')
      	maze.append(row)

    # Take the list return from random_start and save it here for use next
    startpos = random_start(y,x)

    # Startpos is now a path, so add its walls, and set them as 'w'
    maze[startpos[0]][startpos[1]] = 'p'
    walls = []
    up = [startpos[0] - 1, startpos[1]]
    down = [startpos[0] + 1, startpos[1]]
    left = [startpos[0], startpos[1] - 1]
    right = [startpos[0], startpos[1] + 1]
    
  
    walls.append(up)
    walls.append(down)
    walls.append(left)
    walls.append(right)
    
    # Denote walls in maze
    maze[up[0]][up[1]] = 'w'
    maze[down[0]][down[1]] = 'w'
    maze[left[0]][left[1]] = 'w'
    maze[right[0]][right[1]] = 'w'

    return [maze, walls, y, x, False]

# Function to make a growing maze
def generate(vars):
    maze = vars[0]
    walls = vars[1]
    y = vars[2]
    x = vars[3]
    endcase = vars[4]
  
    if walls:
      	# Choose random wall
        randompos = walls[int(random.random()*len(walls))-1]
  
        # If left wall, add a path if there is only one adjacent path
        if randompos[1] != 0 and maze[randompos[0]][randompos[1]-1] == ' ' and maze[randompos[0]][randompos[1]+1] == 'p':
            adjacents = adjacent(randompos)
            if adjacents < 2:
                
                # set this random wall as path
                maze[randompos[0]][randompos[1]] = 'p'
    
                # Left cell wall
                if randompos[1] != 0:
                    if maze[randompos[0]][randompos[1]-1] != 'p':
                        maze[randompos[0]][randompos[1]-1] = 'w'
                    if [randompos[0], randompos[1]-1] not in walls:
                        walls.append([randompos[0], randompos[1]-1])
                
                # Top cell wall
                if randompos[0] != 0:
                    if maze[randompos[0]-1][randompos[1]] != 'p':
                        maze[randompos[0]-1][randompos[1]] = 'w'
                    if [randompos[0]-1, randompos[1]] not in walls:
                        walls.append([randompos[0]-1, randompos[1]])
        
        
                # Bottom cell wall
                if randompos[0] != y-1:
                    if maze[randompos[0]+1][randompos[1]] != 'p':
                        maze[randompos[0]+1][randompos[1]] = 'w'
                    if [randompos[0]+1, randompos[1]] not in walls:
                        walls.append([randompos[0]+1, randompos[1]])
    
            # Delete this wall from the list since it has been iterated on
            for i in walls:
                if i[0] == randompos[0] and i[1] == randompos[1]:
                    walls.remove(i)
      
      
      	# If upper wall and 1 adjacent path, make it a path
        if randompos[0] != 0 and maze[randompos[0]-1][randompos[1]] == ' ' and maze[randompos[0]+1][randompos[1]] == 'p':
           
            adjacents = adjacent(randompos)
            if adjacents < 2:
                # set this random wall as path
                maze[randompos[0]][randompos[1]] = 'p'
              
                # Left cell wall
                if randompos[1] != 0:
                    if maze[randompos[0]][randompos[1]-1] != 'p':
                        maze[randompos[0]][randompos[1]-1] = 'w'
                    if [randompos[0], randompos[1]-1] not in walls:
                        walls.append([randompos[0], randompos[1]-1])
                      
                # Top cell wall
                if randompos[0] != 0:
                    if maze[randompos[0]-1][randompos[1]] != 'p':
                        maze[randompos[0]-1][randompos[1]] = 'w'
                    if [randompos[0]-1, randompos[1]] not in walls:
                        walls.append([randompos[0]-1, randompos[1]])
                      
                # Right cell wall
                if randompos[1] != x-1:
                    if maze[randompos[0]][randompos[1]+1] != 'p':
                        maze[randompos[0]][randompos[1]+1] = 'w'
                    if [randompos[0], randompos[1]+1] not in walls:
                        walls.append([randompos[0], randompos[1]+1])
      
            # Delete this random wall from the list since it has been iterated on
            for i in walls:
                if i[0] == randompos[0] and i[1] == randompos[1]:
                    walls.remove(i)
      
      
      	# If bottom wall and 1 adjacent path, make it a path
        if randompos[0] != y-1 and maze[randompos[0]+1][randompos[1]] == ' ' and maze[randompos[0]-1][randompos[1]] == 'p':
            adjacents = adjacent(randompos)
            if adjacents < 2:
                # set this random wall as path
                maze[randompos[0]][randompos[1]] = 'p'
                    
                # Left cell wall
                if randompos[1] != 0:
                    if maze[randompos[0]][randompos[1]-1] != 'p':
                        maze[randompos[0]][randompos[1]-1] = 'w'
                    if [randompos[0], randompos[1]-1] not in walls:
                        walls.append([randompos[0], randompos[1]-1])
    
                # Right cell wall
                if randompos[1] != x-1:
                    if maze[randompos[0]][randompos[1]+1] != 'p':
                        maze[randompos[0]][randompos[1]+1] = 'w'
                    if [randompos[0], randompos[1]+1] not in walls:
                        walls.append([randompos[0], randompos[1]+1])
                      
                # Bottom cell wall
                if randompos[0] != y-1:
                    if maze[randompos[0]+1][randompos[1]] != 'p':
                        maze[randompos[0]+1][randompos[1]] = 'w'
                    if [randompos[0]+1, randompos[1]] not in walls:
                        walls.append([randompos[0]+1, randompos[1]])
      
            # Delete this random wall from the list since it has been iterated on
            for i in walls:
                if i[0] == randompos[0] and i[1] == randompos[1]:
                    walls.remove(i)
      
      
      	# If right wall and 1 adjacent path, make it a path
        if randompos[1] != x-1 and maze[randompos[0]][randompos[1]+1] == ' ' and maze[randompos[0]][randompos[1]-1] == 'p':
            adjacents = adjacent(randompos)
            if adjacents < 2:
                # set this random wall as path
                maze[randompos[0]][randompos[1]] = 'p'
                    
                # Right cell wall
                if randompos[1] != x-1:
                    if maze[randompos[0]][randompos[1]+1] != 'p':
                        maze[randompos[0]][randompos[1]+1] = 'w'
                    if [randompos[0], randompos[1]+1] not in walls:
                        walls.append([randompos[0], randompos[1]+1])
    
                # Top cell wall
                if randompos[0] != 0:
                    if maze[randompos[0]-1][randompos[1]] != 'p':
                        maze[randompos[0]-1][randompos[1]] = 'w'
                    if [randompos[0]-1, randompos[1]] not in walls:
                        walls.append([randompos[0]-1, randompos[1]])
                      
                # Bottom cell wall
                if randompos[0] != y-1:
                    if maze[randompos[0]+1][randompos[1]] != 'p':
                        maze[randompos[0]+1][randompos[1]] = 'w'
                    if [randompos[0]+1, randompos[1]] not in walls:
                        walls.append([randompos[0]+1, randompos[1]])
      
            # Delete this random wall from the list since it has been iterated on
            for i in walls:
                if i[0] == randompos[0] and i[1] == randompos[1]:
                    walls.remove(i)
      
      
      	# If not any of the cases, still remove from list since it was checked
        for i in walls:
      		  if i[0] == randompos[0] and i[1] == randompos[1]:
      			   walls.remove(i)

        endcase = False
      
    else:
        finishmaze([maze, y, x])
        endcase = True
    return [maze, walls, y, x, endcase]

# Function to generate an instant maze
def generate_instant(vars):
    maze = vars[0]
    walls = vars[1]
    y = vars[2]
    x = vars[3]
  
    while walls:
      	# Choose random wall
        randompos = walls[int(random.random()*len(walls))-1]
  
        # If left wall, add a path if there is only one adjacent path
        if randompos[1] != 0 and maze[randompos[0]][randompos[1]-1] == ' ' and maze[randompos[0]][randompos[1]+1] == 'p':
            adjacents = adjacent(randompos)
            if adjacents < 2:
                
                # set this random wall as path
                maze[randompos[0]][randompos[1]] = 'p'
    
                # Left cell wall
                if randompos[1] != 0:
                    if maze[randompos[0]][randompos[1]-1] != 'p':
                        maze[randompos[0]][randompos[1]-1] = 'w'
                    if [randompos[0], randompos[1]-1] not in walls:
                        walls.append([randompos[0], randompos[1]-1])
                
                # Up cell wall
                if randompos[0] != 0:
                    if maze[randompos[0]-1][randompos[1]] != 'p':
                        maze[randompos[0]-1][randompos[1]] = 'w'
                    if [randompos[0]-1, randompos[1]] not in walls:
                        walls.append([randompos[0]-1, randompos[1]])
        
        
                # Bottom cell wall
                if randompos[0] != y-1:
                    if maze[randompos[0]+1][randompos[1]] != 'p':
                        maze[randompos[0]+1][randompos[1]] = 'w'
                    if [randompos[0]+1, randompos[1]] not in walls:
                        walls.append([randompos[0]+1, randompos[1]])
    
            # Delete this wall from the list since it has been iterated on
            for i in walls:
                if i[0] == randompos[0] and i[1] == randompos[1]:
                    walls.remove(i)
      
      
      	# If upper wall and 1 adjacent path, make it a path
        if randompos[0] != 0 and maze[randompos[0]-1][randompos[1]] == ' ' and maze[randompos[0]+1][randompos[1]] == 'p':
           
            adjacents = adjacent(randompos)
            if adjacents < 2:
                # set this random wall as path
                maze[randompos[0]][randompos[1]] = 'p'
              
                # Left cell wall
                if randompos[1] != 0:
                    if maze[randompos[0]][randompos[1]-1] != 'p':
                        maze[randompos[0]][randompos[1]-1] = 'w'
                    if [randompos[0], randompos[1]-1] not in walls:
                        walls.append([randompos[0], randompos[1]-1])
                      
                # Top cell wall
                if randompos[0] != 0:
                    if maze[randompos[0]-1][randompos[1]] != 'p':
                        maze[randompos[0]-1][randompos[1]] = 'w'
                    if [randompos[0]-1, randompos[1]] not in walls:
                        walls.append([randompos[0]-1, randompos[1]])
                      
                # Right cell wall
                if randompos[1] != x-1:
                    if maze[randompos[0]][randompos[1]+1] != 'p':
                        maze[randompos[0]][randompos[1]+1] = 'w'
                    if [randompos[0], randompos[1]+1] not in walls:
                        walls.append([randompos[0], randompos[1]+1])
      
            # Delete this random wall from the list since it has been iterated on
            for i in walls:
                if i[0] == randompos[0] and i[1] == randompos[1]:
                    walls.remove(i)
      
      
      	# If bottom wall and 1 adjacent path, make it a path
        if randompos[0] != y-1 and maze[randompos[0]+1][randompos[1]] == ' ' and maze[randompos[0]-1][randompos[1]] == 'p':
            adjacents = adjacent(randompos)
            if adjacents < 2:
                # set this random wall as path
                maze[randompos[0]][randompos[1]] = 'p'
                    
                # Left cell wall
                if randompos[1] != 0:
                    if maze[randompos[0]][randompos[1]-1] != 'p':
                        maze[randompos[0]][randompos[1]-1] = 'w'
                    if [randompos[0], randompos[1]-1] not in walls:
                        walls.append([randompos[0], randompos[1]-1])
    
                # Right cell wall
                if randompos[1] != x-1:
                    if maze[randompos[0]][randompos[1]+1] != 'p':
                        maze[randompos[0]][randompos[1]+1] = 'w'
                    if [randompos[0], randompos[1]+1] not in walls:
                        walls.append([randompos[0], randompos[1]+1])
                      
                # Bottom cell wall
                if randompos[0] != y-1:
                    if maze[randompos[0]+1][randompos[1]] != 'p':
                        maze[randompos[0]+1][randompos[1]] = 'w'
                    if [randompos[0]+1, randompos[1]] not in walls:
                        walls.append([randompos[0]+1, randompos[1]])
      
            # Delete this random wall from the list since it has been iterated on
            for i in walls:
                if i[0] == randompos[0] and i[1] == randompos[1]:
                    walls.remove(i)
      
      
      	# If right wall and 1 adjacent path, make it a path
        if randompos[1] != x-1 and maze[randompos[0]][randompos[1]+1] == ' ' and maze[randompos[0]][randompos[1]-1] == 'p':
            adjacents = adjacent(randompos)
            if adjacents < 2:
                # set this random wall as path
                maze[randompos[0]][randompos[1]] = 'p'
                    
                # Right cell wall
                if randompos[1] != x-1:
                    if maze[randompos[0]][randompos[1]+1] != 'p':
                        maze[randompos[0]][randompos[1]+1] = 'w'
                    if [randompos[0], randompos[1]+1] not in walls:
                        walls.append([randompos[0], randompos[1]+1])
    
                # Top cell wall
                if randompos[0] != 0:
                    if maze[randompos[0]-1][randompos[1]] != 'p':
                        maze[randompos[0]-1][randompos[1]] = 'w'
                    if [randompos[0]-1, randompos[1]] not in walls:
                        walls.append([randompos[0]-1, randompos[1]])
                      
                # Bottom cell wall
                if randompos[0] != y-1:
                    if maze[randompos[0]+1][randompos[1]] != 'p':
                        maze[randompos[0]+1][randompos[1]] = 'w'
                    if [randompos[0]+1, randompos[1]] not in walls:
                        walls.append([randompos[0]+1, randompos[1]])
      
            # Delete this random wall from the list since it has been iterated on
            for i in walls:
                if i[0] == randompos[0] and i[1] == randompos[1]:
                    walls.remove(i)
      
      
      	# If not any of the cases, still remove from list since it was checked
        for i in walls:
      		  if i[0] == randompos[0] and i[1] == randompos[1]:
      			   walls.remove(i)

      
    # Make any ' ' instances 'w'
    for i in range(y):
        for j in range(x):
            if maze[i][j] == ' ':
                maze[i][j] = 'w'
    
    # Add a start and end to the first path on the left top, and bottom right
    for i in range (x):
        if maze[1][i] == 'p':
    		    maze[0][i] = 'p'
    		    break
    
    for i in range(x-1, 0, -1):
        if maze[y-2][i] == 'p':
    		    maze[y-1][i] = 'p'
    		    break

    return maze

# Completes growing maze
def finishmaze(vars):

    maze = vars[0]
    y = vars[1]
    x = vars[2]
    
    # Make any ' ' instances 'w'
    for i in range(y):
        for j in range(x):
            if maze[i][j] == ' ':
                maze[i][j] = 'w'
    
    # Add a start and end to the first path on the left top, and bottom right
    for i in range (x):
        if maze[1][i] == 'p':
    		    maze[0][i] = 'p'
    		    break
    
    for i in range(x-1, 0, -1):
        if maze[y-2][i] == 'p':
    		    maze[y-1][i] = 'p'
    		    break
  
    return maze
