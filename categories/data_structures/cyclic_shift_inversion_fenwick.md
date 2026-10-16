# Cyclic Shift Inversion Update via Fenwick Tree

**Domain**: `Data Structures`  
**Subtopic**: `Fenwick Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Cyclic Shift Inversion Update via Fenwick Tree**.

---

## Curated Problems

### [problem:AtCoder-abc190_f] — Shift and Inversions
- **Contest**: `abc190`
- **Rating / Difficulty**: 1321
- **Specific Skill**: Cyclic Shift Inversion Update via Fenwick Tree
- **Individual Analysis**: [`../../analysis/AtCoder-abc190_f.md`](../../analysis/AtCoder-abc190_f.md)
- **Problem Statement Summary**: Given a permutation a_0, ..., a_{N-1} of 0..N-1. For each k from 0 to N-1, find the inversion number of the cyclically shifted sequence b_i = a_{(i + k) % N}.
- **Core Insight**: When shifting the first element a_k to the back of the array: (1) a_k was previously before all other elements, forming a_k inversions with the elements smaller than a_k; (2) a_k is now placed after all other elements, forming (N - 1 - a_k) new inversions with elements larger than a_k! Thus, the inversion count updates by: inv_{k+1} = inv_k - a_k + (N - 1 - a_k).
- **Complexity**: Time: `O(N log N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, int val) {
        for (; i <= n; i += i & -i) tree[i] += val;
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
    Fenwick bit(n);
    long long inv = 0;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        inv += i - bit.query(a[i] + 1);
        bit.add(a[i] + 1, 1);
    }

    cout << inv << "\n";
    for (int k = 0; k < n - 1; ++k) {
        inv += (n - 1 - a[k]) - a[k];
        cout << inv << "\n";
    }

    return 0;
}
```
