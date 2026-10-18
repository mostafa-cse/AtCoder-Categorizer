# Problem Analysis: AtCoder-keyence2019_e — E - Connecting Cities

**Problem ID**: `AtCoder-keyence2019_e`  
**Contest**: `keyence2019`  
**Rating / Difficulty**: 2623  
**URL**: https://atcoder.jp/contests/keyence2019/tasks/keyence2019_e  
**VJudge Tag**: `[problem:AtCoder-keyence2019_e]`  
**Category File**: [`../categories/graph_theory/connecting_cities_boruvka_mst.md`](../categories/graph_theory/connecting_cities_boruvka_mst.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Minimum Spanning Tree (MST)`  
- **Topic (Skill)**: `Boruvka's Algorithm`  

---

## 1. Problem Statement & Key Idea
In a complete graph of N cities on a line, the edge weight between i < j is (A_i - i D) + (A_j + j D). Find the minimum spanning tree weight.

## 2. Core Observation & Invariant
Boruvka's algorithm runs in at most ceil(log_2 N) contraction rounds. In each round, every component seeks its cheapest outgoing edge. Because the edge weight separates into (A_i - i D) + (A_j + j D) for i < j, maintaining the top 2 components with minimum A_i - i D in a prefix sweep and minimum A_j + j D in a suffix sweep identifies the cheapest outgoing edge for all components in O(N) time.

## 3. Step-by-Step Algorithm
1. Initialize DSU with N single-vertex components.
2. Repeat while number of components > 1:
3. Perform forward sweep 1 to N, maintaining top 2 components with min A_i - i D.
4. Perform backward sweep N to 1, maintaining top 2 components with min A_j + j D.
5. For each node, select the minimum outgoing edge to a different component.
6. Add all selected edges into DSU and accumulate MST weight.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

using ll = long long;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        for (int i = 0; i < n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            return true;
        }
        return false;
    }
};

const ll INF = 4e18;

struct BestEdge {
    ll cost;
    int u, v;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    ll D;
    if (!(cin >> N >> D)) return 0;

    vector<ll> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    DSU dsu(N);
    int num_components = N;
    ll total_cost = 0;

    while (num_components > 1) {
        vector<BestEdge> best(N, {INF, -1, -1});

        // Prefix sweep: finding best left neighbor i < k
        ll b1_val = INF; int b1_u = -1, b1_c = -1;
        ll b2_val = INF; int b2_u = -1, b2_c = -1;

        for (int k = 0; k < N; ++k) {
            int c_k = dsu.find(k);
            int cand_u = -1;
            ll cand_val = INF;

            if (b1_c != -1 && b1_c != c_k) {
                cand_u = b1_u;
                cand_val = b1_val;
            } else if (b2_c != -1 && b2_c != c_k) {
                cand_u = b2_u;
                cand_val = b2_val;
            }

            if (cand_u != -1) {
                ll cost = (A[k] + (ll)k * D) + cand_val;
                if (cost < best[c_k].cost) {
                    best[c_k] = {cost, k, cand_u};
                }
            }

            ll val_k = A[k] - (ll)k * D;
            if (b1_c == c_k) {
                if (val_k < b1_val) {
                    b1_val = val_k;
                    b1_u = k;
                }
            } else if (b2_c == c_k) {
                if (val_k < b2_val) {
                    b2_val = val_k;
                    b2_u = k;
                    if (b2_val < b1_val) {
                        swap(b1_val, b2_val);
                        swap(b1_u, b2_u);
                        swap(b1_c, b2_c);
                    }
                }
            } else {
                if (val_k < b1_val) {
                    b2_val = b1_val; b2_u = b1_u; b2_c = b1_c;
                    b1_val = val_k; b1_u = k; b1_c = c_k;
                } else if (val_k < b2_val) {
                    b2_val = val_k; b2_u = k; b2_c = c_k;
                }
            }
        }

        // Suffix sweep: finding best right neighbor j > k
        b1_val = INF; b1_u = -1; b1_c = -1;
        b2_val = INF; b2_u = -1; b2_c = -1;

        for (int k = N - 1; k >= 0; --k) {
            int c_k = dsu.find(k);
            int cand_u = -1;
            ll cand_val = INF;

            if (b1_c != -1 && b1_c != c_k) {
                cand_u = b1_u;
                cand_val = b1_val;
            } else if (b2_c != -1 && b2_c != c_k) {
                cand_u = b2_u;
                cand_val = b2_val;
            }

            if (cand_u != -1) {
                ll cost = (A[k] - (ll)k * D) + cand_val;
                if (cost < best[c_k].cost) {
                    best[c_k] = {cost, k, cand_u};
                }
            }

            ll val_k = A[k] + (ll)k * D;
            if (b1_c == c_k) {
                if (val_k < b1_val) {
                    b1_val = val_k;
                    b1_u = k;
                }
            } else if (b2_c == c_k) {
                if (val_k < b2_val) {
                    b2_val = val_k;
                    b2_u = k;
                    if (b2_val < b1_val) {
                        swap(b1_val, b2_val);
                        swap(b1_u, b2_u);
                        swap(b1_c, b2_c);
                    }
                }
            } else {
                if (val_k < b1_val) {
                    b2_val = b1_val; b2_u = b1_u; b2_c = b1_c;
                    b1_val = val_k; b1_u = k; b1_c = c_k;
                } else if (val_k < b2_val) {
                    b2_val = val_k; b2_u = k; b2_c = c_k;
                }
            }
        }

        bool merged = false;
        for (int i = 0; i < N; ++i) {
            if (best[i].cost < INF) {
                if (dsu.unite(best[i].u, best[i].v)) {
                    total_cost += best[i].cost;
                    num_components--;
                    merged = true;
                }
            }
        }
        if (!merged) break;
    }

    cout << total_cost << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
