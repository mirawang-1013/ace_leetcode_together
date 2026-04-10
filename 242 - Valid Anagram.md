
# 242. Valid Anagram

**Difficulty:** Easy
**Tags:** Hash Table, String, Sorting

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`.

Anagram = 用完全相同的字母重新排列（每个字母出现次数一样）。

- `s = "anagram", t = "nagaram"` → `true`
- `s = "rat", t = "car"` → `false`

## 三种计数方法

### 方法 1: Counter（最简洁）

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

`Counter("anagram")` → `{'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}`

### 方法 2: dict.get(key, default)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1    # 不存在就从 0 开始
        for c in t:
            count[c] = count.get(c, 0) - 1    # 减回去
        return all(v == 0 for v in count.values())
```

`dict.get(key, 0)` — key 存在就返回 value，不存在就返回 0（不会 KeyError）。

### 方法 3: defaultdict(int)

```python
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = defaultdict(int)    # 访问不存在的 key 自动返回 0
        for c in s:
            count[c] += 1
        for c in t:
            count[c] -= 1
        return all(v == 0 for v in count.values())
```

`defaultdict(int)` — 任何 key 第一次访问时自动初始化为 `int()` = 0。

## ⚠️ 三种方法对比

| 方法 | 写法 | 适用场景 |
|------|------|---------|
| `Counter(s)` | 一行搞定 | 快速计数，面试首选 |
| `dict.get(c, 0)` | 手动计数 | 不想 import，练习基础 |
| `defaultdict(int)` | 自动初始化 | 需要频繁更新的场景（如 Valid Sudoku） |

## ⚠️ 常犯错误

1. **`dict[key] += 1` 直接写会 KeyError** — key 不存在时不能直接 +=，必须先初始化
2. **不要多余 `sorted()`** — 排序是 O(n log n)，用 dict 计数是 O(n)，加了排序反而慢

## Notes

- 时间复杂度：O(n) — 遍历两个字符串
- 空间复杂度：O(1) — 最多 26 个字母，常数空间
- `Counter` 底层就是 `dict` 的子类，自带计数功能
