from math import gcd
from collections import defaultdict


def get_asteroids(asteroid_map):
    asteroids = set()

    for y in range(0, len(asteroid_map)):
        for x in range(0, len(asteroid_map[y])):
            if asteroid_map[y][x] == '#':
                asteroids.add((x, y))
    
    return asteroids


def get_visible(asteroid, asteroids):
    visible = defaultdict(list)
    for other_asteroid in asteroids:
        if other_asteroid != asteroid:
            dist_x = other_asteroid[0] - asteroid[0]
            dist_y = other_asteroid[1] - asteroid[1]

            visible[(dist_x / gcd(dist_x, dist_y), dist_y / gcd(dist_x, dist_y))].append(gcd(dist_x, dist_y))

    return visible


def best_location(asteroid_map):
    asteroids = get_asteroids(asteroid_map)
    visible_asteroids = {}

    for asteroid in asteroids:
        visible = get_visible(asteroid, asteroids)
        visible_asteroids[asteroid] = len(visible)

    max_asteroid = max(visible_asteroids, key=visible_asteroids.get)

    return (max_asteroid[0],max_asteroid[1], visible_asteroids[max_asteroid])


def test1():
    print("Test 1: ")

    with open("inputs/input10.txt", "r") as f:
        orbit_list = f.read().splitlines()
        print(best_location(orbit_list))


def test2():
    print("Test 2: ")

if __name__ == "__main__":
    test1()
    test2()