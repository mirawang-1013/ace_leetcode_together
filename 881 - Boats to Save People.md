# 881. Boats to Save People

**Difficulty:** Medium
**Tags:** Array, Two Pointers, Greedy, Sorting

## Problem

给定数组 `people`，`people[i]` 是第 i 个人的体重。每艘船最大承重 `limit`，**每艘船最多载两人**，且两人重量之和不超过 `limit`。返回所需最小船数。

### Examples

**Example 1:**
- Input: `people = [1,2], limit = 3`
- Output: `1`

**Example 2:**
- Input: `people = [3,2,2,1], limit = 3`
- Output: `3` → (1,2), (2), (3)

**Example 3:**
- Input: `people = [3,5,3,4], limit = 5`
- Output: `4` → 每人单独一船

## Key Insight

⭐ **每船最多两人**是这道题的关键约束。正因为最多两人，不需要考虑三人或更多人的组合，问题简化为：每个重的人能不能找一个轻的人配对？

**贪心策略：** 排序后，最重的人尝试和最轻的人配对：
- 能配 → 两人一船，双指针都移动
- 不能配 → 最重的人单独一船，只移右指针

## Code

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo, hi = 0, len(people) - 1
        boats = 0
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1  # 最轻的人上船
            hi -= 1       # 最重的人一定上船
            boats += 1
        return boats
```

## 逐步解析

### Step 1: 排序

```python
people.sort()
```

排序后最轻的在左，最重的在右，方便贪心配对。

### Step 2: 双指针贪心

```python
lo, hi = 0, len(people) - 1
```

`lo` 指向最轻的人，`hi` 指向最重的人。

### Step 3: 配对逻辑

```python
if people[lo] + people[hi] <= limit:
    lo += 1  # 轻的人可以搭便车
hi -= 1       # 不管能不能配对，重的人都要走
boats += 1
```

- **能配对：** 轻 + 重 ≤ limit，两人一船，`lo++` 和 `hi--`
- **不能配对：** 重的人太重，只能单独坐船，只 `hi--`

### 为什么贪心是对的？

最重的人要么单独坐船，要么和某人配对。如果能和**最轻的人**配对都超重，那和任何人配对都超重 → 只能单独坐。如果能和最轻的人配对，那就配（把最轻的名额留给别人不会更优，因为每船最多两人）。

## Walkthrough

`people = [3,2,2,1], limit = 3`

排序后：`[1, 2, 2, 3]`

| Step | lo | hi | Check | Action | boats |
|------|----|----|-------|--------|-------|
| 1 | 0(1) | 3(3) | 1+3=4 > 3 | 3 单独走，hi-- | 1 |
| 2 | 0(1) | 2(2) | 1+2=3 ≤ 3 | (1,2) 配对，lo++, hi-- | 2 |
| 3 | 1(2) | 1(2) | lo==hi | 2 单独走，hi-- | 3 |

## Notes

- **时间复杂度：** O(n log n)（排序）
- **空间复杂度：** O(1)（原地排序）
- 核心：**最多两人** → 双指针贪心，不需要背包/组合
- 类似题型：Two Pointers 系列（如 167 Two Sum II、11 Container With Most Water）
