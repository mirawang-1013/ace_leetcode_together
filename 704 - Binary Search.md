# 704. Binary Search

**Difficulty:** Easy
**Tags:** Array, Binary Search

## Problem

Given a sorted array `nums` and a `target`, return the index of `target`. If not found, return `-1`.

### Examples

**Example 1:**
- Input: `nums = [-1,0,3,5,9,12], target = 9`
- Output: `4`

**Example 2:**
- Input: `nums = [-1,0,3,5,9,12], target = 2`
- Output: `-1`

## Approach: Binary Search

**Key Insight:** 数组已排序，每次看中间值，比 target 大就砍右半边，比 target 小就砍左半边。每次搜索空间减半 → O(log n)。

### Code

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
```

## Walkthrough

`nums = [-1, 0, 3, 5, 9, 12], target = 9`

| Step | left | right | mid | nums[mid] | Action |
|------|------|-------|-----|-----------|--------|
| 1 | 0 | 5 | 2 | 3 | 3 < 9, left = 3 |
| 2 | 3 | 5 | 4 | 9 | found! return 4 |

## ⭐ Key Takeaway: `mid+1` / `mid-1`

更新 left 和 right 时必须**跳过 mid**：

```python
left = mid + 1    # mid 已经比过了，不需要再看
right = mid - 1   # 同理
```

如果写成 `left = mid` 或 `right = mid`，当 left 和 right 相邻时 mid 永远等于 left，**死循环**：

```
left=3, right=4 → mid=3 → left=mid=3 → mid=3 → 永远卡住 ❌
left=3, right=4 → mid=3 → left=mid+1=4 → 继续或结束 ✅
```

## ⭐ 不要用 `target not in nums` 提前判断

`in` 操作是 O(n) 线性扫描，加了这行整个算法变成 O(n)，二分搜索就白写了。让二分搜索自己通过 `left > right` 来判断找不到。

## Notes

- `while left <= right`：用 `<=` 因为 left == right 时还有一个元素没检查
- `mid` 每次在循环里重新算，不需要提前初始化
- 时间复杂度：O(log n)
- 空间复杂度：O(1)
