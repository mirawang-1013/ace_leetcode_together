# 84. Largest Rectangle in Histogram

**Difficulty:** Hard
**Tags:** Array, Stack, Monotonic Stack

## Problem

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

### Examples

**Example 1:**
- Input: `heights = [2,1,5,6,2,3]`
- Output: `10`

**Example 2:**
- Input: `heights = [2,4]`
- Output: `4`

## Approach: Monotonic Stack（单调递增栈）

**Key Insight:** 对每个柱子，找它能向左右延伸多远（作为最矮的那根），宽度 × 高度 = 面积。用单调递增栈来高效找到左右边界。

和 **42 题 Trapping Rain Water** 很像，但区别是：
- 42 题：取两边最大值的 **min**，减去当前高度 → 能接多少水
- 84 题：取当前高度作为最矮，往两边延伸 → 能围多大面积

### Code

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # pair: (index, height)
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
        for index, height in stack:
            max_area = max(max_area, (len(heights) - index) * height)
        return max_area
```

## 逐步解析

### Step 1: 遍历每个柱子

```python
for i, h in enumerate(heights):
    start = i
```

`start` 记录当前柱子的矩形**最左能到哪里**，初始设为自己的位置。

### Step 2: While 循环 — 碰到矮柱子时结算面积

```python
while stack and h < stack[-1][1]:
    index, height = stack.pop()
    max_area = max(max_area, height * (i - index))
    start = index
```

当前柱子比栈顶**矮**时，说明栈顶的柱子**不能再往右延伸了**，所以 pop 出来结算：
- `height * (i - index)` = 被 pop 柱子的高度 × 它能覆盖的宽度

### ⭐ Step 3: `start = index` 的作用（重点！）

> **"我比你矮，所以你的地盘我也能占"**

Pop 掉高柱子后，当前矮柱子可以**往左延伸**到被 pop 柱子的起始位置，因为矮柱子一定能放在高柱子下面。

**例子：`heights = [5, 3]`**

没有 `start` 的话：
```
pop (0, 5) → area = 5*1 = 5
push (1, 3)           ← index=1，以为h=3只从index 1开始
cleanup: 3 * (2-1) = 3  ← 只算了1格宽 ❌
```

有 `start` 的话：
```
pop (0, 5) → area = 5*1 = 5
start = 0             ← 记住被pop掉的柱子从index 0开始
push (0, 3)           ← h=3可以往左延伸到index 0
cleanup: 3 * (2-0) = 6  ← 正确！2格宽 ✅
```

⭐ **`start` 在 cleanup 阶段至关重要**，因为 cleanup 靠 `index` 来算宽度 `len(heights) - index`。如果 index 记错了，宽度就少算了。

### Step 4: Push 当前柱子

```python
stack.append((start, h))
```

注意用 `start` 而不是 `i`，因为当前柱子可能已经"继承"了被 pop 柱子的起始位置。

⭐ **Python 的 list 用 `append()` 添加元素，不是 `push()`！** 大部分其他语言（JS/Java/C++）用 `push`，容易混淆。

### Step 5: Cleanup — 处理栈中剩余的柱子

```python
for index, height in stack:
    max_area = max(max_area, (len(heights) - index) * height)
```

留在栈里的柱子从没遇到比它们矮的，说明它们可以一直延伸到数组末尾。宽度 = `len(heights) - index`。

## 完整 Walkthrough

`heights = [2, 1, 5, 6, 2, 3]`

| Step | Action | Stack | maxArea |
|------|--------|-------|---------|
| i=0, h=2 | push (0,2) | [(0,2)] | 0 |
| i=1, h=1 | pop (0,2): 2×(1-0)=2, start=0. push (0,1) | [(0,1)] | 2 |
| i=2, h=5 | push (2,5) | [(0,1),(2,5)] | 2 |
| i=3, h=6 | push (3,6) | [(0,1),(2,5),(3,6)] | 2 |
| i=4, h=2 | pop (3,6): 6×1=6. pop (2,5): 5×2=10, start=2. push (2,2) | [(0,1),(2,2)] | 10 |
| i=5, h=3 | push (5,3) | [(0,1),(2,2),(5,3)] | 10 |
| Cleanup | (0,1):1×6=6. (2,2):2×4=8. (5,3):3×1=3 | — | **10** |

## Notes

- **单调栈保持递增顺序**：每个柱子最多 push 和 pop 各一次 → O(n)
- **`append` vs `push`**：Python list 用 `append()`，不是 `push()`
- **`start` 不能省**：它把被 pop 柱子的左边界传递给当前柱子，cleanup 阶段靠它算正确的宽度
- 时间复杂度：O(n)
- 空间复杂度：O(n)
