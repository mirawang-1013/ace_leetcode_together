
# 217. Contains Duplicate

**Difficulty:** Easy
**Tags:** Array, Hash Table

## Problem

Given an array `nums`, return `true` if any value appears at least twice, `false` if every element is distinct.

## Approach: Set

**Key Insight:** 只需要判断"见没见过"，不需要存额外信息（如下标、次数），所以用 set 就够了。

### Code

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

## ⚠️ 什么时候用 set vs dict？

1. **只需要判断是否重复** → `set` 就够了
2. **需要看 count 大于多少** → `Counter` 或 `dict`

### 用 Counter 找出现次数 > 1 的数字

```python
from collections import Counter
counts = Counter(nums)  # {值: 出现次数}
return [num for num, count in counts.items() if count > 1]
```

### 用 dict 手动计数

```python
seen = {}
for num in nums:
    seen[num] = seen.get(num, 0) + 1
return [num for num, count in seen.items() if count > 1]
```

## Notes

- `in set` 是 O(1) 查找
- 时间复杂度：O(n)
- 空间复杂度：O(n)
