# Binary Search on Answer with +1/-1 Reduction and Fenwick Tree Prefix Sum Inversion Counting

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Segment Tree / Fenwick Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Search on Answer with +1/-1 Reduction and Fenwick Tree Prefix Sum Inversion Counting**.

---

## Curated Problems

### `[problem:AtCoder-arc101_b]` — Median of Medians
- **Rating / Difficulty**: 2073
- **Contest**: `abc107`
- **Analysis**: [`analysis/AtCoder-arc101_b.md`](../../analysis/AtCoder-arc101_b.md)
- **Key Idea**: Binary search on the answer X. The median of a subsegment A[l..r] is >= X if and only if at least half of its elements are >= X. Replacing each element with b_i = +1 if A_i >= X else -1, the median condition becomes sum_{k=l}^r b_k > 0, which is equivalent to pref[r] > pref[l-1]. Counting such pairs (l-1, r) reduces to counting inversions in the prefix sum array, solvable in O(N log N) using a Fenwick tree. If the number of subsegments with median >= X is >= (N(N+1)/2) / 2 + 1, then the median of medians is >= X.
- **Time Complexity**: `O(N log N log(max A))`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long total_intervals = 1LL * n * (n + 1) / 2;
    long long req = total_intervals / 2 + 1;

    auto check = [&](int x) -> bool {
        int offset = n + 1;
        Fenwick bit(2 * n + 2);
        bit.add(0 + offset, 1);

        long long count_valid = 0;
        int cur_pref = 0;

        for (int i = 0; i < n; ++i) {
            cur_pref += (a[i] >= x ? 1 : -1);
            count_valid += bit.query(cur_pref - 1 + offset);
            bit.add(cur_pref + offset, 1);
        }

        return count_valid >= req;
    };

    int low = 1, high = 1e9, ans = 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
