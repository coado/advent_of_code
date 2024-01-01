import timeit


class Node:
    def __init__(self, hand, bid, rank, left=None, right=None):
        self.hand = hand
        self.bid = bid
        self.rank = rank
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.cards = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "T": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2,
            "J": 1
        }

        self.ranks = {
            "Five of a kind": 7,
            "Four of a kind": 6,
            "Full house": 5,
            "Three of a kind": 4,
            "Two pair": 3,
            "One pair": 2,
            "Highest card": 1
        }

    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read()
        return data
    
    def five_of_kind(self, hand):
        for i in range(1, len(hand)):
            if hand[i] != hand[i-1]:
                return False
        return True
    
    def four_of_kind(self, hand):
        cache = {}
        for i in hand:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
        
        for i in cache:
            if cache[i] == 4:
                return True
        return False
    
    def three_of_kind(self, hand):
        cache = {}
        for i in hand:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
        
        for i in cache:
            if cache[i] == 3:
                return True
        return False
    
    def full_house(self, hand):
        cache = {}
        for i in hand:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
        
        if len(cache) == 2 and len(hand) == 5:
            for i in cache:
                if cache[i] == 2 or cache[i] == 3:
                    return True
        return False
    
    def two_pair(self, hand):
        cache = {}
        for i in hand:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
        
        counter = 0
        for i in cache:
            if cache[i] == 2:
                counter += 1
        return counter == 2
    
    def one_pair(self, hand):
        cache = {}
        for i in hand:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
        
        for i in cache:
            if cache[i] == 2:
                return True
        return False
    
    def compare_hands(self, hand1, hand2):
        for i in range(len(hand1)):
            hand1_card = self.cards[hand1[i]]
            hand2_card = self.cards[hand2[i]]
            if hand1_card > hand2_card:
                return True
            
            if hand1_card < hand2_card:
                return False

        return True

    def get_hand_rank(self, hand):
        if self.five_of_kind(hand):
            return self.ranks["Five of a kind"]
        if self.four_of_kind(hand):
            return self.ranks["Four of a kind"]
        if self.full_house(hand):
            return self.ranks["Full house"]
        if self.three_of_kind(hand):
            return self.ranks["Three of a kind"]
        if self.two_pair(hand):
            return self.ranks["Two pair"]
        if self.one_pair(hand):
            return self.ranks["One pair"]
        return self.ranks["Highest card"]
    

    def get_hand_with_jokers_rank(self, hand):
        jokers = 0
        hand_without_jokers = ""
        for i in hand:
            if i == "J":
                jokers += 1
            else:
                hand_without_jokers += i
        if jokers == 5 or jokers == 4:
            return self.ranks["Five of a kind"]

        hand_without_jokers_rank = self.get_hand_rank(hand_without_jokers)

        if jokers == 3:
            if hand_without_jokers_rank == self.ranks["One pair"]:
                return self.ranks["Five of a kind"]
            elif hand_without_jokers_rank == self.ranks["Highest card"]:
                return self.ranks["Four of a kind"]
            
        if jokers == 2:
            if hand_without_jokers_rank == self.ranks["Three of a kind"]:
                return self.ranks["Five of a kind"]
            elif hand_without_jokers_rank == self.ranks["One pair"]:
                return self.ranks["Four of a kind"]
            elif hand_without_jokers_rank == self.ranks["Highest card"]:
                return self.ranks["Three of a kind"]

        if jokers == 1:
            if hand_without_jokers_rank == self.ranks["Four of a kind"]:
                return self.ranks["Five of a kind"]
            elif hand_without_jokers_rank == self.ranks["Three of a kind"]:
                return self.ranks["Four of a kind"]
            elif hand_without_jokers_rank == self.ranks["Two pair"]:
                return self.ranks["Full house"]
            elif hand_without_jokers_rank == self.ranks["One pair"]:
                return self.ranks["Three of a kind"]
            elif hand_without_jokers_rank == self.ranks["Highest card"]:
                return self.ranks["One pair"]

        return hand_without_jokers_rank

    def insert_hand(self, root, hand, bid, rank):
        if root is None:
            return Node(hand, bid, rank)
        if rank < root.rank:
            root.left = self.insert_hand(root.left, hand, bid, rank)
        elif rank > root.rank:
            root.right = self.insert_hand(root.right, hand, bid, rank)
        else:
            if self.compare_hands(hand, root.hand):
                root.right = self.insert_hand(root.right, hand, bid, rank)
            else:
                root.left = self.insert_hand(root.left, hand, bid, rank)
        return root

    def dfs(self, root, i):
        res_right, cur_index = self.dfs(root.right, i) if root.right else (0, i)
        res = cur_index * int(root.bid)
        res_left, index = self.dfs(root.left, cur_index - 1) if root.left else (0, cur_index - 1)
        return res + res_left + res_right, index

    def part_one(self):
        data = [i.split(" ") for i in self.read_data().split("\n") if i != ""]
        root = Node(data[0][0], data[0][1], self.get_hand_rank(data[0][0]))
        data = data[1:]

        for player in data:
            hand, bid = player
            rank = self.get_hand_rank(hand)
            self.insert_hand(root, hand, bid, rank)

        res, _ = self.dfs(root, len(data) + 1)
        return res

    def part_two(self):
        data = [i.split(" ") for i in self.read_data().split("\n") if i != ""]
        root = Node(data[0][0], data[0][1], self.get_hand_with_jokers_rank(data[0][0]))
        data = data[1:]

        for player in data:
            hand, bid = player
            rank = self.get_hand_with_jokers_rank(hand)
            self.insert_hand(root, hand, bid, rank)

        res, _ = self.dfs(root, len(data) + 1)
        return res


def main():
    sol = Solution()
    print(f"Part one: {sol.part_one()}")
    time_part_one = (timeit.timeit(sol.part_one, number=10) / 10) * 1000
    print(f"Elapsed Time: {time_part_one:.3f} ms")
    print(f"Part two: {sol.part_two()}")
    time_part_two = (timeit.timeit(sol.part_two, number=10) / 10) * 1000
    print(f"Elapsed Time: {time_part_two:.3f} ms")
    # print(sol.compare_hands("33456", "43456"))

main()