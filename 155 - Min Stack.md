# 155. Min Stack

**Difficulty:** Medium
**Tags:** Stack, Design

## Problem

设计一个栈，支持 `push`、`pop`、`top` 和 `getMin`，其中 `getMin` 要在 O(1) 时间内返回栈中最小值。

### Example

```
操作              stack        min_stack     返回
MinStack()       []           []            null
push(-2)         [-2]         [-2]          null
push(0)          [-2,0]       [-2,-2]       null
push(-3)         [-2,0,-3]   [-2,-2,-3]     null
getMin()                                    -3（min_stack 栈顶）
pop()            [-2,0]       [-2,-2]       null（弹掉 -3）
top()                                       0（stack 栈顶）
getMin()                                    -2（min_stack 栈顶）
```

## 难点

普通栈找最小值要遍历 O(n)。如果最小值被 pop 掉了，怎么知道新的最小值是谁？

## Approach: 两个栈

用一个 `min_stack` 同步记录每一步的最小值。push 时两个栈一起 push，pop 时两个栈一起 pop。

### Code

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

## Python 基础笔记

### self

类里面访问自己的属性，都要加 `self.`：

```python
self.stack = []          # 对象属性，所有方法都能访问
temp = val + 1           # 局部变量，方法结束就没了
```

### return

看函数签名判断：
- `-> None` → 只做操作，不需要 return（如 `push`、`pop`）
- `-> int` → 需要 return 返回值（如 `top`、`getMin`）

### 栈顶 vs 栈底

```
push(1) → [1]
push(2) → [1, 2]
push(3) → [1, 2, 3]
                  ^
                栈顶

stack[-1] → 栈顶（最后放进去的）
stack[0]  → 栈底（最先放进去的）
```

### 其他易错点

- 列表添加元素用 `append()`，不是 `add()`
- `__init__` 不能有 return
- 不要用 `min`、`max`、`sum` 作为变量名，会覆盖内置函数

## LeetCode 设计类题目输入格式

```
["MinStack","push","push","getMin"]   ← 操作名列表
[[],[-2],[0],[]]                       ← 每个操作的参数
```

第一行是方法名，第二行是对应参数，`[]` 表示无参数。
