# Permutation Construction with Value Upper Bound Counting

**Domain**: `Basics`  
**Subtopic**: `Permutations`  

This workbook contains curated, high-quality competitive programming problems teaching **Permutation Construction with Value Upper Bound Counting**.

---

## Curated Problems

### `[problem:AtCoder-arc176_c]` — Max Permutation
- **Rating / Difficulty**: 2056
- **Contest**: `arc176`
- **Analysis**: [`analysis/AtCoder-arc176_c.md`](../../analysis/AtCoder-arc176_c.md)
- **Key Idea**: Each condition imposes upper bounds P_{A_i} <= C_i and P_{B_i} <= C_i. For each vertex v, define X_v = min_{v in e} C_e. We determine which position takes value k in descending order k = N, N-1, ..., 1. If multiple edges have weight k, they must all share a unique common vertex v_star, forcing P_{v_star} = k. If exactly one edge (u, v) has weight k, if both endpoints are undecided and valid, either can be chosen (factor of 2). If zero edges have weight k, we choose any available undecided vertex with X_j >= k. This exact greedy counting runs in O(N + M).
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

struct Edge {
    int u, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> X(n + 1, n);
    vector<vector<Edge>> by_c(n + 1);

    for (int i = 0; i < m; ++i) {
        int u, v, c;
        cin >> u >> v >> c;
        X[u] = min(X[u], c);
        X[v] = min(X[v], c);
        by_c[c].push_back({u, v});
    }

    vector<int> count_X(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        count_X[X[i]]++;
    }

    vector<bool> decided(n + 1, false);
    long long ans = 1;
    int avail = 0;

    for (int k = n; k >= 1; --k) {
        avail += count_X[k];
        auto& edges_k = by_c[k];

        if (edges_k.size() >= 2) {
            int u0 = edges_k[0].u, v0 = edges_k[0].v;
            vector<int> cand = {u0, v0};
            for (size_t i = 1; i < edges_k.size(); ++i) {
                int u = edges_k[i].u, v = edges_k[i].v;
                vector<int> next_cand;
                for (int x : cand) {
                    if (x == u || x == v) next_cand.push_back(x);
                }
                cand = next_cand;
            }
            if (cand.size() != 1) {
                cout << 0 << "\n";
                return 0;
            }
            int v_star = cand[0];
            if (X[v_star] < k || decided[v_star]) {
                cout << 0 << "\n";
                return 0;
            }
            decided[v_star] = true;
            avail--;
        } else if (edges_k.size() == 1) {
            int u = edges_k[0].u, v = edges_k[0].v;
            if (decided[u] && decided[v]) {
                cout << 0 << "\n";
                return 0;
            } else if (decided[u]) {
                if (X[v] < k) { cout << 0 << "\n"; return 0; }
                decided[v] = true;
                avail--;
            } else if (decided[v]) {
                if (X[u] < k) { cout << 0 << "\n"; return 0; }
                decided[u] = true;
                avail--;
            } else {
                bool ok_u = (X[u] >= k);
                bool ok_v = (X[v] >= k);
                if (ok_u && ok_v) {
                    ans = (ans * 2) % MOD;
                    decided[u] = true;
                    avail--;
                } else if (ok_u) {
                    decided[u] = true;
                    avail--;
                } else if (ok_v) {
                    decided[v] = true;
                    avail--;
                } else {
                    cout << 0 << "\n";
                    return 0;
                }
            }
        } else {
            if (avail <= 0) {
                cout << 0 << "\n";
                return 0;
            }
            ans = (ans * avail) % MOD;
            avail--;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
