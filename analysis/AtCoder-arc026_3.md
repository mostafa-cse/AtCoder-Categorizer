# Problem Analysis: AtCoder-arc026_3 — 蛍光灯

**Problem ID**: `AtCoder-arc026_3`  
**Contest**: `arc026`  
**Rating / Difficulty**: 1930  
**URL**: https://atcoder.jp/contests/arc026/tasks/arc026_3  
**VJudge Tag**: `[problem:AtCoder-arc026_3]`  
**Category File**: [`../categories/dp/interval_cover_segment_tree_min_dp.md`](../categories/dp/interval_cover_segment_tree_min_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimization using Data Structures`  
- **Topic (Skill)**: `Interval Cover Minimum Cost DP Accelerated by Range Minimum Segment Tree`  

---

## 1. Problem Statement & Key Idea
A street of length L must be illuminated. N lights are available; light i covers [l_i, r_i] with cost c_i. Find the minimum cost to completely illuminate [0, L].

Sort lights by r_i ascending. Let dp[x] be the minimum cost to illuminate [0, x]. For light covering [l_i, r_i] with cost c_i, the new covered prefix can reach r_i if some point in [l_i, r_i] was already illuminated: dp[r_i] = min(dp[r_i], min_{x in [l_i, r_i]} dp[x] + c_i). Range minimum query on [l_i, r_i] is handled by a Segment Tree in O(log L).

## 2. Core Observation & Invariant
Maintaining prefix coverage DP via Segment Tree range minimum queries reduces interval coverage to O(N log L).

## 3. Step-by-Step Algorithm
1. Sort lights by right endpoint r_i.
2. Initialize Segment Tree over [0, L] with INF, and dp[0] = 0.
3. For each light (l_i, r_i, c_i):
4.   best_prev = query_min(l_i, r_i).
5.   if best_prev < INF: update(r_i, best_prev + c_i).
6. Print query_min(L, L).

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + N log L)`
- **Space Complexity**: `O(L)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Light {
    int l, r;
    long long c;
};

int n, L;
vector<long long> tree;

void update(int node, int start, int end, int idx, long long val) {
    if (start == end) {
        tree[node] = min(tree[node], val);
        return;
    }
    int mid = start + (end - start) / 2;
    if (idx <= mid) {
        update(2 * node, start, mid, idx, val);
    } else {
        update(2 * node + 1, mid + 1, end, idx, val);
    }
    tree[node] = min(tree[2 * node], tree[2 * node + 1]);
}

long long query(int node, int start, int end, int l, int r) {
    if (r < start || end < l) return INF;
    if (l <= start && end <= r) return tree[node];
    int mid = start + (end - start) / 2;
    return min(query(2 * node, start, mid, l, r), query(2 * node + 1, mid + 1, end, l, r));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> L)) return 0;

    vector<Light> lights(n);
    for (int i = 0; i < n; ++i) {
        cin >> lights[i].l >> lights[i].r >> lights[i].c;
    }

    sort(lights.begin(), lights.end(), [](const Light& a, const Light& b) {
        if (a.r != b.r) return a.r < b.r;
        return a.l < b.l;
    });

    tree.assign(4 * (L + 1), INF);
    update(1, 0, L, 0, 0);

    for (const auto& lt : lights) {
        long long best_prev = query(1, 0, L, lt.l, lt.r);
        if (best_prev < INF) {
            update(1, 0, L, lt.r, best_prev + lt.c);
        }
    }

    long long ans = query(1, 0, L, L, L);
    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Accelerating 1D contiguous coverage dynamic programming using Segment Tree range minimum queries.
- **Reusable Pattern**: `Interval Cover DP: dp[r] = min_{k in [l, r]} dp[k] + cost, maintained via Segment Tree.`
