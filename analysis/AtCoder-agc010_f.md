# Problem Analysis: AtCoder-agc010_f — F. Tree Game

**Problem ID**: `AtCoder-agc010_f`  
**Contest**: `agc010`  
**Rating / Difficulty**: 2897  
**URL**: https://atcoder.jp/contests/agc010/tasks/agc010_f  
**VJudge Tag**: `[problem:AtCoder-agc010_f]`  
**Category File**: [`../categories/game_theory/tree_stone_game_strict_descent.md`](../categories/game_theory/tree_stone_game_strict_descent.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Graph Games`  
- **Topic (Skill)**: `Games on Arbitrary Graphs`  

---

## 1. Problem Statement & Key Idea
A piece starts at node s on a tree with stone counts A_v. A player moves piece from u to neighbor v with A_v < A_u, removing 1 stone from u. The player unable to move loses. Find all winning starting nodes s.

## 2. Core Observation & Invariant
Because moves require strictly decreasing stone counts A_v < A_u, this defines a DAG on moves. If Takahashi moves piece to v where A_v < A_s and v is a losing starting position for the next player in the tree rooted at s, Takahashi can force a win. If Aoki tries to move back to s, Takahashi simply repeats his winning strategy because A_v < A_s guarantees Takahashi never runs out of stones before Aoki does. Thus, s is winning iff there is a neighbor v with A_v < A_s that is losing.

## 3. Step-by-Step Algorithm
1. 1. For each candidate root s in [1, N], evaluate whether s is winning.
2. 2. Define can_win(u, p): returns true iff u has a neighbor v != p with A_v < A_u such that can_win(v, u) is false.
3. 3. A starting vertex s is winning iff there is some neighbor v with A_v < A_s and !can_win(v, s).
4. 4. Collect and print all winning starting nodes in increasing order.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<long long> a;
vector<vector<int>> adj;

// Returns true if player whose turn it is at u can win, given they just came from p
bool can_win(int u, int p) {
    for (int v : adj[u]) {
        if (v == p) continue;
        if (a[v] < a[u]) {
            // If opponent cannot win from v, we can move to v and win!
            if (!can_win(v, u)) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n)) return 0;
    a.resize(n + 1);
    adj.assign(n + 1, vector<int>());

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> winners;
    for (int r = 1; r <= n; ++r) {
        if (can_win(r, 0)) {
            winners.push_back(r);
        }
    }

    for (size_t i = 0; i < winners.size(); ++i) {
        cout << winners[i] << (i + 1 == winners.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
