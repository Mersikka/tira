class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"


def find_levels(node):
    level_list = []
    find_levels_helper(node, level_list, 0)
    return level_list


def find_levels_helper(node, level_list, depth):
    if depth == len(level_list):
        level_list.append([node.value])
    else:
        level_list[depth].append(node.value)
        level_list[depth].sort()
    for child in node.children:
        find_levels_helper(child, level_list, depth + 1)


if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]), Node(5), Node(2, [Node(6)])])
    print(find_levels(tree1))  # [[1], [2, 4, 5], [3, 6, 7]]

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_levels(tree2))  # [[1], [2], [3], [4]]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_levels(tree3))  # [[1], [2, 3, 4]]
