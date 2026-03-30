# 271. Encode and Decode Strings

**Difficulty:** Medium
**Tags:** String, Design

## Problem

Design an algorithm to encode a list of strings to a single string, then decode it back to the original list.

- 不能用 `eval` 等序列化方法

### Examples

**Example 1:**
- Input: `["leet", "code"]`
- Encode: `"4#leet4#code"`
- Decode: `["leet", "code"]`

## Why Not Simply Join?

直接用逗号拼接会有歧义：

```
["he,llo", "world"] → "he,llo,world"
```

解码时无法确定在哪分割。

## Approach: Length Prefix

**Key Insight:** 在每个字符串前加上 `长度#`，解码时靠长度来确定边界，不管字符串里有什么字符都不会出问题。

### Encode

把每个字符串编码为 `len(s)#s`，拼在一起：

```
["leet", "code"] → "4#leet4#code"
```

注意：`len()` 返回 `int`，拼字符串时需要用 `str()` 转换。

### Decode

1. 找到 `#` 的位置
2. `#` 前面的数字就是字符串长度
3. 从 `#` 后面取对应长度的字符
4. 重复直到结束

### Code

```python
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.index("#", i)          # 从 i 开始找 #
            length = int(s[i:j])          # # 前面是长度
            res.append(s[j + 1:j + 1 + length])  # 取对应长度的字符串
            i = j + 1 + length            # 移到下一段
        return res
```

## Notes

- **encode 时**：`str(len(s))` — 需要转 `str` 来拼字符串
- **decode 时**：`int(s[i:j])` — 需要转 `int` 来做切片
- 时间复杂度：O(n)，n 为所有字符串的总长度
