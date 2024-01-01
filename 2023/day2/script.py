
class Solution:
    def clean(self, arr):
        cleaned_arr = [el.replace(':', '').replace(',', '').replace('\n', '') for el in arr if el != '']
        return cleaned_arr

    def part_one(self):
        data = {
            "red": 12,
            "green": 13,
            "blue": 14
        }

        with open('data.txt', 'r') as f:
            total = 0
            for line in f:
                game_rounds = line.split(';')
                game_id = 0
                is_correct = True
                for i in range(len(game_rounds)):
                    tokens = self.clean(game_rounds[i].split(' '))
                    if i == 0:
                        game_id = int(tokens[1])
                        tokens = tokens[2:]
                    
                    j = 0
                    while j < len(tokens):
                        amount = int(tokens[j])
                        color = tokens[j + 1]
                        if amount > data[color]:
                            is_correct = False
                            break
                        j += 2
                
                if is_correct:
                    total += game_id
            return total
        
    def part_two(self):
        with open('data.txt', 'r') as f:
            total = 0
            for line in f:
                game_rounds = line.split(';')
                min_set = {
                    "red": 0,
                    "green": 0,
                    "blue": 0
                }
                for i in range(len(game_rounds)):
                    tokens = self.clean(game_rounds[i].split(' '))
                    if i == 0:
                        tokens = tokens[2:]
                    
                    j = 0
                    while j < len(tokens):
                        amount = int(tokens[j])
                        color = tokens[j + 1]
                        min_set[color] = max(min_set[color], amount)
                        j += 2

                total += (min_set["red"] * min_set["green"] * min_set["blue"])
                
            return total
                    



def main():
    solution = Solution()
    print(solution.part_one())
    print(solution.part_two())

main()
