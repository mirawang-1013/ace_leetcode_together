# 21. Merge Two Sorted Lists

**Difficulty:** Easy
**Tags:** Linked List, Recursion

## Problem

You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list by splicing together the nodes of the first two lists. Return the head of the merged linked list.

### Examples

**Example 1:**
- Input: `list1 = [1,2,4]`, `list2 = [1,3,4]`
- Output: `[1,1,2,3,4,4]`

**Example 2:**
- Input: `list1 = []`, `list2 = []`
- Output: `[]`

### Constraints

- The number of nodes in both lists is in the range `[0, 50]`.
- Both `list1` and `list2` are sorted in non-decreasing order.

## Approach: Dummy Head + 双指针

**Key Insight:** 用一个 dummy 哨兵节点作为起点，然后比较两个链表的当前节点，小的接上去，直到一方为空，把剩下的直接接上。

### Steps

1. 创建 `dummy = ListNode(0)` 作为哨兵节点，`curr` 指向它。
2. 当 `list1` 和 `list2` 都不为空时，比较值，小的接到 `curr.next`。
3. 某一方为空后，把另一方剩余部分直接接上。
4. 返回 `dummy.next`（跳过哨兵节点）。

### Time & Space Complexity

- **Time:** O(n + m) — n 和 m 分别是两个链表的长度。
- **Space:** O(1) — 只用了几个指针。

## Solution (Python)

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy.next
```

## 我的错误 & 易错点

### 1. 把链表当数组用了

我最初写的代码用 `list1[i]` 来访问节点，用 `result = []` 来存结果。**链表不能用下标访问**，只能用 `.next` 一步步遍历。

| 数组思维 | 链表实现 |
|---------|---------|
| `list1[i]` | `list1.val`（取值），`list1 = list1.next`（前进） |
| `result.append(i)` | `curr.next = node`（接上节点） |
| `i += 1` | `list1 = list1.next` |

### 2. 比较的是索引而不是值

我写了 `if i < j`，这是在比较索引。应该比较的是**节点的值**：`list1.val <= list2.val`。

### 3. `result.append[...]` 语法错误

方括号 `[]` 是索引访问，函数调用应该用圆括号 `()`。

## Key Details

### Dummy Head 哨兵节点

`dummy = ListNode(0)` 不是固有语法，是一个**常用技巧**。它的作用是让你不需要单独处理"第一个节点接谁"的逻辑。最后 `return dummy.next` 会跳过这个哨兵，dummy 里的 0 写成任何值都行。

如果不用 dummy，每次接节点时都要判断 `if head is None`，代码更复杂。

### 链表操作的基本套路

```
curr = curr.next        → 前进一步
curr.next = node        → 把 node 接到当前节点后面
```

这两个操作是所有链表题的基础。
