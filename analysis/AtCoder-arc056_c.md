# Problem Analysis: AtCoder-arc056_c — C. 部門分け

**Problem ID**: `AtCoder-arc056_c`  
**Contest**: `arc056`  
**Rating / Difficulty**: 2179  
**URL**: https://atcoder.jp/contests/arc056/tasks/arc056_c  
**VJudge Tag**: `[problem:AtCoder-arc056_c]`  
**Category File**: [`../categories/dynamic_programming/submask_dp_lowest_bit_department_partition.md`](../categories/dynamic_programming/submask_dp_lowest_bit_department_partition.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
Partition N <= 17 employees into non-empty departments to maximize (m * K) minus the sum of mutual trust w_{i, j} between employees in different departments. Fixing the lowest bit of the remaining vertex subset to belong to the peeled department avoids permutation overcounting.

## 2. Core Observation & Invariant
Let E(mask) be the sum of mutual trust weights between all pairs of employees with both endpoints in mask. For any partition of mask into S and mask \ S, the cut cost is E(mask) - E(S) - E(mask \ S). Submask DP evaluates dp[mask] = max_{S subset mask, lowbit(mask) in S} (dp[mask \ S] + K - (E(mask) - E(S) - E(mask \ S))) in O(3^{N-1}) time.

## 3. Step-by-Step Algorithm
1. Precompute E[mask] for all 2^N masks in O(N * 2^N) time using bitwise recurrence: E[mask] = E[mask \ {v}] + sum_{u in mask \ {v}} w[v][u].
2. Initialize dp[mask] = -INF for all masks, with dp[0] = 0.
3. Iterate mask from 1 to 2^N - 1. Find lowbit = mask & -mask, and let rest = mask ^ lowbit.
4. Enumerate all submasks sub of rest. Let S = lowbit | sub and rem = mask ^ S. Update dp[mask] = max(dp[mask], dp[rem] + K - (E[mask] - E[S] - E[rem])).
5. Output dp[(1 << N) - 1].

## 4. Complexity Analysis
- **Time Complexity**: `O(3^N)`
- **Space Complexity**: `O(2^N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    long long K;
    if (!(cin >> N >> K)) return 0;

    vector<vector<long long>> w(N, vector<long long>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> w[i][j];
        }
    }

    int total_masks = 1 << N;
    vector<long long> E(total_masks, 0);

    for (int mask = 1; mask < total_masks; ++mask) {
        int v = __builtin_ctz(mask);
        int sub = mask ^ (1 << v);
        long long cross_v = 0;
        for (int u = 0; u < N; ++u) {
            if ((sub >> u) & 1) cross_v += w[v][u];
        }
        E[mask] = E[sub] + cross_v;
    }

    vector<long long> dp(total_masks, 0);

    for (int mask = 1; mask < total_masks; ++mask) {
        int lowbit = mask & -mask;
        int rest = mask ^ lowbit;
        long long best = -1e18;

        // S must contain lowbit, so S = lowbit | sub, where sub is any submask of rest
        for (int sub = rest; ; sub = (sub - 1) & rest) {
            int S = lowbit | sub;
            int rem = mask ^ S;
            long long cost = E[mask] - E[S] - E[rem];
            long long val = dp[rem] + K - cost;
            if (val > best) best = val;
            if (sub == 0) break;
        }
        dp[mask] = best;
    }

    cout << dp[total_masks - 1] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
