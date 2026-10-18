# Problem Analysis: AtCoder-arc187_c — C. 1 Loop Bubble Sort

**Problem ID**: `AtCoder-arc187_c`  
**Contest**: `arc187`  
**Rating / Difficulty**: 2574  
**URL**: https://atcoder.jp/contests/arc187/tasks/arc187_c  
**VJudge Tag**: `[problem:AtCoder-arc187_c]`  
**Category File**: [`../categories/dynamic_programming/one_loop_bubble_sort_prefix_maxima_dp.md`](../categories/dynamic_programming/one_loop_bubble_sort_prefix_maxima_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Count permutations $P$ whose single-pass bubble sort output $P'$ matches sequence $Q$ on all non-(-1) entries.

## 2. Core Observation & Invariant
A single pass of bubble sort produces a permutation $P'$ ending with $N$ with fiber size $2^{k-1}$, where $k$ is the number of prefix maxima of $P'$. Placing elements from left to right, each new prefix maximum multiplies the weight by 2. The number of available free elements $\le j$ depends only on $j$ and the number of elements placed so far.

## 3. Step-by-Step Algorithm
1. 1. If $Q_N \ne -1$ and $Q_N \ne N$, or $N$ appears in $Q_1 \dots Q_{N-1}$, return 0.
2. 2. Define $dp[j]$: total weight where the current prefix maximum is $j$.
3. 3. Initialize $dp$ for position 0.
4. 4. For positions $i = 1 \dots N-2$: if $Q_i \ne -1$, transition $j' = \max(j, Q_i)$; if $Q_i = -1$, transition same max via available count $(j - F[j] - free\_placed)$ and new max via prefix sums of $dp$.
5. 5. Multiply final sum by 2 for the terminal element $N$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<int> Q(N);
    for (int i = 0; i < N; ++i) cin >> Q[i];

    if (Q[N - 1] != -1 && Q[N - 1] != N) {
        cout << 0 << "\n";
        return 0;
    }
    for (int i = 0; i < N - 1; ++i) {
        if (Q[i] == N) {
            cout << 0 << "\n";
            return 0;
        }
    }

    vector<bool> is_fixed(N + 1, false);
    for (int x : Q) {
        if (x != -1) is_fixed[x] = true;
    }

    vector<int> F(N + 1, 0);
    for (int j = 1; j <= N; ++j) {
        F[j] = F[j - 1] + (is_fixed[j] ? 1 : 0);
    }

    vector<long long> dp(N + 1, 0);
    int q0 = Q[0];
    if (q0 != -1) {
        dp[q0] = 1;
    } else {
        for (int v = 1; v < N; ++v) {
            if (!is_fixed[v]) {
                dp[v] = 1;
            }
        }
    }

    int free_placed = (Q[0] == -1 ? 1 : 0);

    for (int i = 1; i < N - 1; ++i) {
        vector<long long> next_dp(N + 1, 0);
        int qi = Q[i];

        vector<long long> pref(N + 1, 0);
        for (int j = 1; j <= N; ++j) {
            pref[j] = (pref[j - 1] + dp[j]) % MOD;
        }

        if (qi != -1) {
            for (int j = 1; j <= N; ++j) {
                if (!dp[j]) continue;
                if (qi > j) {
                    next_dp[qi] = (next_dp[qi] + dp[j] * 2) % MOD;
                } else if (qi < j) {
                    next_dp[j] = (next_dp[j] + dp[j]) % MOD;
                }
            }
        } else {
            for (int j = 1; j <= N; ++j) {
                if (!dp[j]) continue;
                int avail = (j - F[j]) - free_placed;
                if (avail > 0) {
                    next_dp[j] = (next_dp[j] + dp[j] * avail) % MOD;
                }
            }
            for (int v = 1; v < N; ++v) {
                if (!is_fixed[v]) {
                    long long sum_less = pref[v - 1];
                    next_dp[v] = (next_dp[v] + sum_less * 2) % MOD;
                }
            }
            free_placed++;
        }
        dp = move(next_dp);
    }

    long long sum_dp = 0;
    for (int j = 1; j <= N; ++j) {
        sum_dp = (sum_dp + dp[j]) % MOD;
    }
    long long ans = (sum_dp * 2) % MOD;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
