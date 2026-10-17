# Problem Analysis: AtCoder-arc175_d — D. LIS on Tree 2

**Problem ID**: `AtCoder-arc175_d`  
**Contest**: `arc175`  
**Rating / Difficulty**: 2276  
**URL**: https://atcoder.jp/contests/arc175/tasks/arc175_d  
**VJudge Tag**: `[problem:AtCoder-arc175_d]`  
**Category File**: [`../categories/basics/constructive_tree_permutation_target_lis_sum.md`](../categories/basics/constructive_tree_permutation_target_lis_sum.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Given a tree of $N$ vertices and a target integer $K$, construct a permutation $P$ of $1, \dots, N$ such that the sum of lengths of longest increasing subsequences over all simple paths starting from the root equals $K$, or determine it is impossible.

## 2. Core Observation & Invariant
In any rooted tree, extending the LIS at vertex $u$ increments the LIS value of all vertices in its subtree $T_u$, contributing exactly $|T_u|$ to $\sum L_i$. Since subtree sizes form an additive hierarchy, greedy selection by descending subtree size solves the subset sum exactly, and ranking vertices by signed depths $x_u = \pm d_u$ reconstructs the permutation.

## 3. Step-by-Step Algorithm
1. 1. Along any root-to-node path, adding node $u$ either increments the LIS by 1 or leaves it unchanged. Minimum total sum is $N$ (strictly decreasing top-to-bottom); maximum is $N + \sum_{i=1}^N d_i = \sum_{i=1}^N |T_i|$. If $K < N$ or $K > N + \sum d_i$, output `No`.\n2. If vertex $u$ is chosen to extend the LIS, it adds $|T_u|$ to the total sum $\sum L_i$. The problem reduces to choosing a subset of vertices $S \subseteq \{2, \dots, N\}$ such that $\sum_{u \in S} |T_u| = K - N$.\n3. By tree structural induction, greedy selection over $u \in \{2, \dots, N\}$ sorted by descending $|T_u|$ is guaranteed to achieve $K - N$ if achievable.\n4. To construct $P$: define $x_1 = 0$; for each $i \ge 2$, set $x_i = d_i$ if $i \in S$, and $x_i = -d_i$ if $i \notin S$. Sorting all vertices by $x_i$ ascending and assigning permutation labels $1, \dots, N$ ensures that along every branch, vertices in $S$ are strictly increasing while vertices not in $S$ are strictly smaller, achieving the target LIS sum in $O(N \log N)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int n;
long long k;
vector<vector<int>> adj;
vector<int> sz;
vector<int> depth;
vector<int> parent_node;
vector<bool> in_S;

void dfs(int u, int p, int d) {
    depth[u] = d;
    parent_node[u] = p;
    sz[u] = 1;
    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u, d + 1);
            sz[u] += sz[v];
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n >> k)) return 0;

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    sz.assign(n + 1, 0);
    depth.assign(n + 1, 0);
    parent_node.assign(n + 1, 0);
    dfs(1, 0, 0);

    long long sum_depth = 0;
    for (int i = 1; i <= n; i++) {
        sum_depth += depth[i];
    }

    long long min_val = n;
    long long max_val = n + sum_depth;

    if (k < min_val || k > max_val) {
        cout << "No\n";
        return 0;
    }

    long long rem = k - n;
    vector<int> order(n - 1);
    iota(order.begin(), order.end(), 2);
    sort(order.begin(), order.end(), [](int a, int b) {
        return sz[a] > sz[b];
    });

    in_S.assign(n + 1, false);
    for (int u : order) {
        if (sz[u] <= rem) {
            in_S[u] = true;
            rem -= sz[u];
        }
    }

    if (rem != 0) {
        cout << "No\n";
        return 0;
    }

    vector<pair<int, int>> nodes;
    nodes.reserve(n);
    nodes.push_back({0, 1});
    for (int i = 2; i <= n; i++) {
        int val = in_S[i] ? depth[i] : -depth[i];
        nodes.push_back({val, i});
    }

    sort(nodes.begin(), nodes.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        if (a.first != b.first) return a.first < b.first;
        return a.second < b.second;
    });

    vector<int> P(n + 1);
    for (int rank = 1; rank <= n; rank++) {
        int u = nodes[rank - 1].second;
        P[u] = rank;
    }

    cout << "Yes\n";
    for (int i = 1; i <= n; i++) {
        cout << P[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
