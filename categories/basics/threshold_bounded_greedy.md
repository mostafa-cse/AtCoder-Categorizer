# Threshold-Bounded Greedy Consumption

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Threshold-Bounded Greedy Consumption**.

---

## Curated Problems

### [problem:AtCoder-abc085_d] — Katana Thrower
- **Contest**: `abc085`
- **Rating / Difficulty**: 954
- **Specific Skill**: Threshold-Bounded Greedy Consumption
- **Individual Analysis**: [`../../analysis/AtCoder-abc085_d.md`](../../analysis/AtCoder-abc085_d.md)
- **Problem Statement Summary**: An enemy has H health. You have N katanas. Katana i can slash for a_i damage (unlimited uses) or be thrown for b_i damage (single use). Minimize attacks to defeat the enemy.
- **Core Insight**: Throwing katana j is superior to slashing if and only if b_j > max_a. Sort throwing damages in descending order and throw all katanas with b_j > max_a as long as H > 0. If health remains, finish with ceil(H / max_a) slashes.
- **Complexity**: Time: `O(N log N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long h;
    if (!(cin >> n >> h)) return 0;

    long long max_a = 0;
    vector<long long> b(n);

    for (int i = 0; i < n; ++i) {
        long long ai;
        cin >> ai >> b[i];
        max_a = max(max_a, ai);
    }

    sort(b.rbegin(), b.rend());

    long long attacks = 0;
    for (int i = 0; i < n; ++i) {
        if (b[i] > max_a && h > 0) {
            h -= b[i];
            attacks++;
        } else {
            break;
        }
    }

    if (h > 0) {
        attacks += (h + max_a - 1) / max_a;
    }

    cout << attacks << "\n";
    return 0;
}
```
