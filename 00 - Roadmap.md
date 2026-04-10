# LeetCode Roadmap: Blind 75 + Top 100

## Study Order by Topic

The recommended order goes from foundational patterns to advanced topics. Master each category before moving on.

---
3.18：6
3.19：6+2=8
3.20：8+1     aimed to hit 15
3.21：9+6=15
3.22:  15+2=17
3.25:  17+5=22 
3.26-3.28=22+3=25
3.26
---

## 4-Day Sprint Schedule (Blind 75 Focus, 3.26 - 3.29)

### Day 1 — 3.26: Sliding Window + Linked List + Easy Trees (13)
- [x] 121 Best Time to Buy and Sell Stock (E) — Sliding Window
- [x] 424 Longest Repeating Character Replacement (M) — Sliding Window
- [x] 76 Minimum Window Substring (H) — Sliding Window
- [x] 206 Reverse Linked List (E)
- [x] 21 Merge Two Sorted Lists (E)
- [x] 141 Linked List Cycle (E)
- [x] 143 Reorder List (M)
- [x] 19 Remove Nth Node From End of List (M)
- [ ] 23 Merge K Sorted Lists (H)
- [x] 226 Invert Binary Tree (E)
- [x] 104 Maximum Depth of Binary Tree (E)
- [ ] 100 Same Tree (E)
- [ ] 572 Subtree of Another Tree (E)

### Day 2 — 3.27: Trees (M/H) + Tries + Graphs (14)
- [ ] 235 Lowest Common Ancestor of a BST (M)
- [ ] 102 Binary Tree Level Order Traversal (M)
- [ ] 98 Validate Binary Search Tree (M)
- [ ] 230 Kth Smallest Element in a BST (M)
- [ ] 105 Construct Binary Tree from Preorder and Inorder (M)
- [ ] 124 Binary Tree Maximum Path Sum (H)
- [ ] 297 Serialize and Deserialize Binary Tree (H)
- [ ] 208 Implement Trie (M)
- [ ] 211 Design Add and Search Words (M)
- [ ] 212 Word Search II (H)
- [ ] 200 Number of Islands (M)
- [ ] 133 Clone Graph (M)
- [ ] 417 Pacific Atlantic Water Flow (M)
- [ ] 207 Course Schedule (M)

### Day 3 — 3.28: DP + Heap + Greedy (14)
- [ ] 70 Climbing Stairs (E) — 1-D DP
- [ ] 198 House Robber (M) — 1-D DP
- [ ] 213 House Robber II (M) — 1-D DP
- [ ] 647 Palindromic Substrings (M) — 1-D DP
- [ ] 91 Decode Ways (M) — 1-D DP
- [ ] 322 Coin Change (M) — 1-D DP
- [ ] 152 Maximum Product Subarray (M) — 1-D DP
- [ ] 139 Word Break (M) — 1-D DP
- [ ] 300 Longest Increasing Subsequence (M) — 1-D DP
- [ ] 62 Unique Paths (M) — 2-D DP
- [ ] 1143 Longest Common Subsequence (M) — 2-D DP
- [ ] 295 Find Median from Data Stream (H) — Heap
- [ ] 53 Maximum Subarray (M) — Greedy
- [ ] 55 Jump Game (M) — Greedy

### Day 4 — 3.29: Intervals + Math + Bits + Backtracking (13)
- [ ] 57 Insert Interval (M)
- [ ] 56 Merge Intervals (M)
- [ ] 435 Non-overlapping Intervals (M)
- [ ] 48 Rotate Image (M)
- [ ] 54 Spiral Matrix (M)
- [ ] 73 Set Matrix Zeroes (M)
- [ ] 191 Number of 1 Bits (E)
- [ ] 338 Counting Bits (E)
- [ ] 190 Reverse Bits (E)
- [ ] 268 Missing Number (E)
- [ ] 371 Sum of Two Integers (M)
- [ ] 39 Combination Sum (M)
- [ ] 79 Word Search (M)

> **Pacing:** Easy ~15min | Medium ~25min cap | Hard ~30min cap. If stuck, read solution and re-implement.

---

## Phase 1: Foundations (Week 1-2)

### 1. Arrays & Hashing
> Core skill: Using hash maps/sets for O(1) lookups to replace nested loops.

| #   | Problem                          | Difficulty | List               | Finish | Date | Review |
| --- | -------------------------------- | ---------- | ------------------ | ------ | ---- | ------ |
| 1   | Two Sum                          | Easy       | Blind 75 / Top 100 | ✅      | 3.18 |        |
| 217 | Contains Duplicate               | Easy       | Blind 75           | ✅      | 3.18 |        |
| 242 | Valid Anagram                    | Easy       | Blind 75           | ✅      | 3.18 |        |
| 49  | Group Anagrams                   | Medium     | Blind 75 / Top 100 | ✅      | 3.18 |        |
| 347 | Top K Frequent Elements          | Medium     | Blind 75 / Top 100 | ✅      | 3.18 | ✅      |
| 238 | Product of Array Except Self     | Medium     | Blind 75 / Top 100 | ✅      | 3.20 |        |
| 271 | Encode and Decode Strings        | Medium     | Blind 75 (Premium) | ✅      | 3.21 |        |
| 128 | [[Longest Consecutive Sequence]] | Medium     | Blind 75 / Top 100 | ✅      | 3.18 |        |
| 36  | Valid Sudoku                     | Medium     | Top 100            |        |      |        |
| 659 | Encode and Decode Strings        | Medium     | Top 100            |        |      |        |

### 2. Two Pointers
> Core skill: Converging/diverging pointers to avoid O(n²) pair checks.

| #   | Problem                   | Difficulty | List               | Finish  | Date | Review                                                                                               |
| --- | ------------------------- | ---------- | ------------------ | ------- | ---- | ---------------------------------------------------------------------------------------------------- |
| 125 | Valid Palindrome          | Easy       | Blind 75           | ✅       | 3.21 |                                                                                                      |
| 167 | Two Sum II                | Medium     | Top 100            | ✅😄     | 3.21 |                                                                                                      |
| 15  | 3Sum                      | Medium     | Blind 75 / Top 100 | ✅😄😄   | 3.21 | 3.25 非常好，除了set() add 之后return list()这里卡了下。 学习了如何增加runtime的方法，重点就是在于，怎么在下一个element相同的时候，continue skip |
| 11  | Container With Most Water | Medium     | Blind 75 / Top 100 | ✅😄😄   | 3.21 |                                                                                                      |
| 42  | Trapping Rain Water       | Hard       | Top 100            | ✅😄😄😄 | 3.21 | 3.25 没能一次性写出来但是印象更深了                                                                                 |
|     |                           |            |                    |         |      |                                                                                                      |

### 3. Stack
> Core skill: LIFO processing for matching/nesting problems.

| #   | Problem                          | Difficulty | List               | Finish                       | Date | Review |
| --- | -------------------------------- | ---------- | ------------------ | ---------------------------- | ---- | ------ |
| 20  | Valid Parentheses                | Easy       | Blind 75 / Top 100 | ✅ 很好玩的一道题目                   | 3.22 |        |
| 155 | Min Stack                        | Medium     | Top 100            | ✅对stack很生疏                   | 3.22 |        |
| 150 | Evaluate Reverse Polish Notation | Medium     | Top 100            | ✅对stack很生疏                   | 3.25 |        |
| 84  | Largest Rectangle in Histogram   | Hard       | Top 100            | 尝试用双指针结果不能work ✅ 非常有成就感和有挑战性 | 3.25 |        |

---

## Phase 2: Search & Sort (Week 3-4)

### 4. Binary Search
> Core skill: Halving search space on sorted/monotonic data.

| #   | Problem                              | Difficulty | List               | Finish                     | Date |
| --- | ------------------------------------ | ---------- | ------------------ | -------------------------- | ---- |
| 704 | Binary Search                        | Easy       | Top 100            | ✅                          | 3.25 |
| 153 | Find Minimum in Rotated Sorted Array | Medium     | Blind 75           | ✅<br>return nums[mid] 卡死我了 | 3.25 |
| 33  | Search in Rotated Sorted Array       | Medium     | Blind 75 / Top 100 | ✅ 和上一道題差不多，二分法都是O(logn)    | 3.25 |
| 4   | Median of Two Sorted Arrays          | Hard       | Top 100            |                            |      |

### 5. Sliding Window
> Core skill: Maintaining a window to avoid recalculating subarrays.

| #   | Problem                                        | Difficulty | List               | Finish    | Date | Review   |
| --- | ---------------------------------------------- | ---------- | ------------------ | --------- | ---- | -------- |
| 121 | Best Time to Buy and Sell Stock                | Easy       | Blind 75 / Top 100 | ✅         | 3.26 |          |
| 3   | Longest Substring Without Repeating Characters | Medium     | Blind 75 / Top 100 | ✅         | 3.19 |          |
| 424 | Longest Repeating Character Replacement        | Medium     | Blind 75           | ✅         | 3.27 |          |
| 567 | Permutation in String                          | Medium     | Top 100            | ✅非常好，手撕成功 | 3.28 |          |
| 76  | Minimum Window Substring                       | Hard       | Blind 75 / Top 100 | ✅         | 3.28 | 3.29 复习了 |


**新学习的567的新方法**：非常灵
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
	        if len(s1) > len(s2):
	            return False

        need = [0] * 26
        window = [0] * 26

        for c in s1:
            need[ord(c) - ord('a')] += 1

        left = 0
        for right in range(len(s2)):
            window[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 > len(s1):
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if window == need:
                return True

        return False



---

## Phase 3: Linked Lists (Week 5)

### 6. Linked List
> Core skill: Pointer manipulation, fast/slow pointers, dummy nodes.

| #   | Problem                          | Difficulty | List               | Finish                | Date |
| --- | -------------------------------- | ---------- | ------------------ | --------------------- | ---- |
| 206 | Reverse Linked List              | Easy       | Blind 75 / Top 100 | ✅，我用stack做的 有点不够灵活    | 3.28 |
| 21  | Merge Two Sorted Lists           | Easy       | Blind 75 / Top 100 | ✅ 感觉还是得继续适应           | 3.29 |
| 141 | Linked List Cycle                | Easy       | Blind 75 / Top 100 | ✅ 还是蛮容易的叭，用了set()这个概念 | 3.29 |
| 143 | Reorder List                     | Medium     | Blind 75           | ✅ 用数组做的               | 3.29 |
| 19  | Remove Nth Node From End of List | Medium     | Blind 75 / Top 100 | ✅ 很灵的写法               | 3.29 |
| 138 | Copy List with Random Pointer    | Medium     | Top 100            |                       |      |
| 2   | Add Two Numbers                  | Medium     | Top 100            | ✅ 学到挺多                | 3.30 |
| 287 | Find the Duplicate Number        | Medium     | Top 100            |                       |      |
| 23  | Merge K Sorted Lists             | Hard       | Blind 75 / Top 100 |                       |      |
| 25  | Reverse Nodes in k-Group         | Hard       | Top 100            |                       |      |

---

## Phase 4: Trees (Week 6-7)

### 7. Binary Trees
> Core skill: Recursion, DFS, BFS traversals.

| #   | Problem                                         | Difficulty | List               | Finish | Date |
| --- | ----------------------------------------------- | ---------- | ------------------ | ------ | ---- |
| 226 | Invert Binary Tree                              | Easy       | Blind 75 / Top 100 | ✅      | 4/6  |
| 104 | Maximum Depth of Binary Tree                    | Easy       | Blind 75 / Top 100 | ✅      | 4/6  |
| 543 | Diameter of Binary Tree                         | Easy       | Top 100            |        |      |
| 110 | Balanced Binary Tree                            | Easy       | Top 100            |        |      |
| 100 | Same Tree                                       | Easy       | Blind 75           |        |      |
| 572 | Subtree of Another Tree                         | Easy       | Blind 75           |        |      |
| 235 | Lowest Common Ancestor of a BST                 | Medium     | Blind 75           |        |      |
| 102 | Binary Tree Level Order Traversal               | Medium     | Blind 75 / Top 100 |        |      |
| 199 | Binary Tree Right Side View                     | Medium     | Top 100            |        |      |
| 98  | Validate Binary Search Tree                     | Medium     | Blind 75 / Top 100 |        |      |
| 230 | Kth Smallest Element in a BST                   | Medium     | Blind 75 / Top 100 |        |      |
| 105 | Construct Binary Tree from Preorder and Inorder | Medium     | Blind 75 / Top 100 |        |      |
| 124 | Binary Tree Maximum Path Sum                    | Hard       | Blind 75 / Top 100 |        |      |
| 297 | Serialize and Deserialize Binary Tree           | Hard       | Blind 75           |        |      |

### 8. Tries
> Core skill: Prefix-based search and storage.

| #   | Problem                                    | Difficulty | List               | Finish | Date |
| --- | ------------------------------------------ | ---------- | ------------------ | ------ | ---- |
| 208 | Implement Trie (Prefix Tree)               | Medium     | Blind 75 / Top 100 |        |      |
| 211 | Design Add and Search Words Data Structure | Medium     | Blind 75           |        |      |
| 212 | Word Search II                             | Hard       | Blind 75           |        |      |

---

## Phase 5: Graphs (Week 8-9)

### 9. Graphs
> Core skill: DFS, BFS, Union-Find, topological sort.

| #   | Problem                        | Difficulty | List               | Finish | Date |
| --- | ------------------------------ | ---------- | ------------------ | ------ | ---- |
| 200 | Number of Islands              | Medium     | Blind 75 / Top 100 |        |      |
| 133 | Clone Graph                    | Medium     | Blind 75 / Top 100 |        |      |
| 695 | Max Area of Island             | Medium     | Top 100            |        |      |
| 994 | Rotting Oranges                | Medium     | Top 100            |        |      |
| 417 | Pacific Atlantic Water Flow    | Medium     | Blind 75           |        |      |
| 207 | Course Schedule                | Medium     | Blind 75 / Top 100 |        |      |
| 210 | Course Schedule II             | Medium     | Top 100            |        |      |
| 323 | Number of Connected Components | Medium     | Blind 75 (Premium) |        |      |
| 261 | Graph Valid Tree               | Medium     | Blind 75 (Premium) |        |      |
| 269 | Alien Dictionary               | Hard       | Blind 75 (Premium) |        |      |

### 10. Heap / Priority Queue
> Core skill: Efficient min/max tracking.

| #   | Problem                         | Difficulty | List               | Finish | Date |
| --- | ------------------------------- | ---------- | ------------------ | ------ | ---- |
| 703 | Kth Largest Element in a Stream | Easy       | Top 100            |        |      |
| 215 | Kth Largest Element in an Array | Medium     | Top 100            |        |      |
| 621 | Task Scheduler                  | Medium     | Top 100            |        |      |
| 355 | Design Twitter                  | Medium     | Top 100            |        |      |
| 295 | Find Median from Data Stream    | Hard       | Blind 75 / Top 100 |        |      |

---

## Phase 6: Dynamic Programming (Week 10-12)

### 11. 1-D Dynamic Programming
> Core skill: State transitions, memoization, tabulation.

| #   | Problem                        | Difficulty | List               | Finish | Date |
| --- | ------------------------------ | ---------- | ------------------ | ------ | ---- |
| 70  | Climbing Stairs                | Easy       | Blind 75 / Top 100 |        |      |
| 746 | Min Cost Climbing Stairs       | Easy       | Top 100            |        |      |
| 198 | House Robber                   | Medium     | Blind 75 / Top 100 |        |      |
| 213 | House Robber II                | Medium     | Blind 75           |        |      |
| 5   | Longest Palindromic Substring  | Medium     | Blind 75 / Top 100 | ✅⚠️    | 3.19 |
| 647 | Palindromic Substrings         | Medium     | Blind 75           |        |      |
| 91  | Decode Ways                    | Medium     | Blind 75 / Top 100 |        |      |
| 322 | Coin Change                    | Medium     | Blind 75 / Top 100 |        |      |
| 152 | Maximum Product Subarray       | Medium     | Blind 75           |        |      |
| 139 | Word Break                     | Medium     | Blind 75 / Top 100 |        |      |
| 300 | Longest Increasing Subsequence | Medium     | Blind 75 / Top 100 |        |      |
| 416 | Partition Equal Subset Sum     | Medium     | Top 100            |        |      |

### 12. 2-D Dynamic Programming
> Core skill: Multi-dimensional state transitions.

| #    | Problem                                       | Difficulty | List               | Finish |  Date |
| ---- | --------------------------------------------- | ---------- | ------------------ | ------ | ----- |
| 62   | Unique Paths                                  | Medium     | Blind 75 / Top 100 |        |       |
| 1143 | Longest Common Subsequence                    | Medium     | Blind 75           |        |       |
| 309  | Best Time to Buy and Sell Stock with Cooldown | Medium     | Top 100            |        |       |
| 518  | Coin Change II                                | Medium     | Top 100            |        |       |
| 494  | Target Sum                                    | Medium     | Top 100            |        |       |
| 97   | Interleaving String                           | Medium     | Top 100            |        |       |
| 72   | Edit Distance                                 | Medium     | Top 100            |        |       |
| 10   | Regular Expression Matching                   | Hard       | Top 100            |        |       |

---

## Phase 7: Greedy, Intervals & Math (Week 13)

### 13. Greedy
> Core skill: Local optimal → global optimal.

| #   | Problem           | Difficulty | List               | Finish | Date |
| --- | ----------------- | ---------- | ------------------ | ------ | ---- |
| 53  | Maximum Subarray  | Medium     | Blind 75 / Top 100 |        |      |
| 55  | Jump Game         | Medium     | Blind 75 / Top 100 |        |      |
| 45  | Jump Game II      | Medium     | Top 100            |        |      |
| 134 | Gas Station       | Medium     | Top 100            |        |      |
| 846 | Hand of Straights | Medium     | Top 100            |        |      |

### 14. Intervals
> Core skill: Sort by start/end, merge overlapping.

| #   | Problem                   | Difficulty | List               | Finish | Date |
| --- | ------------------------- | ---------- | ------------------ | ------ | ---- |
| 57  | Insert Interval           | Medium     | Blind 75 / Top 100 |        |      |
| 56  | Merge Intervals           | Medium     | Blind 75 / Top 100 |        |      |
| 435 | Non-overlapping Intervals | Medium     | Blind 75           |        |      |
| 252 | Meeting Rooms             | Easy       | Blind 75 (Premium) |        |      |
| 253 | Meeting Rooms II          | Medium     | Blind 75 (Premium) |        |      |

### 15. Math & Geometry
> Core skill: Matrix manipulation, bit tricks.

| #   | Problem           | Difficulty | List               | Finish | Date |
| --- | ----------------- | ---------- | ------------------ | ------ | ---- |
| 48  | Rotate Image      | Medium     | Blind 75 / Top 100 |        |      |
| 54  | Spiral Matrix     | Medium     | Blind 75 / Top 100 |        |      |
| 73  | Set Matrix Zeroes | Medium     | Blind 75 / Top 100 |        |      |
| 202 | Happy Number      | Easy       | Top 100            |        |      |
| 66  | Plus One          | Easy       | Top 100            |        |      |
| 50  | Pow(x, n)         | Medium     | Top 100            |        |      |
| 43  | Multiply Strings  | Medium     | Top 100            |        |      |

### 16. Bit Manipulation
> Core skill: XOR, AND, OR, shift operations.

| #   | Problem             | Difficulty | List               | Finish | Date |
| --- | ------------------- | ---------- | ------------------ | ------ | ---- |
| 191 | Number of 1 Bits    | Easy       | Blind 75           |        |      |
| 338 | Counting Bits       | Easy       | Blind 75           |        |      |
| 190 | Reverse Bits        | Easy       | Blind 75           |        |      |
| 268 | Missing Number      | Easy       | Blind 75 / Top 100 |        |      |
| 371 | Sum of Two Integers | Medium     | Blind 75           |        |      |
| 7   | Reverse Integer     | Medium     | Top 100            |        |      |

### 17. Backtracking
> Core skill: Explore all paths, prune invalid branches.

| #   | Problem                               | Difficulty | List               | Finish | Date |
| --- | ------------------------------------- | ---------- | ------------------ | ------ | ---- |
| 78  | Subsets                               | Medium     | Top 100            |        |      |
| 39  | Combination Sum                       | Medium     | Blind 75 / Top 100 |        |      |
| 46  | Permutations                          | Medium     | Top 100            |        |      |
| 90  | Subsets II                            | Medium     | Top 100            |        |      |
| 40  | Combination Sum II                    | Medium     | Top 100            |        |      |
| 79  | Word Search                           | Medium     | Blind 75 / Top 100 |        |      |
| 131 | Palindrome Partitioning               | Medium     | Top 100            |        |      |
| 17  | Letter Combinations of a Phone Number | Medium     | Top 100            |        |      |
| 51  | N-Queens                              | Hard       | Top 100            |        |      |

---

## Progress Tracker

- [ ] Phase 1: Foundations (Arrays, Two Pointers, Stack)
- [ ] Phase 2: Search & Sort (Binary Search, Sliding Window)
- [ ] Phase 3: Linked Lists
- [ ] Phase 4: Trees (Binary Trees, Tries)
- [ ] Phase 5: Graphs (Graphs, Heaps)
- [ ] Phase 6: Dynamic Programming (1-D, 2-D)
- [ ] Phase 7: Greedy, Intervals, Math, Bits, Backtracking

> **Tip:** For each problem, write a note in the `LeetCode/` folder with the pattern, approach, and solution. Review past notes before attempting similar problems.
