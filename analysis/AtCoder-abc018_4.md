# Problem Analysis: AtCoder-abc018_4 — バレンタインデー

**Problem ID**: `AtCoder-abc018_4`  
**Contest**: `abc018`  
**Rating / Difficulty**: 1711  
**URL**: https://atcoder.jp/contests/abc018/tasks/abc018_4  
**VJudge Tag**: `[problem:AtCoder-abc018_4]`  
**Category File**: [`../categories/basics/partial_bitmask_greedy_dual_dimension.md`](../categories/basics/partial_bitmask_greedy_dual_dimension.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bitmask Enumeration`  
- **Topic (Skill)**: `Partial Bitmask Enumeration with Greedy Sorting on Dual Dimension`  

---

## 1. Problem Statement & Key Idea
Given N girls and M boys. Choose exactly P girls and Q boys. There are R relationships (x_i, y_i, z_i) giving happiness z_i if girl x_i and boy y_i are both chosen. Maximize total happiness. (N, M <= 18).

**Key Insight**: Since N <= 18, iterate over all C(N, P) subsets of girls using bitmasks. Once the girls are fixed, each boy's contribution is independent: sum all happiness values from the chosen girls to that boy. Greedily pick the Q boys with the highest happiness.

## 2. Core Observation & Invariant
C(18, 9) = 48,620. For each mask, computing boys' happiness takes O(R) or O(M), and sorting M <= 18 numbers takes negligible time. Total operations around 48,620 * 18 ~ 8.7 * 10^5.

## 3. Step-by-Step Algorithm
1. Store relationships as adj[girl] = list of (boy, z).
2. For mask = 0 to (1 << N) - 1:
3.   if __builtin_popcount(mask) != P: continue.
4.   Initialize boy_happiness[M] = 0.
5.   For each girl i in mask:
6.     For each (boy, z) in adj[i]:
7.       boy_happiness[boy] += z.
8.   Sort boy_happiness descending.
9.   Sum the top Q values.
10.   ans = max(ans, sum).
11. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(C(N, P) * (R + M log M))`
- **Space Complexity**: `O(N + M + R)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int boy;
    int z;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, p, q, r;
    if (!(cin >> n >> m >> p >> q >> r)) return 0;

    vector<vector<Edge>> adj(n);
    for (int i = 0; i < r; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        --x; --y;
        adj[x].push_back({y, z});
    }

    int max_ans = 0;
    for (int mask = 0; mask < (1 << n); ++mask) {
        if (__builtin_popcount(mask) != p) continue;

        vector<int> boy_score(m, 0);
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                for (auto& e : adj[i]) {
                    boy_score[e.boy] += e.z;
                }
            }
        }

        sort(boy_score.rbegin(), boy_score.rend());
        int cur_score = 0;
        for (int j = 0; j < q; ++j) {
            cur_score += boy_score[j];
        }
        max_ans = max(max_ans, cur_score);
    }

    cout << max_ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Breaking a 2D subset selection problem by bitmasking one dimension and greedily taking the top elements of the other.
- **Reusable Pattern**: `Bipartite Subgraph Max Weight: Bitmask small side + Top-K greedy sort on other side.`
