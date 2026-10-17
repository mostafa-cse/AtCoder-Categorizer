# Problem Analysis: AtCoder-abc209_f — F. Deforestation

**Problem ID**: `AtCoder-abc209_f`  
**Contest**: `abc209`  
**Rating / Difficulty**: 2307  
**URL**: https://atcoder.jp/contests/abc209/tasks/abc209_f  
**VJudge Tag**: `[problem:AtCoder-abc209_f]`  
**Category File**: [`../categories/dynamic_programming/permutation_relative_rank_insertion_dp.md`](../categories/dynamic_programming/permutation_relative_rank_insertion_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
In a line of $N$ trees with heights $H_i$, cutting tree $P_i$ costs $H_{P_i-1} + H_{P_i} + H_{P_i+1}$. Count permutations minimizing the total cost, modulo $10^9+7$.

## 2. Core Observation & Invariant
For adjacent trees $(i, i+1)$, cutting $i$ before $i+1$ pays $H_{i+1}$, whereas cutting $i+1$ before $i$ pays $H_i$. Minimizing total cost imposes strict relative order constraints on adjacent cutting positions.

## 3. Step-by-Step Algorithm
1. Deduce that $H_i < H_{i+1}$ requires $pos[i] > pos[i+1]$, and $H_i > H_{i+1}$ requires $pos[i] < pos[i+1]$.
2. Use permutation insertion DP where $dp[j]$ tracks the number of permutations of prefix trees where the newest tree is placed at relative rank $j$.
3. Accelerate transitions across ranks using prefix sums to achieve $O(N^2)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    vector<long long> H(N);
    for (int i = 0; i < N; ++i) cin >> H[i];

    vector<int> dp = {1};

    for (int i = 0; i < N - 1; ++i) {
        int n = i + 2;
        int old_sz = dp.size();
        vector<int> pref(old_sz + 1, 0);
        for (int k = 0; k < old_sz; ++k) {
            pref[k + 1] = (pref[k] + dp[k]) % MOD;
        }

        vector<int> nxt(n, 0);
        long long h_prev = H[i];
        long long h_cur = H[i + 1];

        for (int j = 0; j < n; ++j) {
            if (h_prev < h_cur) {
                if (j < old_sz) {
                    int val = (pref[old_sz] - pref[j]) % MOD;
                    if (val < 0) val += MOD;
                    nxt[j] = val;
                } else {
                    nxt[j] = 0;
                }
            } else if (h_prev > h_cur) {
                int lim = min(j, old_sz);
                nxt[j] = pref[lim];
            } else {
                nxt[j] = pref[old_sz];
            }
        }
        dp = move(nxt);
    }

    int ans = 0;
    for (int x : dp) ans = (ans + x) % MOD;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
