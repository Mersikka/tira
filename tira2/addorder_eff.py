from random import shuffle

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.max_depth = -1

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            self.max_depth = 0
            return

        curr_h = 0
        node = self.root
        while True:
            if node.value == value:
                return
            curr_h += 1
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    self.max_depth = max(self.max_depth, curr_h)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    self.max_depth = max(self.max_depth, curr_h)
                    return
                node = node.right

    def height(self):
        return self.max_depth

nums = range(1, 1001)

numtree = TreeSet()
for i in nums:
    numtree.add(i)
print(f"Pienimmästä suurimpaan populoituna puun korkeus on {numtree.height()}")

nums = list(nums)
shuffle(nums)
numtree = TreeSet()
for i in nums:
    numtree.add(i)
print(f"Satunnaisessa järjestyksessä populoituna korkeus on {numtree.height()}")
