
class Ball:
    def __init__(self, n):
        self.n = n
        self.nodes = []
        for i in range(self.n+1):
            self.nodes.append((i, 0))
            self.nodes.append((i, 1))
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0

        for i in range(self.n+1):
            self.add_pair((0, 0), (i, 0), helper=True)
            self.add_pair((i, 1), (0, 1), helper=True)
        self.add_pair((0, 0), (self.n, 0), helper=True)
        self.add_pair((self.n, 1), (0, 1), helper=True)

    def add_pair(self, a, b, helper=False):
        if helper:
            self.graph[(a, b)] = 1
        else:
            self.graph[((a, 0), (b, 1))] = 1

    def add_flow(self, node, sink, flow):
        if node in self.seen:
            return 0
        self.seen.add(node)
        if node == sink:
            return flow
        for next_node in self.nodes:
            if self.flow[(node, next_node)] > 0:
                new_flow = min(flow, self.flow[(node, next_node)])
                inc = self.add_flow(next_node, sink, new_flow)
                if inc > 0:
                    self.flow[(node, next_node)] -= inc
                    self.flow[(next_node, node)] += inc
                    return inc
        return 0                

    def max_pairs(self):
        source = (0, 0)
        sink = (0, 1)
        self.flow = self.graph.copy()
        total = 0
        while True:
            self.seen = set()
            add = self.add_flow(source, sink, float("inf"))
            if add == 0:
                break
            total += add
        return total

if __name__ == "__main__":
    ball = Ball(4)

    print(ball.max_pairs()) # 0

    ball.add_pair(1, 2)
    print(ball.max_pairs()) # 1

    ball.add_pair(1, 3)
    ball.add_pair(3, 2)
    print(ball.max_pairs()) # 2

    ball.add_pair(2, 1)
    print(ball.max_pairs()) # 3
