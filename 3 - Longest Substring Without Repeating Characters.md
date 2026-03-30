# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Tags:** Hash Table, String, Sliding Window

## Problem

Given a string `s`, find the length of the longest substring without repeating characters.

### Examples

**Example 1:**
- Input: `s = "abcabcbb"`
- Output: `3`
- Explanation: `"abc"` is the longest substring without repeating characters.

**Example 2:**
- Input: `s = "bbbbb"`
- Output: `1`

**Example 3:**
- Input: `s = "pwwkew"`
- Output: `3`
- Explanation: `"wke"` is the answer.

### Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

## Approach: Sliding Window + Set

**Key Insight:** 用一个 set 维护当前窗口内的字符，保证没有重复。当遇到重复字符时，从左边缩小窗口直到重复消除。

### Steps

1. 用 `set()` 记录当前窗口内的字符（有 not repeating 需求时一般都用 set）。
2. `r` 右指针遍历每个字符。
3. 如果 `s[r]` 已经在 set 里，不断从左边 remove 并移动 `l`，直到没有重复。
4. 把 `s[r]` 加入 set，用 `max()` 更新最长长度。

### Time & Space Complexity

- **Time:** O(n) — 每个字符最多被 add 和 remove 各一次。
- **Space:** O(min(n, m)) — m 是字符集大小。

## Solution (Python)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        l = 0
        L = 0
        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            L = max(L, r - l + 1)
        return L
```

## Key Details

### `substring.remove(s[l])` 是按什么顺序在 remove？

**不是按 set 的顺序，是按窗口从左到右的顺序。**

`remove(s[l])` 删的是**左指针 `l` 指向的那个字符**，然后 `l += 1` 往右移。这是在**从左边缩小窗口**，一个一个丢掉最左边的字符，直到重复的那个字符被丢掉为止。

用 `s = "abcb"` 走一遍：

```
r=0: s[r]='a' → set={a}，窗口 "a"，L=1
r=1: s[r]='b' → set={a,b}，窗口 "ab"，L=2
r=2: s[r]='c' → set={a,b,c}，窗口 "abc"，L=3
r=3: s[r]='b' → 'b' 在 set 里！需要缩窗口：
     while 循环：
       remove(s[l=0]) → remove('a') → set={b,c}，l=1
       'b' 还在 set 里！继续：
       remove(s[l=1]) → remove('b') → set={c}，l=2
       'b' 不在 set 了，停止 while
     add('b') → set={c,b}，窗口 "cb"，L=3
```

关键理解：**remove 的不是重复的那个字符本身，而是从左指针开始一个个删，直到把重复的那个删掉。** 中间可能会"误伤"其他字符（比如上面的 `'a'`），但没关系，因为窗口缩小了，这些字符本来就不在窗口里了。

### 为什么用 `max(L, r - l + 1)` 取最长？

`r - l + 1` 是当前窗口的长度。每次窗口变化后，和之前的最长值比较，保留更大的。这是 sliding window 题目里取最优值的标准写法。
