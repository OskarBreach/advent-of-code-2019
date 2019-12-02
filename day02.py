import itertools


def add(memory, instruction_pointer):
    memory[memory[instruction_pointer + 3]] \
            = memory[memory[instruction_pointer + 1]] + memory[memory[instruction_pointer + 2]]

    return instruction_pointer + 4


def multiply(memory, instruction_pointer):
    memory[memory[instruction_pointer + 3]] \
            = memory[memory[instruction_pointer + 1]] * memory[memory[instruction_pointer + 2]]

    return instruction_pointer + 4


def run_program(memory, instruction_pointer=0):
    instruction = memory[instruction_pointer]

    if instruction == 1:
        instruction_pointer = add(memory, instruction_pointer)
    elif instruction == 2:
        instruction_pointer = multiply(memory, instruction_pointer)
    elif instruction == 99:
        return
    else:
        return

    run_program(memory, instruction_pointer)


def test1():
    print("Test 1: ")

    with open("inputs/input02.txt", "r") as f:
        memory = [int(x) for x in f.readline().split(',')]
        memory[1] = 12
        memory[2] = 2

        run_program(memory)
        print(memory[0])


def test2():
    print("Test 2: ")

    with open("inputs/input02.txt", "r") as f:
        initial_memory = [int(x) for x in f.readline().split(',')]

        for noun, verb in itertools.product(range(100), range(100)):
            memory = initial_memory.copy()
            memory[1] = noun
            memory[2] = verb
            run_program(memory)

            if memory[0] == 19690720:
                print(100 * noun + verb)


if __name__ == "__main__":
    test1()
    test2()
