
class Solution:
    def part_one(self):
        res = 0
        with open('data.txt', 'r') as f:
            for line in f:
                first_digit, last_digit = -1, -1
                for char in line.strip():
                    if char.isdigit():
                        if first_digit == -1:
                            first_digit = int(char)
                        last_digit = int(char)

                res += (first_digit * 10) + last_digit    
        return res
    
    def part_two(self):
        res = 0
        words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

        with open('data.txt', 'r') as f:
            for line in f:
                first_digit, last_digit = -1, -1
                line = line.strip()
                for i in range(len(line)):
                    if line[i].isdigit():
                        if first_digit == -1:
                            first_digit = int(line[i])
                        last_digit = int(line[i])
                    else:
                        for w in range(len(words)):
                            word_length = len(words[w]) - 1
                            if i - word_length >= 0 and line[i - word_length:i+1] == words[w]:
                                if first_digit == -1:
                                    first_digit = w + 1
                                last_digit = w + 1
                res += (first_digit * 10) + last_digit  
        return res

def main():
    solution = Solution()
    print('part one: ', solution.part_one())
    print('part two: ', solution.part_two())

        

main()
            
