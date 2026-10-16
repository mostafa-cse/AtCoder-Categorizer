# 2-Phase Feasible State Enumeration / Knapsack Density Maximization

**Domain**: `Basics`  
**Subtopic**: `Complete Search`  

This workbook contains curated, high-quality competitive programming problems teaching **2-Phase Feasible State Enumeration / Knapsack Density Maximization**.

---

## Curated Problems

### [problem:AtCoder-arc083_a] — Sugar Water
- **Contest**: `abc074`
- **Rating / Difficulty**: 1255
- **Specific Skill**: 2-Phase Feasible State Enumeration / Knapsack Density Maximization
- **Individual Analysis**: [`../../analysis/AtCoder-arc083_a.md`](../../analysis/AtCoder-arc083_a.md)
- **Problem Statement Summary**: Operations: add 100A or 100B grams of water, add C or D grams of sugar. Water dissolves up to E grams of sugar per 100g water. Total mass <= F. Maximize sugar concentration 100 * sugar / (water + sugar).
- **Core Insight**: Enumerate all reachable water amounts: water in {100Aa + 100Bb <= F | a, b >= 0, a+b > 0}. Enumerate all reachable sugar amounts: sugar in {Cc + Dd <= F | c, d >= 0}. For every pair (water, sugar), verify: water + sugar <= F and sugar <= (water / 100) * E. Maximize concentration sugar / (water + sugar).
- **Complexity**: Time: `O(F^2 / (100 * C * D)) <= 10^5 operations` | Space: `O(F)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, c, d, e, f;
    if (!(cin >> a >> b >> c >> d >> e >> f)) return 0;

    vector<bool> can_water(f + 1, false);
    for (int i = 0; 100 * a * i <= f; ++i) {
        for (int j = 0; 100 * a * i + 100 * b * j <= f; ++j) {
            int w = 100 * a * i + 100 * b * j;
            if (w > 0) can_water[w] = true;
        }
    }

    vector<bool> can_sugar(f + 1, false);
    can_sugar[0] = true;
    for (int i = 0; c * i <= f; ++i) {
        for (int j = 0; c * i + d * j <= f; ++j) {
            can_sugar[c * i + d * j] = true;
        }
    }

    long long best_total = 100 * a;
    long long best_sugar = 0;

    for (int w = 1; w <= f; ++w) {
        if (!can_water[w]) continue;
        for (int s = 0; w + s <= f; ++s) {
            if (!can_sugar[s]) continue;
            if (s <= (w / 100) * e) {
                // Compare s / (w + s) > best_sugar / best_total
                if (s * best_total > best_sugar * (w + s)) {
                    best_total = w + s;
                    best_sugar = s;
                }
            }
        }
    }

    cout << best_total << " " << best_sugar << "\n";
    return 0;
}
```
