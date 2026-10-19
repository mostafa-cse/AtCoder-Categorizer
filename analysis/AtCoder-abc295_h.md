# Problem Analysis: AtCoder-abc295_h — Ex - E or m

**Problem ID**: `AtCoder-abc295_h`  
**Contest**: `abc295`  
**Rating / Difficulty**: 2728  
**URL**: https://atcoder.jp/contests/abc295/tasks/abc295_h  
**VJudge Tag**: `[problem:AtCoder-abc295_h]`  
**Category File**: [`../categories/dynamic_programming_dp/e_or_m_sos_dp.md`](../categories/dynamic_programming_dp/e_or_m_sos_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
Given an N x M grid X with characters in {'0', '1', '?'}, where N, M <= 18. Count how many completions of '?' can be obtained by taking a grid of all 0s, painting a prefix of 1s in each row, and painting a prefix of 1s in each column, modulo 998244353.

## 2. Core Observation & Invariant
Each column can extend 1s from the top down. A grid profile after processing rows 1..i is represented by a bitmask of length M, where the j-th bit is 1 iff column j can still extend 1s downwards. For row i, we transition by choosing a prefix of row 1s up to some column j, which sets a prefix of row i to 1 and places a subset of the column continuation mask for the remaining columns. This subset transition can be performed across all masks using Sum Over Subsets (SOS) / fast zeta transform in O(2^M * M) per row, incorporating the grid constraints ('0'/'1') on what can be placed.

## 3. Step-by-Step Algorithm
1. 1. Ensure M <= N by transposing the grid if M > N, so that M <= 18.
2. 2. Initialize DP table dp with dp[(1 << M) - 1] = 1 and all other states 0.
3. 3. For each row i from 0 to N - 1:
4.    a. Let ndp = dp.
5.    b. For column j from 0 to M - 1, apply SOS DP transitions based on whether cell (i, j) permits '0' or '1'.
6.    c. If prefix of row i up to column j contains no '0', add the contribution of row prefix continuation.
7.    d. Update dp = ndp.
8. 4. Return the sum of all dp states modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M * 2^M)`
- **Space Complexity**: `O(2^M)`

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

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<string> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }

    // Ensure m <= n so 1 << m <= 2^18
    if (m > n) {
        vector<string> trans(m, string(n, ' '));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                trans[j][i] = s[i][j];
            }
        }
        s = trans;
        swap(n, m);
    }

    vector<long long> dp(1 << m, 0);
    dp[(1 << m) - 1] = 1;

    for (int i = 0; i < n; ++i) {
        vector<long long> ndp = dp;
        for (int j = 0; j < m; ++j) {
            vector<long long> work(1 << m, 0);
            if (s[i][j] != '1') {
                // Put 0
                for (int k = 0; k < (1 << m); ++k) {
                    if (k & (1 << j)) {
                        work[k ^ (1 << j)] = (work[k ^ (1 << j)] + ndp[k]) % MOD;
                    } else {
                        work[k] = (work[k] + ndp[k]) % MOD;
                    }
                }
            }
            if (s[i][j] != '0') {
                // Put 1
                for (int k = 0; k < (1 << m); ++k) {
                    if (k & (1 << j)) {
                        work[k] = (work[k] + ndp[k]) % MOD;
                    }
                }
            }
            ndp = move(work);

            bool ok = true;
            for (int k = 0; k <= j; ++k) {
                if (s[i][k] == '0') {
                    ok = false;
                    break;
                }
            }
            if (!ok) continue;

            for (int k = 0; k < (1 << m); ++k) {
                if (!(k & (1 << j))) {
                    ndp[k] = (ndp[k] + dp[k]) % MOD;
                }
            }
        }
        dp = move(ndp);
    }

    long long res = 0;
    for (long long x : dp) {
        res = (res + x) % MOD;
    }

    cout << res << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
