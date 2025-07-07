# Prompt
---
Given an integer array `nums` and an integer `k`, return `true` _if there are two **distinct indices**_ `i` _and_ `j` _in the array such that_ `nums[i] == nums[j]` _and_ `abs(i - j) <= k`.
## Given:
---
integer array `nums`  
integer `k`

## Examples:
---
### Example 1:
**Input:** nums = [1,2,3,1], k = 3
**Output:** true
### Example 2:
**Input:** nums = [1,0,1,1], k = 1
**Output:** true

## Constraints:
---
$$1 <= nums.length <= 105$$
$$-109 <= nums[i] <= 109$$
$$0 <= k <= 105$$


# Pseudocode
```pseudo
pointer i = 0
pointer j = 0
while false
	if nums[i] == nums[j] && abs(i - j) == k
		return true
	if i - j == k 
	
```

# My Solution
