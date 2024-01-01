## Part One: Binary Tree and DFS ⭐

In this puzzle, the goal is to calculate the total winnings by multiplying the hand ranking with the bid size. To efficiently store and compare thousands of hands, a binary tree is employed with an insert time complexity ranging between O(logn) and O(n).

The initial step is to construct the binary tree. At each node, information about the hand, bid, and hand rank is stored. Assigning a value to each hand type, ranging from the strongest (five of a kind) to the weakest (high card), precedes the insertion of the hand into the tree. When comparing hands during insertion, ranks take precedence, and in the case of identical ranks, a secondary ordering rule is applied (comparing each card until a winner is determined). Starting from the root node, if the inserting hand is stronger, traversal proceeds to the right; otherwise, it goes to the left, continuing until reaching the bottom of the tree.

The strongest hand is positioned at the right bottom of the tree. To calculate winnings, a Depth-First Search (DFS) in-order traversal is employed. Moving from the right to the left mimics a journey from the strongest to the weakest hand. The sum of all winnings obtained through this traversal constitutes the solution to the puzzle.

## Part Two: Binary Tree and DFS ⭐⭐

In part two, a new element is introduced: a joker (J) card that can act as any other card but is considered the weakest in hand comparison. The algorithm for storing and traversing data remains the same as in part one. The modification involves changing the method of assigning ranks to hands. The hand rank is now determined by the number of Jokers and the rank without Jokers. There are five possible scenarios:

- **5J:** `JJJJJ` - Five of a kind
- **4J:** `AJJJJ` - Five of a kind
- **3J:** `AAJJJ`, `AKJJJ` - Five of a kind, Four of a kind
  - If pair `AA` → Five of a kind
  - Otherwise `AK` → Four of a kind
- **2J:** `AAAJJ`, `AAJJK`, `AJJKQ` - Five of a kind, Four of a kind, Three of a kind
  - If three of a kind `AAA` → Five of a kind
  - If pair → Four of a kind
  - Otherwise `AKQ` → Three of a kind
- **1J:** `AAAAJ`, `AAAJK`, `AAJK`, `AAJKQ`, `AKQTJ` - Five of a kind, Four of a kind, Full house, Three of a kind, One pair.
  - If four of a kind `AAAA` → Five of a kind
  - If three of a kind `AAAK` → Four of a kind
  - If two pair `AAK` → Full house
  - If pair `AAKQ` → Three of a kind
  - Otherwise `AKQT` → One pair

![image](https://github.com/coado/advent_of_code_2023/assets/64146291/ba3590c9-93f1-4fe3-8cd3-de77e1721a1e)
