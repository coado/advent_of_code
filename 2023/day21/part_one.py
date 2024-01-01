import timeit
from collections import deque

class Solution:
    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read().strip().split("\n")
        # return [i.split("") for i in data]
        return [list(i) for i in data]
    
    def parse_data(self, data):
        ROWS, COLS = len(data), len(data[0])
        points = {}
        start = (0, 0)

        for y in range(ROWS):
            for x in range(COLS):
                points[(x, y)] = data[y][x]

                if data[y][x] == "S":
                    start = (x, y)
        
        return points, (ROWS, COLS), start


    # def run(self):
    #     data = self.read_data()
    #     points, sizes, start = self.parse_data(data)
    #     ROWS, COLS = sizes

    #     queue = [start]
    #     d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    #     for _ in range(64):
    #         temp = set()
    #         while queue:
    #             x, y = queue.pop()

    #             for dx, dy in d:
    #                 new_x, new_y = x + dx, y + dy
    #                 if (
    #                     new_x not in range(COLS) or 
    #                     new_y not in range(ROWS) or
    #                     (new_x, new_y) in temp or
    #                     points[(new_x, new_y)] == "#"
    #                 ):
    #                     continue

    #                 temp.add((new_x, new_y))

    #         queue = list(temp)
        

    #     dests = set(queue)
    #     grid = ''
    #     for y in range(ROWS):
    #         for x in range(COLS):
    #             if (x, y) in dests:
    #                 grid += 'O'
    #             else:
    #                 grid += points[(x, y)]
    #         grid += '\n'

    #     print(grid)

    #     return len(queue)


    def run(self):
        data = self.read_data()
        points, sizes, start = self.parse_data(data)
        ROWS, COLS = sizes

        xs, ys = start
        res = set()
        visited = {(xs, ys)}
        
        queue = deque([(xs, ys, 64)])

        while queue:
            x, y, steps  = queue.popleft()

            if steps % 2 == 0:
                res.add((x, y))
            elif steps == 0:
                continue
            

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= COLS or ny < 0 or ny >= ROWS or points[(nx, ny)] == "#" or (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                queue.append((nx, ny, steps - 1))

        print(res)
        return len(res)


def main():
    sol = Solution()
    print(f"Part One: {sol.run()}")
    # elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    # print(f"Elapsed Time: {elapsed:.3f} ms")

main()