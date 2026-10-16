# Offline Range Distinct Elements Query using Fenwick Tree

**Domain**: `Data Structures`  
**Subtopic**: `Fenwick Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Offline Range Distinct Elements Query using Fenwick Tree**.

---

## Curated Problems

### `[problem:AtCoder-abc174_f]` — Range Set Query
- **Rating / Difficulty**: 1495
- **Contest**: `abc174`
- **Analysis**: [`analysis/AtCoder-abc174_f.md`](../../analysis/AtCoder-abc174_f.md)
- **Key Idea**: Process queries offline sorted by right endpoint r. Maintain a Fenwick tree where position p holds +1 iff p is the rightmost occurrence of value C[p] up to the current index r.
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N + Q)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    int query(int i) const {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

struct Query {
    int l, r, id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> c(n + 1);
    for (int i = 1; i <= n; ++i) cin >> c[i];

    vector<vector<pair<int, int>>> queries_at(n + 1);
    for (int i = 0; i < q; ++i) {
        int l, r;
        cin >> l >> r;
        queries_at[r].push_back({l, i});
    }

    vector<int> last_pos(n + 1, 0);
    Fenwick bit(n);
    vector<int> ans(q);

    for (int r = 1; r <= n; ++r) {
        if (last_pos[c[r]] > 0) {
            bit.add(last_pos[c[r]], -1);
        }
        bit.add(r, 1);
        last_pos[c[r]] = r;

        for (const auto& qry : queries_at[r]) {
            int l = qry.first;
            int id = qry.second;
            ans[id] = bit.query(r) - bit.query(l - 1);
        }
    }

    for (int i = 0; i < q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```
