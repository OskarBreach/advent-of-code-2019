def fuel_required(mass):
    return mass // 3 - 2


def total_fuel_required(mass):
    fuel = fuel_required(mass)
    total_fuel = 0

    while fuel_required(fuel) > 0:
        total_fuel += fuel
        fuel = fuel_required(fuel)

    total_fuel += fuel

    return total_fuel


def test1():
    print("Test 1: ")

    with open("inputs/input01.txt", "r") as f:
        masses = f.readlines()
        total_fuel = 0
        for mass in masses:
            total_fuel += fuel_required(int(mass))

        print(total_fuel)


def test2():
    print("Test 2: ")

    with open("inputs/input01.txt", "r") as f:
        masses = f.readlines()
        total_fuel = 0
        for mass in masses:
            total_fuel += total_fuel_required(int(mass))

        print(total_fuel)


if __name__ == "__main__":
    test1()
    test2()
