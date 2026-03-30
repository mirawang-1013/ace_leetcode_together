# 347. Top K Frequent Elements

**Difficulty:** Medium
**Tags:** Array, Hash Table, Bucket Sort, Counting

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

### Examples

**Example 1:**
- Input: `nums = [1,1,1,2,2,3], k = 2`
- Output: `[1,2]`

**Example 2:**
- Input: `nums = [1], k = 1`
- Output: `[1]`

### Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.

## Approach: Bucket Sort

**Key Insight:** Use frequency as the array index. Create a bucket where `bucket[i]` stores all numbers that appear `i` times. Then walk backwards from the highest index to collect the top k frequent elements.

### Steps

1. Count frequency of each number with `Counter`.
2. Create a bucket list of size `len(nums) + 1` (because max frequency = `len(nums)`).
3. Place each number into `bucket[its frequency]`.
4. Walk the bucket **backwards** (highest frequency first), collect numbers until we have `k`.

### Time & Space Complexity

- **Time:** O(n) — no sorting needed.
- **Space:** O(n) — for the bucket and counter.

### Comparison with Other Approaches

| Approach | Time | Why |
|---|---|---|
| **Bucket sort** | O(n) | No sorting — frequency becomes index, walk backwards |
| `most_common(k)` | O(n log k) | Uses a heap internally |
| Sort by frequency | O(n log n) | Sorting all unique elements |

## Solution (Python)

```python
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
```

## Key Details

### 为什么 bucket 要 `len(nums) + 1` 个？

某个数字最多可能出现 `len(nums)` 次（整个数组都是它），需要 `bucket[len(nums)]` 存在：

```python
nums = [1, 1, 1]  # 1 出现 3 次
bucket = [[] for _ in range(3)]    # index 0,1,2 → bucket[3] 越界！
bucket = [[] for _ in range(3+1)]  # index 0,1,2,3 → bucket[3] 可以用 ✅
```

### 为什么 bucket 是 `[[] for ...]` 而不是 `[0, 0, ...]`？

每个频率位置可能有**多个数字**，所以需要用 list 来装：

```python
# nums = [1,1,2,2,3], count = {1:2, 2:2, 3:1}
# bucket[2] = [1, 2]  ← 两个数字都出现了 2 次
```

### 为什么倒着走 `range(len(bucket)-1, 0, -1)`？

index 越大 = 频率越高，倒着走就是从最高频率开始取：

```python
# bucket: [], [3], [2], [1], [], [], []
# index:   0   1    2    3   4   5   6

# range(6, 0, -1) → 6, 5, 4, 3, 2, 1
# i=6 → [] 跳过
# i=3 → [1] → 频率最高！取出
# i=2 → [2] → 第二高！取出 → 够 k=2 个了，return
```

### 常见错误

**1. `for freq, num in count` → 报错 `cannot unpack non-iterable int`**

```python
for x in count:            # 只遍历 key（单个 int），不能 unpack
for num, freq in count.items():  # 遍历 (key, value) 对 ✅
```

注意顺序是 `num, freq`，因为 Counter 的 key 是数字，value 是频率。

**2. `result.append(i)` → 加的是 index 而不是数字**

```python
result.append(i)            # 把频率加进去了 ❌
for num in bucket[i]:
    result.append(num)      # 把数字加进去 ✅
```

## Simpler Alternative: `most_common(k)`

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return [num for num, count in freq.most_common(k)]
```

O(n log k) 但代码更简洁。
