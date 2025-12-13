import heapq

class Tasks:
    def __init__(self):
        self.prios_tasks = {}
        self.prios = []

    def add_task(self, name, priority):
        if priority not in self.prios_tasks:
            self.prios_tasks[priority] = []
        heapq.heappush(self.prios_tasks[priority], name)
        heapq.heappush(self.prios, -priority)

    def fetch_task(self):
        res = heapq.heappop(self.prios_tasks[abs(heapq.heappop(self.prios))])
        return res

if __name__ == "__main__":
    tasks = Tasks()

    tasks.add_task("siivous", 20)
    tasks.add_task("koodaus", 90)
    tasks.add_task("treffit", 80)

    print(tasks.fetch_task()) # koodaus

    tasks.add_task("nukkuminen", 20)

    print(tasks.fetch_task()) # treffit
    print(tasks.fetch_task()) # nukkuminen
