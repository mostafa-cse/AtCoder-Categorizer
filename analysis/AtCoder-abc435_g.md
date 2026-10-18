# Problem Analysis: AtCoder-abc435_g — G - Domino Arrangement

**Problem ID**: `AtCoder-abc435_g`  
**Contest**: `abc435`  
**Rating / Difficulty**: 2519  
**URL**: https://atcoder.jp/contests/abc435/tasks/abc435_g  
**VJudge Tag**: `[problem:AtCoder-abc435_g]`  
**Category File**: [`../categories/dynamic_programming_dp/domino_arrangement_interval_active_set_dp.md`](../categories/dynamic_programming_dp/domino_arrangement_interval_active_set_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `More Tricks`  
- **Topic (Skill)**: `Open and Close Interval Trick`  

---

## 1. Problem Statement & Key Idea
Count the number of valid cell colorings where every colored cell is part of an identical 2-cell domino of color $c \in [1, M]$, given color availability intervals $[L_c, R_c]$.

## 2. Core Observation & Invariant
Let $C_k$ be the colors available for both cells $k-1$ and $k$. DP recurrence states: $S_k = S_{k-1} + |C_k| S_{k-2} - \sum_{c \in C_k} \mathrm{dp}[k-2][c]$. Because $k$ only interacts with $k-2$, even and odd $k$ form two completely separate parity systems. In each system, advancing $k \to k+2$ applies a global affine transformation $T_{new} = S_{k-4} - T_{old}$ to active colors, which is maintained in $O(1)$ time with global slope/intercept tags while inserting/removing colors at their interval endpoints ($2M$ events total).

## 3. Step-by-Step Algorithm
1. 1. For each color $c$, interval $[L_c + 1, R_c]$ defines its active set $C_k$. Record entering events at the first $k \ge L_c + 1$ and exiting events at the last $k \le R_c$ for each parity.
2. 2. Maintain two `ParityState` objects (even and odd) with global affine tags $a, b$, active size, sum, and raw color values.
3. 3. For $k = 1, \dots, N$:
4.    - Select parity $p = k \bmod 2$.
5.    - Apply global affine tag $T \gets S_{k-4} - T$.
6.    - Remove colors that exited at $k-2$.
7.    - Insert colors that enter at $k$ with initial value 0.
8.    - Transition $S_k = S_{k-1} + |C_k| S_{k-2} - \sum T_k \pmod{998244353}$.
9. 4. Output $S_N$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

struct ParityState {
    long long a = 1;
    long long b = 0;
    long long size = 0;
    long long sum = 0;
    vector<long long> raw;
    vector<bool> active;

    ParityState(int M) : raw(M, 0), active(M, false) {}

    void apply_affine(long long S_prev) {
        sum = (size * S_prev % MOD - sum + MOD) % MOD;
        a = (MOD - a) % MOD;
        b = (S_prev - b + MOD) % MOD;
    }

    void add_color(int c) {
        raw[c] = (MOD - b) * a % MOD;
        raw[c] = (raw[c] + MOD) % MOD;
        active[c] = true;
        size++;
    }

    void remove_color(int c) {
        if (active[c]) {
            long long val = (a * raw[c] + b) % MOD;
            val = (val + MOD) % MOD;
            sum = (sum - val + MOD) % MOD;
            size--;
            active[c] = false;
        }
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<vector<vector<int>>> enters(2, vector<vector<int>>(N + 4));
    vector<vector<vector<int>>> exits(2, vector<vector<int>>(N + 4));

    for (int c = 0; c < M; ++c) {
        int l, r;
        cin >> l >> r;
        int start = l + 1;
        int end = r;
        if (start <= end) {
            for (int p = 0; p < 2; ++p) {
                int first_k = (start % 2 == p ? start : start + 1);
                int last_k = (end % 2 == p ? end : end - 1);
                if (first_k <= last_k) {
                    enters[p][first_k].push_back(c);
                    exits[p][last_k].push_back(c);
                }
            }
        }
    }

    vector<ParityState> states = {ParityState(M), ParityState(M)};
    vector<long long> S(N + 1, 0);
    S[0] = 1;

    for (int k = 1; k <= N; ++k) {
        int p = k % 2;
        long long S_prev = (k - 4 >= 0 ? S[k - 4] : 0);
        states[p].apply_affine(S_prev);

        if (k >= 2) {
            for (int c : exits[p][k - 2]) {
                states[p].remove_color(c);
            }
        }
        for (int c : enters[p][k]) {
            states[p].add_color(c);
        }

        long long term = (states[p].size * S[k - 2] % MOD - states[p].sum + MOD) % MOD;
        S[k] = (S[k - 1] + term) % MOD;
    }

    cout << S[N] << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
