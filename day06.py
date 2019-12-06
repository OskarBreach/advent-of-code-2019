from collections import defaultdict

def sum_orbits(orbits, parent, indirect_orbits = 0):
    return indirect_orbits + sum([sum_orbits(orbits, x, indirect_orbits + 1) for x in orbits[parent]])


def count_orbits(orbit_list):
    orbits = defaultdict(list)

    for orbit in orbit_list:
        parent = orbit.split(')')[0]
        child = orbit.split(')')[1]

        orbits[parent].append(child)
    
    return sum_orbits(orbits, 'COM')


def build_orbits(orbit_parent, body):
    orbits = [body]

    while body != 'COM':
        body = orbit_parent[body]
        orbits.append(body)

    return orbits


def count_transfers(orbit_list):
    orbit_parent = {}

    for orbit in orbit_list:
        parent = orbit.split(')')[0]
        child = orbit.split(')')[1]

        orbit_parent[child] = parent

    your_orbit = build_orbits(orbit_parent, 'YOU')
    santas_orbit = build_orbits(orbit_parent, 'SAN')

    return len(set(your_orbit) ^ set(santas_orbit)) - 2

def test1():
    print("Test 1: ")

    with open("inputs/input06.txt", "r") as f:
        orbit_list = f.read().splitlines()
        print(count_orbits(orbit_list))


def test2():
    print("Test 2: ")

    with open("inputs/input06.txt", "r") as f:
        orbit_list = f.read().splitlines()
        print(count_transfers(orbit_list))

if __name__ == "__main__":
    test1()
    test2()
