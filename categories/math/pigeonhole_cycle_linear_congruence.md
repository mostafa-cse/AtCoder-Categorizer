# Pigeonhole Cycle Detection on Linear Congruence Sequence

**Domain**: `Math`  
**Subtopic**: `Modular Arithmetic`  

This workbook contains curated, high-quality competitive programming problems teaching **Pigeonhole Cycle Detection on Linear Congruence Sequence**.

---

## Curated Problems

### [problem:AtCoder-abc174_c] — Repsept
- **Contest**: `abc174`
- **Rating / Difficulty**: 902
- **Specific Skill**: Pigeonhole Cycle Detection on Linear Congruence Sequence
- **Individual Analysis**: [`../../analysis/AtCoder-abc174_c.md`](../../analysis/AtCoder-abc174_c.md)
- **Problem Statement Summary**: Given K <= 10^6. Does the sequence 7, 77, 777, ... contain any term divisible by K? If so, find the index of the first such term, else output -1.
- **Core Insight**: Because there are only K possible remainders modulo K, by the Pigeonhole Principle, if 0 does not appear in the first K iterations, a remainder must repeat, entering a deterministic periodic cycle that will never reach 0.
- **Complexity**: Time: `O(K)` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long k;
    if (!(cin >> k)) return 0;

    long long rem = 0;
    for (int i = 1; i <= k; ++i) {
        rem = (rem * 10 + 7) % k;
        if (rem == 0) {
            cout << i << "\n";
            return 0;
        }
    }

    cout << -1 << "\n";
    return 0;
}
```
