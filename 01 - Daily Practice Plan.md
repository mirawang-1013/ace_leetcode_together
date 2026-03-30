# Daily Practice Plan (13 Weeks)

## How to Use This Plan

- **Daily target:** 1-2 problems per day
- **Time per problem:** 25 min attempt → if stuck, read the approach → implement → review
- **Review:** Every Sunday, revisit 2-3 problems from the past week without looking at solutions
- **Note-taking:** After solving, create a note in `LeetCode/` with the pattern and key insight

---

## Week 1: Arrays & Hashing

| Day | Problem                                          | Difficulty | Key Pattern               |
| --- | ------------------------------------------------ | ---------- | ------------------------- |
| Mon | 217 Contains Duplicate                           | Easy       | HashSet membership        |
| Mon | 242 Valid Anagram                                | Easy       | HashMap counting          |
| Tue | 1 Two Sum                                        | Easy       | HashMap complement lookup |
| Tue | 49 Group Anagrams                                | Medium     | HashMap grouping by key   |
| Wed | 347 Top K Frequent Elements                      | Medium     | HashMap + Bucket Sort     |
| Thu | 238 Product of Array Except Self                 | Medium     | Prefix/Suffix arrays      |
| Fri | 128 Longest Consecutive Sequence                 | Medium     | HashSet + sequence start  |
| Sat | 36 Valid Sudoku                                  | Medium     | HashSet per row/col/box   |
| Sun | **Review Day** — redo 2-3 hardest from this week |            |                           |
|     |                                                  |            |                           |

## Week 2: Two Pointers & Stack

| Day | Problem | Difficulty | Key Pattern |
|-----|---------|-----------|------------|
| Mon | 125 Valid Palindrome | Easy | Two pointers inward |
| Mon | 167 Two Sum II | Medium | Two pointers on sorted array |
| Tue | 15 3Sum | Medium | Sort + two pointers |
| Wed | 11 Container With Most Water | Medium | Greedy two pointers |
| Thu | 42 Trapping Rain Water | Hard | Two pointers / monotonic stack |
| Fri | 20 Valid Parentheses | Easy | Stack matching |
| Fri | 155 Min Stack | Medium | Auxiliary stack |
| Sat | 150 Evaluate Reverse Polish Notation | Medium | Stack evaluation |
| Sat | 84 Largest Rectangle in Histogram | Hard | Monotonic stack |
| Sun | **Review Day** | | |

## Week 3: Sliding Window

| Day | Problem | Difficulty | Key Pattern |
|-----|---------|-----------|------------|
| Mon | 121 Best Time to Buy and Sell Stock | Easy | Track min so far |
| Tue | 3 Longest Substring Without Repeating | Medium | Expand/shrink window + set |
| Wed | 424 Longest Repeating Character Replacement | Medium | Window + max frequency |
| Thu | 567 Permutation in String | Medium | Fixed-size window + freq map |
| Fri | 76 Minimum Window Substring | Hard | Shrinkable window + freq map |
| Sat | Catch-up / review | | |
| Sun | **Review Day** | | |

## Week 4: Binary Search

| Day | Problem | Difficulty | Key Pattern |
|-----|---------|-----------|------------|
| Mon | 704 Binary Search | Easy | Classic binary search |
| Tue | 153 Find Min in Rotated Sorted Array | Medium | Modified binary search |
| Wed | 33 Search in Rotated Sorted Array | Medium | Two-part binary search |
| Thu | 4 Median of Two Sorted Arrays | Hard | Binary search on partition |
| Fri | Catch-up / review | | |
| Sun | **Review Day** | | |

## Week 5: Linked Lists

| Day | Problem | Difficulty | Key Pattern |
|-----|---------|-----------|------------|
| Mon | 206 Reverse Linked List | Easy | Iterative pointer reversal |
| Mon | 21 Merge Two Sorted Lists | Easy | Dummy node + merge |
| Tue | 141 Linked List Cycle | Easy | Fast/slow pointers |
| Tue | 287 Find the Duplicate Number | Medium | Floyd's cycle detection |
| Wed | 19 Remove Nth Node From End | Medium | Two pointers with gap |
| Thu | 143 Reorder List | Medium | Split + reverse + merge |
| Thu | 138 Copy List with Random Pointer | Medium | HashMap clone |
| Fri | 2 Add Two Numbers | Medium | Carry propagation |
| Sat | 23 Merge K Sorted Lists | Hard | Min heap / divide & conquer |
| Sat | 25 Reverse Nodes in k-Group | Hard | Iterative k-reversal |
| Sun | **Review Day** | | |

## Week 6: Binary Trees (Part 1)

| Day | Problem | Difficulty | Key Pattern |
|-----|---------|-----------|------------|
| Mon | 226 Invert Binary Tree | Easy | Recursive swap |
| Mon | 104 Maximum Depth of Binary Tree | Easy | DFS depth |
| Tue | 543 Diameter of Binary Tree | Easy | DFS with global max |
| Tue | 110 Balanced Binary Tree | Easy | Height-check DFS |
| Wed | 100 Same Tree | Easy | Parallel DFS |
| Wed | 572 Subtree of Another Tree | Easy | Nested DFS |
| Thu | 235 Lowest Common Ancestor of BST | Medium | BST property |
| Fri | 102 Binary Tree Level Order Traversal | Medium | BFS with queue |
| Fri | 199 Binary Tree Right Side View | Medium | BFS last in level |
| Sat | 98 Validate Binary Search Tree | Medium | In-order / range check |
| Sun | **Review Day** | | |

## Week 7: Binary Trees (Part 2) & Tries

| Day | Problem | Difficulty | Key Pattern |
|-----|---------|-----------|------------|
| Mon | 230 Kth Smallest Element in BST | Medium | In-order traversal |
| Tue | 105 Construct Tree from Preorder & Inorder | Medium | Recursive build |
| Wed | 124 Binary Tree Maximum Path Sum | Hard | DFS with global max |
| Thu | 297 Serialize and Deserialize Binary Tree | Hard | BFS/DFS serialization |
| Fri | 208 Implement Trie | Medium | Trie node structure |
| Sat | 211 Add and Search Words | Medium | Trie + DFS for wildcards |
| Sat | 212 Word Search II | Hard | Trie + backtracking |
| Sun | **Review Day** | | |

## Week 8: Graphs (Part 1)

| Day | Problem | Difficulty | Key Pattern |
|-----|---------|-----------|------------|
| Mon | 200 Number of Islands | Medium | DFS/BFS on grid |
| Mon | 695 Max Area of Island | Medium | DFS area counting |
| Tue | 133 Clone Graph | Medium | BFS/DFS + HashMap |
| Wed | 994 Rotting Oranges | Medium | Multi-source BFS |
| Thu | 417 Pacific Atlantic Water Flow | Medium | Reverse DFS from borders |
| Fri | 207 Course Schedule | Medium | Topological sort (DFS) |
| Sat | 210 Course Schedule II | Medium | Topological sort (order) |
| Sun | **Review Day** | | |

## Week 9: Graphs (Part 2) & Heaps

| Day | Problem | Difficulty | Key Pattern |
|-----|---------|-----------|------------|
| Mon | 323 Number of Connected Components | Medium | Union-Find |
| Tue | 261 Graph Valid Tree | Medium | Union-Find + edge count |
| Wed | 269 Alien Dictionary | Hard | Topological sort |
| Thu | 703 Kth Largest Element in Stream | Easy | Min-heap of size k |
| Thu | 215 Kth Largest Element in Array | Medium | Quickselect / heap |
| Fri | 621 Task Scheduler | Medium | Greedy + heap |
| Sat | 295 Find Median from Data Stream | Hard | Two heaps |
| Sun | **Review Day** | | |

## Week 10: 1-D Dynamic Programming

| Day | Problem | Difficulty | Key Pattern |
|-----|---------|-----------|------------|
| Mon | 70 Climbing Stairs | Easy | Fibonacci DP |
| Mon | 746 Min Cost Climbing Stairs | Easy | Bottom-up DP |
| Tue | 198 House Robber | Medium | Rob or skip DP |
| Tue | 213 House Robber II | Medium | Circular array DP |
| Wed | 5 Longest Palindromic Substring | Medium | Expand from center / DP |
| Wed | 647 Palindromic Substrings | Medium | Count expansions |
| Thu | 91 Decode Ways | Medium | String DP |
| Fri | 322 Coin Change | Medium | Unbounded knapsack DP |
| Sat | 152 Maximum Product Subarray | Medium | Track min and max |
| Sat | 139 Word Break | Medium | DP + set lookup |
| Sun | **Review Day** | | |

## Week 11: More DP

| Day | Problem | Difficulty | Key Pattern |
|-----|---------|-----------|------------|
| Mon | 300 Longest Increasing Subsequence | Medium | DP / patience sort |
| Mon | 416 Partition Equal Subset Sum | Medium | 0/1 knapsack |
| Tue | 62 Unique Paths | Medium | Grid DP |
| Wed | 1143 Longest Common Subsequence | Medium | 2D DP table |
| Thu | 309 Buy and Sell Stock with Cooldown | Medium | State machine DP |
| Thu | 518 Coin Change II | Medium | Unbounded knapsack (count) |
| Fri | 494 Target Sum | Medium | Subset sum DP |
| Sat | 97 Interleaving String | Medium | 2D DP |
| Sat | 72 Edit Distance | Medium | Classic 2D DP |
| Sun | **Review Day** | | |

## Week 12: Greedy, Intervals & Backtracking

| Day | Problem | Difficulty | Key Pattern |
|-----|---------|-----------|------------|
| Mon | 53 Maximum Subarray | Medium | Kadane's algorithm |
| Mon | 55 Jump Game | Medium | Greedy reachability |
| Tue | 45 Jump Game II | Medium | Greedy BFS |
| Tue | 134 Gas Station | Medium | Greedy net-gain |
| Wed | 57 Insert Interval | Medium | Merge logic |
| Wed | 56 Merge Intervals | Medium | Sort + merge |
| Thu | 435 Non-overlapping Intervals | Medium | Greedy interval scheduling |
| Fri | 78 Subsets | Medium | Backtracking template |
| Fri | 39 Combination Sum | Medium | Backtracking with reuse |
| Sat | 46 Permutations | Medium | Backtracking swap |
| Sat | 79 Word Search | Medium | Grid backtracking |
| Sun | **Review Day** | | |

## Week 13: Math, Bits & Final Backtracking

| Day | Problem | Difficulty | Key Pattern |
|-----|---------|-----------|------------|
| Mon | 48 Rotate Image | Medium | Layer-by-layer rotation |
| Mon | 54 Spiral Matrix | Medium | Boundary shrinking |
| Tue | 73 Set Matrix Zeroes | Medium | Marker row/col |
| Wed | 268 Missing Number | Easy | XOR / math |
| Wed | 191 Number of 1 Bits | Easy | Bit counting |
| Wed | 338 Counting Bits | Easy | DP on bits |
| Thu | 190 Reverse Bits | Easy | Bit shifting |
| Thu | 371 Sum of Two Integers | Medium | Bit manipulation |
| Fri | 131 Palindrome Partitioning | Medium | Backtracking + palindrome check |
| Fri | 17 Letter Combinations of Phone Number | Medium | Backtracking |
| Sat | 51 N-Queens | Hard | Backtracking with constraints |
| Sat | 10 Regular Expression Matching | Hard | DP |
| Sun | **Final Review** | | |

---

## After Week 13

- **Mock interviews:** Time yourself (45 min for 2 problems)
- **Spaced review:** Revisit problems you found hardest every 3-5 days
- **Track weak areas:** If a category felt hard, redo it before interviews
