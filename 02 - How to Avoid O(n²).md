# How to Avoid O(n²)

The most common source of O(n²) is **nested loops** — for each element, you scan the rest of the array. The trick is always the same: **replace the inner loop with a smarter data structure or technique.**

---

## 1. Hash Map / Hash Set — O(1) Lookup

### The Problem
You need to find a pair/match in an array → brute force checks every pair.

### Brute Force O(n²)
```python
# Two Sum: find two numbers that add to target
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):  # inner loop = O(n)
        if nums[i] + nums[j] == target:
            return [i, j]
```

### Optimized O(n)
```python
# Store what we've seen, check if complement exists
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:        # O(1) lookup replaces inner loop
        return [seen[complement], i]
    seen[num] = i
```

### Why It Works
The hash map remembers all previous elements, so instead of scanning backwards (O(n)), you just ask "is the complement in the map?" (O(1)).

### LeetCode Examples
- **1 Two Sum** — HashMap for complement lookup
- **128 Longest Consecutive Sequence** — HashSet to check sequence membership
- **217 Contains Duplicate** — HashSet to detect repeats
- **49 Group Anagrams** — HashMap to group by sorted key

> **Rule of thumb:** If your inner loop is just "searching for something," replace it with a hash map.

---

## 2. Two Pointers — Converge from Both Ends

### The Problem
You need to find pairs in a sorted array → brute force tries all pairs.

### Brute Force O(n²)
```python
# Find pair with target sum in sorted array
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

### Optimized O(n)
```python
left, right = 0, len(nums) - 1
while left < right:
    total = nums[left] + nums[right]
    if total == target:
        return [left, right]
    elif total < target:
        left += 1    # need bigger sum
    else:
        right -= 1   # need smaller sum
```

### Why It Works
In a sorted array, if `nums[left] + nums[right]` is too small, moving `left` right increases the sum. If too big, moving `right` left decreases it. Each pointer moves at most n times → O(n) total.

### LeetCode Examples
- **15 3Sum** — Sort + fix one element + two pointers for other two
- **11 Container With Most Water** — Two pointers, move the shorter side
- **42 Trapping Rain Water** — Two pointers tracking max heights

> **Rule of thumb:** If the array is sorted (or you can sort it) and you need pairs, use two pointers.

---

## 3. Sliding Window — Maintain a Running Window

### The Problem
You need to check all subarrays/substrings → brute force generates all of them.

### Brute Force O(n²)
```python
# Longest substring without repeating characters
max_len = 0
for i in range(len(s)):
    seen = set()
    for j in range(i, len(s)):      # inner loop = O(n)
        if s[j] in seen:
            break
        seen.add(s[j])
        max_len = max(max_len, j - i + 1)
```

### Optimized O(n)
```python
seen = set()
left = 0
max_len = 0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1                    # shrink window
    seen.add(s[right])
    max_len = max(max_len, right - left + 1)
```

### Why It Works
Instead of restarting the inner scan from scratch, the window "slides" forward. The `left` pointer only moves right, never backwards. Each element is added and removed from the set at most once → O(n) total.

### LeetCode Examples
- **3 Longest Substring Without Repeating Characters** — Variable window + set
- **424 Longest Repeating Character Replacement** — Window + max frequency
- **76 Minimum Window Substring** — Shrinkable window + frequency map
- **121 Best Time to Buy and Sell Stock** — Track min price (simplified window)

> **Rule of thumb:** If you're checking contiguous subarrays/substrings, slide a window.

---

## 4. Sorting + Single Pass — Sort First, Then Linear Scan

### The Problem
You need to find relationships between elements → brute force compares all pairs.

### Brute Force O(n²)
```python
# Check if any two intervals overlap
for i in range(len(intervals)):
    for j in range(i + 1, len(intervals)):
        if overlaps(intervals[i], intervals[j]):
            return True
```

### Optimized O(n log n)
```python
intervals.sort(key=lambda x: x[0])  # O(n log n)
for i in range(1, len(intervals)):   # O(n)
    if intervals[i][0] < intervals[i - 1][1]:
        return True  # overlap found
```

### Why It Works
After sorting, overlapping intervals are adjacent. You only need to compare neighbors → one pass instead of all pairs. The sort costs O(n log n) but eliminates the O(n²) comparison.

### LeetCode Examples
- **56 Merge Intervals** — Sort by start, merge consecutive overlaps
- **435 Non-overlapping Intervals** — Sort + greedy removal
- **252 Meeting Rooms** — Sort + check adjacent overlaps
- **15 3Sum** — Sort enables two-pointer technique

> **Rule of thumb:** If order doesn't matter in the input but would help with comparisons, sort first.

---

## 5. Prefix Sum — Precompute Cumulative Values

### The Problem
You need sum of subarrays → brute force recomputes each sum from scratch.

### Brute Force O(n²)
```python
# Count subarrays with sum = k
count = 0
for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total += nums[j]
        if total == k:
            count += 1
```

### Optimized O(n)
```python
# prefix[j] - prefix[i] = sum(nums[i..j])
# So we need: prefix[j] - k = prefix[i] (some earlier prefix)
count = 0
prefix_sum = 0
seen = {0: 1}  # empty prefix
for num in nums:
    prefix_sum += num
    if prefix_sum - k in seen:
        count += seen[prefix_sum - k]
    seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
```

### Why It Works
`sum(nums[i..j]) = prefix[j] - prefix[i]`. Instead of recomputing sums, store all prefix sums in a hash map. For each new prefix, check if `prefix - k` was seen before → O(1) lookup.

### LeetCode Examples
- **560 Subarray Sum Equals K** — Prefix sum + hashmap
- **238 Product of Array Except Self** — Prefix/suffix product
- **53 Maximum Subarray** — Running sum (Kadane's is a simplified prefix idea)

> **Rule of thumb:** If you're repeatedly summing subarrays, precompute prefix sums.

---

## 6. Monotonic Stack — Avoid Re-scanning for Next Greater/Smaller

### The Problem
For each element, find the next greater/smaller element → brute force scans right for each.

### Brute Force O(n²)
```python
# Next greater element for each position
result = [-1] * len(nums)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[j] > nums[i]:
            result[i] = nums[j]
            break
```

### Optimized O(n)
```python
stack = []  # stores indices of elements waiting for their next greater
result = [-1] * len(nums)
for i in range(len(nums)):
    while stack and nums[i] > nums[stack[-1]]:
        result[stack.pop()] = nums[i]  # found next greater
    stack.append(i)
```

### Why It Works
The stack keeps elements that haven't found their answer yet, in decreasing order. When a bigger element arrives, it resolves all smaller elements on the stack. Each element is pushed and popped at most once → O(n) total.

### LeetCode Examples
- **84 Largest Rectangle in Histogram** — Monotonic stack for boundaries
- **42 Trapping Rain Water** — Stack-based approach
- **739 Daily Temperatures** — Next warmer day

> **Rule of thumb:** If you need "next greater/smaller" for each element, use a monotonic stack.

---

## 7. Binary Search — Halve the Search Space

### The Problem
You're searching in sorted/monotonic data → brute force scans linearly.

### Brute Force O(n)
```python
# Find target in sorted array
for i in range(len(nums)):
    if nums[i] == target:
        return i
```

### Optimized O(log n)
```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

### Why It Works
Each comparison eliminates half the remaining elements. After log₂(n) steps, only one element remains.

### When It Turns O(n²) → O(n log n)
If your inner loop is a linear search on sorted data, replacing it with binary search drops O(n²) to O(n log n).

### LeetCode Examples
- **33 Search in Rotated Sorted Array** — Modified binary search
- **153 Find Minimum in Rotated Sorted Array** — Binary search on rotation
- **300 Longest Increasing Subsequence** — DP + binary search = O(n log n)

> **Rule of thumb:** If data is sorted or has a monotonic property, binary search.

---

## Quick Reference Cheat Sheet

| Brute Force Pattern | Optimization | Result |
|--------------------|-------------|--------|
| Nested loop searching for match | **Hash Map/Set** | O(n²) → O(n) |
| All pairs in sorted array | **Two Pointers** | O(n²) → O(n) |
| All subarrays/substrings | **Sliding Window** | O(n²) → O(n) |
| All pairs for ordering | **Sort + scan** | O(n²) → O(n log n) |
| Repeated subarray sums | **Prefix Sum** | O(n²) → O(n) |
| Next greater/smaller scan | **Monotonic Stack** | O(n²) → O(n) |
| Linear search in sorted data | **Binary Search** | O(n) → O(log n) |

---

## The Universal Question

When you see O(n²), ask yourself:

> **"What is my inner loop doing, and can a data structure do it in O(1)?"**

- Searching → **Hash Map**
- Comparing pairs → **Two Pointers** (if sorted)
- Re-scanning subarrays → **Sliding Window** or **Prefix Sum**
- Finding next greater/smaller → **Monotonic Stack**
- Searching in sorted data → **Binary Search**
