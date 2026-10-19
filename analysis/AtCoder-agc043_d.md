# Problem Analysis: AtCoder-agc043_d — Merge Triplets

**Problem ID**: `AtCoder-agc043_d`  
**Contest**: `agc043`  
**Rating / Difficulty**: 2708  
**URL**: https://atcoder.jp/contests/agc043/tasks/agc043_d  
**VJudge Tag**: `[problem:AtCoder-agc043_d]`  
**Category File**: [`../categories/dynamic_programming_dp/merge_triplets_prefix_max_dp.md`](../categories/dynamic_programming_dp/merge_triplets_prefix_max_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
A permutation P of length 3N can be formed by merging N sorted triplets iff its prefix-maximum blocks have sizes in {1, 2, 3} and the count of size-1 blocks c_1 >= count of size-2 blocks c_2. Counting such permutations is solved via DP on prefix length s and difference d = c_1 - c_2 with transitions for adding blocks of size 1, 2, 3.

## 2. Core Observation & Invariant
When adding a block of size a in {1, 2, 3} to a prefix of length s, the maximum among the s + a elements must be the first element of the new block, and there are (s + a - 1)! / s! = prod_{j=1}^{a-1} (s + j) ways to choose and arrange the remaining elements. Thus transition weights are 1 (for a=1), s+1 (for a=2), and (s+1)(s+2) (for a=3).

## 3. Step-by-Step Algorithm
1. 1. Let dp[s % 4][d] be the DP table with rolling buffer of size 4 for s = 0..3N and d = -3N..3N (offset by 3N).
2. 2. Base case: dp[0][3N] = 1.
3. 3. For s = 0 to 3N - 1:
4.    - From state (s, d): transition to (s+1, d+1) with weight 1, to (s+2, d-1) with weight s+1, to (s+3, d) with weight (s+1)(s+2).
5.    - Clear row s % 4.
6. 4. Sum dp[3N % 4][d] for all d >= 3N modulo M.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    int total = 3 * n;
    int offset = total;
    int d_size = 2 * total + 1;

    // dp[s][d]
    // Since s transitions to s+1, s+2, s+3, we can use a table or rolling buffer
    // Given n <= 2000, total = 6000, 6001 * 12001 ints is ~288 MB.
    // To be very memory-efficient, use a full 2D table or rolling array of size 4.
    // Wait, if we use rolling array of size 4, at s = total, we just sum dp[total % 4][d >= offset]!
    vector<vector<int>> dp(4, vector<int>(d_size, 0));
    dp[0][offset] = 1;

    for (int s = 0; s < total; ++s) {
        int cur = s % 4;
        long long factor2 = (s + 1) % m;
        long long factor3 = (1LL * (s + 1) * (s + 2)) % m;

        int to1 = (s + 1) % 4;
        int to2 = (s + 2) % 4;
        int to3 = (s + 3) % 4;

        for (int d = 0; d < d_size; ++d) {
            int val = dp[cur][d];
            if (!val) continue;

            // a = 1
            if (s + 1 <= total && d + 1 < d_size) {
                int& target = dp[to1][d + 1];
                target += val;
                if (target >= m) target -= m;
            }
            // a = 2
            if (s + 2 <= total && d - 1 >= 0) {
                int& target = dp[to2][d - 1];
                target = (target + 1LL * val * factor2) % m;
            }
            // a = 3
            if (s + 3 <= total) {
                int& target = dp[to3][d];
                target = (target + 1LL * val * factor3) % m;
            }
        }
        // Clear current row for future reuse
        fill(dp[cur].begin(), dp[cur].end(), 0);
    }

    int target_row = total % 4;
    long long ans = 0;
    for (int d = offset; d < d_size; ++d) {
        ans = (ans + dp[target_row][d]) % m;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
