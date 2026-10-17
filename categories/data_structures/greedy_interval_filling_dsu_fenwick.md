# Greedy Rightmost Interval 1-Filling via DSU Predecessor Jumping and Fenwick Tree

**Domain**: `Data Structures (DS)`  
**Subtopic**: `DSU / Fenwick Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Greedy Rightmost Interval 1-Filling via DSU Predecessor Jumping and Fenwick Tree**.

---

## Curated Problems

### `[problem:AtCoder-abc216_g]` — 01Sequence
- **Rating / Difficulty**: 1963
- **Contest**: `abc216`
- **Analysis**: [`analysis/AtCoder-abc216_g.md`](../../analysis/AtCoder-abc216_g.md)
- **Key Idea**: Sort constraints by R_i ascending. To help future overlapping intervals, any needed 1s should be placed as far right as possible within [L_i, R_i]. Query the number of existing 1s in [L_i, R_i] via a Fenwick Tree. If count < X_i, greedily place 1s at the largest unoccupied indices <= R_i. Finding the largest available 0 position <= x is accelerated to nearly O(1) using a DSU predecessor pointer: parent[x] = find(x - 1) when position x is filled.
- **Time Complexity**: `O(N * alpha(N) + M log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Constraint {
    int l, r, x;
};

int parent_dsu[200005];

int find_set(int v) {
    if (v == parent_dsu[v]) return v;
    return parent_dsu[v] = find_set(parent_dsu[v]);
}

int bit_tree[200005];
int n_size;

void bit_add(int idx, int val) {
    for (; idx <= n_size; idx += idx & -idx) bit_tree[idx] += val;
}

int bit_query(int idx) {
    int sum = 0;
    for (; idx > 0; idx -= idx & -idx) sum += bit_tree[idx];
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    n_size = n;

    vector<Constraint> cons(m);
    for (int i = 0; i < m; ++i) {
        cin >> cons[i].l >> cons[i].r >> cons[i].x;
    }

    sort(cons.begin(), cons.end(), [](const Constraint& a, const Constraint& b) {
        return a.r < b.r;
    });

    for (int i = 0; i <= n; ++i) {
        parent_dsu[i] = i;
    }

    vector<int> ans(n + 1, 0);

    for (const auto& c : cons) {
        int existing = bit_query(c.r) - bit_query(c.l - 1);
        int needed = c.x - existing;

        while (needed > 0) {
            int pos = find_set(c.r);
            if (pos < c.l) break;

            ans[pos] = 1;
            bit_add(pos, 1);
            parent_dsu[pos] = find_set(pos - 1);
            needed--;
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```
