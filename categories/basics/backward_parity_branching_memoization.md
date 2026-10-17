# Backward Parity Branching Recursion with Memoization from Target to Source

**Domain**: `Basics`  
**Subtopic**: `Memoized Recursion`  

This workbook contains curated, high-quality competitive programming problems teaching **Backward Parity Branching Recursion with Memoization from Target to Source**.

---

## Curated Problems

### `[problem:AtCoder-abc188_f]` — +1-1x2
- **Rating / Difficulty**: 1865
- **Contest**: `abc188`
- **Analysis**: [`analysis/AtCoder-abc188_f.md`](../../analysis/AtCoder-abc188_f.md)
- **Key Idea**: Work backward from Y to X: dividing by 2 is only allowed when the current number is even. If Y is odd, we can either add 1 or subtract 1 to make it even, then divide by 2. We can also reach X directly using only +1/-1 with cost |X - Y|.
- **Time Complexity**: `O(log Y)`
- **Space Complexity**: `O(log Y)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

long long X;
map<long long, long long> memo;

long long solve(long long y) {
    if (y <= X) return X - y;
    if (memo.count(y)) return memo[y];

    long long res = y - X; // direct operations

    if (y % 2 == 0) {
        res = min(res, solve(y / 2) + 1);
    } else {
        res = min(res, solve((y + 1) / 2) + 2);
        res = min(res, solve((y - 1) / 2) + 2);
    }

    return memo[y] = res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long y;
    if (!(cin >> X >> y)) return 0;

    cout << solve(y) << "\n";
    return 0;
}
```
