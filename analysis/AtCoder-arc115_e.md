# Problem Analysis: AtCoder-arc115_e — E. LEQ and NEQ

**Problem ID**: `AtCoder-arc115_e`  
**Contest**: `arc115`  
**Rating / Difficulty**: 2363  
**URL**: https://atcoder.jp/contests/arc115/tasks/arc115_e  
**VJudge Tag**: `[problem:AtCoder-arc115_e]`  
**Category File**: [`../categories/dynamic_programming/monotonic_stack_pie_linear_dp.md`](../categories/dynamic_programming/monotonic_stack_pie_linear_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `DP Optimization using Data Structures [Some Practice Problems]`  

---

## 1. Problem Statement & Key Idea
Count sequences with $1 \le X_i \le A_i$ and $X_i \ne X_{i+1}$. By inclusion-exclusion, the recurrence $f[i] = - \sum_{j < i} f[j] \min_{j < k \le i} A_k$ is evaluated dynamically using a monotonic stack with aggregated dot-products in $O(N)$ time.

## 2. Core Observation & Invariant
By Principle of Inclusion-Exclusion on the conditions $X_i \ne X_{i+1}$, the recurrence is $dp[i] = \sum_{j < i} dp[j] (-1)^{i - 1 - j} \min_{j < k \le i} A_k$. Setting $f[i] = (-1)^i dp[i]$ yields $f[i] = - \sum_{j < i} f[j] \min_{j < k \le i} A_k$. The prefix minimum terms form a monotonic histogram that can be maintained dynamically using a monotonic stack with aggregated sums.

## 3. Step-by-Step Algorithm
1. Transform the DP state to $f[i] = (-1)^i dp[i]$ with $f[0] = 1$.
2. Maintain a monotonic stack of pairs $(val, sum\_f)$ and the current total dot product $S = \sum val \cdot sum\_f$.
3. When $A_i$ arrives, pop all stack entries with $val \ge A_i$, subtracting their contributions from $S$ and accumulating their $sum\_f$ into $cur\_f$.
4. Push $(A_i, cur\_f + f[i-1])$ to the stack, update $S$, and set $f[i] = -S \pmod{MOD}$. At the end, $dp[N] = (-1)^N f[N]$ in $O(N)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

struct Entry {
    long long val;
    long long sum_f;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];

    long long f0 = 1;
    vector<Entry> st;
    long long S = 0;

    long long last_f = f0;
    for (int i = 1; i <= n; i++) {
        long long cur_f = last_f;
        while (!st.empty() && st.back().val >= a[i]) {
            S = (S - st.back().val % MOD * st.back().sum_f % MOD + MOD) % MOD;
            cur_f = (cur_f + st.back().sum_f) % MOD;
            st.pop_back();
        }
        st.push_back({a[i], cur_f});
        S = (S + a[i] % MOD * cur_f) % MOD;
        last_f = (MOD - S) % MOD;
    }

    long long ans = last_f;
    if (n % 2 == 1) ans = (MOD - ans) % MOD;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
