# Problem Analysis: AtCoder-agc014_d — D. Black and White Tree

**Problem ID**: `AtCoder-agc014_d`  
**Contest**: `agc014`  
**Rating / Difficulty**: 2266  
**URL**: https://atcoder.jp/contests/agc014/tasks/agc014_d  
**VJudge Tag**: `[problem:AtCoder-agc014_d]`  
**Category File**: [`../categories/game_theory/matching_game_on_tree_perfect_matching.md`](../categories/game_theory/matching_game_on_tree_perfect_matching.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Graph Games`  
- **Topic (Skill)**: `[Problem] Matching Game On A Graph`  

---

## 1. Problem Statement & Key Idea
Takahashi (white) and Aoki (black) alternately color uncolored vertices of a tree of $N$ vertices ($N \le 10^5$), Takahashi going first. At the end, every white vertex adjacent to at least one black vertex is repainted black. Takahashi wins if any white vertex remains; Aoki wins if all vertices turn black. Determine the winner with optimal play.

## 2. Core Observation & Invariant
A white vertex survives repainting if and only if all of its neighbors are white. If the tree possesses a perfect matching $M$ of size $N/2$, Aoki adopts a symmetric mirror strategy: whenever Takahashi colors vertex $u$, Aoki immediately colors the matched vertex $v$ where $(u, v) \in M$. At the end, every white vertex has an adjacent matched partner colored black, so every white vertex is repainted black and Aoki (Second) wins.
Conversely, if the tree lacks a perfect matching, Takahashi can force a win by repeatedly identifying an unmatched leaf and securing its parent, guaranteeing at least one white vertex with all-white neighbors. Hence, Aoki (Second) wins if and only if the tree has a perfect matching (which requires $N$ even and greedy leaf-parent matching covering all $N$ vertices).

## 3. Step-by-Step Algorithm
1. If $N$ is odd, output 'First' immediately.
2. Run a bottom-up post-order DFS on the tree from root 1.
3. For each node $u$, after visiting its children: if $u$ is unmatched and its parent $p \neq 0$ is unmatched, match $u$ with $p$ and increment match count.
4. If the total matching size equals $N / 2$, output 'Second'; otherwise output 'First'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    if (n % 2 != 0) {
        cout << "First\n";
        return 0;
    }

    // Greedy maximum matching on tree
    vector<int> matched(n + 1, 0);
    int match_count = 0;

    auto dfs = [&](auto self, int u, int p) -> void {
        for (int v : adj[u]) {
            if (v != p) {
                self(self, v, u);
            }
        }
        if (p != 0 && !matched[u] && !matched[p]) {
            matched[u] = 1;
            matched[p] = 1;
            match_count++;
        }
    };

    dfs(dfs, 1, 0);

    if (match_count == n / 2) {
        cout << "Second\n";
    } else {
        cout << "First\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
