# Problem Analysis: AtCoder-abc267_g — G - Increasing K Times

**Problem ID**: `AtCoder-abc267_g`  
**Contest**: `abc267`  
**Rating / Difficulty**: 2561  
**URL**: https://atcoder.jp/contests/abc267/tasks/abc267_g  
**VJudge Tag**: `[problem:AtCoder-abc267_g]`  
**Category File**: [`../categories/combinatorics/increasing_k_times_eulerian_multiset_dp.md`](../categories/combinatorics/increasing_k_times_eulerian_multiset_dp.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Product Trick`  

---

## 1. Problem Statement & Key Idea
Count permutations of a multiset $A$ having exactly $K$ positions where $P_i < P_{i+1}$.

## 2. Core Observation & Invariant
When numbers are sorted and inserted in non-decreasing order, each group of identical elements $x$ with frequency $cnt$ can be placed into existing spaces. If an element is inserted into an existing 'ascent' slot, the number of ascents does not increase. If inserted into a non-ascent slot, it creates a new ascent. This generalizes Eulerian numbers to multisets via polynomial DP.

## 3. Step-by-Step Algorithm
1. 1. Sort array $A$ and group identical elements with their frequencies $c_1, c_2, \dots, c_m$.
2. 2. Maintain $DP[j]$: number of permutations of processed elements with $j$ ascents.
3. 3. For each group with frequency $c$, insert $c$ identical elements into $j$ ascents and non-ascent positions using binomial coefficient convolution.
4. 4. Output $DP[K]$ modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \cdot K)`
- **Space Complexity**: `O(K)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    if (!(cin >> N >> K)) return 0;

    vector<int> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    sort(A.begin(), A.end());

    vector<long long> dp(N + 2, 0);
    dp[1] = 1;

    for (int i = 1; i < N; ++i) {
        int c = 0;
        int j = i - 1;
        while (j >= 0 && A[j] == A[i]) {
            c++;
            j--;
        }

        int n = i;
        vector<long long> next_dp(N + 2, 0);
        for (int m = 1; m <= n + 1; ++m) {
            if (dp[m] == 0) continue;
            long long stay_slots = m + c;
            long long inc_slots = (n + 1) - m - c;

            if (stay_slots > 0) {
                next_dp[m] = (next_dp[m] + dp[m] * stay_slots) % MOD;
            }
            if (inc_slots > 0) {
                next_dp[m + 1] = (next_dp[m + 1] + dp[m] * inc_slots) % MOD;
            }
        }
        dp = move(next_dp);
    }

    cout << dp[K + 1] << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
