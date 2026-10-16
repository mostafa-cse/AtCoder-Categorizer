# Bitmask Truth Assignment Consistency Verification

**Domain**: `Basics`  
**Subtopic**: `Bitmask Brute Force`  

This workbook contains curated, high-quality competitive programming problems teaching **Bitmask Truth Assignment Consistency Verification**.

---

## Curated Problems

### [problem:AtCoder-abc147_c] — HonestOrUnkind2
- **Contest**: `abc147`
- **Rating / Difficulty**: 977
- **Specific Skill**: Bitmask Truth Assignment Consistency Verification
- **Individual Analysis**: [`../../analysis/AtCoder-abc147_c.md`](../../analysis/AtCoder-abc147_c.md)
- **Problem Statement Summary**: There are N people (N <= 15). Each person is either honest (always speaks the truth) or unkind (can say anything). Person i makes A_i statements of the form: person x is honest (y=1) or unkind (y=0). Find the maximum number of honest people in any consistent scenario.
- **Core Insight**: Unkind people have no constraints (their statements can be true or false). But if person i is assumed honest ((mask >> i) & 1 == 1), every single claim they make MUST match the assumed mask: if person i says person x is y, then ((mask >> x) & 1) must equal y.
- **Complexity**: Time: `O(2^N * sum(A_i))` | Space: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Statement {
    int x, y;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<Statement>> st(n);
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        st[i].resize(a);
        for (int j = 0; j < a; ++j) {
            cin >> st[i][j].x >> st[i][j].y;
            st[i][j].x--; // 0-indexed
        }
    }

    int max_honest = 0;
    int total_masks = 1 << n;

    for (int mask = 0; mask < total_masks; ++mask) {
        bool ok = true;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                for (const auto& s : st[i]) {
                    int expected = (mask >> s.x) & 1;
                    if (expected != s.y) {
                        ok = false;
                        break;
                    }
                }
            }
            if (!ok) break;
        }

        if (ok) {
            int honest_cnt = __builtin_popcount(mask);
            max_honest = max(max_honest, honest_cnt);
        }
    }

    cout << max_honest << "\n";
    return 0;
}
```
