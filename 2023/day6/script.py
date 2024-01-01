import timeit
import math

class Solution:

    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read()
        return data

    def part_one(self):
        data = self.read_data().split("\n")
        time = [int(i) for i in data[0].split(": ")[1].split(" ") if i != ""]
        distance = [int(i) for i in data[1].split(": ")[1].split(" ") if i != ""]

        res = 1

        for i in range(len(time)):
            race_time = time[i]
            race_distance = distance[i]

            # y = x^2 - race_time * x + race_distance
            a = 1
            b = -race_time
            c = race_distance

            # x = (-b +- sqrt(b^2 - 4ac)) / 2a
            x1 = math.ceil((-b - (b**2 - 4*a*c)**0.5) / (2*a))
            x2 = math.floor((-b + (b**2 - 4*a*c)**0.5) / (2*a))

            res *= (x2 - x1 + 1)

        return res 
    
    def part_two(self):
        data = self.read_data().split("\n")
        time = int(''.join([i for i in data[0].split(": ")[1].split(" ") if i != ""]))
        distance = int(''.join([i for i in data[1].split(": ")[1].split(" ") if i != ""]))
        

        # y = x^2 - race_time * x + race_distance
        a = 1
        b = -time
        c = distance

        # x = (-b +- sqrt(b^2 - 4ac)) / 2a
        x1 = math.ceil((-b - (b**2 - 4*a*c)**0.5) / (2*a))
        x2 = math.floor((-b + (b**2 - 4*a*c)**0.5) / (2*a))
        res = (x2 - x1 + 1)
        return res

def main():
    sol = Solution()
    print(f"Part one: {sol.part_one()}")
    time_part_one = (timeit.timeit(sol.part_one, number=10) / 10) * 1000
    print(f"Elapsed Time: {time_part_one:.3f} ms")
    print(sol.part_two())
    time_part_two = (timeit.timeit(sol.part_two, number=10) / 10) * 1000
    print(f"Elapsed Time: {time_part_two:.3f} ms")

main()
