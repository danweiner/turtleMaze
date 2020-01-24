import turtle

def searchFrom(maze, startRow, startColumn):
  maze.updatePosition(startRow, startColumn)
  # Check for base cases
  # 1. Obstacle, return false
  if maze[startRow][startColumn] == OBSTACLE:
    return False 

  # 2. Found already explored square 
  if maze[startRow][startColumn] == TRIED:
    return False 
  
  # 3. Success, outside edge not Obstacle 
  if maze.isExit(startRow, startColumn):
    maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    return True 
  
  maze.updatePosition(startRow, startColumn, TRIED)

  # Otherwise, use logical short circuiting to try each 
  # direction in turn (if needed)
  found = searchFrom(maze, startRow-1, startColumn) or \
          searchFrom(maze, startRow+1, startColumn) or \
          searchFrom(maze, startRow, startColumn-1) or \
          searchFrom(maze, startRow, startColumn+1)

  if found:
    maze.updatePosition(startRow, startColumn, PART_OF_PATH)
  else:
    maze.updatePosition(startRow, startColumn, DEAD_END)

  return found 

mazeFile = '''
++++++++++++++++++++++\n
+   +   ++ ++     +   \n
+ +   +       +++ + ++\n
+ + +  ++  ++++   + ++\n
+++ ++++++    +++ +  +\n
+          ++  ++    +\n
+++++ ++++++   +++++ +\n
+     +   +++++++  + +\n
+ +++++++      S +   +\n
+                + +++\n
++++++++++++++++++ +++\n
'''

lines = mazeFile.split('\n')
for line in lines:
  if line:
    print(line)


class Maze:
  def __init__(self, mazeFile):
    rowsInMaze = 0
    columnsInMaze = 0
    self.mazeList = []
    lines = mazeFile.split('\n')
    
    for line in lines:
      rowList = []
      col = 0
      for ch in line:
        rowList.append(ch)
        if ch == 'S':
          self.startRow = rowsInMaze
          self.startCol = col
        col += 1
      
      if rowList:
        self.mazeList.append(rowList)
        columnsInMaze = len(rowList)
        rowsInMaze += 1

    self.rowsInMaze = rowsInMaze
    self.columnsInMaze = columnsInMaze
    self.xTranslate = -columnsInMaze/2
    self.yTranslate = rowsInMaze/2
    # self.t = turtle.Turtle()
    # self.t.shape('turtle')
    # self.wn = turtle.Screen()
    # self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5, -(rowsInMaze-1)/2-.5, (columnsInMaze-1)/2+.5, (rowsInMaze-1)/2+.5) 


myMaze = Maze(mazeFile)
print(myMaze.mazeList)
print(myMaze.rowsInMaze)
print(myMaze.columnsInMaze)
