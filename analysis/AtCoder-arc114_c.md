# Problem Analysis: AtCoder-arc114_c — Sequence Scores

**Problem ID**: `AtCoder-arc114_c`  
**Contest**: `arc114`  
**Rating / Difficulty**: 2056  
**URL**: https://atcoder.jp/contests/arc114/tasks/arc114_c  
**VJudge Tag**: `[problem:AtCoder-arc114_c]`  
**Category File**: [`../categories/combinatorics/contribution_linearity_of_expectation.md`](../categories/combinatorics/contribution_linearity_of_expectation.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Counting Principles`  
- **Topic (Skill)**: `Contribution to the Sum and Linearity of Expectation`  

---

## 1. Problem Statement & Key Idea
Starting from an all-zero sequence X of length N, let f(A) be the minimum number of range-max operations [l, r, v] (X_i <- max(X_i, v)) to make X equal A. Compute the sum of f(A) over all M^N sequences A with elements in [1, M] modulo 998244353.

**Key Idea**: An element A_i = v requires a new operation unless there exists a prior j < i with A_j = v such that all intermediate elements A_k > v for k in (j, i). If such j exists, A_i can be merged into the operation that created A_j. Thus f(A) = N - (number of saved indices). By linearity of expectation, we sum the probability of saving over all pairs (j, i) with distance d = i - j: A_j = A_i = v has 1 choice, intermediate d-1 elements must be > v ((M - v) choices each), and the remaining N - 1 - d elements have M choices each.

## 2. Core Observation & Invariant
f(A) is exactly N minus the number of pairs (j, i) such that A_j = A_i and all intermediate elements are strictly greater than A_j.

## 3. Step-by-Step Algorithm
1. Total operations without savings is N * M^N.
2. Iterate distance d = 1 to N - 1.
3. For each d, the number of pairs (j, i) with i - j = d is N - d.
4. Sum over v in [1, M] of (M - v)^(d - 1) is sum_{t=0}^{M-1} t^(d - 1). Precompute/maintain this power sum in O(M).
5. Multiply by (N - d) * M^(N - 1 - d) and accumulate saved operations.
6. Output (N * M^N - total_saved) modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(M)`

## 5. Core Algorithmic Skill & Learning Takeaway
Decomposing complex greedy cost functions into pairwise savings and counting via linearity of expectation.

**Reusable Pattern**: Range overwrite operation savings: A_i merges with previous A_j = A_i iff all elements between them strictly exceed A_i.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    long long total_all = (1LL * n % MOD) * power(m, n) % MOD;
    long long total_saved = 0;
    vector<long long> pow_t(m, 1);

    for (int d = 1; d <= n - 1; ++d) {
        long long sum_t = 0;
        for (int t = 0; t < m; ++t) {
            sum_t = (sum_t + pow_t[t]) % MOD;
            pow_t[t] = (pow_t[t] * t) % MOD;
        }
        long long ways = (1LL * (n - d) % MOD) * power(m, n - 1 - d) % MOD;
        ways = (ways * sum_t) % MOD;
        total_saved = (total_saved + ways) % MOD;
    }

    long long ans = (total_all - total_saved + MOD) % MOD;
    cout << ans << "\n";
    return 0;
}
```
