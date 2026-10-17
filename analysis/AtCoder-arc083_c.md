# Problem Analysis: AtCoder-arc083_c — C. Bichrome Tree

**Problem ID**: `AtCoder-arc083_c`  
**Contest**: `arc083`  
**Rating / Difficulty**: 2289  
**URL**: https://atcoder.jp/contests/arc083/tasks/arc083_c  
**VJudge Tag**: `[problem:AtCoder-arc083_c]`  
**Category File**: [`../categories/dynamic_programming/tree_dp_knapsack_coloring.md`](../categories/dynamic_programming/tree_dp_knapsack_coloring.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
In a tree where each node $u$ requires one color in its subtree to sum to $X_u$, determine if there exists a valid non-negative weight assignment and 2-coloring for all vertices.

## 2. Core Observation & Invariant
In any valid two-coloring of the subtree rooted at $u$, one color has total weight $X_u$. To maximize feasibility for ancestor constraints, $dp[u]$ stores the minimum possible weight of the other color in subtree $u$.

## 3. Step-by-Step Algorithm
1. 1. For each node $u$, vertex $u$ is assigned a color (say Black or White). If $u$ is Black, the sum of weights of all Black vertices in $u$'s subtree must equal $X_u$. The White vertices in $u$'s subtree will have some total weight $W$.
2. 2. For each child $v$ of $u$, subtree $v$ contributes a pair of weights $(X_v, dp[v])$ to subtree $u$, where one color gets $X_v$ and the other gets $dp[v]$. Node $u$ can assign the $X_v$-colored components of $v$ to match $u$'s own color or the opposite color.
3. 3. Thus, for vertex $u$, picking which children share $u$'s color is equivalent to a 0-1 Knapsack problem:
4.    - Let the capacity be $X_u$.
5.    - For each child $v$, we can either add $X_v$ to $u$'s color and $dp[v]$ to the opposite color, OR add $dp[v]$ to $u$'s color and $X_v$ to the opposite color.
6.    - We run a subset-sum DP for the children: $knap[w]$ is the minimum weight on the opposite color when the chosen children assign total weight $w \le X_u$ to $u$'s color.
7. 4. If no combination gives weight $\le X_u$, subtree $u$ cannot be validly colored $\implies$ output `IMPOSSIBLE`.
8. 5. Otherwise, $dp[u] = knap[w]$ over all valid $w \le X_u$. If $dp[1] < \infty$, output `POSSIBLE`.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \max X)`
- **Space Complexity**: `O(N + \max X)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> children(N + 1);
    for (int i = 2; i <= N; ++i) {
        int p;
        cin >> p;
        children[p].push_back(i);
    }

    vector<int> X(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> X[i];
    }

    vector<int> dp(N + 1, 0);

    for (int u = N; u >= 1; --u) {
        if (children[u].empty()) {
            dp[u] = 0;
            continue;
        }

        vector<int> knap(X[u] + 1, INF);
        knap[0] = 0;

        for (int v : children[u]) {
            if (dp[v] >= INF) {
                cout << "IMPOSSIBLE\n";
                return 0;
            }
            vector<int> next_knap(X[u] + 1, INF);
            for (int w = 0; w <= X[u]; ++w) {
                if (knap[w] == INF) continue;
                // Option 1: v's primary color matches u
                if (w + X[v] <= X[u]) {
                    next_knap[w + X[v]] = min(next_knap[w + X[v]], knap[w] + dp[v]);
                }
                // Option 2: v's secondary color matches u
                if (w + dp[v] <= X[u]) {
                    next_knap[w + dp[v]] = min(next_knap[w + dp[v]], knap[w] + X[v]);
                }
            }
            knap = move(next_knap);
        }

        int min_other = INF;
        for (int w = 0; w <= X[u]; ++w) {
            min_other = min(min_other, knap[w]);
        }

        dp[u] = min_other;
        if (dp[u] >= INF) {
            cout << "IMPOSSIBLE\n";
            return 0;
        }
    }

    cout << "POSSIBLE\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
