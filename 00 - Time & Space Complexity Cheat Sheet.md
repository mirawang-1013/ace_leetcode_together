
# Time & Space Complexity Cheat Sheet

## 时间复杂度 — 数"代码跑了几次"

### 看循环和嵌套

| 你看到的 | 时间复杂度 |
|---------|-----------|
| 没有循环 | O(1) |
| 一个 `for` 遍历 n 个元素 | O(n) |
| 两个 `for` **嵌套** | O(n²) |
| 两个 `for` **并列**（不嵌套） | O(n) + O(n) = O(n) |
| 循环里每次砍一半（binary search） | O(log n) |
| 外层 for + 内层砍一半 | O(n log n) |

### 看循环里每一步的操作

| 操作 | 耗时 |
|------|------|
| `if x in set` / `if x in dict` | O(1) |
| `if x in list` | O(n) ← 坑！ |
| `list.append()` | O(1) |
| `list.sort()` | O(n log n) |
| `dict.get()` / `dict[key]` | O(1) |
| `list[i]` 按下标取值 | O(1) |
| `list.pop()` 末尾弹出 | O(1) |
| `list.pop(0)` 头部弹出 | O(n) ← 坑！ |

### 公式

> **总时间 = 循环次数 × 每步操作耗时**

### 实例对比

```python
# ✅ O(n) — set 查找是 O(1)
for num in nums:          # O(n) 次
    if num in seen:       # O(1)，seen 是 set
# → O(n) × O(1) = O(n)

# ❌ O(n²) — list 查找是 O(n)
for i in range(len(nums)):    # O(n) 次
    if gap in nums[i+1:]:     # O(n)，in list 线性扫描
# → O(n) × O(n) = O(n²)
```

---

## 空间复杂度 — 数"额外开了多少空间"

只算**额外**创建的空间，输入本身不算。

| 你看到的 | 空间复杂度 |
|---------|-----------|
| 只用了几个变量 (`left`, `right`, `mid`) | O(1) |
| 建了一个 set/dict，最多存 n 个元素 | O(n) |
| 建了一个二维数组 n×m | O(n×m) |
| 递归深度 d 层 | O(d)（调用栈） |

---

## 速记口诀

> **时间 = 循环层数 × 每步操作耗时**
> **空间 = 额外创建的最大数据结构**

## 常见算法复杂度一览

| 算法 | 时间 | 空间 |
|------|------|------|
| Binary Search | O(log n) | O(1) |
| Two Sum (hash map) | O(n) | O(n) |
| Two Pointers (sorted) | O(n) | O(1) |
| 3Sum (sort + two pointers) | O(n²) | O(1) |
| Sliding Window | O(n) | O(k) |
| BFS / DFS | O(V + E) | O(V) |
| Sorting (built-in) | O(n log n) | O(n) |
