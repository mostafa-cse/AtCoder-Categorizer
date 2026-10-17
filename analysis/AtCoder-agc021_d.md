# Problem Analysis: AtCoder-agc021_d — D. Crossing

**Problem ID**: `AtCoder-agc021_d`  
**Contest**: `agc021`  
**Rating / Difficulty**: 2287  
**URL**: https://atcoder.jp/contests/agc021/tasks/agc021_d  
**VJudge Tag**: `[problem:AtCoder-agc021_d]`  
**Category File**: [`../categories/dynamic_programming/interval_dp_longest_palindromic_subsequence_edits.md`](../categories/dynamic_programming/interval_dp_longest_palindromic_subsequence_edits.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Given a string $S$ of length up to 300 and at most $K$ character modifications, find the maximum possible length of the longest palindromic subsequence of the modified string.

## 2. Core Observation & Invariant
For any substring $S[i..j]$ and budget of $t$ modifications, the length of the longest palindromic subsequence satisfies the Bellman equation: matching $S[i]$ and $S[j]$ costs $0$ modifications if $S[i] = S[j]$ and $1$ modification if $S[i] \ne S[j]$, yielding $2 + dp(i+1, j-1, t - \mathrm{cost})$.

## 3. Step-by-Step Algorithm
1. 1. Let $dp(i, j, t)$ denote the length of the longest palindromic subsequence that can be achieved from $S[i..j]$ using at most $t$ character replacements.
2. 2. Base cases:
3.    - Length 0: $dp(i, i - 1, t) = 0$.
4.    - Length 1: $dp(i, i, t) = 1$.
5. 3. Transitions for interval $S[i..j]$:
6.    - Do not match ends together: $\max(dp(i + 1, j, t), dp(i, j - 1, t))$.
7.    - Match $S[i]$ and $S[j]$:
8.      - If $S[i] = S[j]$: $2 + dp(i + 1, j - 1, t)$.
9.      - If $S[i] \ne S[j]$ and $t > 0$: $2 + dp(i + 1, j - 1, t - 1)$ (replace one of them to match the other).
10. 4. Evaluate intervals in increasing order of length from $2$ to $N$, for all $0 \le t \le K$. Overall complexity is $O(N^2 K)$, where $N \le 300, K \le N$, well within 2 seconds.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 K)`
- **Space Complexity**: `O(N^2 K)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

static short dp[305][305][305];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string S;
    int K;
    if (!(cin >> S >> K)) return 0;

    int N = S.length();
    K = min(K, N);

    for (int i = 0; i < N; ++i) {
        for (int t = 0; t <= K; ++t) {
            dp[i][i][t] = 1;
        }
    }

    for (int len = 2; len <= N; ++len) {
        for (int i = 0; i <= N - len; ++i) {
            int j = i + len - 1;
            for (int t = 0; t <= K; ++t) {
                short res = max(dp[i + 1][j][t], dp[i][j - 1][t]);
                if (S[i] == S[j]) {
                    short match = 2 + (i + 1 <= j - 1 ? dp[i + 1][j - 1][t] : 0);
                    res = max(res, match);
                } else {
                    if (t > 0) {
                        short match = 2 + (i + 1 <= j - 1 ? dp[i + 1][j - 1][t - 1] : 0);
                        res = max(res, match);
                    }
                }
                dp[i][j][t] = res;
            }
        }
    }

    cout << dp[0][N - 1][K] << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
