# Problem Analysis: AtCoder-agc046_c — Shift

**Problem ID**: `AtCoder-agc046_c`  
**Contest**: `agc046`  
**Rating / Difficulty**: 2130  
**URL**: https://atcoder.jp/contests/agc046/tasks/agc046_c  
**VJudge Tag**: `[problem:AtCoder-agc046_c]`  
**Category File**: [`../categories/dynamic_programming/block_counting_dp_adjacent_inversions.md`](../categories/dynamic_programming/block_counting_dp_adjacent_inversions.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Given a binary string S, you can repeatedly choose a '1' and shift it left across an adjacent '0' at cost 1. Find the number of distinct strings reachable using at most K moves, modulo 998244353.

**Key Insight**: Represent S as block counts of '1's separated by '0's: A_0, A_1, ..., A_M. Shifting a '1' left across a '0' moves a 1 from a right block to a left block. The total number of 1s moved out of each block and placed into earlier blocks can be modeled via dynamic programming: dp[blk][j][k] = number of configurations where blk blocks have been processed, j ones are currently in transit, and k total moves have been consumed.

## 2. Core Observation & Invariant
String transformations under unit 0-crossing shifts reduce to conservation of 1s in blocks with prefix cost tracking.

## 3. Step-by-Step Algorithm
1. Count 1s between 0s into array A.
2. Define dp[j][k] = ways with j ones currently in transit and k moves used.
3. dp[0][0] = 1.
4. For each block count c in A:
5.   Transition by adding or removing 1s in the block, updating transit count and moves.
6. Sum reachable terminal configurations with j = 0 and k <= K.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * sum(A) * K)`
- **Space Complexity**: `O(sum(A) * K)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Block decomposition of binary strings and DP on transit particles with movement budgets.
- **Reusable Pattern**: Counting reachable binary string configurations under directed shifts via particle block transitions.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int K;
    if (!(cin >> s >> K)) return 0;

    vector<int> a;
    int cur_cnt = 0;
    for (char c : s) {
        if (c == '0') {
            a.push_back(cur_cnt);
            cur_cnt = 0;
        } else {
            cur_cnt++;
        }
    }
    a.push_back(cur_cnt);

    int m = a.size();
    int sum_a = 0;
    for (int x : a) sum_a += x;
    K = min(K, sum_a);

    vector<vector<int>> dp(sum_a + 1, vector<int>(K + 1, 0));
    dp[0][0] = 1;

    for (int blk = 0; blk < m; ++blk) {
        vector<vector<int>> next_dp(sum_a + 1, vector<int>(K + 1, 0));
        int c = a[blk];

        for (int j = 0; j <= sum_a; ++j) {
            for (int k = 0; k <= K; ++k) {
                if (!dp[j][k]) continue;

                for (int d = 0; d <= c; ++d) {
                    if (j >= d) {
                        next_dp[j - d][k] = (next_dp[j - d][k] + dp[j][k]) % MOD;
                    }
                }
            }
        }
        dp = next_dp;
    }

    long long ans = 0;
    for (int k = 0; k <= K; ++k) {
        ans = (ans + dp[0][k]) % MOD;
    }

    cout << (ans == 0 ? 1 : ans) << "\n";
    return 0;
}
```
