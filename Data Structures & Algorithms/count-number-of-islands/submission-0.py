"""
Number of Islands
Medium

Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:

Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1
Example 2:

Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4
"""


class Solution:

  def numIslands(self, grid: List[List[str]]) -> int:
    # Base case: if the grid is empty, there are no islands
    if not grid or not grid[0]:
      return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    # Helper function to perform Depth-First Search (DFS)
    def dfs(r: int, c: int):
      # Base cases for recursion:
      # Out of bounds, or if the current cell is water ('0')
      if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
        return

      # Mark the current land cell as visited by 'sinking' it (turning it to '0')
      grid[r][c] = "0"

      # Recursively visit all 4 adjacent neighbors (Down, Up, Right, Left)
      dfs(r + 1, c)
      dfs(r - 1, c)
      dfs(r, c + 1)
      dfs(r, c - 1)

    # Traverse every cell in the grid
    for r in range(rows):
      for c in range(cols):
        # When we find unvisited land ('1'), we found a new island
        if grid[r][c] == "1":
          dfs(r, c)  # Destroy/sink the entire connected island using DFS
          island_count += 1  # Increment the total island count

    return island_count