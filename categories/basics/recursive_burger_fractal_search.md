# Recursive Burger Fractal Binary Search / Tree Size Division

**Domain**: `Basics`  
**Subtopic**: `Divide and Conquer`  

This workbook contains curated, high-quality competitive programming problems teaching **Recursive Burger Fractal Binary Search / Tree Size Division**.

---

## Curated Problems

### [problem:AtCoder-abc115_d] — Christmas
- **Contest**: `abc115`
- **Rating / Difficulty**: 1088
- **Specific Skill**: Recursive Burger Fractal Binary Search / Tree Size Division
- **Individual Analysis**: [`../../analysis/AtCoder-abc115_d.md`](../../analysis/AtCoder-abc115_d.md)
- **Problem Statement Summary**: A Level-0 burger is a patty 'P'. A Level-L burger consists of 'B' + (Level-(L-1) burger) + 'P' + (Level-(L-1) burger) + 'B'. Find the number of patties 'P' in the bottom X layers of a Level-N burger (N <= 50, X <= total layers).
- **Core Insight**: Binary search / divide and conquer on X: (1) if X == 1: bottom is 'B', 0 patties; (2) if X <= 1 + len[L-1]: lies in first half burger -> recurse on (L-1, X - 1); (3) if X == 2 + len[L-1]: covers bottom 'B' + entire first half + middle 'P' -> pat[L-1] + 1; (4) if X <= 2 + 2*len[L-1]: covers bottom + first half + middle 'P' + part of second half -> pat[L-1] + 1 + recurse(L-1, X - 2 - len[L-1]); (5) if X == len[L]: entire burger -> pat[L].
- **Complexity**: Time: `O(N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<long long> len_b(51), pat(51);

long long solve(int l, long long x) {
    if (l == 0) return (x > 0 ? 1 : 0);
    if (x <= 1) return 0;
    if (x <= 1 + len_b[l - 1]) {
        return solve(l - 1, x - 1);
    }
    if (x == 2 + len_b[l - 1]) {
        return pat[l - 1] + 1;
    }
    if (x <= 2 + 2 * len_b[l - 1]) {
        return pat[l - 1] + 1 + solve(l - 1, x - 2 - len_b[l - 1]);
    }
    return pat[l];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long x;
    if (!(cin >> n >> x)) return 0;

    len_b[0] = 1;
    pat[0] = 1;
    for (int i = 1; i <= n; ++i) {
        len_b[i] = 2 * len_b[i - 1] + 3;
        pat[i] = 2 * pat[i - 1] + 1;
    }

    cout << solve(n, x) << "\n";
    return 0;
}
```
