# Problem Analysis: AtCoder-arc232_a — A. Permutation Journey

**Problem ID**: `AtCoder-arc232_a`  
**Contest**: `arc232`  
**Rating / Difficulty**: 2331  
**URL**: https://atcoder.jp/contests/arc232/tasks/arc232_a  
**VJudge Tag**: `[problem:AtCoder-arc232_a]`  
**Category File**: [`../categories/dynamic_programming/interval_reachability_monotone_dp.md`](../categories/dynamic_programming/interval_reachability_monotone_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `1D1D DP Optimization`  

---

## 1. Problem Statement & Key Idea
Given intervals $[L_j, R_j]$, find whether there exists a permutation visiting elements such that consecutive steps adhere to interval constraints. Adding sentinels and tracking valid predecessor ranges via 1D monotone reachability DP solves in $O((N + M) \log N)$.

## 2. Core Observation & Invariant
Adding sentinels at 1, 2 and $N+3, N+4$ models full traversals. For each target index $z$, a valid previous position $y$ must satisfy $A_z \le y < B_z$ where $A_z = \max_{R_j < z} L_j$ and $B_z = \min_{z \le R_j} L_j$. The set of reachable earlier positions at each step forms a contiguous interval $[L_{dp}[z], R_{dp}[z]]$ due to monotonicity of $A_z$ and $B_z$.

## 3. Step-by-Step Algorithm
1. Precompute $A_z$ and $B_z$ using two-pointer sweeps or prefix/suffix maximums and minimums.
2. Maintain the reachable interval of previous indices $dp[z]$ using monotone two-pointer or binary search verification, yielding a complete solution in $O((N + M) \log N)$ or $O(N + M)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) \log N)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, m;
    if (!(cin >> n >> m)) return;

    vector<pair<int, int>> intervals(m);
    bool impossible = false;
    for (int i = 0; i < m; ++i) {
        cin >> intervals[i].first >> intervals[i].second;
        if (intervals[i].second - intervals[i].first + 1 < 2) {
            impossible = true;
        }
    }

    if (impossible) {
        cout << "No\n";
        return;
    }

    int n_prime = n + 4;
    vector<vector<int>> by_r(n_prime + 2);
    vector<vector<pair<int, int>>> by_l(n_prime + 2);

    for (int i = 0; i < m; ++i) {
        int l = intervals[i].first + 2;
        int r = intervals[i].second + 2;
        by_r[r].push_back(l);
        by_l[l].emplace_back(l, r);
    }

    const int INF = 1e9;
    vector<int> A(n_prime + 1, -1);
    int cur_a = -1;
    for (int z = 1; z <= n_prime; ++z) {
        for (int l : by_r[z - 1]) {
            cur_a = max(cur_a, l);
        }
        A[z] = cur_a;
    }

    vector<int> B(n_prime + 1, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    for (int z = 1; z <= n_prime; ++z) {
        for (auto &item : by_l[z]) {
            pq.push(item);
        }
        while (!pq.empty() && pq.top().second < z) {
            pq.pop();
        }
        if (!pq.empty()) {
            B[z] = pq.top().first;
        }
    }

    vector<int> dp_min(n_prime + 1, INF);
    vector<int> dp_max(n_prime + 1, -INF);

    dp_min[2] = 1;
    dp_max[2] = 1;

    vector<int> valid_ys;
    valid_ys.push_back(2);

    for (int z = 3; z <= n_prime; ++z) {
        int low_x = A[z];
        int high_x = B[z] - 1;
        if (low_x > high_x) continue;

        int l = 0, r = (int)valid_ys.size() - 1;
        int ans1 = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int y = valid_ys[mid];
            if (dp_max[y] >= low_x) {
                ans1 = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        l = 0;
        r = (int)valid_ys.size() - 1;
        int ans2 = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int y = valid_ys[mid];
            if (dp_min[y] <= high_x) {
                ans2 = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        if (ans1 != -1 && ans2 != -1 && ans1 <= ans2) {
            int y_first = valid_ys[ans1];
            int y_last = valid_ys[ans2];
            if (y_first < z) {
                y_last = min(y_last, z - 1);
                if (y_first <= y_last) {
                    dp_min[z] = y_first;
                    dp_max[z] = y_last;
                    valid_ys.push_back(z);
                }
            }
        }
    }

    if (dp_min[n_prime] <= n_prime - 1 && n_prime - 1 <= dp_max[n_prime]) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
