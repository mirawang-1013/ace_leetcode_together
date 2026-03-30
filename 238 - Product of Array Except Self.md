# 238. Product of Array Except Self

**Difficulty:** Medium
**Tags:** Array, Prefix Product

## Problem

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

- Must run in O(n) time
- Cannot use division

### Examples

**Example 1:**
- Input: `nums = [1,2,3,4]`
- Output: `[24,12,8,6]`

**Example 2:**
- Input: `nums = [-1,1,0,-3,3]`
- Output: `[0,0,9,0,0]`

## Approach: Left & Right Product Arrays

**Key Insight:** "除了自己以外所有元素的乘积" = "左边所有元素的乘积" × "右边所有元素的乘积"。把自己去掉后，剩下的元素天然分成左右两部分。

以 `i=2`（值为3）为例：

```
nums = [1, 2, 3, 4]
             ^
          左边｜右边
        [1, 2]  [4]

左边乘积: 1 × 2 = 2
右边乘积: 4
答案:     2 × 4 = 8   ← 就是 1×2×4，跳过了3
```

### Steps

1. 构建 `left` 数组：`left[i]` = `nums[0]` 到 `nums[i-1]` 的乘积（`left[0] = 1`）
2. 构建 `right` 数组：`right[i]` = `nums[i+1]` 到 `nums[n-1]` 的乘积（`right[n-1] = 1`）
3. `res[i] = left[i] * right[i]`

### Code

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lens = len(nums)
        res = [0] * lens
        left = [0] * lens
        right = [0] * lens

        left[0] = 1
        right[lens - 1] = 1

        for i in range(1, lens):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(lens - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(lens):
            res[i] = left[i] * right[i]

        return res
```

## Notes

- `range(lens-2, -1, -1)`：从倒数第二个下标到0，倒着遍历。`range` 的终点不包含，所以写 `-1` 才能遍历到 `0`
- 时间复杂度：O(n)，三次遍历
- 空间复杂度：O(n)，用了 left、right、res 三个数组
