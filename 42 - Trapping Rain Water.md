# 42. Trapping Rain Water

**Difficulty:** Hard
**Tags:** Array, Two Pointers, Left-Right Array

## Problem

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

### Examples

**Example 1:**
- Input: `height = [0,1,0,2,1,0,1,3,2,1,2,1]`
- Output: `6`

**Example 2:**
- Input: `height = [4,2,0,3,2,5]`
- Output: `9`

## Approach: Left-Right Max Arrays

**Key Insight:** 每个位置能接多少水，取决于它左边最高的柱子和右边最高的柱子中较矮的那个，减去自身高度：

```
water[i] = min(left_max[i], right_max[i]) - height[i]
```

和 **238 题**是同一个模式！238 是左右乘积，这题是左右最大值。

### 图示

```
height:    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
left_max:  [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
right_max: [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
min:       [0, 1, 1, 2, 2, 2, 2, 3, 2, 2, 2, 1]
water:     [0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0] → 总和 = 6
```

### Code

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        total = 0
        for i in range(n):
            total += min(left_max[i], right_max[i]) - height[i]

        return total
```

## Notes

- **不要用 `min`、`max`、`sum` 作为变量名**，会覆盖 Python 内置函数，导致 `TypeError: 'list' object is not callable`
- **预分配 `[0] * n`** 比反复 `append` 快，避免列表动态扩容
- **直接累加 total** 而不是创建额外列表，省空间
- 如果从右往左 `append` 构建 `right_max`，记得最后要 `reverse` 或用 `[::-1]`
- 时间复杂度：O(n)
- 空间复杂度：O(n)

## 左右数组模式总结

| 题目 | 左边算什么 | 右边算什么 | 合并方式 |
|------|-----------|-----------|---------|
| 238 Product of Array Except Self | 左边所有元素的**乘积** | 右边所有元素的**乘积** | 相乘 |
| 42 Trapping Rain Water | 左边所有柱子的**最大值** | 右边所有柱子的**最大值** | 取 min 再减 height |

核心都是：**从左扫一遍，从右扫一遍，合并结果。**
