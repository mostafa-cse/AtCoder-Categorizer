# Problem Analysis: AtCoder-arc214_c — Divide into 4 Teams

**Problem ID**: `AtCoder-arc214_c`  
**Contest**: `arc214`  
**Rating / Difficulty**: 2070  
**URL**: https://atcoder.jp/contests/arc214/tasks/arc214_c  
**VJudge Tag**: `[problem:AtCoder-arc214_c]`  
**Category File**: [`../categories/dynamic_programming/basis_decoupling_subset_sum_dp.md`](../categories/dynamic_programming/basis_decoupling_subset_sum_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Basis Decoupling Sign DP and Subset Sum Reduction`  

---

## 1. Problem Statement & Key Idea
N people with strengths P_i are partitioned into 4 non-empty teams A, B, C, D such that sum(P_A) = sum(P_B) and sum(P_C) = sum(P_D). Count the number of valid formations modulo 998244353.

**Key Idea**: Represent team assignment as independent sign pairs (u_i, v_i) in {+1, -1}^2: A = (+1, +1), B = (-1, -1), C = (+1, -1), D = (-1, +1). The conditions sum(P_A) = sum(P_B) and sum(P_C) = sum(P_D) decouple into two independent equations: sum u_i P_i = 0 and sum v_i P_i = 0. Each choice of signs summing to 0 is equivalent to choosing a subset summing to Total/2. If C is the number of such subsets, there are C^2 total sign assignments. A team can be empty iff an entire pair {A, B} or {C, D} is empty (since P_i >= 1 and sum(A) = sum(B)), which contributes 2C invalid assignments. Thus the answer is exactly C(C - 2) modulo 998244353.

## 2. Core Observation & Invariant
A linear change of basis decouples 4-team balance into two independent 2-team subset sum problems, yielding C^2 - 2C = C(C - 2).

## 3. Step-by-Step Algorithm
1. Compute Total = sum(P_i). If Total is odd, output 0.
2. Run 0-1 knapsack DP to count C = number of subsets with sum Total/2 modulo 998244353.
3. Output C * (C - 2) modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * sum(P))`
- **Space Complexity**: `O(sum(P))`

## 5. Core Algorithmic Skill & Learning Takeaway
Decoupling coupled team constraints using orthogonal sign vectors in a 2D basis.

**Reusable Pattern**: Balanced 4-team partitioning decomposes into independent 2-team subset sums via sign basis transformation.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n);
    int total = 0;
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
        total += p[i];
    }

    if (total % 2 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    int target = total / 2;
    vector<long long> dp(target + 1, 0);
    dp[0] = 1;

    for (int x : p) {
        for (int w = target; w >= x; --w) {
            dp[w] = (dp[w] + dp[w - x]) % MOD;
        }
    }

    long long C = dp[target];
    long long ans = (C * (C - 2 + MOD)) % MOD;
    cout << ans << "\n";
    return 0;
}
```
