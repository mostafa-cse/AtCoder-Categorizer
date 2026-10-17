# Principle of Inclusion-Exclusion on Tree Path Cover Constraints via Bitmask Edge Unions

**Domain**: `Combinatorics`  
**Subtopic**: `Inclusion-Exclusion`  

This workbook contains curated, high-quality competitive programming problems teaching **Principle of Inclusion-Exclusion on Tree Path Cover Constraints via Bitmask Edge Unions**.

---

## Curated Problems

### `[problem:AtCoder-abc152_f]` — Tree and Constraints
- **Rating / Difficulty**: 1965
- **Contest**: `abc152`
- **Analysis**: [`analysis/AtCoder-abc152_f.md`](../../analysis/AtCoder-abc152_f.md)
- **Key Idea**: M <= 20 directly suggests Principle of Inclusion-Exclusion (PIE). Let violation condition i be: all edges on path (u_i, v_i) are white. For a subset of constraints S in {0..M-1}, all edges on paths in S must be colored white. Compute the path edge set for each constraint as a 64-bit integer mask. For any subset S, the union of edges is the bitwise OR of path masks. If S forces K = popcount(mask) edges to be white, the remaining (N - 1 - K) edges have 2 choices each. By PIE, sum_{S} (-1)^{|S|} 2^{N - 1 - popcount(union_mask)} gives the exact answer.
- **Time Complexity**: `O(N + M + M * 2^M)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

struct Edge {
    int to;
    int id;
};

int n, m;
vector<vector<Edge>> adj;
vector<uint64_t> path_mask;

bool get_path(int u, int target, int parent, uint64_t& mask) {
    if (u == target) return true;
    for (const auto& e : adj[u]) {
        if (e.to == parent) continue;
        mask |= (1ULL << e.id);
        if (get_path(e.to, target, u, mask)) return true;
        mask &= ~(1ULL << e.id);
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<Edge>());
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back({v, i});
        adj[v].push_back({u, i});
    }

    cin >> m;
    path_mask.assign(m, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        uint64_t mask = 0;
        get_path(u, v, -1, mask);
        path_mask[i] = mask;
    }

    long long total_valid = 0;
    int total_subsets = 1 << m;

    for (int mask = 0; mask < total_subsets; ++mask) {
        uint64_t union_edges = 0;
        int bits = 0;
        for (int i = 0; i < m; ++i) {
            if ((mask >> i) & 1) {
                union_edges |= path_mask[i];
                bits++;
            }
        }

        int forced_white = __builtin_popcountll(union_edges);
        long long ways = 1LL << ((n - 1) - forced_white);

        if (bits % 2 == 1) {
            total_valid -= ways;
        } else {
            total_valid += ways;
        }
    }

    cout << total_valid << "\n";
    return 0;
}
```
