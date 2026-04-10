
# 104. Maximum Depth of Binary Tree

**Difficulty:** Easy
**Tags:** Binary Tree, DFS, Recursion

## Problem

Given a binary tree, find its maximum depth (longest path from root to leaf).

```
     3
   /   \
  9    20
      /  \
    15    7

Output: 3
```

## Approach: Recursion (DFS)

**Key Insight:** 当前节点的深度 = max(左子树深度, 右子树深度) + 1。递归到 None 返回 0，然后一层一层 +1 往上传。

### Code

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

## Walkthrough (递归 trace)

```
maxDepth(3)
  ├─ left = maxDepth(9)
  │   ├─ maxDepth(None) → 0
  │   ├─ maxDepth(None) → 0
  │   └─ max(0, 0) + 1 = 1
  │
  ├─ right = maxDepth(20)
  │   ├─ maxDepth(15)
  │   │   ├─ maxDepth(None) → 0
  │   │   ├─ maxDepth(None) → 0
  │   │   └─ max(0, 0) + 1 = 1
  │   ├─ maxDepth(7)
  │   │   ├─ maxDepth(None) → 0
  │   │   ├─ maxDepth(None) → 0
  │   │   └─ max(0, 0) + 1 = 1
  │   └─ max(1, 1) + 1 = 2
  │
  └─ max(1, 2) + 1 = 3 ✅
```

值不是一开始就知道的，是**从 None 的 0 开始，一层一层加 1 传上来的**。

## ⚠️ 常犯错误

1. **不要加 `while root`** — `if not root` 已经处理了 None，后面 root 一定存在，不需要 while
2. **递归天然就是 DFS** — 一路钻到底再回来，不是一层一层

## Notes

- 时间复杂度：O(n) — 每个节点访问一次
- 空间复杂度：O(h) — h 是树高（递归调用栈），最坏 O(n)
- 和 226 Invert Tree 用同一个递归模板，只是"处理当前节点"的逻辑不同
