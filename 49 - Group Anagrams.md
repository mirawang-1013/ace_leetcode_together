# 49. Group Anagrams

**Difficulty:** Medium
**Tags:** Array, Hash Table, String, Sorting

## Problem

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

### Examples

**Example 1:**
- Input: `strs = ["eat","tea","tan","ate","nat","bat"]`
- Output: `[["bat"],["nat","tan"],["ate","eat","tea"]]`

**Example 2:**
- Input: `strs = [""]`
- Output: `[[""]]`

**Example 3:**
- Input: `strs = ["a"]`
- Output: `[["a"]]`

### Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Approach: Sorted String as Key

**Key Insight:** Anagrams produce the same string when sorted. Use the sorted string as a dictionary key to group them.

### Steps

1. Create a `defaultdict(list)` to group words.
2. For each word, sort its characters and join into a string → use as key.
3. Append the original word to the list under that key.
4. Return all values as a list.

### Time & Space Complexity

- **Time:** O(n * k log k) — where n is the number of strings, k is the max string length (sorting each string).
- **Space:** O(n * k) — for storing all strings in the dictionary.

## Solution (Python)

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i in strs:
            terms = ''.join(sorted(i))
            group[terms].append(i)
        return list(group.values())
```

## Key Details

### Why `''.join(sorted(i))` instead of just `sorted(i)`?

`sorted(i)` returns a **list**, and lists can't be dictionary keys (they're mutable/unhashable):

```python
sorted("eat")          # ['a', 'e', 't']  → list, CANNOT be a dict key
''.join(sorted("eat")) # 'aet'            → string, CAN be a dict key
```

Using `sorted(i)` directly as a key would raise:
```
TypeError: unhashable type: 'list'
```

**Alternative:** `tuple(sorted(i))` also works since tuples are hashable.

### Why `list(group.values())` instead of just `group.values()`?

`group.values()` returns a `dict_values` view object, not an actual list:

```python
group = {"aet": ["eat","tea","ate"], "ant": ["tan","nat"]}

group.values()       # dict_values([["eat","tea","ate"], ["tan","nat"]])  → view object
list(group.values()) # [["eat","tea","ate"], ["tan","nat"]]               → actual list
```

The return type expects `List[List[str]]`, so `list()` converts the view into a proper list for type correctness.
