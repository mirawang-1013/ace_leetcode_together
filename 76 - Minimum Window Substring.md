# 76. Minimum Window Substring

**Difficulty:** Hard
**Tags:** Hash Table, String, Sliding Window

## Problem

Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return `""`.

### Examples

**Example 1:**
- Input: `s = "ADOBECODEBANC"`, `t = "ABC"`
- Output: `"BANC"`

**Example 2:**
- Input: `s = "a"`, `t = "a"`
- Output: `"a"`

**Example 3:**
- Input: `s = "a"`, `t = "aa"`
- Output: `""` (t 中有两个 'a'，但 s 中只有一个)

### Constraints

- `1 <= s.length, t.length <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

## Approach: Sliding Window + Counter

**Key Insight:**
1. 先用 Counter 记录 t 中需要的字符和数量。
2. 右指针扩大窗口，每遇到一个"真正需要的"字符就减少 `missing`。
3. 当 `missing == 0` 时，窗口满足条件，尝试从左边缩小。
4. 缩小直到不满足条件，记录过程中的最小窗口。

### Steps

1. `need = Counter(t)`，`missing = len(t)` 表示还缺多少个字符。
2. `right` 遍历 s：如果 `need[s[right]] > 0`，说明这个字符是真正需要的，`missing -= 1`。无论如何 `need[s[right]] -= 1`。
3. 当 `missing == 0` 时进入 while 循环，尝试缩小窗口，更新最小值。
4. 缩小时 `need[s[left]] += 1`，如果 `> 0` 说明缩掉了一个必须的字符，`missing += 1`。

### Time & Space Complexity

- **Time:** O(n) — n 是 s 的长度，每个字符最多被访问两次（左右指针各一次）。
- **Space:** O(m) — m 是字符集大小。

## Solution (Python)

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        min_len = float('inf')
        left = 0
        start = 0

        for right in range(len(s)):
            if need[s[right]] > 0:
                missing -= 1
            need[s[right]] -= 1

            while missing == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return "" if min_len == float('inf') else s[start:start + min_len]
```

## 我的错误 & 易错点

### `while missing == 0` 的缩进位置

**我把 `while missing == 0` 写在了 `for` 循环外面。** 这导致只有当 `right` 走完整个字符串后才会尝试缩小窗口，错过了中间所有可能的更短窗口。

```python
# ✗ 错误：while 在 for 外面
for right in range(len(s)):
    ...

while missing == 0:    # right 已经固定在末尾了
    ...

# ✓ 正确：while 在 for 里面
for right in range(len(s)):
    ...

    while missing == 0:    # 每次 right 移动后都尝试缩小
        ...
```

**滑动窗口的关键：扩大和缩小必须在同一个循环内交替进行，不能分开。**

## Key Details

### `need[s[right]]` 的值怎么理解？

- `> 0`：这个字符还被需要，是"真正有用的"。
- `== 0`：刚好够了。
- `< 0`：窗口里这个字符多余了（或者它根本不在 t 里）。

`missing` 只在 `need` 从正变零时减少，从零变正时增加，所以它精确追踪的是"还缺几个有效字符"。

### 为什么 `need[s[right]] -= 1` 无条件执行？

不管这个字符是不是 t 里的，都减 1。如果不在 t 里，`need` 值会变成负数，但不影响 `missing`。这样在缩小窗口时 `+= 1` 回来，如果还是 `<= 0`，就知道它不是必须的字符，不需要增加 `missing`。
