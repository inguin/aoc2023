#! /usr/bin/python

import sys, re

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)
LEFT = { NORTH: WEST, EAST: NORTH, SOUTH: EAST, WEST: SOUTH }
RIGHT = { NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH }

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

grid = []
with open(filename) as f:
    for line in f:
        grid.append([ int(c) for c in line.strip() ])

height = len(grid)
width = len(grid[0])

unvisited = {}

for row in range(height):
    for col in range(width):
        for heading in (NORTH, EAST, SOUTH, WEST):
            for limit in (6, 5, 4, 3, 2, 1, 0):
                unvisited[(row, col, heading, limit)] = 99999999

unvisited[(0, 4, EAST, 6)] = grid[0][1] + grid[0][2] + grid[0][3] + grid[0][4]
unvisited[(4, 0, SOUTH, 6)] = grid[1][0] + grid[2][0] + grid[3][0] + grid[4][0]

unvisited_by_cost = {}
for node, cost in unvisited.items():
    if cost not in unvisited_by_cost:
        unvisited_by_cost[cost] = []
    unvisited_by_cost[cost].append(node)

while True:
    print(len(unvisited))
    nearest_node = None
    min_cost = min(unvisited_by_cost.keys())
    nearest_node = unvisited_by_cost[min_cost].pop()
    if not unvisited_by_cost[min_cost]:
        del unvisited_by_cost[min_cost]
    del unvisited[nearest_node]

    (row, col, heading, limit) = nearest_node
    if row == height - 1 and col == width - 1:
        print(min_cost)
        break

    next_nodes = [
        (row + 4*LEFT[heading][0], col + 4*LEFT[heading][1], LEFT[heading], 6),
        (row + 4*RIGHT[heading][0], col + 4*RIGHT[heading][1], RIGHT[heading], 6)
    ]
    if limit > 0:
        next_nodes.append((row + heading[0], col + heading[1], heading, limit - 1))

    for next_node in next_nodes:
        if next_node in unvisited:
            node_cost = unvisited[next_node]
            next_cost = min_cost + grid[next_node[0]][next_node[1]]
            if next_node[2] != heading:
                next_cost += grid[row + next_node[2][0]][col + next_node[2][1]] + \
                             grid[row + 2*next_node[2][0]][col + 2*next_node[2][1]] + \
                             grid[row + 3*next_node[2][0]][col + 3*next_node[2][1]]
            if next_cost < node_cost:
                unvisited_by_cost[node_cost].remove(next_node)
                if not unvisited_by_cost[node_cost]:
                    del unvisited_by_cost[node_cost]

                unvisited[next_node] = next_cost

                if next_cost not in unvisited_by_cost:
                    unvisited_by_cost[next_cost] = []
                unvisited_by_cost[next_cost].append(next_node)
