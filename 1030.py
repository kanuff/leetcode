class Space:
    def __init__(self, x, y):
        self.pos = [x, y]

class Solution:
    # this solution runs a little slow and also requires an extra class --> on second pass implement without two double nested loops or the additional class
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        self.grid = [ [Space(x,y) for y in range(C)] for x in range(R) ]
        self.cells = []
        
        for row in range(R):
            for col in range(C):
                self.grid[row][col].distance = self.manhattan_distance(r0, c0, row, col)
        
        for row in range(R):
            for col in range(C):
                self.cells.append(self.grid[row][col])

        sortedCells = sorted(self.cells, key = lambda x: x.distance)
        return [ cell.pos for cell in sortedCells ]
    
    def manhattan_distance(self, x0, y0, x1, y1):
        return abs(x0 - x1) + abs(y0 - y1)
    