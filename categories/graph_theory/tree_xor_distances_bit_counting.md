# Tree XOR Distances Bit-by-Bit Counting via Root DFS

**Domain**: `Graph Theory`  
**Subtopic**: `Trees`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree XOR Distances Bit-by-Bit Counting via Root DFS**.

---

## Curated Problems

### `[problem:AtCoder-abc201_e]` — Xor Distances
- **Rating / Difficulty**: 1694
- **Contest**: `abc201`
- **Analysis**: [`analysis/AtCoder-abc201_e.md`](../../analysis/AtCoder-abc201_e.md)
- **Key Idea**: In any tree, the path from u to v can be routed through an arbitrary root (e.g. 1): dist(u, v) = dist(root, u) ^ dist(root, v), because edges on the common path to the LCA cancel out!
- **Time Complexity**: `O(60 * N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

struct Edge {
    int to;
    long long w;
};

vector<vector<Edge>> adj;
vector<long long> xor_dist;

void dfs(int u, int p, long long d) {
    xor_dist[u] = d;
    for (const auto& e : adj[u]) {
        if (e.to != p) {
            dfs(e.to, u, d ^ e.w);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    adj.resize(n + 1);
    xor_dist.resize(n + 1, 0);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    dfs(1, 0, 0);

    long long ans = 0;

    for (int b = 0; b < 60; ++b) {
        long long cnt1 = 0;
        for (int i = 1; i <= n; ++i) {
            if ((xor_dist[i] >> b) & 1) {
                cnt1++;
            }
        }
        long long cnt0 = n - cnt1;
        long long pairs = (cnt1 * cnt0) % MOD;
        long long bit_val = ((1LL << b) % MOD);
        ans = (ans + pairs * bit_val) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```
