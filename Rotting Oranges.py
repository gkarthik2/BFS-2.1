# Time Complexity : O(mn)
# Space Complexity : O(mn)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        queue = []
        fresh = 0
        totalfresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    totalfresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))

        while(len(queue) > 0):
            size = len(queue)
            for i in range(size):
                (p,q) = queue.pop(0)

                if p > 0 and grid[p-1][q] == 1:
                    grid[p-1][q] = 2
                    queue.append((p-1,q))
                    fresh += 1
                
                if p < len(grid)-1 and grid[p+1][q] == 1:
                    grid[p+1][q] = 2
                    queue.append((p+1,q))
                    fresh += 1

                if q > 0 and grid[p][q-1] == 1:
                    grid[p][q-1] = 2
                    queue.append((p,q-1))
                    fresh += 1

                if q < len(grid[0])-1 and grid[p][q+1] == 1:
                    grid[p][q+1] = 2
                    queue.append((p,q+1))
                    fresh += 1
            count += 1
                    
        if totalfresh == 0:
            return 0

        if fresh == totalfresh:
            return count-1
        return -1