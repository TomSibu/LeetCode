# Longest Common Prefix

This repository provides a simple Python solution to the classic problem of finding the longest common prefix string among an array of strings. The solution is implemented in a straightforward manner using a nested loop.

## Problem Description

Given an array of strings `strs`, the goal is to find the longest common prefix string among them. If there is no common prefix, return an empty string (`""`).

### Examples

- **Example 1:**
  - **Input:** `["flower", "flow", "flight"]`
  - **Output:** `"fl"`

- **Example 2:**
  - **Input:** `["dog", "racecar", "car"]`
  - **Output:** `""`
  - **Explanation:** There is no common prefix among the input strings.

## Approach

The solution follows these steps:

1. **Initialization:**
   - Start with an empty result string `result`.
   - Use the first string (`strs[0]`) as the reference for comparison.

2. **Iteration:**
   - Loop over each character index `i` of the first string.
   - For each character, iterate through every string in `strs`.
   - Check two conditions:
     - If `i` is equal to the length of the current string `s` (i.e., the current string is shorter than the prefix we've accumulated so far).
     - If the character at index `i` in `s` is different from the character at index `i` in `strs[0]`.
   - If either condition is met, return the current `result` as no further common prefix can exist.
   - Otherwise, append the character from `strs[0]` at index `i` to the `result`.

3. **Return Result:**
   - If the loop finishes without any break, return the complete `result` string, which is the longest common prefix.

## Implementation

The solution is implemented in two files:

- **`solution.py`**: Contains the `Solution` class with the `longestCommonPrefix` method.
- **`main.py`**: Imports and calls the function with example inputs.

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result
```

# Example usage:
```python
from solution import Solution

sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
```

# How to Run

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/TomSibu/longest-common-prefix.git
    cd longest-common-prefix
    ```

2. **Run the Script:**

    ```bash
    python3 main.py
    ```