# Problem Analysis: AtCoder-arc073_d — F - Many Moves

**Problem ID**: `AtCoder-arc073_d`  
**Contest**: `arc073`  
**Rating / Difficulty**: 2867  
**URL**: https://atcoder.jp/contests/arc073/tasks/arc073_d  
**VJudge Tag**: `[problem:AtCoder-arc073_d]`  
**Category File**: [`../categories/data_structures/two_piece_movement_range_add_min_segment_tree_dp.md`](../categories/data_structures/two_piece_movement_range_add_min_segment_tree_dp.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree with Lazy Propagation`  

---

## 1. Problem Statement & Key Idea
Two pieces are initially at squares A and B on a line of N squares. For each of Q queries x_i, move one piece to x_i. Minimize the total movement distance.

## 2. Core Observation & Invariant
After processing a query at x, one piece is at x while the other is at some square j. Let DP[j] be the minimum cost with the other piece at j. When moving to the next query x' from previous query p: (1) moving the piece at p to x' adds |p - x'| to all DP[j]; (2) moving the other piece from j to x' updates DP[p] with min_j (DP[j] + |j - x'|). Splitting |j - x'| into j <= x' and j > x', this is maintained dynamically using a lazy segment tree storing min(DP[j] - j) and min(DP[j] + j).

## 3. Step-by-Step Algorithm
1. 1. Initialize segment tree of size N with DP[B] = 0 and all other DP[j] = inf, tracking DP[j], DP[j] - j, and DP[j] + j.
2. 2. Set p = A.
3. 3. For each query x: query range minimums for j <= x and j > x to find best transition cost to x.
4. 4. Apply global addition |p - x| via lazy propagation.
5. 5. Point-update DP[p] with the computed minimum transition cost.
6. 6. Update p = x.
7. 7. Output global minimum from root of segment tree.

## 4. Complexity Analysis
- **Time Complexity**: `O(Q log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Node {
    long long min_val;
    long long min_minus; // min(val - j)
    long long min_plus;  // min(val + j)
    long long lazy;
};

int N, Q;
int A, B;
vector<Node> tree;

void apply_lazy(int u, long long v) {
    tree[u].min_val += v;
    tree[u].min_minus += v;
    tree[u].min_plus += v;
    tree[u].lazy += v;
}

void push(int u) {
    if (tree[u].lazy != 0) {
        apply_lazy(u << 1, tree[u].lazy);
        apply_lazy(u << 1 | 1, tree[u].lazy);
        tree[u].lazy = 0;
    }
}

void pull(int u) {
    tree[u].min_val = min(tree[u << 1].min_val, tree[u << 1 | 1].min_val);
    tree[u].min_minus = min(tree[u << 1].min_minus, tree[u << 1 | 1].min_minus);
    tree[u].min_plus = min(tree[u << 1].min_plus, tree[u << 1 | 1].min_plus);
}

void build(int u, int l, int r) {
    tree[u].lazy = 0;
    if (l == r) {
        if (l == B) {
            tree[u].min_val = 0;
            tree[u].min_minus = -l;
            tree[u].min_plus = l;
        } else {
            tree[u].min_val = INF;
            tree[u].min_minus = INF;
            tree[u].min_plus = INF;
        }
        return;
    }
    int mid = (l + r) >> 1;
    build(u << 1, l, mid);
    build(u << 1 | 1, mid + 1, r);
    pull(u);
}

void point_update(int u, int l, int r, int pos, long long new_val) {
    if (l == r) {
        tree[u].min_val = min(tree[u].min_val, new_val);
        tree[u].min_minus = tree[u].min_val - l;
        tree[u].min_plus = tree[u].min_val + l;
        return;
    }
    push(u);
    int mid = (l + r) >> 1;
    if (pos <= mid) point_update(u << 1, l, mid, pos, new_val);
    else point_update(u << 1 | 1, mid + 1, r, pos, new_val);
    pull(u);
}

long long query_minus(int u, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return INF;
    if (ql <= l && r <= qr) return tree[u].min_minus;
    push(u);
    int mid = (l + r) >> 1;
    return min(query_minus(u << 1, l, mid, ql, qr), query_minus(u << 1 | 1, mid + 1, r, ql, qr));
}

long long query_plus(int u, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return INF;
    if (ql <= l && r <= qr) return tree[u].min_plus;
    push(u);
    int mid = (l + r) >> 1;
    return min(query_plus(u << 1, l, mid, ql, qr), query_plus(u << 1 | 1, mid + 1, r, ql, qr));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N >> Q >> A >> B)) return 0;

    tree.resize(4 * N + 1);
    build(1, 1, N);

    int p = A;
    for (int q = 0; q < Q; ++q) {
        int x;
        cin >> x;
        long long delta = abs(p - x);

        // min over j <= x of (DP[j] - j) + x
        long long m1 = query_minus(1, 1, N, 1, x);
        long long val1 = (m1 >= INF / 2) ? INF : (m1 + x);

        // min over j > x of (DP[j] + j) - x
        long long m2 = query_plus(1, 1, N, x + 1, N);
        long long val2 = (m2 >= INF / 2) ? INF : (m2 - x);

        long long best_new_dp = min(val1, val2);

        // Apply global addition delta to all DP[j]
        apply_lazy(1, delta);

        // Update DP[p] with best_new_dp
        if (best_new_dp < INF / 2) {
            point_update(1, 1, N, p, best_new_dp);
        }

        p = x;
    }

    cout << tree[1].min_val << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
