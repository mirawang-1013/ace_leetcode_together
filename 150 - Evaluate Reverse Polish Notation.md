# 150. Evaluate Reverse Polish Notation

**Difficulty:** Medium
**Tags:** Array, Stack

## Problem

Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN). Valid operators are `+`, `-`, `*`, `/`. Each operand may be an integer or another expression. Division truncates toward zero.

### Examples

**Example 1:**
- Input: `tokens = ["2","1","+","3","*"]`
- Output: `9`
- Explanation: `(2 + 1) * 3 = 9`

**Example 2:**
- Input: `tokens = ["4","13","5","/","+"]`
- Output: `6`
- Explanation: `4 + (13 / 5) = 4 + 2 = 6`

## Approach: Stack

**Key Insight:** RPN 的设计就是为栈量身定做的 — 数字就 push，操作符就 pop 两个算完再 push 回去。栈最后只剩一个元素就是答案。

### Code

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+-/*":
                a = stack.pop()  # 右操作数（先pop）
                b = stack.pop()  # 左操作数（后pop）
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(b - a)
                elif i == '*':
                    stack.append(a * b)
                elif i == '/':
                    stack.append(int(b / a))
            else:
                stack.append(int(i))
        return stack[0]
```

## Walkthrough

`tokens = ["3", "4", "+", "2", "*"]` 即 `(3+4)*2`

| Token | Action | Stack |
|-------|--------|-------|
| "3" | push 3 | [3] |
| "4" | push 4 | [3, 4] |
| "+" | pop 4(a), pop 3(b) → 3+4=7, push | [7] |
| "2" | push 2 | [7, 2] |
| "*" | pop 2(a), pop 7(b) → 7*2=14, push | [14] |

Return **14**

## ⭐ 易错点：Pop 顺序

`a = stack.pop()` 是**右操作数**，`b = stack.pop()` 是**左操作数**。

- `+` 和 `*`：交换律，顺序无所谓
- `-` 和 `/`：**必须是 `b - a`、`b / a`（左 op 右）**

例子：`["6", "2", "-"]` 应该是 `6 - 2 = 4`
```
a = pop() → 2 (右)
b = pop() → 6 (左)
b - a = 6 - 2 = 4 ✅
a - b = 2 - 6 = -4 ❌
```

## ⭐ 除法截断

Python 的 `//` 是向负无穷取整（floor division），但题目要求**向零截断**：
- `-7 // 2 = -4` ❌（floor toward -∞）
- `int(-7 / 2) = -3` ✅（truncate toward 0）

所以用 `int(b / a)` 而不是 `b // a`。

## Notes

- 一句话总结：**数字就 push，操作符就 pop 两个算完再 push 回去**
- 只需要一个 stack，不需要分开存数字和操作符
- 判断操作符用 `i in "+-/*"` 即可，因为都是单字符
- 不要用 `isalnum()` 判断数字，负数如 `"-3"` 会判断错误
- 时间复杂度：O(n)
- 空间复杂度：O(n)
