# Problem Analysis: AtCoder-arc095_d — F - Permutation Tree

**Problem ID**: `AtCoder-arc095_d`  
**Contest**: `arc095`  
**Rating / Difficulty**: 2626  
**URL**: https://atcoder.jp/contests/arc095/tasks/arc095_d  
**VJudge Tag**: `[problem:AtCoder-arc095_d]`  
**Category File**: [`../categories/basics/permutation_tree_caterpillar_constructive.md`](../categories/basics/permutation_tree_caterpillar_constructive.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Given a tree of N vertices, determine if it can be realized as a permutation tree and find the lexicographically smallest permutation P.

## 2. Core Observation & Invariant
A tree can be realized by a permutation iff it is a caterpillar tree (all vertices are at distance at most 1 from a central spine path). Pruning all leaves leaves a simple path u_1 - u_2 - ... - u_k. Each spine vertex u_i of degree deg(u_i) corresponds to a block of size deg(u_i) - 1. Blocks of the form (B+1 ... B+s-1, B) can be oriented forward or backward along the spine path.

## 3. Step-by-Step Algorithm
1. Remove all leaves (vertices of degree 1).
2. Verify that remaining internal vertices form a single simple path (caterpillar property). If not, output -1.
3. Extract the spine path and count attached leaves for each spine vertex.
4. Construct candidate permutations for forward and reverse spine orientations.
5. Select and output the lexicographically smaller permutation.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> make_permutation(const vector<int>& sizes) {
    vector<int> p;
    int cur = 1;
    for (int s : sizes) {
        if (s == 1) {
            p.push_back(cur);
            cur++;
        } else {
            for (int v = cur + 1; v < cur + s; ++v) {
                p.push_back(v);
            }
            p.push_back(cur);
            cur += s;
        }
    }
    return p;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    if (n == 2) {
        cout << "1 2\n";
        return 0;
    }

    vector<vector<int>> adj(n + 1);
    vector<int> deg(n + 1, 0);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }

    vector<bool> is_leaf(n + 1, false);
    vector<int> rem_nodes;
    for (int i = 1; i <= n; ++i) {
        if (deg[i] <= 1) is_leaf[i] = true;
        else rem_nodes.push_back(i);
    }

    if (rem_nodes.empty()) {
        cout << "1 2\n";
        return 0;
    }

    vector<bool> in_rem(n + 1, false);
    for (int u : rem_nodes) in_rem[u] = true;

    vector<int> rem_deg(n + 1, 0);
    vector<int> deg1_nodes;
    for (int u : rem_nodes) {
        for (int v : adj[u]) {
            if (in_rem[v]) rem_deg[u]++;
        }
        if (rem_deg[u] == 1) deg1_nodes.push_back(u);
        if (rem_nodes.size() > 1 && rem_deg[u] > 2) {
            cout << "-1\n";
            return 0;
        }
    }

    if (rem_nodes.size() > 1 && deg1_nodes.size() != 2) {
        cout << "-1\n";
        return 0;
    }

    vector<int> path;
    if (rem_nodes.size() == 1) {
        path = rem_nodes;
    } else {
        path.push_back(deg1_nodes[0]);
        vector<bool> visited(n + 1, false);
        visited[deg1_nodes[0]] = true;

        while (path.size() < rem_nodes.size()) {
            int curr = path.back();
            int nxt = -1;
            for (int v : adj[curr]) {
                if (in_rem[v] && !visited[v]) {
                    nxt = v;
                    break;
                }
            }
            if (nxt == -1) {
                cout << "-1\n";
                return 0;
            }
            visited[nxt] = true;
            path.push_back(nxt);
        }
    }

    vector<int> sizes;
    sizes.push_back(1);
    for (int u : path) {
        sizes.push_back(deg[u] - 1);
    }
    sizes.push_back(1);

    vector<int> rev_sizes = sizes;
    reverse(rev_sizes.begin(), rev_sizes.end());

    vector<int> p1 = make_permutation(sizes);
    vector<int> p2 = make_permutation(rev_sizes);

    vector<int> ans = min(p1, p2);
    for (int i = 0; i < (int)ans.size(); ++i) {
        cout << ans[i] << (i + 1 == (int)ans.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
