import heapq
import copy

class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def calculate_cost(state, goal_state):
    return sum(1 for i in range(len(state)) for j in range(len(state[i])) if state[i][j] != goal_state[i][j])

def generate_neighbors(node, goal_state):
    neighbors = []
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    x, y = next((i, j) for i in range(len(node.state)) for j in range(len(node.state[i])) if node.state[i][j] == 0)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(node.state) and 0 <= ny < len(node.state[0]):
            new_state = copy.deepcopy(node.state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            cost = node.cost + 1 + calculate_cost(new_state, goal_state)
            neighbors.append(Node(new_state, node, cost))
    return neighbors

def print_path(node):
    if node is None:
        return
    print_path(node.parent)
    print_state(node.state)
    print()

def print_state(state):
    for row in state:
        print(*row)
    print()

def solve(initial_state, goal_state):
    pq = [Node(initial_state, None, calculate_cost(initial_state, goal_state))]
    while pq:
        current_node = heapq.heappop(pq)
        if current_node.state == goal_state:
            print("Solution found:")
            print_path(current_node)
            return
        for neighbor in generate_neighbors(current_node, goal_state):
            heapq.heappush(pq, neighbor)

initial_state = [[1, 2, 3],
                 [5, 6, 0],
                 [7, 8, 4]]

goal_state = [[1, 2, 3],
              [5, 8, 6],
              [0, 7, 4]]

solve(initial_state, goal_state)
