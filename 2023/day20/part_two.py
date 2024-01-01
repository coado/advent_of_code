from abc import abstractmethod
from collections import deque
import math
import timeit


class Module:
    def __init__(self, next, name, type):
        self.next = next
        self.name = name
        self.type = type
    
    @abstractmethod
    def process_signal(self, signal, from_module=None):
        pass

class Broadcaster(Module):
    def __init__(self, next, name, type):
        super().__init__(next, name, type)
    
    def process_signal(self, signal, _=None):
        res = []
        for receiver in self.next:
            res.append((self.name, receiver, signal))
        return res
    
    def __str__(self) -> str:
        return f"broadcaster: {self.next}"
    

class FlipFlop(Module):
    def __init__(self, next, name, type):
        super().__init__(next, name, type)
        self.isOn = False

    def process_signal(self, signal, _=None):
        res = []
        # If high signal, ignore
        if signal:
            return res
        self.isOn = not self.isOn
        for receiver in self.next:
            res.append((self.name, receiver, self.isOn))
        return res
    
    def __str__(self) -> str:
        return f"flipflop: {self.name}, isOn: {self.isOn}, next: {self.next}"

    
class Conjunction(Module):
    def __init__(self, next, name, type):
        super().__init__(next, name, type)
        self.prev = {}
    
    def process_signal(self, signal, from_module):
        self.prev[from_module] = signal
        states = list(self.prev.values())
        areHigh = all(states)
        new_signal = not areHigh

        res = []
        for receiver in self.next:
            res.append((self.name, receiver, new_signal))
        return res
    
    def __str__(self) -> str:
        return f"conjunction: {self.name}, prev: {self.prev}, next: {self.next}"


class Output(Module):
    def __init__(self, next, name, type):
        super().__init__(next, name, type)
        self.isOn = True
    
    def process_signal(self, signal, _=None):
        self.isOn = signal
        return []
    
    def __str__(self) -> str:
        return f"output: {self.name}, isOn: {self.isOn}, next: {self.next}"


class Solution:
    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read().strip().split("\n")
        
        res = []
        for line in data:
            conf, connected = line.split("->")
            conf = conf.strip()
            connected = connected.strip().split(", ")
            res.append((conf, connected))
        return res

    def create_modules(self, modules):
        res = {}
        
        conjunctions = set()
        connections = {}

        for conf, connected in modules:
            type = conf[0].strip() if conf != "broadcaster" else conf
            name = conf[1:].strip() if conf != "broadcaster" else conf
            
            if type == "%":
                module = FlipFlop(connected, name, type)
            elif type == "&":
                module = Conjunction(connected, name, type)
                conjunctions.add(name)
            elif type == "broadcaster":
                module = Broadcaster(connected, name, type)
            else:
                raise Exception("Unknown type")

            connections[name] = connected

            res[name] = module  
    

        # Connect conjunctions
        for from_module, to_modules in connections.items():
            for to_module in to_modules:
                if to_module in conjunctions:
                    res[to_module].prev[from_module] = False

        res["rx"] = Output([], "rx", "output")
        return res
    
    def run(self):
        data = self.read_data()
        schema = self.create_modules(data)

        (feed, ) = [name for name, module in schema.items() if "rx" in module.next]
        cycles = { name: None for name, module in schema.items() if feed in module.next }

        queue = deque([])
        presses = 0

        while schema["rx"].isOn:
            queue.append(("button", "broadcaster", False))
            presses += 1

            while queue:
                from_module, to_module, signal = queue.popleft()

                if to_module == feed and signal and cycles[from_module] is None:
                    cycles[from_module] = presses

                if all(cycles.values()):
                    x = 1
                    for cycle in cycles.values():
                        x = x * cycle // math.gcd(x, cycle)
                    return x

                module = schema[to_module]
                res = module.process_signal(signal, from_module)
                res = reversed(res)
                for from_module, to_module, signal in res:
                    queue.append((from_module, to_module, signal))

        return -1



def main():
    sol = Solution()
    print(f"Part Two: {sol.run()}")
    elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    print(f"Elapsed Time: {elapsed:.3f} ms")

main()