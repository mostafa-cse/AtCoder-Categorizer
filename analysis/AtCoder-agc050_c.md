# Problem Analysis: AtCoder-agc050_c — C - Block Game

**Problem ID**: `AtCoder-agc050_c`  
**Contest**: `agc050`  
**Rating / Difficulty**: 2528  
**URL**: https://atcoder.jp/contests/agc050/tasks/agc050_c  
**VJudge Tag**: `[problem:AtCoder-agc050_c]`  
**Category File**: [`../categories/dynamic_programming_dp/block_game_doubling_dp.md`](../categories/dynamic_programming_dp/block_game_doubling_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `Divide and Conquer Optimization`  

---

## 1. Problem Statement & Key Idea
Count strings of 'B', 'S', and '?' such that Takahashi wins the Block Game on an infinite 1D board.

## 2. Core Observation & Invariant
Snuke can escape Takahashi's blocks iff the number of 'S' (Snuke moves) between consecutive 'B' (block placements) is large enough. Specifically, when $j$ blocks remain to be placed, Snuke requires at least $2^{j-1}$ moves to evade being trapped. Thus, Snuke wins iff between the $j$-th from last block and the next block, there are $\ge 2^{j-1}$ 'S' moves. Takahashi wins iff Snuke does NOT win. Count Snuke winning strings via DP and subtract from $2^Q$. Since $2^j > N$ for $j > 20$, the DP only needs $\le 20$ active block indices.

## 3. Step-by-Step Algorithm
1. 1. Identify the positions of '?' and 'B' in the string.
2. 2. Let $DP[j][i]$ be the number of valid suffixes where $j$ blocks have been placed, with the latest block placed at index $i$.
3. 3. Since $2^j > N$ for $j \ge 20$, $j$ runs from $0$ to $\min(B_{count}, 20)$.
4. 4. For each $j$, the condition requires at least $2^{j-1}$ 'S' moves between block $j$ and block $j+1$, which corresponds to a suffix sum range on $i$.
5. 5. Optimize transitions using prefix sums in $O(N)$ per layer, achieving $O(N \log N)$ total time.
6. 6. Subtract the count of Snuke winning configurations from $2^{\text{count}(?)} \pmod{998244353}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (!(cin >> s)) return 0;
    int n = s.length();

    long long q_total = 0;
    for (char c : s) if (c == '?') q_total++;
    long long total_ways = power(2, q_total);

    vector<int> pref_B(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        pref_B[i + 1] = pref_B[i] + (s[i] == 'B' ? 1 : 0);
    }

    auto count_B = [&](int l, int r) -> int {
        if (l > r) return 0;
        return pref_B[r + 1] - pref_B[l];
    };

    const int MAX_J = 21;
    vector<vector<int>> f(n, vector<int>(MAX_J, 0));
    for (int i = 0; i < n; ++i) {
        if (s[i] != 'S' && count_B(i + 1, n - 1) == 0) {
            f[i][0] = 1;
        }
    }

    vector<int> next_B(n + 1, n);
    int cur = n;
    for (int i = n - 1; i >= 0; --i) {
        if (s[i] == 'B') cur = i;
        next_B[i] = cur;
    }

    for (int j = 1; j < MAX_J; ++j) {
        int req = 1 << (j - 1);
        vector<int> pref_f(n + 1, 0);
        for (int k = 0; k < n; ++k) {
            pref_f[k + 1] = (pref_f[k] + f[k][j - 1]) % MOD;
        }

        for (int i = 0; i < n; ++i) {
            if (s[i] == 'S') continue;
            int low = i + 1 + req;
            int high = next_B[i + 1];
            if (high == n) high = n - 1;
            if (low <= high) {
                f[i][j] = (pref_f[high + 1] - pref_f[low] + MOD) % MOD;
            }
        }
    }

    long long snuke_wins = 0;
    if (count_B(0, n - 1) == 0) {
        snuke_wins = (snuke_wins + 1) % MOD;
    }

    int first_B_limit = next_B[0];
    if (first_B_limit == n) first_B_limit = n - 1;
    for (int i = 0; i <= first_B_limit; ++i) {
        if (s[i] != 'S') {
            for (int j = 0; j < MAX_J; ++j) {
                snuke_wins = (snuke_wins + f[i][j]) % MOD;
            }
        }
    }

    long long ans = (total_ways - snuke_wins + MOD) % MOD;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
