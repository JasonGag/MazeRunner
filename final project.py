#Class MazeRunner
class MazeRunner:

    def __init__(self):
        self.list = []

    #Function loadData
    def loadData(self, filename):
        #Create a list to hold the maze data
        maze = []

        #Open the file that holds data, read
        mazeFile = open(filename, "r")

        #Read the data
        mazeFileRead = mazeFile.read()

        #Split the data by new lines
        mazeData = mazeFileRead.split("\n")

        #Iterate through lines in maze data to put into list
        for line in mazeData:
            #Append to list
            maze.append(line)
            #print(line)

        #Close the file
        mazeFile.close()

        #Return the maze list
        return maze

    #Function displayMaze
    def displayMaze(self, list):
        #Iterate through list line by line
        for line in list:
            #Print line
            print(line)

    #Function getStart
    def getStart(self, maze):

        #Coordinates for starting position stored in list
        startCoordinate = []

        i = 0
        j = 0

        #Iterate through lines
        while i < len(maze):
            #Iterate through current line
            while j < len(maze):
                #Check if current position is start
                if maze[i][j] == "S":
                    #Append x coordinate
                    startCoordinate.append(i)

                    #Append y coordinate
                    startCoordinate.append(j)

                    #Return the start list
                    return startCoordinate

                j += 1
            j = 0
            i += 1

    #Function dfsHelper    
    def dfsHelper(self, maze, visited, currentNode):
        #Get neighbors of current position
        neighbors = self.getNeighbor(maze, currentNode[0], currentNode[1])

        #Check if position is at end point
        if maze[currentNode[0]][currentNode[1]] == 'E':
            #Display the current path
            self.displayMaze(maze)
            print(visited)
            print(len(visited))

            #Return visited points
            return visited

        #Not end point
        else:
            #Change current list to string to modify to show path
            stringList = list(maze[currentNode[0]])

            #Change character at current position to mark visited path
            stringList[currentNode[1]] = "*"

            #Turn string back to list
            strToList = "".join(stringList)

            #Change lists
            maze[currentNode[0]] = strToList

            #Append to visited list 
            visited.append(currentNode)

            #Check if neighbors not in visited
            for i in neighbors:
                if i not in visited:
                    #Recurse with new position
                    self.dfsHelper(maze, visited, i)

    #Function dfs
    def dfs(self, maze, start):
        #List of visited positions
        visited = []
        
        return self.dfsHelper(maze, visited, start)

    #Function getNeighbor
    def getNeighbor(self, maze, x, y):
        #List of neighbors
        neighbors = []

        #Check boundary
        if x > 0:
            #Check if valid position
            if maze[x - 1][y] == " " or maze[x - 1][y] == 'E':
                #Append to list
                neighbors.append([x - 1, y])

        #Check for boundary
        if x < len(maze)-1:
            #Check if valid position
            if maze[x + 1][y] == " " or maze[x + 1][y] == 'E':
                #Append to list
                neighbors.append([x + 1, y])

        #Check for boundary
        if y > 0:
            #Check if valid position
            if maze[x][y - 1] == " " or maze[x][y - 1] == 'E':
                #Append to list
                neighbors.append([x, y - 1])

        #Check for boundary
        if y < len(maze[x]):
            #Check if valid position
            if maze[x][y + 1] == " " or maze[x][y + 1] == 'E':
                #Append to List
                neighbors.append([x, y + 1])

        #Return neighbors list
        return neighbors
        

s = MazeRunner()

loadedMaze = s.loadData("Hard.txt")
print(len(loadedMaze))
start = s.getStart(loadedMaze)
s.displayMaze(loadedMaze)
print(start)
#print(s.getNeighbor(loadedMaze, start[0], start[1]))
#print(s.dfs(loadedMaze, start))
s.dfs(loadedMaze, start)
