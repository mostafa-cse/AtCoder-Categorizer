# Digit Recursion / 3-Branch DFS Enumeration

**Domain**: `Basics`  
**Subtopic**: `Recursion & Backtracking`  

This workbook contains curated, high-quality competitive programming problems teaching **Digit Recursion / 3-Branch DFS Enumeration**.

---

## Curated Problems

### [problem:AtCoder-abc114_c] — 755
- **Contest**: `abc114`
- **Rating / Difficulty**: 1045
- **Specific Skill**: Digit Recursion / 3-Branch DFS Enumeration
- **Individual Analysis**: [`../../analysis/AtCoder-abc114_c.md`](../../analysis/AtCoder-abc114_c.md)
- **Problem Statement Summary**: A '755 number' is a positive integer <= N whose decimal representation contains only the digits 7, 5, 3, and contains each of 7, 5, and 3 at least once. Count all 755 numbers <= N (N <= 10^9).
- **Core Insight**: Since the search space is fewer than 30,000 numbers, we can generate all candidate numbers recursively via 3-way branching DFS: append 3, 5, or 7, tracking whether 3, 5, and 7 have appeared using bitmask flags.
- **Complexity**: Time: `O(3^D) where D <= 9` | Space: `O(D)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>

using namespace std;

long long n;

int dfs(long long val, int mask) {
    if (val > n) return 0;
    int count = (mask == 7 ? 1 : 0);

    count += dfs(val * 10 + 3, mask | 1);
    count += dfs(val * 10 + 5, mask | 2);
    count += dfs(val * 10 + 7, mask | 4);

    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    cout << dfs(0, 0) << "\n";
    return 0;
}
```
