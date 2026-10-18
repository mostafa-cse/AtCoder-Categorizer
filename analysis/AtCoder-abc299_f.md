# Problem Analysis: AtCoder-abc299_f — F. Square Subsequence

**Problem ID**: `AtCoder-abc299_f`  
**Contest**: `abc299`  
**Rating / Difficulty**: 2349  
**URL**: https://atcoder.jp/contests/abc299/tasks/abc299_f  
**VJudge Tag**: `[problem:AtCoder-abc299_f]`  
**Category File**: [`../categories/dynamic_programming/square_subsequence_automaton_dp.md`](../categories/dynamic_programming/square_subsequence_automaton_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `Substring DP`  

---

## 1. Problem Statement & Key Idea
Count non-empty strings $T$ such that $T T$ is a subsequence of $S$. Fixing the canonical starting position of the second copy of $T$ eliminates duplicate counting, solved via subsequence automaton DP in $O(N^3 \cdot 26)$.

## 2. Core Observation & Invariant
To count each square subsequence $T T$ exactly once, fix the canonical starting index $x$ of the second copy of $T$ in $S$. The first character is $T_1 = S_x$, and the first copy must start at $p_1 = \sigma(0, T_1)$. A common subsequence automaton DP on two pointers $(i, j)$ tracking the positions of $T$ in $S[1..x-1]$ and $S[x..N]$ counts valid $T$ under the termination rule $\sigma(p_n, T_1) = x$.

## 3. Step-by-Step Algorithm
1. Precompute $\sigma(i, c)$ (the next occurrence of character $c$ after index $i$).
2. Iterate over split points $x \in [1, N]$ where the second copy begins with $S_x$.
3. If the first occurrence $p_1 = \sigma(0, S_x) \ge x$, continue.
4. Run DP: $dp[i][j]$ is the number of common subsequences matching up to $i < x$ and $j \ge x$.
5. Transitions: $dp[\sigma(i, c)][\sigma(j, c)] += dp[i][j]$ for all 26 characters $c$.
6. Add $dp[i][j]$ to answer whenever $\sigma(i, S_x) == x$, solving in $O(N^3 \cdot 26)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 \cdot 26)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string S;
    if (!(cin >> S)) return 0;

    int N = S.size();
    // 1-indexed
    S = " " + S;

    // sigma[i][c]: leftmost occurrence of c in S[i+1..N]
    vector<vector<int>> sigma(N + 2, vector<int>(26, N + 1));
    for (int c = 0; c < 26; ++c) {
        sigma[N + 1][c] = N + 1;
    }
    for (int i = N; i >= 0; --i) {
        for (int c = 0; c < 26; ++c) {
            sigma[i][c] = sigma[i + 1][c];
        }
        if (i + 1 <= N) {
            sigma[i][S[i + 1] - 'a'] = i + 1;
        }
    }

    long long total_ans = 0;

    // x is the index where the second copy of T begins
    for (int x = 1; x <= N; ++x) {
        int c0 = S[x] - 'a';
        int p1 = sigma[0][c0];
        if (p1 >= x) continue; // cannot start first T before x

        // dp[i][j]: number of prefixes of T matched up to i in first copy and j in second copy
        vector<vector<int>> dp(x + 1, vector<int>(N + 1, 0));
        dp[p1][x] = 1;

        for (int i = p1; i < x; ++i) {
            for (int j = x; j <= N; ++j) {
                if (dp[i][j] == 0) continue;
                long long cur = dp[i][j];

                for (int c = 0; c < 26; ++c) {
                    int ni = sigma[i][c];
                    int nj = sigma[j][c];
                    if (ni < x && nj <= N) {
                        dp[ni][nj] = (dp[ni][nj] + cur) % MOD;
                    }
                }
            }
        }

        // T is valid iff the first occurrence of c0 after p_n is x: sigma[i][c0] == x
        for (int i = 1; i < x; ++i) {
            if (sigma[i][c0] == x) {
                for (int j = x; j <= N; ++j) {
                    total_ans = (total_ans + dp[i][j]) % MOD;
                }
            }
        }
    }

    cout << total_ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
