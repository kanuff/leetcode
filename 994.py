# REALLY SLOW SOLUTION --> Redo on second pass
class Solution:
    def rotten_neighbors(grid, pos):
        row,col = pos
        if grid[row][col] == 0:
            return False
        height = len(grid)
        width = len(grid[0])
        cardinals = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0],
        ]
        check_pos = [
            [row + dx, col + dy] for dx,dy in cardinals if 0 <= (row+dx) < height and 0 <= (col+dy)< width
        ]
        for o_pos in check_pos:
            ox, oy = o_pos
            if grid[ox][oy] == 2:
                return True
        return False
    
    def rot(grid):
        height = len(grid)
        width = len(grid[0])
        rotted_grid = [[0 for col in range(width)] for row in range(height)]
        for row in range(height):
            for col in range(width):
                if Solution.rotten_neighbors(grid, [row,col]):
                    rotted_grid[row][col] = 2
                else:
                    rotted_grid[row][col] = grid[row][col]
        return rotted_grid
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        old_grid = grid
        minutes = 0
        while(any(1 in row for row in old_grid)):
            new_grid = Solution.rot(old_grid)
            if new_grid == old_grid and any(1 in row for row in new_grid):
                return -1
            else:
                minutes+=1
            old_grid = new_grid
        return minutes
        