import timeit

class Solution:
    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read().strip()
        workflows, ratings = data.split("\n\n")
        workflows = workflows.split("\n")
        ratings = ratings.split("\n")
        return workflows
    
    def parse_workflow(self, workflow):
        name, rules = workflow.split("{")
        rules = rules[:-1].split(",")
        res = []
        last = rules[-1]
        for rule in rules[:-1]:
            condition, next = rule.split(":")
            category = condition[0]
            sign = condition[1]
            value = int(condition[2:])
            res.append((category, sign, value, next))
        res.append(last)
        return name, res 
    
    def parse_workflows(self, workflows):
        res = {}
        for workflow in workflows:
            name, rules = self.parse_workflow(workflow)
            res[name] = rules
        return res
    
    def calculate_combinations(self, constraints):
        res = 1
        for key in constraints:
            res *= (constraints[key][1] - constraints[key][0] + 1)
        return res

    def run(self):
        workflows = self.read_data()
        workflows = self.parse_workflows(workflows)   
        
        def dfs(workflow, constraints):
            if workflow == "A":
                return self.calculate_combinations(constraints)
            
            if workflow == "R":
                return 0

            total = 0
            rules, fb = workflows[workflow][:-1], workflows[workflow][-1]
            # copy constraints
            constraints = dict(constraints)

            for rule in rules:
                category, sign, value, next = rule
                lo, hi = constraints[category]
                if sign == "<":
                    T = (lo, min(hi, value - 1))
                    F = (max(lo, value), hi)
                elif sign == ">":
                    T = (max(lo, value + 1), hi)
                    F = (lo, min(hi, value))
                
                if T[0] <= T[1]:
                    # set a new range in category constraint
                    constraints[category] = T
                    # traverse next branch
                    total += dfs(next, constraints)

                if F[0] <= F[1]:
                    # backtrack to the opposite range
                    constraints[category] = F
                else:
                    break
            
            total += dfs(fb, constraints)
            return total
                
            
        return dfs("in", {key: (1, 4000) for key in "xmas"})
        
        



def main():
    sol = Solution()
    print(f"Part Two: {sol.run()}")
    elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    print(f"Elapsed Time: {elapsed:.3f} ms")

main()