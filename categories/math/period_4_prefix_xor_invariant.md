# Period-4 Prefix XOR Invariant

**Domain**: `Math`  
**Subtopic**: `Bitwise Invariants`  

This workbook contains curated, high-quality competitive programming problems teaching **Period-4 Prefix XOR Invariant**.

---

## Curated Problems

### [problem:AtCoder-abc121_d] — XOR World
- **Contest**: `abc121`
- **Rating / Difficulty**: 1164
- **Specific Skill**: Period-4 Prefix XOR Invariant
- **Individual Analysis**: [`../../analysis/AtCoder-abc121_d.md`](../../analysis/AtCoder-abc121_d.md)
- **Problem Statement Summary**: Compute the XOR sum of all integers between A and B inclusive: A XOR (A + 1) ... XOR B (A, B <= 10^12).
- **Core Insight**: Every 4 consecutive integers starting at an even multiple of 4 (4k, 4k+1, 4k+2, 4k+3) XOR to 0: (4k XOR (4k+1)) = 1, and ((4k+2) XOR (4k+3)) = 1, and 1 XOR 1 = 0! Therefore F(n) depends only on n % 4: n % 4 == 0 -> n; n % 4 == 1 -> 1; n % 4 == 2 -> n + 1; n % 4 == 3 -> 0.
- **Complexity**: Time: `O(1)` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>

using namespace std;

long long f(long long n) {
    if (n < 0) return 0;
    long long rem = n % 4;
    if (rem == 0) return n;
    if (rem == 1) return 1;
    if (rem == 2) return n + 1;
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    cout << (f(b) ^ f(a - 1)) << "\n";
    return 0;
}
```
