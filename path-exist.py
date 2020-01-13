"""
Instructions:
    - Implement the function `path_exists` below.
    - Save this file as `{first_name}_{last_name}_solve.py`.

Constraints:
    - Your solution will be run in a Python2.7 environment.
    - Only python standard library imports can be used and they must be imported within `path_exists`.
    - The function signature of `path_exists` cannot be modified.
    - Additional functions can be included, but must be defined within `path_exists`.
    - There will be two sets of input, small and large, each with different time limits.
"""

from collections import deque

def path_exists(grid, queries):
    """
    Determines whether for every start=(i1, j1) -> end=(i2, j2) query in `queries`,
    there exists a path in `grid` from start to end.

    The rules for a path are as follows:
        - A path consists of only up-down-left-right segments (no diagonals).
        - A path must consist of the same values. i.e. if grid[i1][j1] == 1, the path is comprised of only 1's.

    Examples:
        grid (visual only)

                1 0 0
                1 1 0
                0 1 1

        start     end       answer
        (0, 0) -> (2, 2)    True
        (2, 0) -> (0, 2)    False


    :param grid:        The grid on which `queries` are asked.
    :type grid:         list[list[int]], values can only be [0, 1].
    :param queries:     A set of queries for `grid`. Queries will be non-trivial.
    :type queries:      Iterable, contains elements of type tuple[tuple[int, int]].

    :return:            The result for each query, whether a path exists from start -> end.
    :rtype:             list[bool]
    """

# Define the start and the end
    srow = queries[0][0]
    scolm =queries[0][1]
    frow = queries[1][0]
    fcolm = queries[1][1]

# Define the number of rows and columns of the grid
    Nrow = len(grid)
    Ncolm = len(grid[0])

# Up-down-left-right direction vectors
    dr = [-1,1,0,0]
    dc = [0,0,1,-1]

# Mark all the vertices as not visited
    Visited = [[False] * Ncolm for i in range(Nrow)]

# Create a queue for the path search
    queue_row = deque()
    queue_colm = deque()

# Mark the start vertices as visited and enqueue it
    queue_row.append(srow)
    queue_colm.append(scolm)
    Visited[srow][scolm] = True

    while len(queue_row) !=0 and len(queue_colm)!=0:

          irow = queue_row.popleft()
          icolm = queue_colm.popleft()
#          print(irow,icolm,grid[irow][icolm])

          if irow == frow and icolm==fcolm:
             return True

# Explore neighbor
          for i in range(4):
              rr = irow+dr[i]
              cc = icolm+dc[i]

# Skip out of bounds locations
              if rr<0 or cc<0:
                 continue
              if rr>= Nrow or cc>=Ncolm:
                 continue

# Skip visited location or not equal path value
              if Visited[rr][cc]:
                 continue
              if grid[rr][cc]!= grid[srow][scolm]:
                 continue

              queue_row.append(rr)
              queue_colm.append(cc)
              Visited[rr][cc] = True


    return False

    raise NotImplementedError



# Main program 

grid = [[1,0,0],[1,1,0],[0,1,1]]
queries = ((1,0),(0,2))

print (path_exists(grid,queries))
