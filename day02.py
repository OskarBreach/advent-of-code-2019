import itertools
from collections import defaultdict

class Computer:
    def __init__(self, memory, input = []):
        #self.memory = memory
        self.memory = defaultdict(int)
        for i in range(0, len(memory)):
            self.memory[i] = memory[i]
        self.ip = 0
        self.output = []
        self.input = input
        self.halted = False
        self.relative_base = 0

    def get_arguments(self, num_args, num_writes):
        parameters = list(str(self.memory[self.ip] // 100).zfill(num_args + num_writes)[::-1])

        for x in range(num_args, num_args + num_writes):
            if parameters[x] == '0':
                parameters[x] = '1'

        args = []
        self.ip += 1

        while len(args) < num_args + num_writes:
            args.append(self.memory[self.ip] if parameters[len(args)] == '1' else self.memory[self.relative_base + self.memory[self.ip]] if parameters[len(args)] == '2' else self.memory[self.memory[self.ip]])
            self.ip += 1

        return args

    def run(self):
        instruction = self.memory[self.ip] % 100

        if instruction == 1: # add
            args = self.get_arguments(2, 1)
            self.memory[args[2]] = args[0] + args[1]
        elif instruction == 2: # multiply
            args = self.get_arguments(2, 1)
            self.memory[args[2]] = args[0] * args[1]     
        elif instruction == 3: # input
            if len(self.input) > 0:
                args = self.get_arguments(0, 1)

                self.memory[args[0]] = self.input.pop(0)
            else:
                return
        elif instruction == 4: # output
            args = self.get_arguments(1, 0)

            self.output.append(args[0])
        elif instruction == 5: # jump-if-true
            args = self.get_arguments(2, 0)

            if args[0] != 0:
                self.ip = args[1]
        elif instruction == 6: # jump-if-false
            args = self.get_arguments(2, 0)

            if args[0] == 0:
                self.ip = args[1]
        elif instruction == 7: # less than
            args = self.get_arguments(2, 1)

            self.memory[args[2]] = 1 if args[0] < args[1] else 0
        elif instruction == 8: # equals
            args = self.get_arguments(2, 1)

            self.memory[args[2]] = 1 if args[0] == args[1] else 0
        elif instruction == 9: # adjust relative base
            args = self.get_arguments(1, 0)

            self.relative_base += args[0]
        elif instruction == 99: # halt
            self.halted = True
            return
        else: # error
            return

        self.run()

    def add_input(self, input):
        self.input += input

    def get_output(self):
        ret = self.output
        self.output = []
        return ret

    def get_memory(self):
        return [self.memory[k] for k in self.memory]

def test1():
    print("Test 1: ")

    with open("inputs/input02.txt", "r") as f:
        memory = [int(x) for x in f.readline().split(',')]
        memory[1] = 12
        memory[2] = 2

        computer = Computer(memory)
        computer.run()
        print(computer.get_memory()[0])


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
