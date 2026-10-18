# Problem Analysis: AtCoder-abc269_g — G. Reversible Cards 2

**Problem ID**: `AtCoder-abc269_g`  
**Contest**: `abc269`  
**Rating / Difficulty**: 2440  
**URL**: https://atcoder.jp/contests/abc269/tasks/abc269_g  
**VJudge Tag**: `[problem:AtCoder-abc269_g]`  
**Category File**: [`../categories/dynamic_programming/reversible_cards_bounded_knapsack.md`](../categories/dynamic_programming/reversible_cards_bounded_knapsack.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Subset Sum Optimizations`  

---

## 1. Problem Statement & Key Idea
Given $N$ cards with front $A_i$ and back $B_i$ such that $\sum (A_i + B_i) = M \le 200000$, find the minimum flips to achieve sum $k$ for each $k \in [0, M]$. The initial sum is $S_0 = \sum A_i$, and flipping card $i$ changes the sum by $\Delta_i = B_i - A_i$. Since $\sum |\Delta_i| \le M$, there are at most $O(\sqrt{M})$ distinct non-zero deltas. Binary splitting converts this into a bounded knapsack problem solvable in $O(M \sqrt{M})$ time.

## 2. Core Observation & Invariant
Because the sum of absolute deltas is bounded by $M$, grouping identical deltas and applying binary powers of 2 reduces the number of items to at most $O(\sqrt{M} \log M)$, easily processed by 0-1 knapsack DP.

## 3. Step-by-Step Algorithm
1. 1. Compute initial sum $S_0 = \sum A_i$ and count the frequencies of each delta $d = B_i - A_i$.
2. 2. Decompose each delta count $c_d$ into binary chunks $k = 1, 2, 4, \dots$ with weight $d \times k$ and cost $k$.
3. 3. Initialize $dp[S_0] = 0$ and all other states to $\infty$.
4. 4. For each chunk $(wt, cost)$, update $dp$ in $O(M)$ time (forward for $wt > 0$, backward for $wt < 0$).
5. 5. Output $dp[k]$ for each $k = 0 \dots M$ (or -1 if unreachable).

## 4. Complexity Analysis
- **Time Complexity**: `O(M sqrt(M))`
- **Space Complexity**: `O(M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

static const int INF = 1e9;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    map<int, int> diff_counts;
    int S0 = 0;

    for (int i = 0; i < N; ++i) {
        int a, b;
        cin >> a >> b;
        S0 += a;
        int d = b - a;
        if (d != 0) {
            diff_counts[d]++;
        }
    }

    vector<pair<int, int>> items; // (weight, cost)
    for (auto& entry : diff_counts) {
        int d = entry.first;
        int c = entry.second;
        int k = 1;
        while (c > 0) {
            int take = min(k, c);
            items.push_back({d * take, take});
            c -= take;
            k *= 2;
        }
    }

    vector<int> dp(M + 1, INF);
    dp[S0] = 0;

    for (auto& it : items) {
        int wt = it.first;
        int cost = it.second;
        vector<int> new_dp = dp;

        if (wt > 0) {
            for (int s = 0; s <= M - wt; ++s) {
                if (dp[s] != INF) {
                    if (dp[s] + cost < new_dp[s + wt]) {
                        new_dp[s + wt] = dp[s] + cost;
                    }
                }
            }
        } else {
            int abs_wt = -wt;
            for (int s = abs_wt; s <= M; ++s) {
                if (dp[s] != INF) {
                    if (dp[s] + cost < new_dp[s - abs_wt]) {
                        new_dp[s - abs_wt] = dp[s] + cost;
                    }
                }
            }
        }
        dp = move(new_dp);
    }

    for (int k = 0; k <= M; ++k) {
        cout << (dp[k] == INF ? -1 : dp[k]) << "\n";
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
