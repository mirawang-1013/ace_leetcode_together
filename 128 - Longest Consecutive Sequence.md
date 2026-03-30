# 128. Longest Consecutive Sequence

**Difficulty:** Medium
**Tags:** Array, Hash Table, Union Find

## Problem

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in **O(n)** time.

### Examples

**Example 1:**
- Input: `nums = [100, 4, 200, 1, 3, 2]`
- Output: `4`
- Explanation: `[1, 2, 3, 4]` is the longest consecutive sequence.

**Example 2:**
- Input: `nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]`
- Output: `9`
- Explanation: `[0, 1, 2, 3, 4, 5, 6, 7, 8]`

### Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Approach: HashSet

**Key Insight:** Only start counting from the **beginning** of a sequence (i.e., when `num - 1` is not in the set). This avoids redundant work and keeps the algorithm O(n).

### Steps

1. Add all numbers to a HashSet for O(1) lookup.
2. Iterate through each number:
   - If `num - 1` is **not** in the set → this is the start of a new sequence.
   - Count consecutive numbers starting from `num`.
   - Update the max length.
3. Return the max length.

### Time & Space Complexity

- **Time:** O(n) — each element is visited at most twice.
- **Space:** O(n) — for the HashSet.

## Solution (Python)

```python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only start counting if num is the start of a sequence
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest
```

## Why This Works

- By checking `num - 1 not in num_set`, we ensure we only start counting from the **smallest** element of each consecutive sequence.
- The inner `while` loop runs at most once per element across the entire outer loop, so total work is O(n), not O(n²).
- Example: for `[100, 4, 200, 1, 3, 2]`:
  - `100`: `99` not in set → count `[100]` → length 1
  - `4`: `3` is in set → skip (not a sequence start)
  - `200`: `199` not in set → count `[200]` → length 1
  - `1`: `0` not in set → count `[1, 2, 3, 4]` → length 4
  - `3`: `2` is in set → skip
  - `2`: `1` is in set → skip


```python
from typing import List

  
class Solution:

	def longestConsecutive(self, nums: List[int]) -> int:
	
	#check if the starting point int the number set first, and then use while to loop through to see how long the consecutive string could be.
	
		num_set = set(nums)
		longest = 0
	
		for num in num_set:
			print('num:',num)
		#如果比这个数小的数不在num_set里，那就是说明是起点
			if num-1 not in num_set:
				print('num-1',num-1)
				current = num
				print('current = num',current)
				count = 1
				print('count=1',)
		#看这个数+1是否在里面，如果是的话count一直往上加数字
				while current+1 in num_set: 
					current += 1
					print('current+=1',current)
					count += 1
					print('count+=1',count)
				longest = max(longest, count)
		
		return longest
```