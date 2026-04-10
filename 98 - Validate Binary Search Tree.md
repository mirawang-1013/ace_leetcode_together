
# 98. Validate Binary Search Tree

**Difficulty:** Medium
**Tags:** Binary Tree, DFS, Recursion, BST

## Problem

Given a binary tree, determine if it is a valid **Binary Search Tree (BST)**.

BST 规则：
- 左子树**所有**节点 < 当前节点
- 右子树**所有**节点 > 当前节点
- 左右子树也必须是 BST

```
Input:           Input:
    2                5
   / \              / \
  1   3            1   4
                      / \
Output: true         3   6
                 Output: false (4 < 5，不能在右子树)
```

## Approach: 递归 + 传递合法范围 (low, high)

**Key Insight:** 每个节点都有一个合法范围 `(low, high)`，是从所有祖先那里继承来的。往左走 → 上界收紧为父节点值；往右走 → 下界收紧为父节点值。范围不只是来自父节点，而是**一路从 root 累积下来的**。

### Code

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:  # 出界了就不合法
                return False
            if not helper(node.left, lower, val):   # 左子树: upper 收紧为 val
                return False
            if not helper(node.right, val, upper):   # 右子树: lower 收紧为 val
                return False
            return True
        return helper(root)
```

### 为什么 Naive 做法是错的

```python
# WRONG: 只检查了直接孩子，没有传递祖先的约束
if root.left and root.left.val >= root.val:
    return False
```

Naive 做法**每次递归不传任何信息**，所以节点 3 只知道"我 < 父节点 6"，不知道"我还必须 > 爷爷节点 5"。正确做法通过 `lower` 和 `upper` 参数把祖先的约束一路传下去。

## Walkthrough (递归 trace)

```
         10
        /  \
       5    15
      / \   /
     2   7 12

helper(10, -inf, +inf)         ← 10 在 (-inf, +inf) 内? ✓
│
├─ helper(5, -inf, 10)         ← upper 收紧为 10
│   ├─ helper(2, -inf, 5)     ← upper 收紧为 5
│   │   ├─ helper(None) → True
│   │   └─ helper(None) → True
│   └─ helper(7, 5, 10)       ← lower=5 来自父节点, upper=10 来自爷爷!
│       ├─ helper(None) → True
│       └─ helper(None) → True
│
└─ helper(15, 10, +inf)       ← lower 收紧为 10
    └─ helper(12, 10, 15)     ← lower=10 来自爷爷, upper=15 来自父节点
        ├─ helper(None) → True
        └─ helper(None) → True

全部通过 → return True ✅
```

### 范围变化表

| 节点 | lower | upper | 谁设的 lower | 谁设的 high | 合法？ |
|------|-------|-------|-------------|------------|--------|
| 10 | -inf | +inf | 初始值 | 初始值 | ✓ |
| 5 | -inf | **10** | 初始值 | 节点 10 | ✓ |
| 2 | -inf | **5** | 初始值 | 节点 5 | ✓ |
| 7 | **5** | **10** | 节点 5 | 节点 10 | ✓ |
| 15 | **10** | +inf | 节点 10 | 初始值 | ✓ |
| 12 | **10** | **15** | 节点 10 | 节点 15 | ✓ |

**规律：** `lower` = 最近一次往右拐的祖先值，`upper` = 最近一次往左拐的祖先值。

## ⚠️ 常犯错误

1. **只检查直接孩子** — 必须把范围从祖先一路传下来，不能只看 parent-child
2. **用 `<` 而不是 `<=`** — BST 要求严格大于/小于，等于也不行
3. **用 `int` 的最小最大值** — 节点值可以是 `-2^31`，必须用 `float('-inf')` / `float('inf')`
4. **搞反 `<=` 的方向** — `val <= lower or val >= upper` 检查的是"出界了吗？"，不是"在范围内吗？"

## 替代解法：中序遍历

BST 的中序遍历（左→根→右）一定是**严格递增**的。

```python
class Solution:
    def isValidBST(self, root):
        self.prev = float('-inf')

        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)

        return inorder(root)
```

## 递归两种方向：Bottom-Up vs Top-Down

### 判断标准

> 站在当前节点，做决定需要的信息在**上面（祖先）**还是**下面（孩子）**？

### Bottom-Up：答案在下面，等孩子先算完

当前节点的答案**依赖子节点的返回值**。代码特征：**用递归的返回值来计算**。

```python
# 104 - 我的深度 = 孩子的深度 + 1
# 不知道孩子多深，就没法算自己 → 必须等孩子先返回
left = self.maxDepth(root.left)      # 先问左孩子
right = self.maxDepth(root.right)    # 再问右孩子
return max(left, right) + 1          # 用孩子的结果算自己的
```

### Top-Down：规则在上面，从祖先传下来

当前节点的答案**依赖祖先传下来的信息**。代码特征：**递归调用时多传参数**。

```python
# 98 - 我合不合法取决于祖先给我的范围
# 范围不是自己算的，是从上面传来的 → 必须靠参数
helper(node.left, lower, val)     # 把约束传下去
helper(node.right, node.val, upper)
```

### 代码上的区别

```python
# Bottom-Up → 关键在 return
result = recurse(child)        # 接收孩子的返回值
return f(result)               # 用它算自己的答案

# Top-Down → 关键在参数
recurse(child, constraint)     # 把信息往下传
```

### 三道题对比

| | 104 maxDepth | 226 invertTree | 98 isValidBST |
|---|---|---|---|
| 方向 | Bottom-Up | Top-Down | Top-Down |
| 信息流 | 底→上 (return) | 上→下 (处理完往下走) | 上→下 (参数传约束) |
| base case | `return 0` | `return None` | `return True` |
| 为什么 | 空节点深度为 0 | 没有节点可交换 | 空节点不违反规则 |
| 关键代码 | `return max(l,r)+1` | 先 swap 再递归 | `helper(child, lower, val)` |

### 怎么判断新题用哪个

| 情况 | 方向 | 例子 |
|------|------|------|
| 得先知道孩子的结果 | Bottom-Up | 104: 不知道孩子多深，算不了自己 |
| 得先知道祖先的约束 | Top-Down | 98: 不知道祖先的范围，判断不了自己 |
| 直接做完然后往下走 | Top-Down | 226: 直接 swap，然后递归下去 |

## Notes

- 时间复杂度：O(n) — 每个节点访问一次
- 空间复杂度：O(h) — 递归调用栈，h 是树高，最坏 O(n)
- 和 104、226 用同一个递归模板，但多了**参数传递**这个技巧 — 用参数把约束往下传
- 这是第一道需要"递归传参"的题，之前的树题（maxDepth, invertTree）递归时不需要额外参数
- 递归传参的本质：**函数调用 = 赋值**，写 `helper(child, val, upper)` 就等于在下一层执行了 `lower = val`
