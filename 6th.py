import itertools

def total_distance(route, distances):
    distance = 0
    for i in range(len(route)-1):
        distance += distances[route[i]][route[i+1]]
    distance += distances[route[-1]][route[0]]
    return distance

def tsp_bruteforce(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    shortest_route = None
    shortest_distance = float('inf')

    for route in itertools.permutations(cities):
        distance = total_distance(route, distances)
        if distance<shortest_distance:
            shortest_distance = distance
            shortest_route = route

    return shortest_route, shortest_distance

distances = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]

shortest_route, shortest_distance = tsp_bruteforce(distances)
print("Shortest Route:", shortest_route)
print("Shortest Distance:", shortest_distance)
