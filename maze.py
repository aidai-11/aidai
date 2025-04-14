import random
import sys
sys.setrecursionlimit(10000)
import random
import sys
sys.setrecursionlimit(10000)

ROWS, COLS = 15, 15

DIRS = [(-2, 0), (2, 0), (0, -2), (0, 2)]
def create_empty_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    return maze

def generate_maze(maze, x, y):
    maze[x][y] = ' '
    random.shuffle(DIRS)
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if 1 <= nx < ROWS - 1 and 1 <= ny < COLS - 1 and maze[nx][ny] == '#':
            maze[x + dx // 2][y + dy // 2] = ' '
            generate_maze(maze, nx, ny)
            def print_maze(maze):
    for row in maze:
        print(''.join(row))
        def find_path(maze, x, y, visited):
    if x < 0 or y < 0 or x >= ROWS or y >= COLS:
        return False
    if maze[x][y] == '#' or visited[x][y]:
        return False
    if (x, y) == (ROWS - 2, COLS - 2):
        maze[x][y] = '.'
        return True

    visited[x][y] = True

    if (find_path(maze, x + 1, y, visited) or
        find_path(maze, x - 1, y, visited) or
        find_path(maze, x, y + 1, visited) or
        find_path(maze, x, y - 1, visited)):
        maze[x][y] = '.'
        return True

    return False
    def main():
    maze = create_empty_maze(ROWS, COLS)
    generate_maze(maze, 1, 1)
    maze[1][1] = 'S'
    maze[ROWS - 2][COLS - 2] = 'E
    maze[1][1] = 'S'
    maze[ROWS - 2][COLS - 2] = 'E'
    print_maze(maze)
    if name == "__main__":
    main()