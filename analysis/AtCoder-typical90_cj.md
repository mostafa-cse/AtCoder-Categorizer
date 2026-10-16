# Problem Analysis: AtCoder-typical90_cj — Similar but Different Ways

**Problem ID**: `AtCoder-typical90_cj`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 088)  
**Rating / Difficulty**: 2150 (★6)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_cj  
**VJudge Tag**: `[problem:AtCoder-typical90_cj]`  
**Category File**: [`../categories/math/pigeonhole_subset_sum.md`](../categories/math/pigeonhole_subset_sum.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Pigeonhole Principle`  
- **Topic (Skill)**: `Pigeonhole Principle Collision Search on Subset Sums`  

---

## 1. Problem Statement & Key Idea
N <= 88 cards with values A_i <= 88. Q incompatible pairs. Find TWO distinct valid subsets of cards having identical sum of values.

**Core Idea**: The maximum possible sum of cards is 88 * 88 = 7,744. The number of valid subsets exponentially exceeds 7,744.

## 2. Core Observation & Invariant
By the Pigeonhole Principle, a collision (two subsets with identical sum) MUST exist! Run DFS backtracking to collect subsets; store the first subset reaching each sum in an array. The moment a sum collides, terminate and output both subsets!

## 3. Step-by-Step Algorithm
1. Backtracking DFS(card_idx, cur_sum, chosen_subset).
2. If cur_sum already seen in memo: output memo[cur_sum] and chosen_subset, terminate immediately.
3. Else: memo[cur_sum] = chosen_subset.
4. Branch: include card (if compatible with chosen) or skip card.

## 4. Complexity Analysis
Time: O(MaxSum * N) <= 7744 * 88 ops (< 0.05s), Space: O(MaxSum * N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

int n, q;
vector<int> a;
vector<vector<bool>> bad;
vector<vector<int>> memo(88 * 88 + 1);
bool found = false;

void dfs(int idx, int cur_sum, vector<int>& chosen) {
    if (found) return;

    if (!chosen.empty()) {
        if (!memo[cur_sum].empty()) {
            // Found collision!
            cout << memo[cur_sum].size() << "\n";
            for (size_t i = 0; i < memo[cur_sum].size(); ++i) {
                cout << memo[cur_sum][i] << (i + 1 == memo[cur_sum].size() ? "" : " ");
            }
            cout << "\n";

            cout << chosen.size() << "\n";
            for (size_t i = 0; i < chosen.size(); ++i) {
                cout << chosen[i] << (i + 1 == chosen.size() ? "" : " ");
            }
            cout << "\n";

            found = true;
            return;
        }
        memo[cur_sum] = chosen;
    }

    if (idx > n) return;

    // Option 1: Pick card idx (if compatible)
    bool ok = true;
    for (int prev : chosen) {
        if (bad[prev][idx]) {
            ok = false;
            break;
        }
    }

    if (ok) {
        chosen.push_back(idx);
        dfs(idx + 1, cur_sum + a[idx], chosen);
        chosen.pop_back();
    }

    // Option 2: Skip card idx
    dfs(idx + 1, cur_sum, chosen);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> q)) return 0;

    a.resize(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    bad.assign(n + 1, vector<bool>(n + 1, false));
    for (int i = 0; i < q; ++i) {
        int u, v;
        cin >> u >> v;
        bad[u][v] = bad[v][u] = true;
    }

    vector<int> chosen;
    dfs(1, 0, chosen);
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Pigeonhole Principle collision search on bounded subset sum capacity.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Pigeonhole Principle guarantee of collisions, early termination search, and hashing subset sum states.
- **Reusable Pattern**: `Pigeonhole Principle Subset Sum Collision.`

---
Back to [Pigeonhole Principle Collision Search on Subset Sums](../categories/math/pigeonhole_subset_sum.md) | [Categories Directory](../categories/README.md)