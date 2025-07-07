# Prompt
---
You are given a **sorted unique** integer array `nums`.
A **range** `[a,b]` is the set of all integers from `a` to `b` (inclusive).
Return _the **smallest sorted** list of ranges that **cover all the numbers in the array exactly**_. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.
## Given:
---
Each range `[a,b]` in the list should be output as:

- `"a->b"` if `a != b`
- `"a"` if `a == b`
## Examples:
---
### Example 1:
**Input:** nums = [0,1,2,4,5,7]
**Output:** ["0->2","4->5","7"]
**Explanation:** The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
### Example 2:
**Input:** nums = [0,2,3,4,6,8,9]
**Output:** ["0","2->4","6","8->9"]
**Explanation:** The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9

## Constraints:
---
- `0 <= nums.length <= 20`
- `-231 <= nums[i] <= 231 - 1`
- All the values of `nums` are **unique**.
- `nums` is sorted in ascending order.
# Pseudocode
---
```pseudo
pointer i;
pointer j;
List<int> ranges = new();
for i in nums
	if nums[i + 1] is not nums[i] + 1
		ranges add [j, i];
		j = i + 1;
return ranges
	
```

# My Solution
---
```c#
public class Solution {
    public IList<string> SummaryRanges(int[] nums) {
        int j = 0;
        List<string> ranges = new();
        for (int i = 0; i < nums.Length;i++) {
            if (i != nums.Length -1) {
                if (nums[i+1] != nums[i] + 1) {
                    if (i == j) {
                        ranges.Add($"{nums[j]}");
                        j = i + 1;
                        continue;
                    } 
                    ranges.Add($"{nums[j]}->{nums[i]}");
                    j = i + 1;
                }
            } else {
                if (i == j) {
                    ranges.Add($"{nums[j]}");
                    continue;
                }
                ranges.Add($"{nums[j]}->{nums[i]}");
            }

        }
        return ranges;
    }
}
```
