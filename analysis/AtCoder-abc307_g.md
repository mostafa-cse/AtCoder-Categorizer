# Problem Analysis: AtCoder-abc307_g — G. Approximate Equalization

**Problem ID**: `AtCoder-abc307_g`  
**Contest**: `abc307`  
**Rating / Difficulty**: 2330  
**URL**: https://atcoder.jp/contests/abc307/tasks/abc307_g  
**VJudge Tag**: `[problem:AtCoder-abc307_g]`  
**Category File**: [`../categories/dynamic_programming/prefix_sum_approximate_equalization_dp.md`](../categories/dynamic_programming/prefix_sum_approximate_equalization_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Given array $A$ of length $N$, you can repeatedly choose an index $i$ and replace $(A_i, A_{i+1})$ with $(A_i - 1, A_{i+1} + 1)$. Minimize the sum of squared differences or prefix sum deviations to equalize the elements.

## 2. Core Observation & Invariant
The total sum $S = \sum A_i$ is invariant under adjacent transfer. The target sequence $B$ consists of exactly $r = S \bmod N$ elements equal to $q + 1$ and $N - r$ elements equal to $q = \lfloor S / N \rfloor$. The minimum operations equals $\sum_{i=1}^{N-1} |\text{pref}_A[i] - \text{pref}_B[i]|$.

## 3. Step-by-Step Algorithm
1. If $j$ elements among $B_1 \dots B_i$ are $q + 1$, then $\text{pref}_B[i] = i \cdot q + j$.
2. Formulate a 2D DP $dp[i][j]$ representing the minimum prefix sum difference after deciding the first $i$ elements with $j$ values of $q + 1$.
3. Transition in $O(1)$ by choosing $B_i = q$ or $B_i = q + 1$, optimizing space to 2 rows to solve the problem in $O(N \cdot r) = O(N^2)$ time and $O(N)$ space.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    long long s = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        s += a[i];
    }

    long long q = s / n;
    long long r = s % n;
    if (r < 0) {
        r += n;
        q -= 1;
    }

    vector<long long> pref_a(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        pref_a[i + 1] = pref_a[i] + a[i];
    }

    vector<long long> dp(r + 1, INF);
    dp[0] = 0;

    for (int i = 1; i <= n; ++i) {
        vector<long long> next_dp(r + 1, INF);
        int j_min = max(0LL, r - (n - i));
        int j_max = min(1LL * i, r);

        for (int j = j_min; j <= j_max; ++j) {
            long long cost_cur = (i < n ? abs(pref_a[i] - (1LL * i * q + j)) : 0);

            if (dp[j] < INF) {
                next_dp[j] = min(next_dp[j], dp[j] + cost_cur);
            }
            if (j > 0 && dp[j - 1] < INF) {
                next_dp[j] = min(next_dp[j], dp[j - 1] + cost_cur);
            }
        }
        dp = std::move(next_dp);
    }

    cout << dp[r] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
