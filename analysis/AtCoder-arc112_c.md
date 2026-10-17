# Problem Analysis: AtCoder-arc112_c — DFS Game

**Problem ID**: `AtCoder-arc112_c`  
**Contest**: `arc112`  
**Rating / Difficulty**: 1913  
**URL**: https://atcoder.jp/contests/arc112/tasks/arc112_c  
**VJudge Tag**: `[problem:AtCoder-arc112_c]`  
**Category File**: [`../categories/game_theory/tree_dfs_minimax_parity_inversion.md`](../categories/game_theory/tree_dfs_minimax_parity_inversion.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Tree Games / Minimax`  
- **Topic (Skill)**: `Tree DFS Minimax Game with Subtree Size Parity Inversion and Greedy Child Ordering`  

---

## 1. Problem Statement & Key Idea
Rooted tree with N vertices, 1 coin per vertex. Two players explore tree via DFS. When entering a node, player collects its coin. Player chooses which unvisited child to visit next. When DFS returns from a child, player who moves next depends on whether subtree size is odd or even. Minimax coins for Takahashi.

Let f[u] be the net difference (mover - other) from subtree u. Node u gives +1 coin. If child v has even size sz[v], the same player gets the turn upon return. Thus first player greedily takes all even subtrees with f[v] > 0 first. Odd subtrees change the turn upon return; first player sorts odd subtrees to alternate picks greedily. Finally, even subtrees with negative values are consumed by whoever is left with the turn.

## 2. Core Observation & Invariant
Subtree parity dictates control flow: even size preserves initiative, odd size flips initiative.

## 3. Step-by-Step Algorithm
1. Post-order DFS computing sz[u] and f[u].
2. Categorize children into even_pos (sz even, f > 0), even_neg (sz even, f <= 0), and odd (sz odd).
3. base_val = 1 + sum(even_pos).
4. Sort odd ascending; alternate signs: base_val += sign * odd[i], sign = -sign.
5. Add remaining even_neg with current sign: base_val += sign * sum(even_neg).
6. f[u] = base_val.
7. Takahashi's total coins = (N + f[1]) / 2.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int n;
vector<vector<int>> adj;
vector<int> sz;
vector<int> f;

void dfs(int u) {
    sz[u] = 1;
    vector<int> even_pos;
    vector<int> even_neg;
    vector<int> odd;

    int base_val = 1;

    for (int v : adj[u]) {
        dfs(v);
        sz[u] += sz[v];
        if (sz[v] % 2 == 0) {
            if (f[v] > 0) {
                even_pos.push_back(f[v]);
            } else {
                even_neg.push_back(f[v]);
            }
        } else {
            odd.push_back(f[v]);
        }
    }

    for (int x : even_pos) {
        base_val += x;
    }

    sort(odd.begin(), odd.end());
    int sign = -1;
    for (int x : odd) {
        base_val += sign * x;
        sign = -sign;
    }

    for (int x : even_neg) {
        base_val += sign * x;
    }

    f[u] = base_val;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    sz.assign(n + 1, 0);
    f.assign(n + 1, 0);

    for (int i = 2; i <= n; ++i) {
        int p;
        cin >> p;
        adj[p].push_back(i);
    }

    dfs(1);

    int takahashi = (n + f[1]) / 2;
    cout << takahashi << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Minimax game theory on trees with parity-driven initiative transfer and optimal child sorting.
- **Reusable Pattern**: `Tree DFS Minimax: Even sz subtrees retain turn; odd sz subtrees flip turn, sorted greedily.`
