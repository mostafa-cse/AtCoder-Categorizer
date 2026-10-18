# Problem Analysis: AtCoder-arc128_d — D. Neq Neq

**Problem ID**: `AtCoder-arc128_d`  
**Contest**: `arc128`  
**Rating / Difficulty**: 2554  
**URL**: https://atcoder.jp/contests/arc128/tasks/arc128_d  
**VJudge Tag**: `[problem:AtCoder-arc128_d]`  
**Category File**: [`../categories/dynamic_programming_dp/neq_neq_linear_dp_alternating_runs.md`](../categories/dynamic_programming_dp/neq_neq_linear_dp_alternating_runs.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Count reachable subsets of remaining elements when deleting $y$ from three consecutive elements $(x, y, z)$ with $x \ne y$ and $y \ne z$. An internal segment $A[j+1 \dots i-1]$ can be completely deleted leaving $A[j]$ and $A[i]$ adjacent iff: for $i - j = 1$ (always); for $i - j = 2$ (iff $A[j] \ne A[j+1] \ne A[i]$); and for $i - j \ge 3$ (iff $A[j \dots i]$ has no adjacent duplicates AND contains at least 3 distinct values).

## 2. Core Observation & Invariant
Because adjacent duplicates $A_k = A_{k+1}$ can never both be deleted, any valid $j$ must have $j \ge last\_dup$. Furthermore, an alternating sequence $a, b, a, b \dots$ has only 2 distinct values. By tracking $alt\_len[i]$, the start of the alternating suffix ending at $i$ is $i - alt\_len[i] + 1$. Thus, every $j \le i - alt\_len[i]$ has $\ge 3$ distinct values! Transitions for $j \le i - 3$ reduce to range sum $\max(0, last\_dup) \le j \le \min(i - 3, i - alt\_len[i])$.

## 3. Step-by-Step Algorithm
1. 1. Initialize $DP[0] = 1$, prefix sums $pref[1] = 1$, $last\_dup = -1$.
2. 2. For $i$ from 1 to $N-1$:
3.    a. Update $last\_dup = i$ if $A[i] == A[i-1]$.
4.    b. Update $alt\_len[i]$ (length of alternating run $a, b, a, b$ ending at $i$).
5.    c. Add $DP[i-1]$ (direct step).
6.    d. If $i \ge 2$ and $A[i] \ne A[i-1] \ne A[i-2]$, add $DP[i-2]$.
7.    e. For $j \le i - 3$: query prefix sum for $j \in [\max(0, last\_dup), \min(i - 3, i - alt\_len[i])]$.
8.    f. Update prefix sum array.
9. 3. Output $DP[N - 1] \pmod{998244353}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> dp(n, 0);
    vector<long long> pref(n + 1, 0);

    dp[0] = 1;
    pref[1] = 1;

    int last_dup = -1;
    vector<int> alt_len(n, 1);

    for (int i = 1; i < n; ++i) {
        if (a[i] == a[i - 1]) {
            last_dup = i;
            alt_len[i] = 1;
        } else if (i >= 2 && a[i] == a[i - 2]) {
            alt_len[i] = alt_len[i - 1] + 1;
        } else {
            alt_len[i] = 2;
        }

        // 1. Direct step from i-1
        dp[i] = (dp[i] + dp[i - 1]) % MOD;

        // 2. Step from i-2 if a[i] != a[i-1] && a[i-1] != a[i-2]
        if (i >= 2 && a[i] != a[i - 1] && a[i - 1] != a[i - 2]) {
            dp[i] = (dp[i] + dp[i - 2]) % MOD;
        }

        // 3. Step from j <= i - 3 where [j, i] has no duplicates and >= 3 distinct values
        // That is: max(0, last_dup) <= j <= min(i - 3, i - alt_len[i])
        int min_j = max(0, last_dup);
        int max_j = min(i - 3, i - alt_len[i]);

        if (min_j <= max_j) {
            long long sum_range = (pref[max_j + 1] - pref[min_j] + MOD) % MOD;
            dp[i] = (dp[i] + sum_range) % MOD;
        }

        pref[i + 1] = (pref[i] + dp[i]) % MOD;
    }

    cout << dp[n - 1] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
