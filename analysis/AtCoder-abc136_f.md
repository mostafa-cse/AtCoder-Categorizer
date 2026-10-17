# Problem Analysis: AtCoder-abc136_f — F. Enclosed Points

**Problem ID**: `AtCoder-abc136_f`  
**Contest**: `abc136`  
**Rating / Difficulty**: 2334  
**URL**: https://atcoder.jp/contests/abc136/tasks/abc136_f  
**VJudge Tag**: `[problem:AtCoder-abc136_f]`  
**Category File**: [`../categories/data_structures/bounding_box_quadrant_inclusion_fenwick.md`](../categories/data_structures/bounding_box_quadrant_inclusion_fenwick.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Binary Indexed Tree (BIT)`  
- **Topic (Skill)**: `BIT / Fenwick Tree`  

---

## 1. Problem Statement & Key Idea
Sum the number of points enclosed in bounding boxes over all non-empty subsets. By quadrant complementary counting, a point $P$ is enclosed unless all chosen points lie in a single half-plane, computed via Fenwick sweep in $O(N \log N)$.

## 2. Core Observation & Invariant
A point $P$ is inside the bounding box of subset $T$ if and only if $T$ contains $P$ or $T$ has points in opposing quadrants relative to $P$. By complementary counting, $P$ is covered in all non-empty subsets except those strictly contained within any single half-plane (North, South, East, West).

## 3. Step-by-Step Algorithm
1. Coordinate compress $X$ and $Y$ coordinates and sort points by $X$.
2. Sweep from left to right with a Fenwick tree over $Y$ coordinates to compute the counts $(c_1, c_2, c_3, c_4)$ of points in each of the 4 open quadrants around $P$.
3. Add the contribution $2^N - 1 - [2^{c_1+c_4} + 2^{c_2+c_3} + 2^{c_1+c_2} + 2^{c_3+c_4} - 2^{c_1} - 2^{c_2} - 2^{c_3} - 2^{c_4}] - [2^{N - 1 - c_1 - c_2 - c_3 - c_4} - 1]$ to total in $O(N \log N)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

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

    vector<pair<int, int>> pts(n);
    vector<int> ys(n);
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].first >> pts[i].second;
        ys[i] = pts[i].second;
    }

    // Coordinate compress y
    sort(ys.begin(), ys.end());
    ys.erase(unique(ys.begin(), ys.end()), ys.end());

    auto get_y = [&](int y) {
        return (int)(lower_bound(ys.begin(), ys.end(), y) - ys.begin()) + 1;
    };

    // Sort by x
    sort(pts.begin(), pts.end(), [&](const pair<int, int> &a, const pair<int, int> &b) {
        return a.first < b.first;
    });

    vector<long long> pow2(n + 1);
    pow2[0] = 1;
    for (int i = 1; i <= n; ++i) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    Fenwick bit(n);
    long long total_ans = 0;

    for (int i = 0; i < n; ++i) {
        int y_idx = get_y(pts[i].second);
        int c3 = bit.query(y_idx - 1);
        int c2 = i - c3;
        int c4 = (y_idx - 1) - c3;
        int c1 = (n - 1) - c2 - c3 - c4;

        long long contrib = pow2[n] - 1;
        contrib -= pow2[c1 + c4];
        contrib -= pow2[c2 + c3];
        contrib -= pow2[c1 + c2];
        contrib -= pow2[c3 + c4];
        contrib += pow2[c1];
        contrib += pow2[c2];
        contrib += pow2[c3];
        contrib += pow2[c4];

        contrib %= MOD;
        if (contrib < 0) contrib += MOD;

        total_ans = (total_ans + contrib) % MOD;
        bit.add(y_idx, 1);
    }

    cout << total_ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
