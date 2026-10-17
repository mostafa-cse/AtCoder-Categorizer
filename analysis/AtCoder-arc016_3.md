# Problem Analysis: AtCoder-arc016_3 — Gacha

**Problem ID**: `AtCoder-arc016_3`  
**Contest**: `arc016`  
**Rating / Difficulty**: 2087  
**URL**: https://atcoder.jp/contests/arc016/tasks/arc016_3  
**VJudge Tag**: `[problem:AtCoder-arc016_3]`  
**Category File**: [`../categories/dynamic_programming/bitmask_expected_cost_dp_self_transition.md`](../categories/dynamic_programming/bitmask_expected_cost_dp_self_transition.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
There are N prizes (1 to N) and M gacha machines. The j-th gacha costs C_j yen and drops prize k with probability P_{j,k} percent. Find the minimum expected total cost to collect all N prizes.

**Key Insight**: Let dp[mask] be the minimum expected cost to collect all remaining prizes when the currently collected set of prizes is mask. From state mask, if we decide to roll gacha j, some prize we roll might already be in mask (a self-loop occurring with probability p_stay = sum_{k in mask} P_{j,k} / 100), or it might yield a new prize k not in mask. Setting up the Bellman expectation equation: E_j[mask] = C_j + p_stay * E_j[mask] + sum_{k not in mask} (P_{j,k} / 100) * dp[mask | (1 << k)]. Solving for E_j[mask]: E_j[mask] = (C_j + sum_{k not in mask} (P_{j,k}/100) * dp[mask | (1 << k)]) / (1 - p_stay). Then dp[mask] = min_j E_j[mask].

## 2. Core Observation & Invariant
Self-loops in expectation DP are resolved algebraically: E = (Cost + sum p_i * E_next) / (1 - p_self).

## 3. Step-by-Step Algorithm
1. Initialize dp[(1 << N) - 1] = 0.
2. Iterate mask from (1 << N) - 2 down to 0:
3.   For each gacha j from 1 to M:
4.     Compute p_stay = probability of rolling an item already in mask.
5.     If p_stay == 1.0 (cannot obtain any new item), skip gacha j.
6.     Sum trans = sum_{k not in mask} (P_{j,k} / 100) * dp[mask | (1 << k)].
7.     cost_j = (C_j + trans) / (1.0 - p_stay).
8.     dp[mask] = min(dp[mask], cost_j).
9. Output dp[0].

## 4. Complexity Analysis
- **Time Complexity**: `O(M * N * 2^N)`
- **Space Complexity**: `O(2^N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Bitmask expectation DP with self-loop elimination in Markov decision processes.
- **Reusable Pattern**: Solving infinite retry loops in expectation DP by isolating the self-transition term into the denominator (1 - p_self).

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

struct Gacha {
    double cost;
    vector<pair<int, double>> prizes; // (id, prob)
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Gacha> gachas(m);
    for (int j = 0; j < m; ++j) {
        int c, cost;
        cin >> c >> cost;
        gachas[j].cost = cost;
        for (int i = 0; i < c; ++i) {
            int prize;
            double p;
            cin >> prize >> p;
            gachas[j].prizes.push_back({prize - 1, p / 100.0});
        }
    }

    int full = 1 << n;
    vector<double> dp(full, 1e18);
    dp[full - 1] = 0.0;

    for (int mask = full - 2; mask >= 0; --mask) {
        for (int j = 0; j < m; ++j) {
            double p_stay = 0.0;
            double next_exp = 0.0;
            for (auto& item : gachas[j].prizes) {
                int prize = item.first;
                double prob = item.second;
                if ((mask >> prize) & 1) {
                    p_stay += prob;
                } else {
                    next_exp += prob * dp[mask | (1 << prize)];
                }
            }
            if (p_stay >= 1.0 - 1e-9) continue;
            double cost = (gachas[j].cost + next_exp) / (1.0 - p_stay);
            dp[mask] = min(dp[mask], cost);
        }
    }

    cout << fixed << setprecision(10) << dp[0] << "\n";
    return 0;
}
```
