# Problem Analysis: AtCoder-abc311_g — G. One More Grid Task

**Problem ID**: `AtCoder-abc311_g`  
**Contest**: `abc311`  
**Rating / Difficulty**: 2265  
**URL**: https://atcoder.jp/contests/abc311/tasks/abc311_g  
**VJudge Tag**: `[problem:AtCoder-abc311_g]`  
**Category File**: [`../categories/data_structures_ds/monotonic_stack_2d_grid_min_sum.md`](../categories/data_structures_ds/monotonic_stack_2d_grid_min_sum.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Monotonic Data Structures`  
- **Topic (Skill)**: `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum`  

---

## 1. Problem Statement & Key Idea
Given an $N \times M$ grid of non-negative integers ($N, M \le 300, A_{i,j} \le 300$), select a rectangular subgrid $R$ to maximize $(\sum_{(i,j) \in R} A_{i,j}) \times \min_{(i,j) \in R} A_{i,j}$.

## 2. Core Observation & Invariant
Iterate over all $O(N^2)$ row boundary pairs $[u, d]$. For a fixed pair $[u, d]$, collapse columns into two 1D arrays: column sum $S_j = \sum_{i=u}^d A_{i, j}$ and column minimum $B_j = \min_{i=u}^d A_{i, j}$. Any subsegment of columns $[l, r]$ has subgrid sum $\sum_{j=l}^r S_j$ and minimum $\min_{j=l}^r B_j$. Because all entries $A_{i,j} \ge 1 > 0$, column sums are strictly positive; thus, for a column $k$ acting as the minimum, extending the column range as far left and right as possible while $B_j \ge B_k$ strictly maximizes the sum. Using a monotonic stack, we find the maximal span $[L_k, R_k]$ for each column $k$ in $O(M)$ time.

## 3. Step-by-Step Algorithm
1. Loop over row upper bound $u$ from $0$ to $N-1$.
2. Maintain column sum array $S$ and column minimum array $B$, resetting $S_j = 0, B_j = \infty$.
3. Loop over lower row bound $d$ from $u$ to $N-1$:
4. Accumulate $S_j += A_{d, j}$ and $B_j = \min(B_j, A_{d, j})$, and compute prefix sums of $S$.
5. Use a monotonic stack to compute the left bound $L_j$ (furthest index with elements $\ge B_j$) for all columns in $O(M)$.
6. Use a monotonic stack to compute the right bound $R_j$ (furthest index with elements $\ge B_j$) for all columns in $O(M)$.
7. For each column $j$, update global maximum with $(\text{pref}[R_j + 1] - \text{pref}[L_j]) \times B_j$.
8. Output the maximum result.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 M)`
- **Space Complexity**: `O(N M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> a(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }

    long long ans = 0;
    vector<long long> s(m);
    vector<int> b(m);
    vector<long long> pref(m + 1, 0);
    vector<int> l_bound(m), r_bound(m);
    vector<int> st(m);

    for (int u = 0; u < n; ++u) {
        for (int j = 0; j < m; ++j) {
            s[j] = 0;
            b[j] = 1e9;
        }
        for (int d = u; d < n; ++d) {
            for (int j = 0; j < m; ++j) {
                s[j] += a[d][j];
                b[j] = min(b[j], a[d][j]);
                pref[j + 1] = pref[j] + s[j];
            }

            // Monotonic stack for left bounds
            int top = 0;
            for (int j = 0; j < m; ++j) {
                while (top > 0 && b[st[top - 1]] >= b[j]) {
                    --top;
                }
                l_bound[j] = (top == 0 ? 0 : st[top - 1] + 1);
                st[top++] = j;
            }

            // Monotonic stack for right bounds
            top = 0;
            for (int j = m - 1; j >= 0; --j) {
                while (top > 0 && b[st[top - 1]] >= b[j]) {
                    --top;
                }
                r_bound[j] = (top == 0 ? m - 1 : st[top - 1] - 1);
                st[top++] = j;
            }

            for (int j = 0; j < m; ++j) {
                long long sum_r = pref[r_bound[j] + 1] - pref[l_bound[j]];
                long long cur = sum_r * b[j];
                if (cur > ans) ans = cur;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
