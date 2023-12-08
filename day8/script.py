from collections import deque
import timeit


class Solution:
    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read()
        return data
    
    def gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x

    def lcm(self, x, y):
        return x * y // self.gcd(x, y)


    def part_one(self):
        data = self.read_data().split("\n")
        commands = data[0]
        states = data[2:]
        state_machine = {}
        
        for i in range(len(states)):
            from_state, to_states = states[i].split("=")
            from_state = from_state.strip()
            
            to_left, to_right = [x.replace("(", "").replace(")", "").strip() for x in to_states.split(",")]
            state_machine[from_state] = (to_left, to_right)
        
        
        cur_state = "AAA"
        i = 0
        counter = 0
        while cur_state != "ZZZ":
            left, right = state_machine[cur_state]
            if commands[i] == "L":
                cur_state = left
            else:
                cur_state = right

            
            counter += 1
            i = i + 1 if i < len(commands) - 1 else 0

        return counter
    
    def part_two(self):
        data = self.read_data().split("\n")
        commands = data[0]
        states = data[2:]
        state_machine = {}
        start_states = []

        
        for i in range(len(states)):
            from_state, to_states = states[i].split("=")
            from_state = from_state.strip()
            
            to_left, to_right = [x.replace("(", "").replace(")", "").strip() for x in to_states.split(",")]
            state_machine[from_state] = (to_left, to_right)

            if from_state[-1] == "A":
                start_states.append(from_state)

        distances = []

        for start_state in start_states:
            cur = start_state
            i = 0
            distance = 0
            while cur[-1] != "Z":
                left, right = state_machine[cur]
                cur = left if commands[i] == "L" else right
                distance += 1
                i = i + 1 if i < len(commands) - 1 else 0

            distances.append(distance)

        res = 1
        for distance in distances:
            res = self.lcm(res, distance)

        return res


def main():
    sol = Solution()
    print(f"Part one: {sol.part_one()}")
    time_part_one = (timeit.timeit(sol.part_one, number=10) / 10) * 1000
    print(f"Elapsed Time: {time_part_one:.3f} ms")
    print(f"Part two: {sol.part_two()}")
    time_part_two = (timeit.timeit(sol.part_two, number=10) / 10) * 1000
    print(f"Elapsed Time: {time_part_two:.3f} ms")

main()