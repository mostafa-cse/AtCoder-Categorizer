# Problem Analysis: AtCoder-abc153_e — Crested Ibis vs Monster

**Problem ID**: `AtCoder-abc153_e`  
**Contest**: `abc153`  
**Rating / Difficulty**: 1015  
**URL**: https://atcoder.jp/contests/abc153/tasks/abc153_e  
**VJudge Tag**: `[problem:AtCoder-abc153_e]`  
**Category File**: [`../categories/dp/unbounded_knapsack_min_cost.md`](../categories/dp/unbounded_knapsack_min_cost.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Unbounded Knapsack / Minimum Cost Target Reachability`  

---

## 1. Problem Statement & Key Idea
A monster has H health. You have N spells. Spell i deals A_i damage and costs B_i magic points. Each spell can be used any number of times. Find the minimum total magic points to deal at least H damage.

**Key Idea**: Let dp[h] be the minimum magic points to deal at least h damage. This is Unbounded Knapsack.

## 2. Core Observation & Invariant
Transitions: for each damage state h from 0 to H - 1, and for each spell (A_i, B_i): dealing damage A_i transitions to min(H, h + A_i) at cost dp[h] + B_i. Since spells can be reused, update in-place in increasing order of h.

## 3. Step-by-Step Algorithm
1. Initialize dp array of size H + 1 to INF; dp[0] = 0.
2. For h = 0 to H - 1:
3.   If dp[h] == INF continue.
4.   For each spell (A, B): next_h = min((long long)H, h + A); dp[next_h] = min(dp[next_h], dp[h] + B).
5. Output dp[H].

## 4. Complexity Analysis
- **Time Complexity**: `O(N * H)`
- **Space Complexity**: `O(H)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, n;
    if (!(cin >> h >> n)) return 0;

    vector<pair<int, int>> spells(n);
    for (int i = 0; i < n; ++i) {
        cin >> spells[i].first >> spells[i].second;
    }

    vector<long long> dp(h + 1, INF);
    dp[0] = 0;

    for (int cur = 0; cur < h; ++cur) {
        if (dp[cur] == INF) continue;
        for (const auto& [dmg, cost] : spells) {
            int nxt = min(h, cur + dmg);
            dp[nxt] = min(dp[nxt], dp[cur] + cost);
        }
    }

    cout << dp[h] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Unbounded Knapsack formulation with target saturation min(H, h + A).
- **Reusable Pattern**: `Unbounded Knapsack min cost: dp[min(H, h + dmg)] = min(..., dp[h] + cost).`
