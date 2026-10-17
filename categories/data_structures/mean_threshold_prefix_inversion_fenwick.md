# Mean Threshold Normalization to Prefix Monotonic Inversion Counting via Fenwick Tree

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Fenwick Tree / Coordinate Compression`  

This workbook contains curated, high-quality competitive programming problems teaching **Mean Threshold Normalization to Prefix Monotonic Inversion Counting via Fenwick Tree**.

---

## Curated Problems

### `[problem:AtCoder-arc075_c]` — Meaningful Mean
- **Rating / Difficulty**: 1979
- **Contest**: `arc075`
- **Analysis**: [`analysis/AtCoder-arc075_c.md`](../../analysis/AtCoder-arc075_c.md)
- **Key Idea**: The condition sum_{i=l}^r A_i / (r - l + 1) >= K is equivalent to sum_{i=l}^r (A_i - K) >= 0. Transform array A into B_i = A_i - K. Compute prefix sums P_i = sum_{j=1}^i B_j with P_0 = 0. The condition becomes P_r - P_{l-1} >= 0, or P_r >= P_{l-1}. Coordinate-compress the N + 1 prefix sum values, and use a Fenwick tree to count pairs i < j with P_i <= P_j in O(N log N).
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
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
    void add(int idx, int val) {
        for (; idx <= n; idx += idx & -idx) tree[idx] += val;
    }
    int query(int idx) {
        int sum = 0;
        for (; idx > 0; idx -= idx & -idx) sum += tree[idx];
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> p(n + 1, 0);
    vector<long long> vals;
    vals.push_back(0);

    for (int i = 0; i < n; ++i) {
        p[i + 1] = p[i] + (a[i] - k);
        vals.push_back(p[i + 1]);
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    auto get_rank = [&](long long val) -> int {
        return lower_bound(vals.begin(), vals.end(), val) - vals.begin() + 1;
    };

    Fenwick ft(vals.size());
    long long ans = 0;

    for (int i = 0; i <= n; ++i) {
        int r = get_rank(p[i]);
        ans += ft.query(r);
        ft.add(r, 1);
    }

    cout << ans << "\n";
    return 0;
}
```
