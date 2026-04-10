
# 226. Invert Binary Tree

**Difficulty:** Easy
**Tags:** Binary Tree, DFS, Recursion

## Problem

Given a binary tree, invert it (mirror flip — swap every left and right child).

```
Input:          Output:
     4               4
   /   \            /   \
  2     7          7     2
 / \   / \        / \   / \
1   3 6   9      9   6 3   1
```

## Approach: Recursion (DFS)

**Key Insight:** 递归 = 我只管当前这一层的交换，剩下的交给"未来的自己"去处理。每个节点做三件事：swap 左右孩子 → 递归左 → 递归右。碰到 None 就停。

### Code

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left  # 交换当前层
        self.invertTree(root.left)                       # 递归左子树
        self.invertTree(root.right)                      # 递归右子树
        return root
```

## Walkthrough (递归 trace)

```
     4
   /   \
  2     7
 / \
1   3

invertTree(4)
  ├─ swap: 4 的左右交换 → 7 到左边, 2 到右边
  ├─ invertTree(7)          ← 进入左子树
  │   ├─ 7 没有孩子（left=None, right=None）
  │   ├─ swap: None ↔ None（没变化）
  │   ├─ invertTree(None) → return None  ← 碰到 None，停！
  │   ├─ invertTree(None) → return None  ← 碰到 None，停！
  │   └─ return 7 ✅
  ├─ invertTree(2)          ← 进入右子树
  │   ├─ swap: 1 ↔ 3
  │   ├─ invertTree(3)
  │   │   ├─ invertTree(None) → return None
  │   │   ├─ invertTree(None) → return None
  │   │   └─ return 3 ✅
  │   ├─ invertTree(1)
  │   │   ├─ invertTree(None) → return None
  │   │   ├─ invertTree(None) → return None
  │   │   └─ return 1 ✅
  │   └─ return 2 ✅
  └─ return 4 ✅           ← 最终返回根节点
```

## ⚠️ 理解要点

### 1. 递归不是"一层一层"，而是 DFS（深度优先）
一路往左钻到 None → 回来 → 再往右钻到 None → 回来

### 2. swap 只交换当前节点的左右指针
```python
root.left, root.right = root.right, root.left
```
不是创建新节点，只是修改指针方向。想象成火车车厢换挂钩。

### 3. 为什么还需要递归？
swap 只管当前一层。子树内部的左右关系没变，需要递归下去每一层都交换。

### 4. return root 返回的是指针
树本来就在内存里，`return root` 只是把根节点地址传回去。整个过程是**原地修改**（in-place），没有创建新树。

## 树题的通用递归模板

```python
def solve(root):
    if not root:           # 1. Base case: 空节点，停
        return ...
    # 2. 处理当前节点     （这题：swap）
    # 3. 递归左子树        solve(root.left)
    # 4. 递归右子树        solve(root.right)
    return root            # 5. 返回当前节点
```

## Notes

- 时间复杂度：O(n) — 每个节点访问一次
- 空间复杂度：O(h) — h 是树的高度（递归调用栈），最坏 O(n)
- `self.invertTree()` 里的 `self` 只是因为函数在 class 里，Python 的语法要求
