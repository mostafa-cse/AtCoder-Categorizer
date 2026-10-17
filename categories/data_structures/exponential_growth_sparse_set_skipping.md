# Exponential Growth Sparse Set Skipping with Fenwick Range Sum

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Fenwick Tree + Set Skipping`  

This workbook contains curated, high-quality competitive programming problems teaching **Exponential Growth Sparse Set Skipping with Fenwick Range Sum**.

---

## Curated Problems

### `[problem:AtCoder-abc368_g]` — Add and Multiply Queries
- **Rating / Difficulty**: 1841
- **Contest**: `abc368`
- **Analysis**: [`analysis/AtCoder-abc368_g.md`](../../analysis/AtCoder-abc368_g.md)
- **Key Idea**: If B_i = 1, multiplying does nothing so we always add A_i. If B_i >= 2, multiplying doubles v. Since v <= 10^{18}, at most ~60 multiplications by B_i >= 2 can occur. Maintain indices where B_i >= 2 in a std::set.
- **Time Complexity**: `O((Q * 60 + N) log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

struct Fenwick {
    int sz;
    vector<long long> tree;
    Fenwick(int n) : sz(n), tree(n + 1, 0) {}
    void add(int i, long long delta) {
        for (; i <= sz; i += i & -i) tree[i] += delta;
    }
    long long query(int i) {
        long long sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
    long long query(int l, int r) {
        if (l > r) return 0;
        return query(r) - query(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1), b(n + 1);
    Fenwick ft(n);
    set<int> big_b;

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        ft.add(i, a[i]);
    }
    for (int i = 1; i <= n; ++i) {
        cin >> b[i];
        if (b[i] >= 2) big_b.insert(i);
    }

    int q;
    cin >> q;
    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int i;
            long long x;
            cin >> i >> x;
            ft.add(i, x - a[i]);
            a[i] = x;
        } else if (type == 2) {
            int i;
            long long x;
            cin >> i >> x;
            b[i] = x;
            if (b[i] >= 2) big_b.insert(i);
            else big_b.erase(i);
        } else {
            int l, r;
            cin >> l >> r;
            long long v = 1;
            int cur = l;

            while (cur <= r) {
                auto it = big_b.lower_bound(cur);
                if (it == big_b.end() || *it > r) {
                    v += ft.query(cur, r);
                    break;
                }
                int idx = *it;
                v += ft.query(cur, idx - 1);
                v = max(v + a[idx], v * b[idx]);
                cur = idx + 1;
            }
            cout << v << "\n";
        }
    }

    return 0;
}
```
