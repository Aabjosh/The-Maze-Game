# Aabjosh Singh
# The Maze Game - CS PROJECT (3UI)
# Maze solving file

# Init variables to be empty

# Keeps track of visited paths
visited = []

# All options at recent intersecion
intersection_options = []
increment = 0

# Saves current path after an intersection 
path = []

# KEeps track of intersection paths prior to current
error_path = []

# Keeps track of all grid coords where there is an intersection
intersection_points = []

# Function to determine starting position, goal, distance to end (estimatedcost), and resets vars for subsequent mazes
def manhattandist (maze):
    global estimatedcost
    global startposition
    global goal
    global currentposition
    global error_path
    global intersection_options
    global options
    global path
    global intersection_points

    # Check start
    for i in range(len(maze[0])):
        if maze[0][i] == "p":
            startposition = [0, i]
            break

    # Check end
    for i in range (len(maze[len(maze)-1])):
        if maze[len(maze)-1][i] == "p":
            goal = [len(maze)-1, i]
            break

    estimatedcost = (goal[0]-startposition[0]) + (goal[1]-startposition[1])
    visited.append(startposition)
    currentposition = startposition
    error_path = []
    intersection_options = []
    options = []
    path = []
    intersection_points = []
    
# Main function that solves the maze
def modified_astarsearch (maze, start):
    global error_path
    global intersection_options
    global currentposition
    global options
    global addcondition
    global path
    global intersection_points

    addcondition = True

    # Add currentposition to path if past an intersection
    if intersection_options != []:
        path.append(currentposition)

    # Current position marker
    maze[currentposition[0]][currentposition[1]] = "cu"

    # Saves positions of where to go
    options = []

    # Checks all directions if possible to travel, and adds possibilities to options
    if maze[currentposition[0]][currentposition[1]+1] == "p":
        options.append([currentposition[0],currentposition[1]+1])

    if maze[currentposition[0]+1][currentposition[1]] == "p":
        options.append([currentposition[0]+1,currentposition[1]])

    if maze[currentposition[0]][currentposition[1]-1] == "p":
        options.append([currentposition[0],currentposition[1]-1])

    if maze[currentposition[0]-1][currentposition[1]] == "p":
        options.append([currentposition[0]-1,currentposition[1]])

    # If no new options, look for visited cells
    if options == []:
        if maze[currentposition[0]][currentposition[1]+1] == "v":
            options.append([currentposition[0],currentposition[1]+1])
     
        if maze[currentposition[0]+1][currentposition[1]] == "v":
            options.append([currentposition[0]+1,currentposition[1]])
        
        if maze[currentposition[0]][currentposition[1]-1] == "v":
            options.append([currentposition[0],currentposition[1]-1])
    
        if maze[currentposition[0]-1][currentposition[1]] == "v":
            options.append([currentposition[0]-1,currentposition[1]])
        
    # If more than one option, this is a new intersecion so add all options except one that is being used to intersection_options, and add path to error_path. Reset path. If path is empty, add currentposition. 
    if len(options) > 1:
        intersection_options.append(options[1::])
        intersection_points.append(currentposition)
        if path != []:
            error_path.append(path)
            path = []
        else:
            path.append(currentposition)

    # Sort options based on how close they are to the goal (closest to farthest)
    sortlist = []
    for i in range (len(options)):
        sortlist.append(goal[0] - options[i][0] + goal[1] - options[i][1])
    sortlist.sort(reverse=True)
    zip(sortlist, options)
    options = options

    # Set nextpos to first option
    nextpos = options[0]

    # Make currentposition visited in grid
    maze[currentposition[0]][currentposition[1]] = "v"

    # Basically, if the next position is already visited, roll back to the most recent intersection and go down another route. Otherwise and after, add currentposition to visited and move to the next position
    if nextpos in visited:
        path_length = len(path)
        while i < path_length:
            if path[i] in intersection_points and addcondition:
                path.pop(i)
            path_length = len(path)
            i += 1
        error_path.append(path)
        maze[currentposition[0]][currentposition[1]] = "p"
        if intersection_options != []:
            nextpos = intersection_options[len(intersection_options)-1][0]
            intersection_options[len(intersection_options)-1].pop(0)
        if error_path != []:
            if intersection_points != []:
                intersection_points.pop()
            for i in range (len(error_path[len(error_path)-1])-1):
                maze[error_path[len(error_path)-1][i][0]][error_path[len(error_path)-1][i][1]] = "p"
            error_path.pop()
            addcondition = False
        if intersection_options != []:
            if intersection_options[len(intersection_options)-1] == []:
                intersection_options.pop(len(intersection_options)-1)
                if len(error_path) > 0:
                    path = error_path[-1]
                    error_path.pop()
            
    visited.append(currentposition)
    currentposition = nextpos
    maze[currentposition[0]][currentposition[1]] = "cu"

# Function called by pygame file to solve maze and return correctpositions
def ExecuteSolver(maze):
    global visited
    global intersection_options
    global increment
    global path
    global error_path
    global intersection_points

    # Make all vars empty in case of subsequent maze
    visited = []
    intersection_options = []
    increment = 0
    path = []
    error_path = []
    intersection_points = []
    returnlist = []

    # Init solver
    manhattandist(maze)

    # While not at the end, run the search
    while True:
        modified_astarsearch(maze, startposition)
        if currentposition == goal:
            break

    # Every "v" and the user position = correctpositions, so add to the list. Return the list
    for i in range (len(maze)):
        for j in range (len(maze[0])):
            if maze[i][j] == "v" or maze[i][j] == "cu":
                returnlist.append([j,i])
    print("CORRECTPOSITIONS: " + str(returnlist))

    return returnlist