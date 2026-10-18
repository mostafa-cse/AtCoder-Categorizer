# Problem Analysis: AtCoder-agc030_b — B. Tree Burning

**Problem ID**: `AtCoder-agc030_b`  
**Contest**: `agc030`  
**Rating / Difficulty**: 2342  
**URL**: https://atcoder.jp/contests/agc030/tasks/agc030_b  
**VJudge Tag**: `[problem:AtCoder-agc030_b]`  
**Category File**: [`../categories/basics/alternating_circular_walk_burning.md`](../categories/basics/alternating_circular_walk_burning.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Find the maximum distance to burn all trees along a circular walk. The optimal path alternates visiting the leftmost and rightmost unburned trees, evaluated over all $N$ split points using prefix sums in $O(N)$.

## 2. Core Observation & Invariant
To maximize walking distance on a circle of length $L$, the traveler must alternate moving between the leftmost and rightmost unburned trees (crossing origin 0 each time to maximize step length). The optimal trajectory visits a prefix of $k$ trees from one direction and $N-k$ from the opposite, with strictly alternating steps at the end.

## 3. Step-by-Step Algorithm
1. Express tree distances $X_i$ clockwise and $L - X_i$ counterclockwise.
2. For each split point $k \in [1, N]$, Takahashi visits $k$ trees on the right and $N-k$ on the left. The total distance expands as a linear combination of tree positions with alternating coefficients $2, 4, 6, \dots$.
3. Compute prefix sums of $X_i$ and $i \cdot X_i$ (or standard prefix sums) to evaluate each candidate split point in $O(1)$, taking $O(N)$ time overall.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L;
    int n;
    if (!(cin >> L >> n)) return 0;

    vector<long long> X(n);
    for (int i = 0; i < n; ++i) {
        cin >> X[i];
    }

    vector<long long> A(n + 1, 0), B(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        A[i] = X[i - 1];
        B[i] = L - X[n - i];
    }

    vector<long long> sumA(n + 1, 0), sumB(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        sumA[i] = sumA[i - 1] + A[i];
        sumB[i] = sumB[i - 1] + B[i];
    }

    auto query = [&](const vector<long long>& vA, const vector<long long>& vB,
                     const vector<long long>& sA, const vector<long long>& sB) -> long long {
        long long best = 0;
        for (int k = 1; k <= n; ++k) {
            int m = n - k;
            if (k > m) {
                long long val = 2 * sB[m] + 2 * (sA[k] - sA[k - m - 1]) - vA[k];
                best = max(best, val);
            } else {
                long long val = 2 * sA[k] - vA[k] + 2 * (sB[m] - sB[m - k]);
                best = max(best, val);
            }
        }
        return best;
    };

    long long ans = max(query(A, B, sumA, sumB), query(B, A, sumB, sumA));
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
