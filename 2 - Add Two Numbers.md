# 2. Add Two Numbers

**Difficulty:** Medium
**Tags:** Linked List, Math

## Problem

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each node contains a single digit. Add the two numbers and return the sum as a linked list.

### Examples

**Example 1:**
- Input: `l1 = [2,4,3]`, `l2 = [5,6,4]`
- Output: `[7,0,8]`
- Explanation: 342 + 465 = 807

**Example 2:**
- Input: `l1 = [0]`, `l2 = [0]`
- Output: `[0]`

**Example 3:**
- Input: `l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`
- Output: `[8,9,9,9,0,0,0,1]`

### Constraints

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- The list does not contain leading zeros (except the number 0 itself).

## Approach: Dummy Head + 逐位相加 + 进位

**Key Insight:** 数字已经是反向存储的（个位在前），所以可以直接从头开始逐位相加，就像手算加法一样。用 `carry` 跟踪进位，用 `or` 保证两条链表长度不同时也能处理完。

### Steps

1. 创建 `dummy = ListNode(0)` 作为哨兵节点，`curr` 指向它。
2. 当 `l1` 或 `l2` 还有节点，或者还有进位时，循环继续。
3. 取出当前节点的值（如果节点为 `None` 则用 0）。
4. 计算 `total = val1 + val2 + carry`，更新 `carry = total // 10`。
5. 创建新节点 `ListNode(total % 10)` 接到 `curr.next`。
6. 返回 `dummy.next`。

### Time & Space Complexity

- **Time:** O(max(m, n)) — m 和 n 分别是两个链表的长度。
- **Space:** O(1) — 除了输出链表外只用了几个变量。

## Solution (Python)

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
```

## Walkthrough (Example 1)

| Step | l1 | l2 | carry (in) | total | digit | carry (out) | 链表 |
|------|----|----|------------|-------|-------|-------------|------|
| 1 | 2 | 5 | 0 | 7 | 7 | 0 | 7 |
| 2 | 4 | 6 | 0 | 10 | 0 | 1 | 7→0 |
| 3 | 3 | 4 | 1 | 8 | 8 | 0 | 7→0→8 |

## 我的错误 & 易错点

### 1. `while curr1, curr2` 语法错误

逗号不是逻辑运算符。应该用 `or`：`while l1 or l2 or carry`。
- 用 `or` 而不是 `and`，因为两条链表长度可能不同，只要有一条还有节点就要继续。
- 加上 `or carry` 处理最后的进位（比如 99 + 1 = 100）。

### 2. `new = dummy.next` 从 None 开始

`dummy.next` 初始是 `None`，所以 `new.next = ...` 会报 `AttributeError`。应该从 `curr = dummy` 开始，往后接节点。

### 3. 给 `.next` 赋值 int 而不是 ListNode

`new.next = (val)` 赋的是数字，但链表节点的 `.next` 应该指向一个 `ListNode` 对象：
```python
curr.next = ListNode(total % 10)
```

### 4. 进位逻辑顺序错

先算 carry 再用，但 carry 应该是上一步的。正确顺序：
```python
total = val1 + val2 + carry   # 先加上一步的 carry
carry = total // 10           # 再算这一步产生的新 carry
```

## Key Details

### 为什么 `while l1 or l2` 不需要额外赋值？

`l1` 和 `l2` 是函数参数，已经指向链表头节点。Python 中对象不是 `None` 就是 truthy。
- 节点存在 → truthy → 循环继续
- `l1 = l1.next` 走到末尾变成 `None` → falsy → 该链表处理完毕

### Dummy Head 模式（同 #21）

这道题和 #21 Merge Two Sorted Lists 用了同样的 dummy head 技巧，避免单独处理第一个节点的特殊情况。这是链表题的标准套路。