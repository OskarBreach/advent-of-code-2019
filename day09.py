from day02 import Computer

def test1():
    print("Test 1: ")

    with open("inputs/input09.txt", "r") as f:
        memory = [int(x) for x in f.readline().split(',')]
        computer = Computer(memory, [1])
        computer.run()
        print(computer.get_output())


def test2():
    print("Test 2: ")

    with open("inputs/input09.txt", "r") as f:
        memory = [int(x) for x in f.readline().split(',')]
        computer = Computer(memory, [2])
        computer.run()
        print(computer.get_output())

if __name__ == "__main__":
    test1()
    test2()
