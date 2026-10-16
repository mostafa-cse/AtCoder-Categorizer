# Invariant Value Coordinate Assignment + Fenwick Inversion Counting

**Domain**: `Data Structures`  
**Subtopic**: `Fenwick Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Invariant Value Coordinate Assignment + Fenwick Inversion Counting**.

---

## Curated Problems

### `[problem:AtCoder-arc120_c]` — Swaps 2
- **Rating / Difficulty**: 1478
- **Contest**: `arc120`
- **Analysis**: [`analysis/AtCoder-arc120_c.md`](../../analysis/AtCoder-arc120_c.md)
- **Key Idea**: Notice the invariant: under swapping A[i] and A[i+1], their new values become A'[i] = A[i+1] - 1 and A'[i+1] = A[i] + 1. Thus, A[i] + i is an INVARIANT under adjacent transpositions!
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

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

    vector<long long> a(n), b(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a[i] += i;
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
        b[i] += i;
    }

    vector<long long> sa = a, sb = b;
    sort(sa.begin(), sa.end());
    sort(sb.begin(), sb.end());

    if (sa != sb) {
        cout << -1 << "\n";
        return 0;
    }

    map<long long, queue<int>> pos;
    for (int i = 0; i < n; ++i) {
        pos[b[i]].push(i + 1);
    }

    vector<int> p(n);
    for (int i = 0; i < n; ++i) {
        p[i] = pos[a[i]].front();
        pos[a[i]].pop();
    }

    Fenwick bit(n);
    long long inversions = 0;
    for (int i = 0; i < n; ++i) {
        inversions += i - bit.query(p[i]);
        bit.add(p[i], 1);
    }

    cout << inversions << "\n";
    return 0;
}
```
