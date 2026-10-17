# Problem Analysis: AtCoder-abc287_g — G. Balance Update Query

**Problem ID**: `AtCoder-abc287_g`  
**Contest**: `abc287`  
**Rating / Difficulty**: 2180  
**URL**: https://atcoder.jp/contests/abc287/tasks/abc287_g  
**VJudge Tag**: `[problem:AtCoder-abc287_g]`  
**Category File**: [`../categories/data_structures/segment_tree_point_update_range_query_kth_walk.md`](../categories/data_structures/segment_tree_point_update_range_query_kth_walk.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree (Point Update Range Query)`  

---

## 1. Problem Statement & Key Idea
Maintain N card types with score a_i and quota b_i under point score updates, quota updates, and queries asking for the maximum score achievable by selecting x cards total. Greedily taking cards with the highest scores is optimal, implemented via segment tree walking.

## 2. Core Observation & Invariant
Coordinate compressing all initial scores and query score updates yields at most N + Q distinct values. A segment tree over the sorted values maintains card count and score sum. Query x checks if total count >= x, then walks from root to leaf, recursively descending into the right child if it has sufficient cards, or taking all right child cards and descending into the left child.

## 3. Step-by-Step Algorithm
1. Collect all initial scores a_i and update scores y into a vector, sort and deduplicate to form coordinate compression basis.
2. Build a segment tree over compressed indices tracking tree_cnt and tree_sum.
3. Initialize the tree by adding (b_i, b_i * a_i) at the index of a_i for each card 1 <= i <= N.
4. Handle Type 1 (score update): subtract old (b_x, b_x * a_x) at old position, update a_x, add (b_x, b_x * a_x) at new position.
5. Handle Type 2 (quota update): update delta b_x at position of a_x.
6. Handle Type 3 (query x): if tree_cnt[root] < x, output -1; otherwise walk the segment tree taking cards from largest scores down in O(log(N+Q)) time.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log(N + Q))`
- **Space Complexity**: `O(N + Q)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Query {
    int type;
    long long x, y;
};

const int MAXK = 400005;
long long tree_cnt[4 * MAXK];
long long tree_sum[4 * MAXK];

void update(int node, int l, int r, int pos, long long delta_cnt, long long delta_sum) {
    if (l == r) {
        tree_cnt[node] += delta_cnt;
        tree_sum[node] += delta_sum;
        return;
    }
    int mid = (l + r) / 2;
    if (pos <= mid) update(2 * node, l, mid, pos, delta_cnt, delta_sum);
    else update(2 * node + 1, mid + 1, r, pos, delta_cnt, delta_sum);
    tree_cnt[node] = tree_cnt[2 * node] + tree_cnt[2 * node + 1];
    tree_sum[node] = tree_sum[2 * node] + tree_sum[2 * node + 1];
}

long long query_kth(int node, int l, int r, long long rem, const vector<long long>& vals) {
    if (l == r) {
        return rem * vals[l];
    }
    int mid = (l + r) / 2;
    if (tree_cnt[2 * node + 1] >= rem) {
        return query_kth(2 * node + 1, mid + 1, r, rem, vals);
    } else {
        long long right_sum = tree_sum[2 * node + 1];
        long long right_cnt = tree_cnt[2 * node + 1];
        return right_sum + query_kth(2 * node, l, mid, rem - right_cnt, vals);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> a(N + 1), b(N + 1);
    vector<long long> vals;
    vals.reserve(N + 200005);

    for (int i = 1; i <= N; ++i) {
        cin >> a[i] >> b[i];
        vals.push_back(a[i]);
    }

    int Q;
    cin >> Q;
    vector<Query> queries(Q);
    for (int i = 0; i < Q; ++i) {
        cin >> queries[i].type;
        if (queries[i].type == 1) {
            cin >> queries[i].x >> queries[i].y;
            vals.push_back(queries[i].y);
        } else if (queries[i].type == 2) {
            cin >> queries[i].x >> queries[i].y;
        } else {
            cin >> queries[i].x;
        }
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    auto get_pos = [&](long long v) {
        return int(lower_bound(vals.begin(), vals.end(), v) - vals.begin());
    };

    int K = (int)vals.size() - 1;

    for (int i = 1; i <= N; ++i) {
        int pos = get_pos(a[i]);
        update(1, 0, K, pos, b[i], b[i] * a[i]);
    }

    for (int i = 0; i < Q; ++i) {
        if (queries[i].type == 1) {
            int x = queries[i].x;
            long long new_a = queries[i].y;
            int old_pos = get_pos(a[x]);
            update(1, 0, K, old_pos, -b[x], -b[x] * a[x]);
            a[x] = new_a;
            int new_pos = get_pos(a[x]);
            update(1, 0, K, new_pos, b[x], b[x] * a[x]);
        } else if (queries[i].type == 2) {
            int x = queries[i].x;
            long long new_b = queries[i].y;
            int pos = get_pos(a[x]);
            update(1, 0, K, pos, new_b - b[x], (new_b - b[x]) * a[x]);
            b[x] = new_b;
        } else {
            long long x = queries[i].x;
            if (tree_cnt[1] < x) {
                cout << -1 << "\n";
            } else {
                cout << query_kth(1, 0, K, x, vals) << "\n";
            }
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
