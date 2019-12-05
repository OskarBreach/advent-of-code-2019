import itertools

class Computer:
    def __init__(self, memory, inputs = []):
        self.memory = memory
        self.ip = 0
        self.output = []
        self.inputs = inputs

    def run(self):
        instruction = self.memory[self.ip] % 100
        max_params_required = 2
        parameters = str(self.memory[self.ip] // 100).zfill(max_params_required)[::-1]

        if instruction == 1: # add
            a = self.memory[self.ip + 1] if parameters[0] == '1' else self.memory[self.memory[self.ip + 1]]
            b = self.memory[self.ip + 2] if parameters[1] == '1' else self.memory[self.memory[self.ip + 2]]
            pos = self.memory[self.ip + 3]

            self.memory[pos] = a + b
            self.ip += 4
        elif instruction == 2: # multiply
            a = self.memory[self.ip + 1] if parameters[0] == '1' else self.memory[self.memory[self.ip + 1]]
            b = self.memory[self.ip + 2] if parameters[1] == '1' else self.memory[self.memory[self.ip + 2]]
            pos = self.memory[self.ip + 3]

            self.memory[pos] = a * b
            self.ip += 4        
        elif instruction == 3: # input
            pos = self.memory[self.ip + 1]

            self.memory[pos] = self.inputs.pop(0)
            self.ip += 2
        elif instruction == 4: # output
            a = self.memory[self.ip + 1] if parameters[0] == '1' else self.memory[self.memory[self.ip + 1]]

            self.output.append(a)
            self.ip += 2
        elif instruction == 99: # halt
            return
        else: # error
            return

        self.run()

    def get_output(self):
        return self.output


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
