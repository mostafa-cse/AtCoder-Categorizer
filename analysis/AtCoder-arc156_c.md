# Problem Analysis: AtCoder-arc156_c — Tree and LCS

**Problem ID**: `AtCoder-arc156_c`  
**Contest**: `arc156`  
**Rating / Difficulty**: 2155  
**URL**: https://atcoder.jp/contests/arc156/tasks/arc156_c  
**VJudge Tag**: `[problem:AtCoder-arc156_c]`  
**Category File**: [`../categories/basics/leaf_peeling_inversion_matching_tree_lcs.md`](../categories/basics/leaf_peeling_inversion_matching_tree_lcs.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Construct a permutation P of tree vertices that minimizes the maximum LCS between any simple path x and its mapped sequence P(x). A similarity of 1 can always be achieved by iteratively peeling pairs of leaves and swapping their permutation values.

## 2. Core Observation & Invariant
If two opposite leaves u and v are paired with P[u] = v and P[v] = u, no simple path can contain both in its common subsequence with mapped values. By peeling leaves in pairs and assigning cross-mappings, we inductively reduce the tree by 2 vertices while preserving the invariant that no path shares more than 1 common vertex with its image.

## 3. Step-by-Step Algorithm
1. Initialize vertex degrees and push all leaves (degree <= 1) onto a stack.
2. While the stack has >= 2 vertices, pop u and v, assign P[u] = v and P[v] = u.
3. Remove u and v from the tree by decrementing neighbor degrees; if any neighbor becomes a leaf, push it onto the stack.
4. If one central vertex remains (when N is odd), assign P[x] = x.
5. Output the resulting 1-indexed permutation P.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> g(n + 1);
    vector<int> deg(n + 1, 0);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }

    vector<int> st;
    for (int i = 1; i <= n; ++i) {
        if (deg[i] <= 1) {
            st.push_back(i);
        }
    }

    vector<int> p(n + 1, 0);
    while (st.size() >= 2) {
        int u = st.back(); st.pop_back();
        int v = st.back(); st.pop_back();
        p[u] = v;
        p[v] = u;

        for (int to : g[u]) {
            deg[to]--;
            if (deg[to] == 1) st.push_back(to);
        }
        for (int to : g[v]) {
            deg[to]--;
            if (deg[to] == 1) st.push_back(to);
        }
    }

    if (!st.empty()) {
        int x = st.back();
        st.pop_back();
        p[x] = x;
    }

    for (int i = 1; i <= n; ++i) {
        cout << p[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
