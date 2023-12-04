import timeit

class Solution:
    def get_data(self):
        winning_cards = []
        cards = []
        with open('data.txt', 'r') as f:
                for line in f:
                    tokens = line.split('|')
                    winning_cards.append([int(i) for i in tokens[0].split(':')[1].split(' ') if i != ''])
                    cards.append([int(i) for i in tokens[1].split(' ') if i != ''])
        return cards, winning_cards
                    

    def part_one(self):
        with open('data.txt', 'r') as f:
            total = 0
            for line in f:
                tokens = line.split('|')
                winning_cards = set([int(i) for i in tokens[0].split(':')[1].split(' ') if i != ''])
                cards = [int(i) for i in tokens[1].split(' ') if i != '']
                score = 0
                for card in cards:
                    if card in winning_cards:
                        score = max(1, score * 2)
                
                total += score
            return total
                                
    def part_two(self):
        cards, winning_cards = self.get_data()
        stack = [1] * len(cards)
        cache = {}

        for i in range(len(stack)):
            for _ in range(stack[i]):
                score = 0

                if i in cache:
                    score = cache[i]
                else:
                    cur_cards = cards[i]
                    cur_winning_cards = set(winning_cards[i])
        
                    for card in cur_cards:
                        if card in cur_winning_cards:
                            score += 1
                    cache[i] = score

                for k in range(1, score + 1):
                    stack[i + k] += 1

        result = sum(stack)
        return result

            

def main():
    solution = Solution()
    print(solution.part_one())
    time_part_two = timeit.timeit(solution.part_two, number=10)
    print(f"Time taken: {time_part_two} seconds")

main()