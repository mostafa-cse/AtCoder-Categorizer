# Bitmask Complete Problem Sets with Fractional Greedy Fill

**Domain**: `Basics`  
**Subtopic**: `Bitmask Brute Force`  

This workbook contains curated, high-quality competitive programming problems teaching **Bitmask Complete Problem Sets with Fractional Greedy Fill**.

---

## Curated Problems

### [problem:AtCoder-abc104_c] — All Green
- **Contest**: `abc104`
- **Rating / Difficulty**: 1393
- **Specific Skill**: Bitmask Complete Problem Sets with Fractional Greedy Fill
- **Individual Analysis**: [`../../analysis/AtCoder-abc104_c.md`](../../analysis/AtCoder-abc104_c.md)
- **Problem Statement Summary**: D problem scores: 100i points for solving problem i, plus complete bonus c_i if all p_i problems are solved. Find the minimum total problems solved to achieve score >= G (D <= 10).
- **Core Insight**: Enumerate the 2^D subsets of problem sets that are COMPLETELY solved. If total score from full sets is still < G, greedily solve problems from the highest available unsolved problem set until score >= G. The minimum problems needed across all 2^D masks is optimal.
- **Complexity**: Time: `O(2^D * D)` | Space: `O(D)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct SetInfo {
    int p;
    long long c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int d;
    long long g;
    if (!(cin >> d >> g)) return 0;

    vector<SetInfo> sets(d);
    for (int i = 0; i < d; ++i) {
        cin >> sets[i].p >> sets[i].c;
    }

    int min_problems = 1e9;

    for (int mask = 0; mask < (1 << d); ++mask) {
        long long current_score = 0;
        int current_count = 0;

        for (int i = 0; i < d; ++i) {
            if ((mask >> i) & 1) {
                current_score += (long long)(i + 1) * 100 * sets[i].p + sets[i].c;
                current_count += sets[i].p;
            }
        }

        if (current_score < g) {
            for (int i = d - 1; i >= 0; --i) {
                if (!((mask >> i) & 1)) {
                    long long pt = (i + 1) * 100;
                    long long needed = (g - current_score + pt - 1) / pt;
                    if (needed < sets[i].p) {
                        current_count += needed;
                        current_score += needed * pt;
                        break;
                    } else {
                        current_count += sets[i].p - 1;
                        current_score += (sets[i].p - 1) * pt;
                    }
                }
            }
        }

        if (current_score >= g) {
            min_problems = min(min_problems, current_count);
        }
    }

    cout << min_problems << "\n";
    return 0;
}
```
