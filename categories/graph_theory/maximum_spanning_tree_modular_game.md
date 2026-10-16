# Maximum Spanning Tree on Complete Graph with Modular Exponentiation

**Domain**: `Graph Theory`  
**Subtopic**: `Minimum Spanning Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Maximum Spanning Tree on Complete Graph with Modular Exponentiation**.

---

## Curated Problems

### `[problem:AtCoder-abc282_e]` — Choose Two and Eat One
- **Rating / Difficulty**: 1604
- **Contest**: `abc282`
- **Analysis**: [`analysis/AtCoder-abc282_e.md`](../../analysis/AtCoder-abc282_e.md)
- **Key Idea**: The process of eating one of two balls corresponds exactly to building a spanning tree on the N balls! Total points collected is the sum of edge weights of the tree.
- **Time Complexity**: `O(N^2 log M + N^2 log N)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

long long power(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return res;
}

struct Edge {
    int u, v;
    long long weight;
    bool operator<(const Edge& other) const {
        return weight > other.weight; // Descending for Max Spanning Tree
    }
};

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int u) {
        return parent[u] == u ? u : parent[u] = find(parent[u]);
    }
    bool unite(int u, int v) {
        int ru = find(u), rv = find(v);
        if (ru == rv) return false;
        parent[ru] = rv;
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<Edge> edges;
    edges.reserve(n * (n - 1) / 2);

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            long long w = (power(a[i], a[j], m) + power(a[j], a[i], m)) % m;
            edges.push_back({i, j, w});
        }
    }

    sort(edges.begin(), edges.end());

    DSU dsu(n);
    long long max_score = 0;
    int edges_used = 0;

    for (const auto& e : edges) {
        if (dsu.unite(e.u, e.v)) {
            max_score += e.weight;
            if (++edges_used == n - 1) break;
        }
    }

    cout << max_score << "\n";
    return 0;
}
```
