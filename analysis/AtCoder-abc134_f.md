# Problem Analysis: AtCoder-abc134_f — F. Permutation Oddness

**Problem ID**: `AtCoder-abc134_f`  
**Contest**: `abc134`  
**Rating / Difficulty**: 2532  
**URL**: https://atcoder.jp/contests/abc134/tasks/abc134_f  
**VJudge Tag**: `[problem:AtCoder-abc134_f]`  
**Category File**: [`../categories/dynamic_programming_dp/permutation_oddness_open_close_interval_trick.md`](../categories/dynamic_programming_dp/permutation_oddness_open_close_interval_trick.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `More Tricks`  
- **Topic (Skill)**: `Open and Close Interval Trick`  

---

## 1. Problem Statement & Key Idea
Count permutations $P$ of $1 \dots N$ with 'oddness' $\sum_{i=1}^N |i - P_i| = K$. Since $|i - P_i| = \max(i, P_i) - \min(i, P_i)$, think of each pair $(i, P_i)$ as an interval between $i$ and $P_i$. The oddness is equal to $2 \times \sum_{i=1}^{N-1} (\text{number of intervals crossing boundary } i + 0.5)$.

## 2. Core Observation & Invariant
Use the Open and Close Interval Trick (Profile DP). Process positions $i = 1 \dots N$. At boundary $i$, suppose $j$ indices $x \le i$ have not yet been assigned their values $P_x > i$, and symmetrically $j$ values $y \le i$ have not yet been matched to indices $P_z = y$ with $z > i$. Crossing from $i$ to $i + 1$, each of these $2j$ open lines contributes $+2j$ to the total oddness.

## 3. Step-by-Step Algorithm
1. 1. If $K$ is odd, output 0 immediately.
2. 2. DP state: $DP[i][j][k]$ = number of ways after step $i$ with $j$ open pairs and accumulated cost $k$.
3. 3. At step $i$, moving to $i+1$ increases cost by $2j$. Then for element $i$, we choose how index $i$ and value $i$ are matched:
4.    - Both matched immediately to each other: $j \to j$ (1 way).
5.    - Both left open: $j \to j + 1$ (1 way).
6.    - One matched to an existing open partner, one left open: $j \to j$ ($2j$ ways).
7.    - Both matched to existing open partners: $j \to j - 1$ ($j^2$ ways).
8. 4. Transitions sum up modulo $10^9 + 7$.
9. 5. Answer is $DP[N][0][K]$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 K)`
- **Space Complexity**: `O(N K)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 1000000007;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    if (k % 2 != 0 || k > n * n) {
        cout << 0 << "\n";
        return 0;
    }

    vector<vector<long long>> dp(n + 1, vector<long long>(k + 1, 0));
    dp[0][0] = 1;

    for (int i = 0; i < n; ++i) {
        vector<vector<long long>> nxt(n + 1, vector<long long>(k + 1, 0));
        for (int j = 0; j <= i; ++j) {
            for (int w = 0; w <= k; ++w) {
                long long ways = dp[j][w];
                if (!ways) continue;

                // 1. Stay j open: (1 + 2j) ways, cost added is 2j
                int cost = w + 2 * j;
                if (cost <= k) {
                    long long add = (ways * (1 + 2 * j)) % MOD;
                    nxt[j][cost] = (nxt[j][cost] + add >= MOD ? nxt[j][cost] + add - MOD : nxt[j][cost] + add);
                }

                // 2. Close: j -> j - 1: j * j ways, cost added is 2 * (j - 1)
                if (j >= 1) {
                    cost = w + 2 * (j - 1);
                    if (cost <= k) {
                        long long add = (ways * ((long long)j * j % MOD)) % MOD;
                        nxt[j - 1][cost] = (nxt[j - 1][cost] + add >= MOD ? nxt[j - 1][cost] + add - MOD : nxt[j - 1][cost] + add);
                    }
                }

                // 3. Open: j -> j + 1: 1 way, cost added is 2 * (j + 1)
                if (j + 1 <= n) {
                    cost = w + 2 * (j + 1);
                    if (cost <= k) {
                        nxt[j + 1][cost] = (nxt[j + 1][cost] + ways >= MOD ? nxt[j + 1][cost] + ways - MOD : nxt[j + 1][cost] + ways);
                    }
                }
            }
        }
        dp = move(nxt);
    }

    cout << dp[0][k] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
