from collections import defaultdict
from day02 import Computer

def draw_screen(computer, screen):
    computer.run()

    output = computer.get_output()

    for i in range(0, len(output), 3):
        screen[output[i]][output[i+1]] = output[i+2]

def count_blocks(screen):
    return sum(sum(1 if row[1][x] == 2 else 0 for x in row[1]) for row in screen.items())

def get_ball(screen):
    top = max(max(row[1]) for row in screen.items())
    bottom = min(min(row[1]) for row in screen.items())

    left = min(screen)
    right = max(screen)

    for y in range(bottom, top + 1):
        for x in range(left, right + 1):
            if screen[x][y] == 4:
                return x

    return None

def get_paddle(screen):
    top = max(max(row[1]) for row in screen.items())
    bottom = min(min(row[1]) for row in screen.items())

    left = min(screen)
    right = max(screen)

    for y in range(bottom, top + 1):
        for x in range(left, right + 1):
            if screen[x][y] == 3:
                return x

    return None
    

def test1():
    print("Test 1: ")

    with open("inputs/input13.txt", "r") as f:
        memory = [int(x) for x in f.readline().split(',')]
        computer = Computer(memory)
        screen = defaultdict(lambda: defaultdict(int))
        draw_screen(computer, screen)
        print(count_blocks(screen))


def test2():
    print("Test 2: ")

    with open("inputs/input13.txt", "r") as f:
        memory = [int(x) for x in f.readline().split(',')]
        memory[0] = 2
        computer = Computer(memory)
        screen = defaultdict(lambda: defaultdict(int))

        while not computer.halted:
            draw_screen(computer, screen)

            ball = get_ball(screen)
            paddle = get_paddle(screen)

            if ball < paddle:
                computer.add_input([-1])
            elif ball > paddle:
                computer.add_input([1])
            else:
                computer.add_input([0])

        print(screen[-1][0])


if __name__ == "__main__":
    test1()
    test2()
