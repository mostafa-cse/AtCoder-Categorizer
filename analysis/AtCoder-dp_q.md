# Problem Analysis: AtCoder-dp_q — Flowers

**Problem ID**: `AtCoder-dp_q`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1600  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_q  
**VJudge Tag**: `[problem:AtCoder-dp_q]`  
**Category File**: [`../categories/data_structures/fenwick_segment_tree.md`](../categories/data_structures/fenwick_segment_tree.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `DP Optimization using Data Structures [Some Practice Problems]`  

---

## 1. Problem Statement & Key Idea
Given N flowers with distinct heights h_i and beauties a_i, choose a subsequence of strictly increasing heights maximizing total beauty.

**Core Idea**: dp[h_i] = a_i + max_{0 <= h < h_i} dp[h]. Querying max in [0, h_i - 1] and updating point h_i is dynamically solved in O(log N) by a Fenwick or Segment Tree.

## 2. Core Observation & Invariant
Transforming quadratic inner-loop search into dynamic range queries via data structures.

## 3. Step-by-Step Algorithm
1. Maintain Fenwick tree supporting point-update and prefix-max queries.
2. For each flower i: best = fenwick.query(h_i - 1); fenwick.update(h_i, best + a_i).
3. Return fenwick.query(N).

## 4. Complexity Analysis
Time: O(N log N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Fenwick {
    int n;
    vector<long long> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void update(int i, long long val) {
        for (; i <= n; i += i & -i) tree[i] = max(tree[i], val);
    }

    long long query(int i) {
        long long res = 0;
        for (; i > 0; i -= i & -i) res = max(res, tree[i]);
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> h(n);
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> h[i];
    for (int i = 0; i < n; ++i) cin >> a[i];

    Fenwick bit(n);
    for (int i = 0; i < n; ++i) {
        long long best = bit.query(h[i] - 1);
        bit.update(h[i], best + a[i]);
    }

    cout << bit.query(n) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Fenwick tree / Segment tree accelerated LIS.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Transforming quadratic inner-loop search into dynamic range queries via data structures.
- **Reusable Pattern**: `BIT/Segment Tree accelerated DP.`

---
Back to [DP Optimization using Data Structures [Some Practice Problems]](../categories/data_structures/fenwick_segment_tree.md) | [Categories Directory](../categories/README.md)