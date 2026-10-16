# Kruskal MST on Ring via Modular GCD Component Reduction

**Domain**: `Graph Theory`  
**Subtopic**: `Minimum Spanning Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Kruskal MST on Ring via Modular GCD Component Reduction**.

---

## Curated Problems

### `[problem:AtCoder-abc210_e]` — Ring MST
- **Rating / Difficulty**: 1618
- **Contest**: `abc210`
- **Analysis**: [`analysis/AtCoder-abc210_e.md`](../../analysis/AtCoder-abc210_e.md)
- **Key Idea**: Kruskal's greedy paradigm! Sort operations by cost C_j ascending. Adding ring edges of step A_j reduces the number of connected components from current g to gcd(g, A_j).
- **Time Complexity**: `O(M log M)`
- **Space Complexity**: `O(M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

long long gcd_ll(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

struct Op {
    long long a, c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int m;
    if (!(cin >> n >> m)) return 0;

    vector<Op> ops(m);
    for (int i = 0; i < m; ++i) {
        cin >> ops[i].a >> ops[i].c;
    }

    sort(ops.begin(), ops.end(), [](const Op& x, const Op& y) {
        return x.c < y.c;
    });

    long long g = n;
    long long total_cost = 0;

    for (const auto& op : ops) {
        long long g_next = gcd_ll(g, op.a);
        if (g_next < g) {
            total_cost += (g - g_next) * op.c;
            g = g_next;
        }
    }

    if (g == 1) {
        cout << total_cost << "\n";
    } else {
        cout << -1 << "\n";
    }

    return 0;
}
```
