# Problem Analysis: AtCoder-abc293_h — Ex - Optimal Path Decomposition

**Problem ID**: `AtCoder-abc293_h`  
**Contest**: `abc293`  
**Rating / Difficulty**: 2831  
**URL**: https://atcoder.jp/contests/abc293/tasks/abc293_h  
**VJudge Tag**: `[problem:AtCoder-abc293_h]`  
**Category File**: [`../categories/dynamic_programming/tree_simple_path_coloring_decomposition_dp.md`](../categories/dynamic_programming/tree_simple_path_coloring_decomposition_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Partition vertices of an N-vertex tree into monochromatic simple paths such that any simple path in the tree intersects at most K colors. Find the minimum possible K.

## 2. Core Observation & Invariant
Color monochromatic edges 'black' (weight 0) and inter-color edges 'white' (weight 1). Black edges form vertex-disjoint paths, meaning each vertex has degree at most 2 in black edges. The maximum number of colors on any tree path is (diameter in {0, 1} weights) + 1. By HLD, the optimal K is at most 2 * floor(log2 N) + 1. For a fixed K, tree DP determines whether a {0, 1} weighting with diameter <= K - 1 exists in O(N) time.

## 3. Step-by-Step Algorithm
1. 1. Binary search K in [1, N].
2. 2. Tree DP defines dp[u][0/1]: minimum maximum distance into subtree u when the parent edge has weight 0 or 1, requiring subtree diameter <= K - 1.
3. 3. For vertex u, sort children by dp[v][1] descending.
4. 4. Select at most 1 child (for dp0) or at most 2 children (for dp1) to have edge weight 0, keeping others at weight 1.
5. 5. Check that max1 + max2 <= K - 1 for path through u, minimizing max1.
6. 6. Binary search returns the minimal valid K.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int n;
vector<vector<int>> adj;

pair<int, int> dfs(int u, int p, int K, bool& valid) {
    if (!valid) return {INF, INF};

    vector<pair<int, int>> sons;
    for (int v : adj[u]) {
        if (v != p) {
            auto dp_v = dfs(v, u, K, valid);
            if (!valid) return {INF, INF};
            sons.push_back(dp_v);
        }
    }

    if (sons.empty()) {
        return {0, 0};
    }

    vector<int> cand_indices;
    int inf_cnt = 0;
    for (int i = 0; i < (int)sons.size(); ++i) {
        if (sons[i].second == INF) {
            cand_indices.push_back(i);
            inf_cnt++;
        }
    }
    if (inf_cnt > 2) {
        valid = false;
        return {INF, INF};
    }

    vector<int> sorted_indices(sons.size());
    for (int i = 0; i < (int)sons.size(); ++i) sorted_indices[i] = i;
    sort(sorted_indices.begin(), sorted_indices.end(), [&](int a, int b) {
        return sons[a].second > sons[b].second;
    });

    for (int idx : sorted_indices) {
        if (find(cand_indices.begin(), cand_indices.end(), idx) == cand_indices.end()) {
            cand_indices.push_back(idx);
            if (cand_indices.size() >= 5) break;
        }
    }

    int best_dp0 = INF, best_dp1 = INF;
    int C_size = (int)cand_indices.size();

    // Check subsets of size 0, 1, 2
    for (int mask = 0; mask < (1 << C_size); ++mask) {
        int sz = __builtin_popcount(mask);
        if (sz > 2) continue;

        bool ok = true;
        // Check if all sons with dp1 == INF are included
        for (int i = 0; i < C_size; ++i) {
            int son_idx = cand_indices[i];
            if (sons[son_idx].second == INF && !(mask & (1 << i))) {
                ok = false;
                break;
            }
            if ((mask & (1 << i)) && sons[son_idx].first == INF) {
                ok = false;
                break;
            }
        }
        if (!ok) continue;

        int max1 = 0, max2 = 0;
        for (int i = 0; i < (int)sons.size(); ++i) {
            int val;
            // Check if i is chosen in mask
            bool in_s = false;
            for (int j = 0; j < C_size; ++j) {
                if (cand_indices[j] == i && (mask & (1 << j))) {
                    in_s = true;
                    break;
                }
            }

            if (in_s) {
                val = sons[i].first;
            } else {
                val = sons[i].second + 1;
            }

            if (val > max1) {
                max2 = max1;
                max1 = val;
            } else if (val > max2) {
                max2 = val;
            }
        }

        if (max1 + max2 <= K - 1 && max1 <= K - 1) {
            if (sz <= 1) best_dp0 = min(best_dp0, max1);
            if (sz <= 2) best_dp1 = min(best_dp1, max1);
        }
    }

    if (best_dp0 == INF && best_dp1 == INF) {
        valid = false;
    }

    return {best_dp0, best_dp1};
}

bool check(int K) {
    bool valid = true;
    auto res = dfs(1, 0, K, valid);
    return valid && (res.first < INF || res.second < INF);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int low = 1, high = n;
    int ans = n;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
