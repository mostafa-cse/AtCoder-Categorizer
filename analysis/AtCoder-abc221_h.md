# Problem Analysis: AtCoder-abc221_h — H - Count Multiset

**Problem ID**: `AtCoder-abc221_h`  
**Contest**: `abc221`  
**Rating / Difficulty**: 2793  
**URL**: https://atcoder.jp/contests/abc221/tasks/abc221_h  
**VJudge Tag**: `[problem:AtCoder-abc221_h]`  
**Category File**: [`../categories/combinatorics/count_multisets_integer_partition_dp.md`](../categories/combinatorics/count_multisets_integer_partition_dp.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Partitions`  
- **Topic (Skill)**: `Partitions of an Integer, Partition Function and Pentagonal Number Theorem`  

---

## 1. Problem Statement & Key Idea
Find the number of multisets of positive integers with sum N such that each element has multiplicity at most M, for each multiset size k from 1 to N. Output the count for each k modulo 998244353.

## 2. Core Observation & Invariant
A partition of n into k parts corresponds to a Young diagram. In the conjugate partition, parts are bounded and adjacent differences are bounded. Alternatively, we can use the standard partition DP where dp[k][n] is the number of partitions of n into k parts with multiplicity <= M. Transitions:
1. Increment all k parts by 1: dp[k][n - k]
2. Add a new part of size 1: dp[k - 1][n - 1]
3. Subtract invalid configurations where the part 1 was repeated > M times: dp[k - 1 - M][n - k].
This yields a 3-term recurrence computable in O(N^2) time.

## 3. Step-by-Step Algorithm
1. 1. Initialize dp[0][0] = 1, all other entries 0.
2. 2. For n from 1 to N:
3.    For k from 1 to n:
4.      dp[k][n] = (dp[k][n - k] + dp[k - 1][n - 1] - dp[k - 1 - M][n - k]) mod MOD.
5. 3. Print dp[k][N] for each k = 1 to N.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;

// Allocate globally to avoid stack overflow and heap allocation overhead
static int dp[5005][5005];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    dp[0][0] = 1;

    for (int n = 1; n <= N; ++n) {
        for (int k = 1; k <= n; ++k) {
            long long val = 0;
            // term 1: dp[k][n - k]
            if (n - k >= 0) {
                val += dp[k][n - k];
            }
            // term 2: dp[k - 1][n - 1]
            if (n - 1 >= 0 && k - 1 >= 0) {
                val += dp[k - 1][n - 1];
            }
            // term 3: - dp[k - 1 - M][n - k]
            if (k - 1 - M >= 0 && n - k >= 0) {
                val -= dp[k - 1 - M][n - k];
            }
            val %= MOD;
            if (val < 0) val += MOD;
            dp[k][n] = val;
        }
    }

    for (int k = 1; k <= N; ++k) {
        cout << dp[k][N] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
