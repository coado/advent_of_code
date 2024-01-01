import timeit


class Solution:

    def __init__(self):
        self.directions = {
            "R": (1, 0),
            "L": (-1, 0),
            "U": (0, -1),
            "D": (0, 1)
        }

    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read().strip()
        
        data = data.split("\n")
        res = []
        for line in data:
            tokens = line.split(" ")
            tokens[1] = int(tokens[1])
            tokens[2] = tokens[2][1:-1]
            res.append(tokens)
        return res
    
    def run(self):
        data = self.read_data()

        points = [(0, 0)]
        b = 0
        for dir, n, _ in data:
            dx, dy = self.directions[dir]
            x, y = points[-1]
            b += n
            points.append((x + dx * n, y + dy * n))

        area_sum = 0
        for i in range(len(points)):
            area_i = points[i][1] * (points[i-1][0] - points[(i+1) % len(points)][0])
            area_sum += area_i

        A = abs(area_sum) // 2
        i = A - b // 2 + 1
        return i + b
            

def main():
    sol = Solution()
    print(f"Part One: {sol.run()}")
    elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    print(f"Elapsed Time: {elapsed:.3f} ms")

main()