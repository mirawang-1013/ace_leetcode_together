# 19. Remove Nth Node From End of List

**Difficulty:** Medium
**Tags:** Linked List, Two Pointers

## Problem

Given the head of a linked list, remove the `n`th node from the end of the list and return its head.

### Examples

**Example 1:**
- Input: `head = [1,2,3,4,5]`, `n = 2`
- Output: `[1,2,3,5]`

**Example 2:**
- Input: `head = [1]`, `n = 1`
- Output: `[]`

### Constraints

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `1 <= n <= sz`

## Approach: 快慢指针 + Dummy Head

**Key Insight:** 让快指针先走 n 步，然后快慢一起走。快指针到尾时，慢指针刚好在要删节点的**前一位**，执行 `slow.next = slow.next.next` 跳过即可。

### 图解

```
n = 2，链表：1 → 2 → 3 → 4 → 5

fast 先走 2 步：
slow              fast
 ↓                 ↓
dummy → 1 → 2 → 3 → 4 → 5

一起走到 fast 到尾：
               slow         fast
                ↓             ↓
dummy → 1 → 2 → 3 → 4 → 5

slow.next(4) 就是要删的节点
slow.next = slow.next.next → 跳过 4，直接连到 5
```

### Steps

1. 创建 `dummy` 节点指向 `head`，`fast` 和 `slow` 都从 `dummy` 出发。
2. `fast` 先走 `n` 步。
3. `fast` 和 `slow` 一起走，直到 `fast.next` 为空。
4. `slow.next = slow.next.next` 删除目标节点。
5. 返回 `dummy.next`。

### Time & Space Complexity

- **Time:** O(n) — 一次遍历。
- **Space:** O(1)

## Solution (Python)

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        # fast 先走 n 步
        for _ in range(n):
            fast = fast.next

        # 一起走，直到 fast 到最后一个节点
        while fast.next:
            fast = fast.next
            slow = slow.next

        # 跳过要删的节点
        slow.next = slow.next.next

        return dummy.next
```

## Key Details

### `slow.next = slow.next.next` 在做什么？

就是把要删的节点"跳过去"，让 slow 直接连到目标节点的下一个：

```
删除前：slow → 4 → 5
删除后：slow ------→ 5
```

4 从链表里断开了，就等于被删除了。

### 为什么 `return dummy.next` 而不是 `return head`？

因为如果删的就是 head 本身，head 已经被跳过了：

```
例：1 → 2，删倒数第 2 个（就是 1）

dummy → 1 → 2
slow.next = slow.next.next
dummy → 2

return dummy.next → 返回 2 ✓
return head       → 返回 1 ✗（1 已经被删了）
```

### 为什么需要 Dummy Head？

如果不用 dummy，删除 head 时前面没有节点，没法用 `前一个.next = 前一个.next.next`，必须单独写 if 判断。Dummy 让每个节点（包括 head）前面都有一个节点，统一了操作逻辑，不需要特殊处理。

### 为什么间隔 n 步就能找到倒数第 n 个？

fast 和 slow 之间始终差 n 步。fast 到末尾时离终点 0 步，所以 slow 离终点 n 步，刚好在要删节点的前一个位置。
