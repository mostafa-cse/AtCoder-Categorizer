# Problem Analysis: AtCoder-hitachi2020_d — D. Manga Market

**Problem ID**: `AtCoder-hitachi2020_d`  
**Contest**: `hitachi2020`  
**Rating / Difficulty**: 2547  
**URL**: https://atcoder.jp/contests/hitachi2020/tasks/hitachi2020_d  
**VJudge Tag**: `[problem:AtCoder-hitachi2020_d]`  
**Category File**: [`../categories/miscellaneous/manga_market_exchange_argument_knapsack.md`](../categories/miscellaneous/manga_market_exchange_argument_knapsack.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Greedy Algorithms`  
- **Topic (Skill)**: `Exchange Arguments`  

---

## 1. Problem Statement & Key Idea
There are $N$ stores. Visiting store $i$ with arrival time $t$ has departure time $(a_i + 1)t + (b_i + 1)$. For stores with $a_i \ge 1$, visiting store $i$ then $j$ is better than $j$ then $i$ when $(b_i + 1) a_j < (b_j + 1) a_i$ by exchange argument. Furthermore, because $(a_i + 1) \ge 2$, time doubles at each step, so at most $\log_2(T) \le 30$ stores with $a_i \ge 1$ can be visited before time $T$.

## 2. Core Observation & Invariant
Stores with $a_i = 0$ add a constant cost $b_i + 1$ independent of arrival time. They should be visited greedily in increasing order of $b_i + 1$. For stores with $a_i \ge 1$, sort by $(b_i + 1) / a_i$ and run Knapsack DP: $DP[k]$ is the minimum time to visit $k$ stores ($0 \le k \le 30$). The remaining time $T - DP[k]$ greedily accommodates $a_i = 0$ stores via binary search.

## 3. Step-by-Step Algorithm
1. 1. Separate stores into $a_i > 0$ and $a_i = 0$.
2. 2. Sort $a_i > 0$ stores by exchange argument condition $(b_i + 1) a_j < (b_j + 1) a_i$.
3. 3. Sort $a_i = 0$ stores by $b_i + 1$ and compute prefix sums.
4. 4. Run 1D DP: $DP[k]$ = min departure time after $k$ stores ($0 \le k \le 35$).
5. 5. For each $k$, binary search on prefix sums of $a_i = 0$ stores to find how many fit in $T - DP[k]$.
6. 6. Maximize $k + \text{count}_{a=0}$ over all $k$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N + 35 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Store {
    long long a, b;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long T;
    if (!(cin >> n >> T)) return 0;

    vector<Store> pos_a;
    vector<long long> zero_a;

    for (int i = 0; i < n; ++i) {
        long long a, b;
        cin >> a >> b;
        if (a > 0) {
            pos_a.push_back({a, b});
        } else {
            zero_a.push_back(b + 1); // cost is travel 1 + waiting b
        }
    }

    // Sort pos_a by exchange argument: (b_i + 1) * a_j < (b_j + 1) * a_i
    sort(pos_a.begin(), pos_a.end(), [](const Store& x, const Store& y) {
        return (x.b + 1) * y.a < (y.b + 1) * x.a;
    });

    sort(zero_a.begin(), zero_a.end());
    vector<long long> pref_zero(zero_a.size() + 1, 0);
    for (size_t i = 0; i < zero_a.size(); ++i) {
        pref_zero[i + 1] = pref_zero[i] + zero_a[i];
    }

    int max_pos = min(35, (int)pos_a.size());
    const long long INF = 2e18;
    vector<long long> dp(max_pos + 1, INF);
    dp[0] = 0;

    for (const auto& st : pos_a) {
        for (int k = max_pos - 1; k >= 0; --k) {
            if (dp[k] >= INF) continue;
            // arrival at dp[k] + 1
            long long arr = dp[k] + 1;
            if (arr > T) continue;
            // departure at (a + 1) * arr + b
            long long nxt;
            if (__builtin_mul_overflow(st.a + 1, arr, &nxt)) continue;
            nxt += st.b;
            if (nxt <= T && nxt < dp[k + 1]) {
                dp[k + 1] = nxt;
            }
        }
    }

    int ans = 0;
    for (int k = 0; k <= max_pos; ++k) {
        if (dp[k] > T) continue;
        long long rem_time = T - dp[k];
        // Binary search how many zero_a stores can be visited
        auto it = upper_bound(pref_zero.begin(), pref_zero.end(), rem_time);
        int cnt_zero = (it - pref_zero.begin()) - 1;
        ans = max(ans, k + cnt_zero);
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
