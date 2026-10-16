# 1D Parity Difference Array (Imos Mod 2)

**Domain**: `Data Structures`  
**Subtopic**: `Difference Arrays`  

This workbook contains curated, high-quality competitive programming problems teaching **1D Parity Difference Array (Imos Mod 2)**.

---

## Curated Problems

### [problem:AtCoder-abc035_c] — Othello
- **Contest**: `abc035`
- **Rating / Difficulty**: 1096
- **Specific Skill**: 1D Parity Difference Array (Imos Mod 2)
- **Individual Analysis**: [`../../analysis/AtCoder-abc035_c.md`](../../analysis/AtCoder-abc035_c.md)
- **Problem Statement Summary**: An array of N pieces initially all white (0). Q queries flip the pieces in range [l, r] between white and black. Output the final board state.
- **Core Insight**: Apply difference array modulo 2: diff[l] ^= 1 and diff[r + 1] ^= 1. Then compute prefix XORs running_xor ^= diff[i] to determine the final state of each piece in O(N + Q).
- **Complexity**: Time: `O(N + Q)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> diff(n + 2, 0);
    for (int i = 0; i < q; ++i) {
        int l, r;
        cin >> l >> r;
        diff[l] ^= 1;
        diff[r + 1] ^= 1;
    }

    int cur = 0;
    for (int i = 1; i <= n; ++i) {
        cur ^= diff[i];
        cout << cur;
    }
    cout << "\n";

    return 0;
}
```
