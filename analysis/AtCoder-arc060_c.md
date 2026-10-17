# Problem Analysis: AtCoder-arc060_c — Tak and Hotels

**Problem ID**: `AtCoder-arc060_c`  
**Contest**: `arc060`  
**Rating / Difficulty**: 2154  
**URL**: https://atcoder.jp/contests/arc060/tasks/arc060_c  
**VJudge Tag**: `[problem:AtCoder-arc060_c]`  
**Category File**: [`../categories/graph_theory/binary_lifting_interval_reachability.md`](../categories/graph_theory/binary_lifting_interval_reachability.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Lowest Common Ancestor (LCA)`  
- **Topic (Skill)**: `Binary Lifting and LCA`  

---

## 1. Problem Statement & Key Idea
Given N sorted hotels on a line and maximum daily travel distance L, answer Q queries finding the minimum number of days to travel between hotel a and hotel b. Monotonicity implies each step greedily jumps to the farthest reachable hotel, modeled as binary lifting on functional graphs.

## 2. Core Observation & Invariant
Because staying at a hotel further along the line strictly dominates staying closer, the optimal next hotel from hotel i is the maximum j such that x[j] - x[i] <= L (when moving right) or minimum j such that x[i] - x[j] <= L (when moving left). Binary lifting precomputes the hotel reached after 2^k daily maximal jumps.

## 3. Step-by-Step Algorithm
1. For each hotel i, use binary search (upper_bound / lower_bound) to find the farthest reachable hotel in one day to the right and left.
2. Build binary lifting tables up_r[k][i] and up_l[k][i] for k = 0..17.
3. For each query (a, b) with a < b, binary lift from a using up_r while the 2^k destination is strictly less than b, accumulating 2^k days, and add 1 final day.
4. Handle queries with a > b symmetrically using up_l.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N log N)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXLOG = 18;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> x(n + 1);
    for (int i = 1; i <= n; ++i) cin >> x[i];

    long long L;
    cin >> L;

    int q;
    cin >> q;

    vector<vector<int>> up_r(MAXLOG, vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        int idx = upper_bound(x.begin() + 1, x.end(), x[i] + L) - x.begin() - 1;
        up_r[0][i] = idx;
    }

    for (int k = 1; k < MAXLOG; ++k) {
        for (int i = 1; i <= n; ++i) {
            up_r[k][i] = up_r[k - 1][up_r[k - 1][i]];
        }
    }

    vector<vector<int>> up_l(MAXLOG, vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        int idx = lower_bound(x.begin() + 1, x.end(), x[i] - L) - x.begin();
        up_l[0][i] = idx;
    }

    for (int k = 1; k < MAXLOG; ++k) {
        for (int i = 1; i <= n; ++i) {
            up_l[k][i] = up_l[k - 1][up_l[k - 1][i]];
        }
    }

    while (q--) {
        int a, b;
        cin >> a >> b;
        if (a < b) {
            int ans = 0;
            int curr = a;
            for (int k = MAXLOG - 1; k >= 0; --k) {
                if (up_r[k][curr] < b) {
                    ans += (1 << k);
                    curr = up_r[k][curr];
                }
            }
            ans++;
            cout << ans << "\n";
        } else {
            int ans = 0;
            int curr = a;
            for (int k = MAXLOG - 1; k >= 0; --k) {
                if (up_l[k][curr] > b) {
                    ans += (1 << k);
                    curr = up_l[k][curr];
                }
            }
            ans++;
            cout << ans << "\n";
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
