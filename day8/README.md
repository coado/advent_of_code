## Part One - State Machine Traversal ⭐

In this puzzle, we are provided with a set of commands and a state machine. The state machine consists of states, each leading to two corresponding states: left and right. Starting from the initial state `AAA`, the decision to move left or right is dictated by the current command value: `L` or `R`, respectively. We proceed to traverse the state space based on the given commands until we reach the final state `ZZZ`.

## Part Two - Concurrent State Machine Traversal and LCM ⭐⭐

In this section, the puzzle introduces multiple starting states, all concluding with `A`. The objective is to concurrently traverse these starting states until they reach end states concluding with `Z`. If certain routes reach their end states earlier, those end states are treated as regular states, and traversal continues. The challenge lies in optimizing the solution due to the increasing complexity, as the number of starting states grows.

The crafted input data ensures that each starting state leads to a unique ending state, and the ending state always connects to the second state in the loop. This characteristic enables the detection of loop lengths by calculating the steps required from the starting point to the ending node.

This information results in an array of distances from each starting state to its corresponding ending state, forming a representation like `[3, 4, 6]`. To determine the number of steps required to synchronize all states to the ending state simultaneously, the Least Common Multiple (LCM) is calculated. In the provided example, the LCM of distances `[3, 4, 6]` is `12`. This implies making `12 / 3 = 4` loops for the first state, `12 / 4 = 3` loops for the second one, and `12 / 6 = 2` loops for the third one. All these loops culminate in the last possible state (the ending state) before transitioning to the next iteration of the loop.
