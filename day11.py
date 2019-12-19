from day02 import Computer
from collections import defaultdict

def paint_grid(computer, grid):
    pos_x = 0
    pos_y = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    direction_symbol = ['^', '>', 'V', '<'] 
    direction = 0

    while not computer.halted:
        computer.add_input([grid[pos_x][pos_y]])
        computer.run()
        output = computer.get_output()
        grid[pos_x][pos_y] = output[0]
        direction += -1 if output[1] == 0 else 1
        pos_x += directions[direction % 4][0]
        pos_y += directions[direction % 4][1]


def squares_painted(grid):
    return sum(len(row[1]) for row in grid.items())


def grid_drawing(grid):
    top = max(max(row[1]) for row in grid.items())
    bottom = min(min(row[1]) for row in grid.items())

    left = min(grid)
    right = max(grid)

    drawing = []

    for y in range(top, bottom -1, -1):
        line = ''
        for x in range(left, right + 1):
            line += '#' if grid[x][y] == 1 else '.'
        drawing.append(line)

    return drawing


def test1():
    print("Test 1: ")

    with open("inputs/input11.txt", "r") as f:
        memory = [int(x) for x in f.readline().split(',')]
        computer = Computer(memory)
        grid = defaultdict(lambda: defaultdict(int))
        paint_grid(computer, grid)
        print(squares_painted(grid))


def test2():
    print("Test 2: ")

    with open("inputs/input11.txt", "r") as f:
        memory = [int(x) for x in f.readline().split(',')]
        computer = Computer(memory)
        grid = defaultdict(lambda: defaultdict(int))
        grid[0][0] = 1
        paint_grid(computer, grid)
        for line in grid_drawing(grid):
            print(line)

if __name__ == "__main__":
    test1()
    test2()