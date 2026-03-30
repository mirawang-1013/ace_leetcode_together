

## 核心问题

在数组中找两个数，使它们的和等于 target。

## 关键区别：数组是否有序

| | 1. Two Sum | 167. Two Sum II |
|---|---|---|
| 数组有序？ | 否 | 是 |
| 最优解法 | Hash Map | 双指针 |
| 时间复杂度 | O(n) | O(n) |
| 空间复杂度 | O(n) | O(1) |

---

## 1. Two Sum — Hash Map

**思路：** 遍历数组，用字典记录见过的数和它的下标。对于每个数，算出配对数 `target - nums[i]`，如果配对数已经在字典里，直接返回。

```
nums = [2, 7, 11, 15], target = 9

i=0: nums[0]=2, 需要 9-2=7, 字典里没有7 → 存 {2: 0}
i=1: nums[1]=7, 需要 9-7=2, 字典里有2！下标是0 → 返回 [0, 1]
```

### Code

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums): #这个好，顺便记录了index
            diff = target - num
            if diff in seen:
                return [seen[diff], i] #在字典里找到的话就可以返回{index1,index2}
            seen[num] = i# 存入{值：index}
```

---

## 167. Two Sum II — 双指针

**思路：** 数组有序，一个指针从最左（最小），一个从最右（最大）：
- 两数之和太小 → 左指针右移，让和变大
- 两数之和太大 → 右指针左移，让和变小

```
numbers = [2, 7, 11, 15], target = 9

left=0, right=3: 2+15=17 > 9 → right--
left=0, right=2: 2+11=13 > 9 → right--
left=0, right=1: 2+7=9 == 9 → 返回 [1, 2]
```

### Code

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
```

---

## 融汇贯通

遇到 Two Sum 类题目，先看数组是否有序：

- **无序** → Hash Map（用空间换时间）
- **有序** → 双指针（利用有序性，不需要额外空间）

双指针为什么需要有序？因为它靠"太小就左移，太大就右移"来逼近答案。无序的话移动指针没有方向性，不知道该往哪走。

无序数组也能用双指针，但要先排序 O(n log n)，反而比 Hash Map 的 O(n) 慢。

---

## 15. 3Sum — 排序 + 固定一个数 + 双指针

**思路：** 本质就是在 167 Two Sum II 外面套一层 for 循环。先排序，然后固定第一个数 `nums[i]`，对右边的部分用双指针找两个数使三数之和 = 0。

```
nums = [-1, 0, 1, 2, -1, -4]
排序后: [-4, -1, -1, 0, 1, 2]

i=0, 固定 -4: 在 [-1,-1,0,1,2] 里找两个数使和=4 → 找不到
i=1, 固定 -1: 在 [-1,0,1,2] 里找两个数使和=1 → [-1,0,1] ✅ 和 [-1,-1,2] ✅
i=2, nums[2]==-1==nums[1], 跳过（去重）
i=3, 固定 0: 在 [1,2] 里找两个数使和=0 → 找不到
```

### 去重：跳过重复 vs set

用 set 去重虽然能 work，但效率差：

| 方式 | 时间 | 空间 |
|---|---|---|
| 跳过重复 | O(n²) | O(1) |
| set 去重 | O(n²) | O(n²) — 每个 tuple 都要 hash |

跳过重复的做法：
- **外层**：`if i > 0 and nums[i] == nums[i-1]: continue` — 同一个值不重复当第一个数
- **内层**：找到答案后，`while` 跳过相同的 left 和 right

### Code

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:  # 跳过重复的 i
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:   # 跳过重复
                        left += 1
                    while left < right and nums[right] == nums[right-1]: # 跳过重复
                        right -= 1
                    left += 1
                    right -= 1
        return result
```

My answer
```python
result=set()
nums.sort()
print(nums)

left,right=0,len(nums)-1

for i,value in enumerate(nums):

	left,right=i+1,len(nums)-1
	while left<right:
		total=nums[i]+nums[left]+nums[right]
		if total<0:
			left+=1
		if total>0:
			right-=1
		if total==0:
			result.add(tuple([value,nums[left],nums[right]]))
			left+=1
			right-=1
	return [list(t) for t in result]


```

### 和 Two Sum II 的关系

```
3Sum = for 循环固定第一个数 + Two Sum II 找剩下两个数
```

这就是为什么先做 167 再做 15 会很顺——内层逻辑完全一样，只是外面多了一层循环和去重。
