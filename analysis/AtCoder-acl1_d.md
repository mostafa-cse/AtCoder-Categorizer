# Problem Analysis: AtCoder-acl1_d — D - Keep Distances

**Problem ID**: `AtCoder-acl1_d`  
**Contest**: `acl1`  
**Rating / Difficulty**: 2764  
**URL**: https://atcoder.jp/contests/acl1/tasks/acl1_d  
**VJudge Tag**: `[problem:AtCoder-acl1_d]`  
**Category File**: [`../categories/graph_theory/keep_distances_binary_lifting_union.md`](../categories/graph_theory/keep_distances_binary_lifting_union.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Lowest Common Ancestor (LCA)`  
- **Topic (Skill)**: `Binary Lifting and LCA`  

---

## 1. Problem Statement & Key Idea
Given N points on a line X_1 < ... < X_N and an integer K, process Q queries. Each query gives [L, R]. A good set is a maximum-size subset of points in [L, R] with pairwise distance >= K. Find the size of the union of all good sets.

## 2. Core Observation & Invariant
Let m be the maximum size of a good set in [L, R]. Greedy selection from left to right yields indices a_1 < a_2 < ... < a_m, and greedy selection from right to left yields b_1 < b_2 < ... < b_m. It holds that a_1 <= b_1 < a_2 <= b_2 < ... < a_m <= b_m. A point p belongs to some good set if and only if p in [a_i, b_i] for some i. The size of the union is sum_{i=1}^m (b_i - a_i + 1) = m + sum b_i - sum a_i. Both the sequence a_i and b_i and their index sums can be computed using binary lifting (doubling) in O(log N) per query.

## 3. Step-by-Step Algorithm
1. 1. Precompute binary lifting tables up_r[k][i] and cost_r[k][i] for the first point >= X_i + K.
2. 2. Precompute binary lifting tables up_l[k][i] and cost_l[k][i] for the last point <= X_i - K.
3. 3. For each query (L, R):
4.    a. Jump forward from L using up_r to find m and total_a = sum a_i.
5.    b. Jump backward m-1 steps from R using up_l to find total_b = sum b_i.
6.    c. Answer is m + total_b - total_a.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N log N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int LOG = 19;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) cin >> x[i];

    vector<vector<int>> up_r(LOG, vector<int>(n + 2, n + 1));
    vector<vector<long long>> cost_r(LOG, vector<long long>(n + 2, 0));
    vector<vector<int>> up_l(LOG, vector<int>(n + 2, 0));
    vector<vector<long long>> cost_l(LOG, vector<long long>(n + 2, 0));

    for (int i = 1; i <= n; ++i) {
        // First j such that x[j] >= x[i-1] + k
        auto it = lower_bound(x.begin(), x.end(), x[i - 1] + k);
        if (it != x.end()) {
            int idx = (int)(it - x.begin()) + 1;
            up_r[0][i] = idx;
            cost_r[0][i] = idx;
        } else {
            up_r[0][i] = n + 1;
            cost_r[0][i] = 0;
        }

        // Last j such that x[j] <= x[i-1] - k
        auto it_l = upper_bound(x.begin(), x.end(), x[i - 1] - k);
        if (it_l != x.begin()) {
            int idx = (int)(it_l - x.begin());
            up_l[0][i] = idx;
            cost_l[0][i] = idx;
        } else {
            up_l[0][i] = 0;
            cost_l[0][i] = 0;
        }
    }

    for (int step = 1; step < LOG; ++step) {
        for (int i = 1; i <= n; ++i) {
            int mid_r = up_r[step - 1][i];
            if (mid_r <= n) {
                up_r[step][i] = up_r[step - 1][mid_r];
                cost_r[step][i] = cost_r[step - 1][i] + cost_r[step - 1][mid_r];
            } else {
                up_r[step][i] = n + 1;
                cost_r[step][i] = cost_r[step - 1][i];
            }

            int mid_l = up_l[step - 1][i];
            if (mid_l >= 1) {
                up_l[step][i] = up_l[step - 1][mid_l];
                cost_l[step][i] = cost_l[step - 1][i] + cost_l[step - 1][mid_l];
            } else {
                up_l[step][i] = 0;
                cost_l[step][i] = cost_l[step - 1][i];
            }
        }
    }

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int L, R;
        cin >> L >> R;

        int cur_r = L;
        long long total_a = L;
        int m = 1;
        for (int step = LOG - 1; step >= 0; --step) {
            if (up_r[step][cur_r] <= R) {
                total_a += cost_r[step][cur_r];
                cur_r = up_r[step][cur_r];
                m += (1 << step);
            }
        }

        int cur_l = R;
        long long total_b = R;
        int rem = m - 1;
        for (int step = 0; step < LOG; ++step) {
            if ((rem >> step) & 1) {
                total_b += cost_l[step][cur_l];
                cur_l = up_l[step][cur_l];
            }
        }

        long long ans = (long long)m + total_b - total_a;
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
