import itertools

class Computer:
    def __init__(self, memory):
        self.memory = memory
        self.ip = 0

    def __add(self):
        self.memory[self.memory[self.ip + 3]] \
                = self.memory[self.memory[self.ip + 1]] + self.memory[self.memory[self.ip + 2]]

        self.ip = self.ip + 4

    def __multiply(self):
        self.memory[self.memory[self.ip + 3]] \
                = self.memory[self.memory[self.ip + 1]] * self.memory[self.memory[self.ip + 2]]

        self.ip = self.ip + 4

    def run(self):
        instruction = self.memory[self.ip]

        if instruction == 1:
            self.__add()
        elif instruction == 2:
            self.__multiply()
        elif instruction == 99:
            return
        else:
            return

        self.run()


def test1():
    print("Test 1: ")

    with open("inputs/input02.txt", "r") as f:
        memory = [int(x) for x in f.readline().split(',')]
        memory[1] = 12
        memory[2] = 2

        computer = Computer(memory)
        computer.run()
        print(memory[0])


def test2():
    print("Test 2: ")

    with open("inputs/input02.txt", "r") as f:
        initial_memory = [int(x) for x in f.readline().split(',')]

        for noun, verb in itertools.product(range(100), range(100)):
            memory = initial_memory.copy()
            memory[1] = noun
            memory[2] = verb
            computer = Computer(memory)
            computer.run()

            if computer.memory[0] == 19690720:
                print(100 * noun + verb)


if __name__ == "__main__":
    test1()
    test2()
