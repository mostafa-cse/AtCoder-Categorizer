# Dual Graph Joint Connectivity Counting via Component Root Hash Pairing

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Disjoint Set Union (DSU)`  

This workbook contains curated, high-quality competitive programming problems teaching **Dual Graph Joint Connectivity Counting via Component Root Hash Pairing**.

---

## Curated Problems

### `[problem:AtCoder-arc065_b]` — Connectivity
- **Rating / Difficulty**: 1996
- **Contest**: `arc065`
- **Analysis**: [`analysis/AtCoder-arc065_b.md`](../../analysis/AtCoder-arc065_b.md)
- **Key Idea**: Build two separate DSU structures: one for the road network and one for the railway network. City i belongs to road component root R_i = find_road(i) and railway component root T_i = find_rail(i). Two cities p, q are jointly connected iff R_p == R_q AND T_p == T_q. Thus, joint connectivity is an equivalence relation where each city's equivalence class is uniquely defined by the pair of canonical roots (R_i, T_i). Count frequencies of each pair using a hash map or sorting in O(N log N).
- **Time Complexity**: `O((N + K + L) * alpha(N) + N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <map>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int v) {
        if (v == parent[v]) return v;
        return parent[v] = find(parent[v]);
    }
    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) parent[b] = a;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, l;
    if (!(cin >> n >> k >> l)) return 0;

    DSU road(n), rail(n);

    for (int i = 0; i < k; ++i) {
        int u, v;
        cin >> u >> v;
        road.unite(u, v);
    }

    for (int i = 0; i < l; ++i) {
        int u, v;
        cin >> u >> v;
        rail.unite(u, v);
    }

    map<pair<int, int>, int> freq;
    vector<pair<int, int>> sig(n + 1);

    for (int i = 1; i <= n; ++i) {
        sig[i] = {road.find(i), rail.find(i)};
        freq[sig[i]]++;
    }

    for (int i = 1; i <= n; ++i) {
        cout << freq[sig[i]] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```
