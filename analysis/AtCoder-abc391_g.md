# Problem Analysis: AtCoder-abc391_g — Many LCS

**Problem ID**: `AtCoder-abc391_g`  
**Contest**: `abc391`  
**Rating / Difficulty**: 2247  
**URL**: https://atcoder.jp/contests/abc391/tasks/abc391_g  
**VJudge Tag**: `[problem:AtCoder-abc391_g]`  
**Category File**: [`../categories/strings/bit_lcs_automaton_dp_of_dp.md`](../categories/strings/bit_lcs_automaton_dp_of_dp.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Longest Common Subsequence (LCS)`  
- **Topic (Skill)**: `Bit LCS`  

---

## 1. Problem Statement & Key Idea
Count the number of lowercase strings of length M whose longest common subsequence with a given string S of length N <= 10 has length exactly k, for all 0 <= k <= N.

## 2. Core Observation & Invariant
In the standard dynamic programming table for LCS between S and a prefix of T, adjacent DP entries satisfy 0 <= dp[i] - dp[i-1] <= 1. Thus, the DP state against S is fully encoded by the binary difference vector Delta in {0, 1}^N (a bitmask of 2^N states). Precomputing the deterministic automaton transition next_mask = trans[mask][c] for all 2^N masks and 26 characters turns the problem into counting paths of length M in the LCS DFA.

## 3. Step-by-Step Algorithm
1. 1. Precompute transition function trans[mask][c] for all masks in [0, 2^N - 1] and characters c in ['a', 'z'] by reconstructing dp[0..N] and calculating next_dp[0..N].
2. 2. Initialize DP table: ways[0] = 1, all others 0.
3. 3. For each step 1 to M: update next_ways[trans[mask][c]] += ways[mask] mod 998244353.
4. 4. For each mask, the final LCS value is popcount(mask). Accumulate ways[mask] into ans[popcount(mask)].
5. 5. Output ans[0..N].

## 4. Complexity Analysis
- **Time Complexity**: `O(2^N * 26 * N + M * 2^N * 26)`
- **Space Complexity**: `O(2^N * 26)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    string S;
    cin >> S;

    int num_states = 1 << N;
    // precompute transitions: trans[mask][c]
    vector<vector<int>> trans(num_states, vector<int>(26, 0));

    vector<int> dp(N + 1, 0), next_dp(N + 1, 0);

    for (int mask = 0; mask < num_states; ++mask) {
        dp[0] = 0;
        for (int i = 0; i < N; ++i) {
            dp[i + 1] = dp[i] + ((mask >> i) & 1);
        }

        for (int c = 0; c < 26; ++c) {
            char ch = 'a' + c;
            next_dp[0] = 0;
            for (int i = 1; i <= N; ++i) {
                if (S[i - 1] == ch) {
                    next_dp[i] = dp[i - 1] + 1;
                } else {
                    next_dp[i] = max(next_dp[i - 1], dp[i]);
                }
            }
            int next_mask = 0;
            for (int i = 0; i < N; ++i) {
                if (next_dp[i + 1] - next_dp[i] == 1) {
                    next_mask |= (1 << i);
                }
            }
            trans[mask][c] = next_mask;
        }
    }

    // DP: ways[mask]
    vector<int> ways(num_states, 0);
    ways[0] = 1; // start with empty string, diffs are all 0

    for (int step = 0; step < M; ++step) {
        vector<int> next_ways(num_states, 0);
        for (int mask = 0; mask < num_states; ++mask) {
            if (!ways[mask]) continue;
            long long cur = ways[mask];
            for (int c = 0; c < 26; ++c) {
                int nxt = trans[mask][c];
                next_ways[nxt] = (next_ways[nxt] + cur);
                if (next_ways[nxt] >= MOD) next_ways[nxt] -= MOD;
            }
        }
        ways = move(next_ways);
    }

    vector<int> ans(N + 1, 0);
    for (int mask = 0; mask < num_states; ++mask) {
        int k = __builtin_popcount(mask);
        ans[k] = (ans[k] + ways[mask]) % MOD;
    }

    for (int k = 0; k <= N; ++k) {
        cout << ans[k] << (k == N ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
