# Problem Analysis: AtCoder-abc292_h — Rating Estimator

**Problem ID**: `AtCoder-abc292_h`  
**Contest**: `abc292`  
**Rating / Difficulty**: 2248  
**URL**: https://atcoder.jp/contests/abc292/tasks/abc292_h  
**VJudge Tag**: `[problem:AtCoder-abc292_h]`  
**Category File**: [`../categories/data_structures/walk_on_segment_tree_rating_estimator_prefix_average.md`](../categories/data_structures/walk_on_segment_tree_rating_estimator_prefix_average.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree (Point Update Range Query)`  

---

## 1. Problem Statement & Key Idea
Maintain performance estimates under point updates and report final rating, where rating freezes at the first contest where average performance reaches at least B.

## 2. Core Observation & Invariant
Average performance at contest n is >= B iff sum_{i=1}^n (a_i - B) >= 0. Defining b_i = a_i - B, the rating freezes at the smallest prefix index n with prefix_sum(b, n) >= 0. We can maintain sum and max_prefix_sum in a Segment Tree over b_i. A walk on the Segment Tree in O(log N) identifies the first index n where prefix sum >= 0.

## 3. Step-by-Step Algorithm
1. 1. Initialize b_i = a_i - B. Build a Segment Tree where each node maintains sum and max_prefix.
2. 2. For each query updating contest c to performance x: update b_c = x - B in the Segment Tree.
3. 3. If root max_prefix >= 0: walk on the Segment Tree to find the first index n with accumulated prefix sum >= 0, and compute final rating as B + (sum_{i=1}^n b_i) / n.
4. 4. Otherwise: rating never reaches B, so final rating is B + (sum_{i=1}^N b_i) / N.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

struct Node {
    long long sum;
    long long max_pref;
};

int N;
long long B;
vector<long long> A;
vector<Node> tree;

Node merge_nodes(const Node& L, const Node& R) {
    Node res;
    res.sum = L.sum + R.sum;
    res.max_pref = max(L.max_pref, L.sum + R.max_pref);
    return res;
}

void build(int node, int start, int end) {
    if (start == end) {
        long long b = A[start] - B;
        tree[node] = {b, b};
        return;
    }
    int mid = start + (end - start) / 2;
    build(2 * node, start, mid);
    build(2 * node + 1, mid + 1, end);
    tree[node] = merge_nodes(tree[2 * node], tree[2 * node + 1]);
}

void update(int node, int start, int end, int idx, long long val) {
    if (start == end) {
        long long b = val - B;
        tree[node] = {b, b};
        return;
    }
    int mid = start + (end - start) / 2;
    if (idx <= mid) update(2 * node, start, mid, idx, val);
    else update(2 * node + 1, mid + 1, end, idx, val);
    tree[node] = merge_nodes(tree[2 * node], tree[2 * node + 1]);
}

// Walk on segment tree to find first index where pref_sum >= 0
// Returns pair: (index, sum_of_b_up_to_index)
pair<int, long long> find_first_nonneg(int node, int start, int end, long long cur_sum) {
    if (start == end) {
        return {start, cur_sum + tree[node].sum};
    }
    int mid = start + (end - start) / 2;
    if (cur_sum + tree[2 * node].max_pref >= 0) {
        return find_first_nonneg(2 * node, start, mid, cur_sum);
    } else {
        return find_first_nonneg(2 * node + 1, mid + 1, end, cur_sum + tree[2 * node].sum);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int Q;
    if (!(cin >> N >> B >> Q)) return 0;

    A.resize(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
    }

    tree.resize(4 * N + 1);
    build(1, 1, N);

    cout << fixed << setprecision(15);

    while (Q--) {
        int c;
        long long x;
        cin >> c >> x;
        A[c] = x;
        update(1, 1, N, c, x);

        if (tree[1].max_pref >= 0) {
            auto res = find_first_nonneg(1, 1, N, 0);
            int idx = res.first;
            long long sum_b = res.second;
            double rating = (double)B + (double)sum_b / (double)idx;
            cout << rating << "\n";
        } else {
            // Never reaches >= B
            long long sum_b = tree[1].sum;
            double rating = (double)B + (double)sum_b / (double)N;
            cout << rating << "\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
