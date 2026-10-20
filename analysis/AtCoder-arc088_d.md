# Problem Analysis: AtCoder-arc088_d — F - Christmas Tree

**Problem ID**: `AtCoder-arc088_d`  
**Contest**: `arc088`  
**Rating / Difficulty**: 2983  
**URL**: https://atcoder.jp/contests/arc088/tasks/arc088_d  
**VJudge Tag**: `[problem:AtCoder-arc088_d]`  
**Category File**: [`../categories/graph_theory/tree_edge_path_partition_binary_search_greedy_pairing.md`](../categories/graph_theory/tree_edge_path_partition_binary_search_greedy_pairing.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `More Tree Stuff`  
- **Topic (Skill)**: `Union of Two Paths on a Tree`  

---

## 1. Problem Statement & Key Idea
Decompose the edges of a tree with N vertices into a minimum number of paths A, and under this minimum A, minimize the maximum length B of any path.

## 2. Core Observation & Invariant
Every vertex with odd degree must be an endpoint of at least one path, so minimum A is exactly O/2 where O is the count of odd-degree vertices. To minimize B, binary search over B in [1, N]. Root the tree at an arbitrary leaf. In tree DP, each vertex pairs up paths from its children with sums <= B, passing at most one path upwards to its parent. Validity of pairing is monotonic in the chosen upward path length, solved via binary search and two-pointer greedy pairing.

## 3. Step-by-Step Algorithm
1. 1. Compute degree of each vertex; set A = (count of odd degrees) / 2.
2. 2. Root the tree at any leaf vertex and compute BFS traversal order.
3. 3. Binary search B in range [1, N].
4. 4. For a fixed B, run bottom-up tree DP: at vertex u, collect child path lengths. Pad with 0 if even count to ensure an odd number of candidates. Binary search the index r of the path to extend to parent such that the remaining candidates pair up with sum <= B.
5. 5. If all vertices succeed and root path length <= B, B is feasible.
6. 6. Output lexicographically smallest (A, B).

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N \log (\deg))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<vector<int>> adj;
vector<int> deg;
vector<int> parent_node;
vector<int> order;
vector<int> dp;

void bfs(int root) {
    parent_node.assign(N + 1, 0);
    order.clear();
    vector<bool> visited(N + 1, false);
    vector<int> q;
    q.push_back(root);
    visited[root] = true;
    int head = 0;
    while (head < (int)q.size()) {
        int u = q[head++];
        order.push_back(u);
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                parent_node[v] = u;
                q.push_back(v);
            }
        }
    }
}

bool can_pair(const vector<int>& vals, int skip_idx, int B) {
    int m = vals.size();
    int l = 0, r = m - 1;
    while (l < r) {
        if (l == skip_idx) {
            l++;
            continue;
        }
        if (r == skip_idx) {
            r--;
            continue;
        }
        if (vals[l] + vals[r] > B) return false;
        l++;
        r--;
    }
    return true;
}

bool check_B(int root, int B) {
    dp.assign(N + 1, 0);
    for (int i = N - 1; i >= 0; --i) {
        int u = order[i];
        vector<int> child_vals;
        for (int v : adj[u]) {
            if (v != parent_node[u]) {
                if (dp[v] == -1) return false;
                child_vals.push_back(dp[v]);
            }
        }

        if (child_vals.size() % 2 == 0) {
            child_vals.push_back(0);
        }
        sort(child_vals.begin(), child_vals.end());

        int m = child_vals.size();
        int low = 0, high = m - 1;
        int best_r = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (can_pair(child_vals, mid, B)) {
                best_r = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        if (best_r == -1) {
            dp[u] = -1;
            if (u == root) return false;
        } else {
            dp[u] = child_vals[best_r] + 1;
        }
    }

    return dp[root] != -1 && (dp[root] - 1 <= B);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return 0;

    adj.assign(N + 1, vector<int>());
    deg.assign(N + 1, 0);

    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }

    int odd_count = 0;
    int root = 1;
    for (int i = 1; i <= N; ++i) {
        if (deg[i] % 2 != 0) odd_count++;
        if (deg[i] == 1) root = i;
    }

    int A = odd_count / 2;

    bfs(root);

    int low = 1, high = N;
    int best_B = N;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check_B(root, mid)) {
            best_B = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << A << " " << best_B << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
