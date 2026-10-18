# Problem Analysis: AtCoder-agc062_b — B. Split and Insert

**Problem ID**: `AtCoder-agc062_b`  
**Contest**: `agc062`  
**Rating / Difficulty**: 2407  
**URL**: https://atcoder.jp/contests/agc062/tasks/agc062_b  
**VJudge Tag**: `[problem:AtCoder-agc062_b]`  
**Category File**: [`../categories/dynamic_programming/radix_sort_inverse_permutation_trie_interval_dp.md`](../categories/dynamic_programming/radix_sort_inverse_permutation_trie_interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `Substring DP`  

---

## 1. Problem Statement & Key Idea
Find the minimum cost to transform permutation A into P using K suffix-split-and-insert operations. Reversing the process maps directly to base-2 radix sort on the inverse permutation Q, solved via Trie-based interval DP.

## 2. Core Observation & Invariant
In reverse, each operation takes a subset of elements to the end maintaining relative order—identical to stable sort by a binary digit. A valid sequence of K stable sorts places element i into final order if its assigned K-bit integer X_i satisfies X_i < X_{i+1} whenever Q_i > Q_{i+1}.

## 3. Step-by-Step Algorithm
1. 1. Invert permutation P to obtain Q where P[Q[i]] = i.
2. 2. Check inversions in all subarrays of Q: has_inv[l][r] = true if exists an adjacent descent.
3. 3. Base case (level 0): dp[l][r] = 0 if no inversions exist, else INF.
4. 4. For step s = 1 to K with cost C[K - s]:
5.    dp[l][r] = min(dp[l][r], dp[l][r] + (r-l+1)*cost, min_{m} (dp[l][m-1] + dp[m][r] + (r-m+1)*cost)).

## 4. Complexity Analysis
- **Time Complexity**: `O(K * N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<ll> c(k);
    for (int i = 0; i < k; i++) cin >> c[i];
    reverse(c.begin(), c.end());

    vector<int> p(n);
    vector<int> q(n + 1);
    for (int i = 0; i < n; i++) {
        cin >> p[i];
        q[p[i]] = i + 1;
    }

    vector<vector<bool>> has_inv(n + 1, vector<bool>(n + 1, false));
    for (int l = 1; l <= n; l++) {
        for (int r = l + 1; r <= n; r++) {
            has_inv[l][r] = has_inv[l][r - 1] || (q[r - 1] > q[r]);
        }
    }

    vector<vector<ll>> dp(n + 1, vector<ll>(n + 1, INF));
    for (int l = 1; l <= n; l++) {
        for (int r = l; r <= n; r++) {
            if (!has_inv[l][r]) dp[l][r] = 0;
        }
    }

    for (int s = 1; s <= k; s++) {
        ll cost = c[s - 1];
        vector<vector<ll>> new_dp(n + 1, vector<ll>(n + 1, INF));
        for (int len = 1; len <= n; len++) {
            for (int l = 1; l + len - 1 <= n; l++) {
                int r = l + len - 1;
                ll val = dp[l][r];
                val = min(val, dp[l][r] + (ll)(r - l + 1) * cost);
                for (int m = l + 1; m <= r; m++) {
                    val = min(val, dp[l][m - 1] + dp[m][r] + (ll)(r - m + 1) * cost);
                }
                new_dp[l][r] = val;
            }
        }
        dp = move(new_dp);
    }

    ll ans = dp[1][n];
    if (ans >= INF / 2) {
        cout << -1 << "\n";
    } else {
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
