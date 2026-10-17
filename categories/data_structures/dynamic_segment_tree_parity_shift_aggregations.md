# Dynamic Segment Tree with Parity-Dependent Index Shift Aggregations

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Segment Tree / Fenwick Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Dynamic Segment Tree with Parity-Dependent Index Shift Aggregations**.

---

## Curated Problems

### `[problem:AtCoder-abc403_g]` — Odd Position Sum Query
- **Rating / Difficulty**: 2028
- **Contest**: `abc403`
- **Analysis**: [`analysis/AtCoder-abc403_g.md`](../../analysis/AtCoder-abc403_g.md)
- **Key Idea**: In a sorted order-statistic structure (Dynamic Segment Tree or Treap), each node represents a range of values and maintains: subtree size sz, sum of odd-indexed elements sum_odd, and sum of even-indexed elements sum_even. When merging left and right children: if left.sz is even, right child's elements retain their parity: combined.sum_odd = left.sum_odd + right.sum_odd. If left.sz is odd, right child's elements flip parity: combined.sum_odd = left.sum_odd + right.sum_even. Dynamic Segment Tree on coordinate range [1, 10^9] processes each insertion in O(log(max X)).
- **Time Complexity**: `O(Q log(max X))`
- **Space Complexity**: `O(Q log(max X))`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX_VAL = 1000000000;

struct Node {
    int sz;
    long long sum_odd;
    long long sum_even;
    int left, right;
    Node() : sz(0), sum_odd(0), sum_even(0), left(0), right(0) {}
};

vector<Node> tree;

int new_node() {
    tree.emplace_back();
    return (int)tree.size() - 1;
}

void pull(int u) {
    int l = tree[u].left;
    int r = tree[u].right;

    int l_sz = (l ? tree[l].sz : 0);
    long long l_odd = (l ? tree[l].sum_odd : 0);
    long long l_even = (l ? tree[l].sum_even : 0);

    int r_sz = (r ? tree[r].sz : 0);
    long long r_odd = (r ? tree[r].sum_odd : 0);
    long long r_even = (r ? tree[r].sum_even : 0);

    tree[u].sz = l_sz + r_sz;

    if (l_sz % 2 == 0) {
        tree[u].sum_odd = l_odd + r_odd;
        tree[u].sum_even = l_even + r_even;
    } else {
        tree[u].sum_odd = l_odd + r_even;
        tree[u].sum_even = l_even + r_odd;
    }
}

void insert_val(int& u, int l, int r, int val) {
    if (!u) u = new_node();

    if (l == r) {
        tree[u].sz++;
        if (tree[u].sz % 2 == 1) {
            tree[u].sum_odd += val;
        } else {
            tree[u].sum_even += val;
        }
        return;
    }

    int mid = l + (r - l) / 2;
    if (val <= mid) {
        insert_val(tree[u].left, l, mid, val);
    } else {
        insert_val(tree[u].right, mid + 1, r, val);
    }
    pull(u);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    tree.reserve(q * 32);
    tree.emplace_back(); // 1-based indexing for dummy node 0
    int root = 0;

    long long z = 0;

    for (int i = 0; i < q; ++i) {
        long long y;
        cin >> y;
        long long x = ((y + z) % MAX_VAL) + 1;

        insert_val(root, 1, MAX_VAL, (int)x);
        z = tree[root].sum_odd;
        cout << z << "\n";
    }

    return 0;
}
```
