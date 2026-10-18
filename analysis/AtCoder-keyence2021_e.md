# Problem Analysis: AtCoder-keyence2021_e — E. Greedy Ant

**Problem ID**: `AtCoder-keyence2021_e`  
**Contest**: `keyence2021`  
**Rating / Difficulty**: 2560  
**URL**: https://atcoder.jp/contests/keyence2021/tasks/keyence2021_e  
**VJudge Tag**: `[problem:AtCoder-keyence2021_e]`  
**Category File**: [`../categories/dynamic_programming_dp/greedy_ant_interval_dp.md`](../categories/dynamic_programming_dp/greedy_ant_interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
There are $N$ candies $a_1 \dots a_N$. Ant starts between candies $p$ and $p + 1$. Snuke and Ant alternate turns. Snuke can pick any candy. Ant greedily picks $\max(a_{l-1}, a_{r+1})$ adjacent to the eaten range $[l, r]$. Find Snuke's maximum score for each starting position $p \in [0, N]$. Ant's eaten candies always form a contiguous interval $[l, r]$. Model as Interval DP where $k$ is the number of tokens (unclaimed turns) Snuke holds.

## 2. Core Observation & Invariant
State $DP[l][r][k]$ is the maximum tastiness Snuke gets from remaining candies outside $[l, r]$ given $k$ available turns. Snuke can spend 1 turn to take $a_{l-1}$ or $a_{r+1}$, or let Ant move (Ant takes $\max(a_{l-1}, a_{r+1})$ and Snuke receives $+1$ turn). The DP table is independent of $p$! Computing the table once answers all $p$ via $DP[p + 1][p][1]$ in $O(N^3)$ total time.

## 3. Step-by-Step Algorithm
1. 1. Memoized DFS over state $(l, r, k)$:
2.    - Base: if $l == 1$ and $r == N$, return 0.
3.    - Cap $k \le \min((N - (r - l + 1) + 1)/2 + 1, N)$.
4.    - If $k \ge 1$ and $l > 1$: test Snuke taking $a_{l-1} + DP(l - 1, r, k - 1)$.
5.    - If $k \ge 1$ and $r < N$: test Snuke taking $a_{r+1} + DP(l, r + 1, k - 1)$.
6.    - Ant move: if $a_{l-1} > a_{r+1}$, $DP(l - 1, r, k + 1)$ else $DP(l, r + 1, k + 1)$.
7.    - Return maximum.
8. 2. For each $p \in [0, N]$, output $DP[p + 1][p][1]$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^3)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int n;
int a[405];
int dp[405][405][205];
bool vis[405][405][205];

int get_dp(int l, int r, int k) {
    if (l == 1 && r == n) return 0;
    int max_k = min((n - (r - l + 1) + 1) / 2 + 1, n);
    if (k > max_k) k = max_k;

    if (vis[l][r][k]) return dp[l][r][k];

    int res = 0;
    // Option 1: Snuke takes left
    if (l > 1 && k >= 1) {
        res = max(res, a[l - 1] + get_dp(l - 1, r, k - 1));
    }
    // Option 2: Snuke takes right
    if (r < n && k >= 1) {
        res = max(res, a[r + 1] + get_dp(l, r + 1, k - 1));
    }
    // Option 3: Ant moves
    int cand_l = (l > 1 ? a[l - 1] : -1);
    int cand_r = (r < n ? a[r + 1] : -1);
    if (cand_l > cand_r) {
        res = max(res, get_dp(l - 1, r, k + 1));
    } else {
        res = max(res, get_dp(l, r + 1, k + 1));
    }

    vis[l][r][k] = true;
    return dp[l][r][k] = res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n)) return 0;

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    memset(vis, 0, sizeof(vis));

    for (int p = 0; p <= n; ++p) {
        int ans = get_dp(p + 1, p, 1);
        cout << ans << "\n";
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
