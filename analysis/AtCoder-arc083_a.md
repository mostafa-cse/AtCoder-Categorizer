# Problem Analysis: AtCoder-arc083_a — Sugar Water

**Problem ID**: `AtCoder-arc083_a`  
**Contest**: `abc074`  
**Rating / Difficulty**: 1255  
**URL**: https://atcoder.jp/contests/abc074/tasks/arc083_a  
**VJudge Tag**: `[problem:AtCoder-arc083_a]`  
**Category File**: [`../categories/basics/knapsack_density_maximization.md`](../categories/basics/knapsack_density_maximization.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Complete Search`  
- **Topic (Skill)**: `2-Phase Feasible State Enumeration / Knapsack Density Maximization`  

---

## 1. Problem Statement & Key Idea
Operations: add 100A or 100B grams of water, add C or D grams of sugar. Water dissolves up to E grams of sugar per 100g water. Total mass <= F. Maximize sugar concentration 100 * sugar / (water + sugar).

**Key Idea**: The search space for valid water amounts and sugar amounts is small (total mass F <= 3000).

## 2. Core Observation & Invariant
Enumerate all reachable water amounts: water in {100Aa + 100Bb <= F | a, b >= 0, a+b > 0}. Enumerate all reachable sugar amounts: sugar in {Cc + Dd <= F | c, d >= 0}. For every pair (water, sugar), verify: water + sugar <= F and sugar <= (water / 100) * E. Maximize concentration sugar / (water + sugar).

## 3. Step-by-Step Algorithm
1. Collect all reachable water masses <= F in set water_set.
2. Collect all reachable sugar masses <= F in set sugar_set.
3. Iterate w in water_set, s in sugar_set:
4.   If w + s <= F and s * 100 <= w * E: check if s * best_total > best_sugar * (w + s); if so update best.
5. Output best_total and best_sugar.

## 4. Complexity Analysis
- **Time Complexity**: `O(F^2 / (100 * C * D)) <= 10^5 operations`
- **Space Complexity**: `O(F)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Exhaustive reachable state generation for multi-component constraint optimization.
- **Reusable Pattern**: `Independent knapsack generation: enumerate reachable A-states and B-states, test cross product.`
