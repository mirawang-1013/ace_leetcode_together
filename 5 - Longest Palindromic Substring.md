# 5. Longest Palindromic Substring

**Difficulty:** Medium
**Tags:** String, Dynamic Programming, Two Pointers

## Problem

Given a string `s`, return the longest palindromic substring in `s`.

### Examples

**Example 1:**
- Input: `s = "babad"`
- Output: `"bab"` (or `"aba"`)

**Example 2:**
- Input: `s = "cbbd"`
- Output: `"bb"`

### Constraints

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

## Approach: Expand from Center

**Key Insight:** 回文从中心向两边对称。把每个位置当中心，向两边扩展，看能扩多长。

注意回文有两种：
- **奇数长度**：单中心，如 `"bab"` 中心是 `a`
- **偶数长度**：双中心，如 `"bb"` 中心是两个 `b`

所以每个位置要展开两次。

### Steps

1. 定义 `expand(l, r)` 函数，从中心向两边扩展。
2. 遍历每个位置 `i`：
   - 奇数展开：`expand(i, i)`
   - 偶数展开：`expand(i, i+1)`
3. 每次取 odd、even 和之前 result 中最长的。

### Time & Space Complexity

- **Time:** O(n²) — n 个中心，每个最多展开 n 次。
- **Space:** O(1) — 只用了指针，不算返回值。

## Solution (Python)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i+1)
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even

        return result
```

## Key Details

### expand 在做什么？

从中心向两边走，每一步检查 `s[l] == s[r]`（这就是确认对称的地方），相等就继续往外扩：

```
expand(2, 2)，s = "babad"
                ↓ 中心
            b a b a d

l=2, r=2 → s[2]='b' == s[2]='b' ✅ → l=1, r=3
l=1, r=3 → s[1]='a' == s[3]='a' ✅ → l=0, r=4
l=0, r=4 → s[0]='b' != s[4]='d' ❌ → 停止
返回 s[1:4] = "aba"
```

### 为什么返回 `s[l+1:r]`？

while 停下来时，`l` 和 `r` 多走了一步，指向的是**不对称的位置**：

```
s = "babad"，expand(2,2)

while 结束时: l=0, r=4
s[0]='b' != s[4]='d'  ← 这两个不是回文的一部分

实际回文是 s[1] 到 s[3] = "aba"
所以 s[l+1 : r] = s[1:4] = "aba"
```

### 为什么要展开两次（odd 和 even）？

```python
odd  = expand(i, i)    # 单中心：奇数长度回文，如 "aba"
even = expand(i, i+1)  # 双中心：偶数长度回文，如 "bb"
```

如果只展开一次，会漏掉一种情况。比如 `s = "cbbd"`：
- `expand(1,1)` → `"b"` — 只找到奇数回文
- `expand(1,2)` → `"bb"` ✅ — 偶数回文在这里

### 三者取最长怎么理解？

每个位置产生两个候选，和之前的最长比较，谁长留谁：

```
s = "cbbd"

i=0: odd="c"   even=""    → result="c"
i=1: odd="b"   even="bb"  → result="bb"   ← even 更长，更新！
i=2: odd="b"   even=""    → result="bb"   ← 没更长，不变
i=3: odd="d"   even=""    → result="bb"

最终 return "bb"
```
