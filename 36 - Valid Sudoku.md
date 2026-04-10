
# 36. Valid Sudoku

**Difficulty:** Medium
**Tags:** Array, Hash Table, Matrix

## Problem

Determine if a 9×9 Sudoku board is valid. Only check filled cells:
1. Each row — no duplicate digits
2. Each column — no duplicate digits
3. Each 3×3 box — no duplicate digits

Empty cells are `"."`，忽略。

## Approach: Hash Set 查重 × 3

**Key Insight:** 本质就是 217 Contains Duplicate 的升级版。217 是一个 list 查重，这题是 27 个 list 同时查重（9 行 + 9 列 + 9 box）。用三组 set 分别追踪每行、每列、每个 box 出现过的数字。

### 关键：cell (r, c) 属于哪个 box？

```
r//3 → 0, 1, 2 (哪一行 box)
c//3 → 0, 1, 2 (哪一列 box)

(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
```

用 `(r//3, c//3)` 作为 key 唯一标识 9 个 box。

### Code

```python
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                if (num in rows[r] or
                    num in cols[c] or
                    num in boxes[(r//3, c//3)]):
                    return False
                rows[r].add(num)
                cols[c].add(num)
                boxes[(r//3, c//3)].add(num)

        return True
```

## Walkthrough

```
board[0] = ["5","3",".",".","7",".",".",".","."]

r=0, c=0: num="5"
  rows[0]={}, cols[0]={}, boxes[(0,0)]={}
  没有重复 → 加入三个 set

r=0, c=1: num="3"
  rows[0]={"5"}, cols[1]={}, boxes[(0,0)]={"5"}
  没有重复 → 加入三个 set

r=0, c=2: num="." → skip

...以此类推，如果某个数字已经在 set 里 → return False
```

## ⚠️ 常犯错误

1. **box 编号不需要 +1** — `r//3` 和 `c//3` 本身就是 0~2，直接用 tuple `(r//3, c//3)` 即可
2. **`defaultdict(set)` vs 手动初始化** — `defaultdict` 访问不存在的 key 时自动创建空 set，省去初始化代码
3. **棋盘里的值是字符串** — `board[r][c]` 是 `"5"` 不是 `5`，但不影响 set 查重

## Notes

- 时间复杂度：O(81) = O(1) — 棋盘固定 9×9
- 空间复杂度：O(81) = O(1) — 同理
- 核心思路：**三组 set 同时查重**，和 Contains Duplicate 一脉相承
