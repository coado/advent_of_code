import timeit


class Solution:

    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read()
        return data

    def part_one(self):
        data = self.read_data().split("\n")
        time = [int(i) for i in data[0].split(": ")[1].split(" ") if i != ""]
        distance = [int(i) for i in data[1].split(": ")[1].split(" ") if i != ""]

        def race_fun(time):
            return lambda hold_time: hold_time * (time - hold_time)

        res = 1

        for i in range(len(time)):
            f = race_fun(time[i])
            counter = 0
            for j in range(1, time[i] + 1):
                if f(j) > distance[i]:
                    counter = time[i] - 2*j + 1
                    break
            res *= counter  

        return res 
    
    def part_two(self):
        data = self.read_data().split("\n")
        time = int(''.join([i for i in data[0].split(": ")[1].split(" ") if i != ""]))
        distance = int(''.join([i for i in data[1].split(": ")[1].split(" ") if i != ""]))

        def race_fun(time):
            return lambda hold_time: hold_time * (time - hold_time)
        f = race_fun(time)

        for j in range(1, time + 1):
            if f(j) > distance:
                return time - 2*j + 1

def main():
    sol = Solution()
    print(f"Part one: {sol.part_one()}")
    time_part_one = (timeit.timeit(sol.part_one, number=10) / 10) * 1000
    print(f"Elapsed Time: {time_part_one:.3f} ms")
    print(sol.part_two())

main()




# class Solution:

#     def read_data(self):
#         with open("data.txt", "r") as f:
#             data = f.read()
#         return data

#     def part_one(self):
#         data = self.read_data().split("\n")
#         time = [int(i) for i in data[0].split(": ")[1].split(" ") if i != ""]
#         distance = [int(i) for i in data[1].split(": ")[1].split(" ") if i != ""]
#         print(time, distance)

#         def race_fun(time):
#             return lambda hold_time: hold_time * (time - hold_time)

#         res = 1

#         for i in range(len(time)):
#             f = race_fun(time[i])
#             counter = 0
#             for j in range(1, time[i] + 1):
#                 if f(j) > distance[i]:
#                     counter = time[i] - 2*j + 1
#                     print(j)
#                     break
#             print(counter, time[i])
#             res *= counter  

#         return res 
    
# def main():
#     sol = Solution()
#     print(sol.part_one())
#     # print(sol.part_two())

# main()