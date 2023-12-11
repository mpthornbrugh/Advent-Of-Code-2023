import math
from inputs import *


class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.name} -> {self.left.name if self.left else None}, {self.right.name if self.right else None}"


def get_to_end(start_node, end_node, pattern):
    node = start_node
    steps = 0
    pattern_index = 0
    while node != end_node:
        direction = pattern[pattern_index]
        if direction == "L":
            node = node.left
        elif direction == "R":
            node = node.right
        steps += 1
        pattern_index += 1
        if pattern_index >= len(pattern):
            pattern_index = 0
    return steps


def get_to_combined_end(start_nodes, pattern):
    steps = 0
    pattern_index = 0
    successes = {}
    for i in range(len(start_nodes)):
        successes[i] = []
    broke_out_early = False
    while len(start_nodes) > 0:
        direction = pattern[pattern_index]
        new_start_nodes = []
        found_end = True
        for node_num, node in enumerate(start_nodes):
            if direction == "L":
                next_node = node.left
            else:
                next_node = node.right
            if not next_node.name.endswith("Z"):
                found_end = False
            else:
                successes[node_num].append(steps)
            new_start_nodes.append(next_node)
        start_nodes = new_start_nodes
        steps += 1
        pattern_index += 1
        if pattern_index >= len(pattern):
            pattern_index = 0
        if found_end:
            break
        need_to_break = True
        for node_num, node in enumerate(start_nodes):
            if len(successes[node_num]) < 2:
                need_to_break = False
                break
        if need_to_break:
            broke_out_early = True
            break
    if broke_out_early:
        iterations_to_end = []
        for node_num, node in enumerate(start_nodes):
            iterations_to_end.append(successes[node_num][1] - successes[node_num][0])
        # Find the LCM of the iterations to end
        return math.lcm(*iterations_to_end)
    return steps


def calculate(input_string):
    lines = input_string.split("\n")
    pattern = [*lines[0]]
    node_blob = lines[2:]
    start_node = None
    end_node = None
    nodes = {}
    starting_nodes = []
    for node_line in node_blob:
        name, directions = node_line.split(" = ")
        if name in nodes:
            node = nodes[name]
        else:
            node = Node(name)
            nodes[name] = node
        left, right = directions.replace("(", "").replace(")", "").split(", ")
        if left in nodes:
            left_node = nodes[left]
        else:
            left_node = Node(left)
            nodes[left] = left_node
        node.left = left_node
        if right in nodes:
            right_node = nodes[right]
        else:
            right_node = Node(right)
            nodes[right] = right_node
        node.right = right_node
        if name == "AAA":
            start_node = node
        elif name == "ZZZ":
            end_node = node
        if name.endswith("A"):
            starting_nodes.append(node)
    # Part 1
    # steps = get_to_end(start_node, end_node, pattern)
    # Part 2
    steps = get_to_combined_end(starting_nodes, pattern)
    print(steps)


if __name__ == "__main__":
    # calculate(example_input_3)
    calculate(puzzle_input)
