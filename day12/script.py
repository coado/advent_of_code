import timeit
import re

class Solution:
    def __init__(self):
        self.cache = {}

    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read()
        return data
    
    def is_spring_correct(self, spring, damaged):
        springs_count = list(map(lambda x: len(x), [i for i in spring.split(".") if i != ""]))
        return springs_count == damaged

    def is_partial_spring_correct(self, spring, damaged):
        springs_count = list(map(lambda x: len(x), [i for i in spring.split(".") if i != ""]))
        damaged_group = damaged[:len(springs_count)]

        if not springs_count:
            # There is nothing to check
            return True



        print(spring, springs_count, damaged_group)
        print([i for i in spring.split(".") if i != ""])


    def combinations(self, springs, groups, i=0):
        if (i, str(groups), springs) in self.cache:
            return self.cache[(i, str(groups), springs)]
        
        if i >= len(springs):
            # Return 1 if there is no groups left
            return 1 if len(groups) == 0 else 0
        
        if not groups:
            slice = springs[i:]
            # Check if it doesn't contain any #
            if '#' not in slice:
                return 1
            return 0
            
        
        if springs[i] == '.':
            return self.combinations(springs, groups, i+1)
        
        results = 0
        if springs[i] == '?':
            # We assume that ? might be a .
            results += self.combinations(springs, groups, i+1)

        cur_group = groups[0]

        if i + cur_group > len(springs):
            self.cache[(i, str(groups), springs)] = results
            # We can't take this group
            return results
        
        slice = springs[i:i+cur_group]

        are_all_springs_broken = re.match(r'^[#?]+$', slice)
        is_group_closed = (i + cur_group == len(springs)) or (springs[i+cur_group] in ['.', '?'])

        if are_all_springs_broken and is_group_closed:
            # We can take this group
            results += self.combinations(springs, groups[1:], i+cur_group+1)

        self.cache[(i, str(groups), springs)] = results
        return results



    def part_one(self):
        data = self.read_data().split("\n")

        for i in range(len(data)):
            row = data[i].split(" ")
            row[1] = list(map(int, row[1].split(",")))
            data[i] = row
            

        res = 0
        for row in data:
            springs = row[0]
            damaged = row[1]
            res += self.combinations(springs, damaged)

        return res

    def part_two(self):
        data = self.read_data().split("\n")
        for i in range(len(data)):
            row = data[i].split(" ")
            row[1] = list(map(int, row[1].split(","))) * 5
            row[0] = "?".join([row[0]] * 5)
            data[i] = row

        res = 0
        for i, row in enumerate(data):
            springs = row[0]
            damaged = row[1]
            res += self.combinations(springs, damaged)

        return res


def main():
    sol = Solution()
    # print(f"Part one: {sol.part_one()}")
    # time_part_one = (timeit.timeit(sol.part_one, number=10) / 10) * 1000
    # print(f"Elapsed Time: {time_part_one:.3f} ms")
    print(f"Part two: {sol.part_two()}")
    # time_part_two = (timeit.timeit(sol.part_two, number=10) / 10) * 1000
    # print(f"Elapsed Time: {time_part_two:.3f} ms")
    # sol.is_partial_spring_correct("..#......##.", [1, 2, 1, 2])

main()