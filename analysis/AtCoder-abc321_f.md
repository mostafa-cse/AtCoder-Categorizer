# Problem Analysis: AtCoder-abc321_f — #(subset sum = K) with Add and Erase

**Problem ID**: `AtCoder-abc321_f`  
**Contest**: `abc321`  
**Rating / Difficulty**: 1645  
**URL**: https://atcoder.jp/contests/abc321/tasks/abc321_f  
**VJudge Tag**: `[problem:AtCoder-abc321_f]`  
**Category File**: [`../categories/dp/knapsack_addition_and_rollback.md`](../categories/dp/knapsack_addition_and_rollback.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Dynamic 0-1 Knapsack with Rollback / Subtraction Undo`  

---

## 1. Problem Statement & Key Idea
An initially empty multiset of integers. Process Q queries: 1) add integer x; 2) remove integer x. After each query, output the number of subsets with sum equal to K, modulo 998244353. K <= 5000.

**Key Insight**: Online 0-1 knapsack DP rollback! Adding element x transitions forward: dp[s] += dp[s - x]. Removing element x reverses the recurrence: dp[s] -= dp[s - x].

## 2. Core Observation & Invariant
Because 0-1 knapsack additions are linear and commutative, undoing the addition of item x is achieved by subtracting dp[s - x] from dp[s] in INCREASING order of s from x to K. Each addition and deletion takes O(K) time.

## 3. Step-by-Step Algorithm
1. Initialize dp[K + 1] = 0; dp[0] = 1.
2. For query ('+', x):
3.   For s from K down to x: dp[s] = (dp[s] + dp[s - x]) % MOD.
4.   Print dp[K].
5. For query ('-', x):
6.   For s from x to K: dp[s] = (dp[s] - dp[s - x] + MOD) % MOD.
7.   Print dp[K].

## 4. Complexity Analysis
- **Time Complexity**: `O(Q * K)`
- **Space Complexity**: `O(K)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q, k;
    if (!(cin >> q >> k)) return 0;

    vector<int> dp(k + 1, 0);
    dp[0] = 1;

    while (q--) {
        char type;
        int x;
        cin >> type >> x;

        if (type == '+') {
            for (int s = k; s >= x; --s) {
                dp[s] = (dp[s] + dp[s - x]) % MOD;
            }
        } else {
            for (int s = x; s <= k; ++s) {
                dp[s] = (dp[s] - dp[s - x] + MOD) % MOD;
            }
        }

        cout << dp[k] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Rollback and inverse transitions in 0-1 knapsack DP.
- **Reusable Pattern**: `Knapsack Add & Delete: add runs high-to-low (+), erase runs low-to-high (-).`
