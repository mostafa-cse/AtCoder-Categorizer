# Layered Graph Counting by BFS Distance Levels

**Domain**: `Combinatorics`  
**Subtopic**: `Graph Counting`  

This workbook contains curated, high-quality competitive programming problems teaching **Layered Graph Counting by BFS Distance Levels**.

---

## Curated Problems

### `[problem:AtCoder-arc044_b]` — 最短路問題
- **Rating / Difficulty**: 1744
- **Contest**: `arc044`
- **Analysis**: [`analysis/AtCoder-arc044_b.md`](../../analysis/AtCoder-arc044_b.md)
- **Key Idea**: The graph naturally decomposes into layers of nodes by distance d = A_i. For a node at layer d, it must have at least one edge to the nodes at layer d - 1, and can have any subset of edges to nodes in its own layer d.
- **Time Complexity**: `O(N + max_d)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    int max_d = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_d = max(max_d, a[i]);
    }

    if (a[0] != 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<long long> c(max_d + 1, 0);
    for (int i = 0; i < n; ++i) {
        c[a[i]]++;
    }

    if (c[0] != 1) {
        cout << 0 << "\n";
        return 0;
    }

    long long ans = 1;
    for (int d = 1; d <= max_d; ++d) {
        if (c[d] == 0) {
            cout << 0 << "\n";
            return 0;
        }

        long long ways_to_prev = (power(2, c[d - 1]) - 1 + MOD) % MOD;
        long long layer_edges = power(ways_to_prev, c[d]);

        long long same_pairs = c[d] * (c[d] - 1) / 2;
        long long same_layer_edges = power(2, same_pairs);

        ans = (ans * layer_edges) % MOD;
        ans = (ans * same_layer_edges) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```
