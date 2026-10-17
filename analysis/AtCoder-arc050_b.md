# Problem Analysis: AtCoder-arc050_b — 花束

**Problem ID**: `AtCoder-arc050_b`  
**Contest**: `arc050`  
**Rating / Difficulty**: 1838  
**URL**: https://atcoder.jp/contests/arc050/tasks/arc050_b  
**VJudge Tag**: `[problem:AtCoder-arc050_b]`  
**Category File**: [`../categories/basics/binary_search_dual_recipe_allocation.md`](../categories/basics/binary_search_dual_recipe_allocation.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Binary Search`  
- **Topic (Skill)**: `Binary Search on Answer for Dual-Recipe Resource Allocation`  

---

## 1. Problem Statement & Key Idea
You have R red flowers and B blue flowers. Bouquet type 1 needs x red and 1 blue. Bouquet type 2 needs 1 red and y blue. Find the maximum total number of bouquets you can make.

**Key Insight**: Binary search on total bouquets K. If we make K bouquets, every bouquet needs at least 1 red and 1 blue (requiring R >= K and B >= K). The remaining R - K red flowers and B - K blue flowers can absorb extra requirements (x - 1 and y - 1).

## 2. Core Observation & Invariant
Feasibility condition for K: R >= K and B >= K and floor((R - K) / (x - 1)) + floor((B - K) / (y - 1)) >= K.

## 3. Step-by-Step Algorithm
1. low = 0, high = min(R, B), ans = 0.
2. While low <= high:
3.   K = low + (high - low) / 2.
4.   extra_type1 = (R - K) / (x - 1).
5.   extra_type2 = (B - K) / (y - 1).
6.   if extra_type1 + extra_type2 >= K: ans = K, low = K + 1.
7.   else high = K - 1.
8. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(log(min(R, B)))`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long R, B, x, y;
    if (!(cin >> R >> B >> x >> y)) return 0;

    long long low = 0, high = min(R, B), ans = 0;

    while (low <= high) {
        long long K = low + (high - low) / 2;
        long long extra1 = (R - K) / (x - 1);
        long long extra2 = (B - K) / (y - 1);

        if (extra1 + extra2 >= K) {
            ans = K;
            low = K + 1;
        } else {
            high = K - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Basing resource feasibility on baseline consumption plus fractional extra absorptions.
- **Reusable Pattern**: `Dual Recipe Allocation: Reserve baseline K, then verify sum floor((Total - K)/(Cost - 1)) >= K.`
