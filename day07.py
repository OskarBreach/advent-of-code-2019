from itertools import permutations 
from day02 import Computer

def highest_signal(program):
    signals = []

    for signal in permutations(range(0, 5)):
        output = [0]
        computers = []
        for phase in signal:
            computers.append(Computer(program.copy(), [phase]))

        for computer in computers:
            computer.add_input(output)
            computer.run()
            output = computer.get_output()  
        
        signals.append(output[0])

    return max(signals)


def feedback_highest_signal(program):
    signals = []

    for signal in permutations(range(5, 10)):
        output = [0]
        computers = []
        for phase in signal:
            computers.append(Computer(program.copy(), [phase]))

        while(not computers[4].halted):
            for computer in computers:
                computer.add_input(output)
                computer.run()
                output = computer.get_output()  
        
        signals.append(output[0])

    return max(signals)

def test1():
    print("Test 1: ")

    with open("inputs/input07.txt", "r") as f:
        memory = [int(x) for x in f.readline().split(',')]
        print(highest_signal(memory))


def test2():
    print("Test 2: ")

    with open("inputs/input07.txt", "r") as f:
        memory = [int(x) for x in f.readline().split(',')]
        print(feedback_highest_signal(memory))


if __name__ == "__main__":
    test1()
    test2()
