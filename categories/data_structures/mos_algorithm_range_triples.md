# Mo's Algorithm for Range Triples C(c, 3)

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Mo's Algorithm`  

This workbook contains curated, high-quality competitive programming problems teaching **Mo's Algorithm for Range Triples C(c, 3)**.

---

## Curated Problems

### `[problem:AtCoder-abc293_g]` — Triple Index
- **Rating / Difficulty**: 1753
- **Contest**: `abc293`
- **Analysis**: [`analysis/AtCoder-abc293_g.md`](../../analysis/AtCoder-abc293_g.md)
- **Key Idea**: For a value occurring c times in a range, the number of triples is C(c, 3) = c * (c - 1) * (c - 2) / 6. Using Mo's Algorithm with block size B = N / sqrt(Q), update the triple count in O(1) when extending or shrinking the range.
- **Time Complexity**: `O((N + Q) * sqrt(N))`
- **Space Complexity**: `O(N + Q + max_val)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Query {
    int l, r, id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].l >> queries[i].r;
        queries[i].id = i;
    }

    int block_size = max(1, (int)(n / sqrt(q)));
    sort(queries.begin(), queries.end(), [&](const Query& x, const Query& y) {
        int b1 = x.l / block_size;
        int b2 = y.l / block_size;
        if (b1 != b2) return b1 < b2;
        return (b1 & 1) ? (x.r < y.r) : (x.r > y.r);
    });

    vector<long long> cnt(200005, 0);
    vector<long long> ans(q);
    long long cur_triples = 0;

    auto add = [&](int val) {
        cur_triples += cnt[val] * (cnt[val] - 1) / 2;
        cnt[val]++;
    };

    auto remove = [&](int val) {
        cnt[val]--;
        cur_triples -= cnt[val] * (cnt[val] - 1) / 2;
    };

    int cur_l = 1, cur_r = 0;
    for (auto& qry : queries) {
        while (cur_l > qry.l) add(a[--cur_l]);
        while (cur_r < qry.r) add(a[++cur_r]);
        while (cur_l < qry.l) remove(a[cur_l++]);
        while (cur_r > qry.r) remove(a[cur_r--]);
        ans[qry.id] = cur_triples;
    }

    for (int i = 0; i < q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```
