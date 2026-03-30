# Avoiding O(n²) — Patterns and Techniques

> **Core insight:** Almost every O(n²) brute force comes from the same shape — a nested loop where the inner loop re-examines work the outer loop already touched. Each technique below eliminates that redundancy in a different way.

---

## 1. Hash Map / Hash Set — O(1) Lookups Replace Inner Loops

### Why the brute force is O(n²)
You check every pair `(i, j)` with two nested loops to find a match, a duplicate, or a relationship.

### How it helps
Store already-seen elements in a hash map/set. Instead of scanning backwards with an inner loop, do a single O(1) lookup.

### Optimized complexity
**O(n)** time, **O(n)** space.

### Classic examples

#### Two Sum (LC 1)
```
Brute force: for each i, scan j = i+1..n to find target - nums[i].  → O(n²)

Optimized:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```
One pass, one lookup per element.

#### Contains Duplicate (LC 217)
```
Brute force: compare every pair.  → O(n²)

Optimized:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

#### Longest Consecutive Sequence (LC 128)
```
Brute force: for each number, scan the array repeatedly to build its streak.  → O(n²)

Optimized:
    num_set = set(nums)
    best = 0
    for num in num_set:
        if num - 1 not in num_set:        # only start from the bottom of a streak
            length = 1
            while num + length in num_set:
                length += 1
            best = max(best, length)
    return best
```
Each number is visited at most twice → **O(n)**.

---

## 2. Two Pointers — Converging From Both Ends

### Why the brute force is O(n²)
You enumerate all pairs `(i, j)` to find the best/valid one.

### How it helps
After sorting (or on a sorted/structured input), place one pointer at the start and one at the end. Move them inward based on a condition, pruning huge swaths of pairs you never need to check.

### Optimized complexity
**O(n)** for the scan (often **O(n log n)** total if sorting is required).

### Classic examples

#### 3Sum (LC 15)
```
Brute force: three nested loops over all triplets.  → O(n³)

Optimized (sort + two pointers brings it to O(n²), which is the known optimal):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue                        # skip duplicate anchor
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if s < 0:    lo += 1
            elif s > 0:  hi -= 1
            else:
                result.append([nums[i], nums[lo], nums[hi]])
                while lo < hi and nums[lo] == nums[lo+1]: lo += 1
                while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
                lo += 1; hi -= 1
```
The outer loop is O(n); the two-pointer scan inside is O(n) → **O(n²)** total, down from O(n³).

#### Container With Most Water (LC 11)
```
Brute force: check area for every pair of lines.  → O(n²)

Optimized:
    lo, hi = 0, len(height) - 1
    best = 0
    while lo < hi:
        best = max(best, min(height[lo], height[hi]) * (hi - lo))
        if height[lo] < height[hi]:
            lo += 1       # moving the shorter line inward is the only way to possibly increase area
        else:
            hi -= 1
    return best
```
Single pass → **O(n)**.

---

## 3. Sliding Window — Maintain a Window Instead of Recalculating

### Why the brute force is O(n²)
For every starting index, you expand rightward recalculating a property from scratch.

### How it helps
Keep a running window `[left, right]`. Expand `right` to include new elements; shrink `left` to restore the invariant. Each element enters and leaves the window at most once.

### Optimized complexity
**O(n)** time (amortized — each pointer moves at most n times).

### Classic examples

#### Longest Substring Without Repeating Characters (LC 3)
```
Brute force: for every start i, expand j until a repeat; track max length.  → O(n²)

Optimized:
    seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best
```

#### Minimum Window Substring (LC 76)
```
Brute force: check all substrings for containment.  → O(n²·m)

Optimized: expand right to satisfy the requirement, then shrink left to minimize.
Both pointers traverse the string once → O(n).
```

**When to suspect sliding window:** the problem asks for a *contiguous subarray/substring* optimizing some property (longest, shortest, max sum with constraint).

---

## 4. Sorting + Linear Scan

### Why the brute force is O(n²)
Without order, you must compare every element to every other to detect overlaps, duplicates, or adjacency.

### How it helps
Sort first — O(n log n). Now related elements are adjacent, so a single left-to-right pass finishes the job.

### Optimized complexity
**O(n log n)** (dominated by the sort).

### Classic examples

#### Meeting Rooms (LC 252)
```
Brute force: compare every pair of intervals for overlap.  → O(n²)

Optimized:
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False        # overlap
    return True
```

#### Merge Intervals (LC 56)
```
Brute force: repeatedly scan for overlapping pairs and merge.  → O(n²)

Optimized:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```
Sort once, merge in one pass → **O(n log n)**.

---

## 5. Prefix Sum — Precompute Cumulative Sums

### Why the brute force is O(n²)
To find the sum of every subarray `nums[i..j]`, you re-add elements for each `(i, j)` pair.

### How it helps
Build `prefix[k] = nums[0] + ... + nums[k-1]`. Then `sum(nums[i..j]) = prefix[j+1] - prefix[i]` in O(1). Combine with a hash map to find matching prefix sums in a single pass.

### Optimized complexity
**O(n)** time, **O(n)** space.

### Classic examples

#### Subarray Sum Equals K (LC 560)
```
Brute force: enumerate all subarrays and sum each.  → O(n²) or O(n³)

Optimized:
    count = 0
    current_sum = 0
    prefix_counts = {0: 1}      # empty prefix has sum 0
    for num in nums:
        current_sum += num
        # If (current_sum - k) was a prefix sum before, then the subarray
        # between that prefix and here sums to k.
        count += prefix_counts.get(current_sum - k, 0)
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
    return count
```

#### Range Sum Query — Immutable (LC 303)
```
Precompute prefix sums once in O(n), answer every query in O(1).
Without prefix sums, each query is O(n).
```

**Key pattern:** whenever you see "subarray sum equals / divisible by / at most K", think *prefix sum + hash map*.

---

## 6. Monotonic Stack — Avoid Re-scanning for Next Greater/Smaller

### Why the brute force is O(n²)
For each element, you scan rightward (or leftward) to find the next greater/smaller element.

### How it helps
Maintain a stack of *candidates* in monotonic order. As you process each new element, pop all candidates it "answers." Each element is pushed and popped at most once → amortized O(1) per element.

### Optimized complexity
**O(n)** time, **O(n)** space.

### Classic examples

#### Next Greater Element (LC 496 / LC 503)
```
Brute force: for each element, scan right for the first larger value.  → O(n²)

Optimized:
    stack = []          # stores indices; values are in decreasing order
    result = [-1] * len(nums)
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            result[stack.pop()] = num
        stack.append(i)
```

#### Largest Rectangle in Histogram (LC 84)
```
Brute force: for each bar, expand left and right to find how far it extends.  → O(n²)

Optimized:
    stack = []          # indices of bars in increasing height order
    max_area = 0
    for i, h in enumerate(heights + [0]):   # sentinel 0 forces final flush
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area
```
Every bar is pushed once and popped once → **O(n)**.

**When to suspect monotonic stack:** the problem asks "for each element, find the nearest larger/smaller element to the left/right."

---

## 7. Binary Search — Divide the Search Space

### Why the brute force is O(n²)
An inner loop performs a linear scan to find a value or boundary.

### How it helps
If the data is sorted (or you can sort it), replace the inner linear scan with binary search: O(log n) per query instead of O(n).

### Optimized complexity
**O(n log n)** (n outer iterations × log n binary search each).

### Classic examples

#### Two Sum II — Input Array Is Sorted (LC 167)
```
Brute force: check all pairs.  → O(n²)

Option A — Binary search: for each element, binary search for complement.  → O(n log n)
Option B — Two pointers (see §2) brings it to O(n).
```

#### Find K Closest Elements (LC 658)
```
Brute force: compute distance for every element, sort, take top k.

Optimized: binary search for the left boundary of the k-length window.  → O(log n + k)
```

#### Russian Doll Envelopes (LC 354)
```
Brute force DP: for each envelope, scan all previous ones.  → O(n²)

Optimized: sort by width ascending (height descending for ties), then find the
Longest Increasing Subsequence on heights using binary search (patience sorting).
→ O(n log n)
```

**General rule:** whenever an inner loop is searching a sorted range, replace it with `bisect_left` / `bisect_right`.

---

## 8. Divide and Conquer — Split the Problem in Half

### Why the brute force is O(n²)
Processing the entire array in a nested fashion because subproblems overlap or aren't decomposed.

### How it helps
Split the array in half, solve each half recursively, then merge. If the merge step is O(n), the recurrence `T(n) = 2T(n/2) + O(n)` gives **O(n log n)** by the Master Theorem.

### Optimized complexity
**O(n log n)**.

### Classic examples

#### Merge Sort / Sort an Array (LC 912)
```
Brute force (selection/insertion sort): find min in unsorted portion, repeat.  → O(n²)

Merge sort:
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)       # merge two sorted halves in O(n)
```

#### Count of Smaller Numbers After Self (LC 315)
```
Brute force: for each element, count how many elements to its right are smaller.  → O(n²)

Optimized: modified merge sort — during the merge step, count inversions
(how many elements from the right half get placed before elements from the left half).
Each merge is O(n), recursion depth is log n → O(n log n).
```

---

## Quick-Reference Decision Table

| Signal in the problem | Try this first |
|---|---|
| "Find a pair that sums to X" | Hash Map |
| "Find all pairs / triplets" on sorted data | Two Pointers |
| "Longest/shortest contiguous subarray with property P" | Sliding Window |
| "Overlapping intervals" or "sort then compare neighbors" | Sort + Linear Scan |
| "Subarray sum equals / divisible by K" | Prefix Sum + Hash Map |
| "Next greater/smaller element" or "largest rectangle" | Monotonic Stack |
| Inner loop searches a sorted range | Binary Search |
| Problem naturally splits into independent halves | Divide and Conquer |

---

## General Heuristics

1. **If you see two nested loops and the inner loop is a lookup** → hash map / set.
2. **If you see two nested loops and the data is sorted** → two pointers or binary search.
3. **If you see repeated subarray/substring sum calculations** → prefix sum or sliding window.
4. **If the brute force scans left/right for every element** → monotonic stack.
5. **If the problem has optimal substructure and splits cleanly** → divide and conquer.

The goal is always the same: **make the inner loop do O(1) or O(log n) work, or eliminate it entirely.**
