import timeit

class Solution:


    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read().strip()
        workflows, ratings = data.split("\n\n")
        workflows = workflows.split("\n")
        ratings = ratings.split("\n")
        return workflows, ratings
    
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
    
    def parse_rating(self, rating):
        rating = rating[1:-1].split(",")
        res = {}
        for i in range(len(rating)):
            key, value = rating[i].split("=")
            res[key] = int(value)
        return res

    def parse_ratings(self, ratings):
        return [self.parse_rating(rating) for rating in ratings]
    
    def compare(self, rating, thr, sign):
        if sign == ">":
            return rating > thr
        elif sign == "<":
            return rating < thr
        elif sign == "=":
            return rating == thr
        elif sign == ">=":
            return rating >= thr
        elif sign == "<=":
            return rating <= thr
        else:
            return False
        
    def run_workflow(self, workflow, rating):
        for i in range(len(workflow) - 1):
            category, sign, value, next = workflow[i]
            if self.compare(rating[category], value, sign):
                return next
        
        return workflow[-1]

    def run(self):
        workflows, ratings = self.read_data()
        workflows = self.parse_workflows(workflows)   
        ratings = self.parse_ratings(ratings)
        
        res = 0

        for rating in ratings:
            workflow = workflows["in"]
            is_accepted = False
            is_rejected = False

            while not is_accepted and not is_rejected:
                worklow_res = self.run_workflow(workflow, rating)
                
                if worklow_res == "R":
                    is_rejected = True
                elif worklow_res == "A":
                    is_accepted = True
                else:
                    workflow = workflows[worklow_res]

            if is_accepted:
                for value in rating.values():
                    res += value

        return res

        

def main():
    sol = Solution()
    print(f"Part One: {sol.run()}")
    elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    print(f"Elapsed Time: {elapsed:.3f} ms")

main()