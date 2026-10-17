# Problem Analysis: AtCoder-arc077_c — guruguru

**Problem ID**: `AtCoder-arc077_c`  
**Contest**: `arc077`  
**Rating / Difficulty**: 2117  
**URL**: https://atcoder.jp/contests/arc077/tasks/arc077_c  
**VJudge Tag**: `[problem:AtCoder-arc077_c]`  
**Category File**: [`../categories/basics/second_order_difference_array_slope_imos.md`](../categories/basics/second_order_difference_array_slope_imos.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `More Techniques`  
- **Topic (Skill)**: `Difference Array`  

---

## 1. Problem Statement & Key Idea
A circular dial has M positions 1..M. In each transition a_i -> a_{i+1}, you can step +1 or jump directly to a preset favorite button x. Find the optimal x to minimize total button presses.

**Key Insight**: For a transition from u to v of distance d = (v - u + M) mod M, setting the favorite button to x saves presses if x lies on the forward arc: savings start at 0 at u+1, increase with slope +1 up to v (where savings = d - 1), then drop to 0 at v+1. Because the savings function is piecewise linear, we can use second-order difference arrays (slope changes) to add the piecewise linear functions from all transitions in O(1) each, then integrate twice to find the maximum savings.

## 2. Core Observation & Invariant
Piecewise linear cost functions on circular domains are efficiently aggregated via second-order difference arrays (slope imos).

## 3. Step-by-Step Algorithm
1. Compute base cost sum (a_{i+1} - a_i + M) mod M.
2. For each transition with distance d > 1:
3.   Add +1 slope change at u + 2.
4.   Add -d slope change at u + d + 1.
5.   Add +(d - 1) slope change at u + d + 2.
6. Integrate second-order differences twice to recover savings for each x in [1, M].
7. Find maximum savings and subtract from base cost.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(M)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Second-order difference array integration for circular piecewise linear optimization.
- **Reusable Pattern**: Aggregating piecewise linear savings functions over circular intervals via double prefix sums.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    long long base_cost = 0;
    vector<long long> d2(2 * m + 5, 0);

    for (int i = 0; i < n - 1; ++i) {
        int from = a[i];
        int to = a[i + 1];
        long long dist = (to - from + m) % m;
        base_cost += dist;

        if (dist > 1) {
            int l = from + 2;
            int r = from + dist;
            d2[l] += 1;
            d2[r + 1] -= (dist);
            d2[r + 2] += (dist - 1);
        }
    }

    vector<long long> slope(2 * m + 5, 0);
    vector<long long> savings_extended(2 * m + 5, 0);

    long long cur_slope = 0;
    long long cur_savings = 0;
    for (int x = 1; x <= 2 * m; ++x) {
        cur_slope += d2[x];
        slope[x] = cur_slope;
        cur_savings += cur_slope;
        savings_extended[x] = cur_savings;
    }

    vector<long long> savings(m + 1, 0);
    for (int x = 1; x <= 2 * m; ++x) {
        int actual_x = (x - 1) % m + 1;
        savings[actual_x] += savings_extended[x];
    }

    long long max_savings = 0;
    for (int x = 1; x <= m; ++x) {
        max_savings = max(max_savings, savings[x]);
    }

    cout << base_cost - max_savings << "\n";
    return 0;
}
```
