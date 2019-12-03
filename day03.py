def wire_locations(wire):
    locations = {}
    current_location = (0,0)
    distance = 0

    for segment in wire:
        if segment[0] == 'U':
            direction = (0, 1)
        elif segment[0] == 'R':
            direction = (1, 0)
        elif segment[0] == 'D':
            direction = (0, -1)
        elif segment[0] == 'L':
            direction = (-1, 0)

        for _ in range(int(segment[1:])):
            current_location = (current_location[0] + direction[0], current_location[1] + direction[1])
            distance = distance + 1
            if current_location not in locations:
                locations[current_location] = distance

    return locations


def closest_intersection(wire_a, wire_b):
    wire_a_locations = wire_locations(wire_a)
    wire_b_locations = wire_locations(wire_b)

    intersections = wire_a_locations.keys() & wire_b_locations.keys()
    
    closest = min(intersections, key=lambda t: abs(t[0]) + abs(t[1]))

    return abs(closest[0]) + abs(closest[1])

def fewest_steps(wire_a, wire_b):
    wire_a_locations = wire_locations(wire_a)
    wire_b_locations = wire_locations(wire_b)

    intersections = wire_a_locations.keys() & wire_b_locations.keys()
    distances = []
    for intersection in intersections:
        distances.append(wire_a_locations[intersection] + wire_b_locations[intersection])

    return min(distances)

def test1():
    print("Test 1: ")

    with open("inputs/input03.txt", "r") as f:
        wire_a = f.readline().split(',')
        wire_b = f.readline().split(',')

        print(closest_intersection(wire_a, wire_b))


def test2():
    print("Test 1: ")

    with open("inputs/input03.txt", "r") as f:
        wire_a = f.readline().split(',')
        wire_b = f.readline().split(',')

        print(fewest_steps(wire_a, wire_b))


if __name__ == "__main__":
    test1()
    test2()