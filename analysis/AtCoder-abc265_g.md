# Problem Analysis: AtCoder-abc265_g — G. 012 Inversion

**Problem ID**: `AtCoder-abc265_g`  
**Contest**: `abc265`  
**Rating / Difficulty**: 2436  
**URL**: https://atcoder.jp/contests/abc265/tasks/abc265_g  
**VJudge Tag**: `[problem:AtCoder-abc265_g]`  
**Category File**: [`../categories/data_structures/012_inversion_lazy_segment_tree.md`](../categories/data_structures/012_inversion_lazy_segment_tree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree with Lazy Propagation`  

---

## 1. Problem Statement & Key Idea
Maintain a sequence of values in $\{0, 1, 2\}$ under range substitutions $0 \to S, 1 \to T, 2 \to U$ and range inversion queries. A Lazy Segment Tree maintains counts of 0s, 1s, and 2s, along with the 9 cross-inversion pair counts $inv[x][y]$. Lazy tags represent mapping functions $P: \{0, 1, 2\} \to \{0, 1, 2\}$, which compose via function substitution.

## 2. Core Observation & Invariant
Inversion count in any range is $inv[1][0] + inv[2][0] + inv[2][1]$. When two segments $L$ and $R$ merge, cross-pairs contribute $L.cnt[x] \times R.cnt[y]$. Applying mapping $P$ permutes the counts and cross-inversion matrices in $O(3^2) = O(1)$ time.

## 3. Step-by-Step Algorithm
1. 1. Construct a segment tree where each node stores $cnt[3]$ and $inv[3][3]$, with lazy mapping tag initialized to identity $(0, 1, 2)$.
2. 2. Define node merge: $res.inv[x][y] = L.inv[x][y] + R.inv[x][y] + L.cnt[x] \cdot R.cnt[y]$.
3. 3. Define tag application: $new\_cnt[P[x]] += cnt[x]$, $new\_inv[P[x]][P[y]] += inv[x][y]$, and tag composition $new\_tag[x] = tag_{new}[tag_{old}[x]]$.
4. 4. For query 1: range query to retrieve root node for $[L, R]$ and output $inv[1][0] + inv[2][0] + inv[2][1]$.
5. 5. For query 2: range update with tag $(S, T, U)$.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <array>

using namespace std;

struct Node {
    array<int, 3> cnt;
    array<array<long long, 3>, 3> inv;
    array<int, 3> tag; // permutation tag

    Node() {
        cnt = {0, 0, 0};
        for (int i = 0; i < 3; ++i)
            for (int j = 0; j < 3; ++j) inv[i][j] = 0;
        tag = {0, 1, 2};
    }
};

int N, Q;
vector<int> A;
vector<Node> tree;

Node merge(const Node& L, const Node& R) {
    Node res;
    for (int i = 0; i < 3; ++i) {
        res.cnt[i] = L.cnt[i] + R.cnt[i];
    }
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            res.inv[i][j] = L.inv[i][j] + R.inv[i][j] + 1LL * L.cnt[i] * R.cnt[j];
        }
    }
    return res;
}

void apply_tag(int u, const array<int, 3>& t) {
    array<int, 3> new_cnt = {0, 0, 0};
    array<array<long long, 3>, 3> new_inv;
    for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 3; ++j) new_inv[i][j] = 0;

    for (int i = 0; i < 3; ++i) {
        new_cnt[t[i]] += tree[u].cnt[i];
    }
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            new_inv[t[i]][t[j]] += tree[u].inv[i][j];
        }
    }

    tree[u].cnt = new_cnt;
    tree[u].inv = new_inv;

    array<int, 3> new_tag;
    for (int i = 0; i < 3; ++i) {
        new_tag[i] = t[tree[u].tag[i]];
    }
    tree[u].tag = new_tag;
}

void push(int u) {
    if (tree[u].tag != array<int, 3>{0, 1, 2}) {
        apply_tag(2 * u, tree[u].tag);
        apply_tag(2 * u + 1, tree[u].tag);
        tree[u].tag = {0, 1, 2};
    }
}

void build(int u, int l, int r) {
    if (l == r) {
        tree[u].cnt[A[l]] = 1;
        return;
    }
    int mid = (l + r) / 2;
    build(2 * u, l, mid);
    build(2 * u + 1, mid + 1, r);
    tree[u] = merge(tree[2 * u], tree[2 * u + 1]);
}

void update(int u, int l, int r, int ql, int qr, const array<int, 3>& t) {
    if (ql <= l && r <= qr) {
        apply_tag(u, t);
        return;
    }
    push(u);
    int mid = (l + r) / 2;
    if (ql <= mid) update(2 * u, l, mid, ql, qr, t);
    if (qr > mid) update(2 * u + 1, mid + 1, r, ql, qr, t);
    tree[u] = merge(tree[2 * u], tree[2 * u + 1]);
}

Node query(int u, int l, int r, int ql, int qr) {
    if (ql <= l && r <= qr) {
        return tree[u];
    }
    push(u);
    int mid = (l + r) / 2;
    if (qr <= mid) return query(2 * u, l, mid, ql, qr);
    if (ql > mid) return query(2 * u + 1, mid + 1, r, ql, qr);
    return merge(query(2 * u, l, mid, ql, qr), query(2 * u + 1, mid + 1, r, ql, qr));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N >> Q)) return 0;
    A.resize(N + 1);
    for (int i = 1; i <= N; ++i) cin >> A[i];

    tree.resize(4 * N + 1);
    build(1, 1, N);

    while (Q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            cin >> l >> r;
            Node res = query(1, 1, N, l, r);
            long long inv_count = res.inv[1][0] + res.inv[2][0] + res.inv[2][1];
            cout << inv_count << "\n";
        } else {
            int l, r, s, t, u;
            cin >> l >> r >> s >> t >> u;
            array<int, 3> tag = {s, t, u};
            update(1, 1, N, l, r, tag);
        }
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
