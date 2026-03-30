# 143. Reorder List

**Difficulty:** Medium
**Tags:** Linked List, Two Pointers, Stack

## Problem

Given the head of a singly linked list: `L0 → L1 → … → Ln-1 → Ln`, reorder it to: `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …`

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

### Examples

**Example 1:**
- Input: `head = [1,2,3,4]`
- Output: `[1,4,2,3]`

**Example 2:**
- Input: `head = [1,2,3,4,5]`
- Output: `[1,5,2,4,3]`

### Constraints

- The number of nodes in the list is in the range `[1, 5 * 10^4]`.

## Approach 1: 数组法（最直观）

**Key Insight:** 链表不能用下标访问，但把节点存进数组就可以了。然后从两头交替取节点重新连起来。

### Steps

1. 遍历链表，把所有节点存入数组 `nodes`。
2. 用 `left` 和 `right` 两个指针从两头向中间走。
3. 交替连接：`nodes[left] → nodes[right] → nodes[left+1] → ...`
4. 最后记得把尾节点的 `.next` 设为 `None`。

### Time & Space Complexity

- **Time:** O(n)
- **Space:** O(n) — 额外数组存了所有节点。

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            nodes[right].next = nodes[left]
            right -= 1
        nodes[left].next = None
```

## Approach 2: 找中点 + 反转 + 合并（最优解）

**Key Insight:** 观察规律，结果就是**前半部分**和**反转后的后半部分**交替合并。

```
原始：  1 → 2 → 3 → 4 → 5

前半：  1 → 2 → 3
后半：  4 → 5
反转后半：5 → 4

交替合并：1 → 5 → 2 → 4 → 3
```

本质上是 3 个基础链表操作的组合：**找中点（876）+ 反转链表（206）+ 合并链表（21）**。

### Time & Space Complexity

- **Time:** O(n)
- **Space:** O(1) — 面试最优解。

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: 快慢指针找中点
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: 反转后半部分
        second = slow.next
        slow.next = None  # 断开前后两半

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev

        # Step 3: 交替合并
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
```

## Key Details

### 为什么链表法要分三步？

链表不能从尾部往前走，所以先**反转后半部分**，把"从尾部取"变成"从头部取"。反转之后就变成了两个链表的合并问题，和 21 题一样。

### 链表法的三个子操作都是独立的高频题

如果链表操作不熟，建议先单独练这三道基础题，再回来做 143：
- **206 Reverse Linked List** — 反转链表
- **876 Middle of the Linked List** — 快慢指针找中点
- **21 Merge Two Sorted Lists** — 合并两个链表
