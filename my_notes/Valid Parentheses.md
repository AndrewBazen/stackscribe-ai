# Prompt
---
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
## Given:
---
An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples:
---
### Example 1:
**Input:** s = "()"

**Output:** true
### Example 2:
**Input:** s = "()[]{}"

**Output:** true

### Example 3:
**Input:** s = "(]"

**Output:** false

## Constraints:
---
- `1 <= s.length <= 104`
- `s` consists of parentheses only `'()[]{}'`.
# Pseudocode
---
```pseudo
	new stack
	for items in the string
		if i = string length
			if stack is not empty
				return false
			return true
		else
			peek the stack
				if empty
					push the stack
				else if the top of the stack is does not match the next char
					return false
				else
					pop the stack
	return true;
```

# My Solution
---
```c#
public class Solution {
    public bool IsValid(string s) {
        if (s.Length % 2 != 0) { return false; }
        Dictionary<char,char> pairs = new();
        pairs.Add('(',')');
        pairs.Add('{','}');
        pairs.Add('[',']');
        Stack<char> stack = new();
        for (int i = 0; i < s.Length; i++) {
            if (pairs.ContainsKey(s[i]) ) {
                stack.Push(s[i]);
                continue;
            } else {
                if (stack.TryPeek(out char c)) {
                    if (s[i] != pairs[c]) {
                        return false;
                    } else {
                        stack.Pop();
                    }
                } else {
                    return false;
                }
            }
        }
        if (stack.Count != 0) {
            return false;
        }
        return true;
    }
}
```
