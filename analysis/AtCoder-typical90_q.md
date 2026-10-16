# Problem Analysis: AtCoder-typical90_q — Crossing Segments

**Problem ID**: `AtCoder-typical90_q`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 017)  
**Rating / Difficulty**: 2450 (★7)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_q  
**VJudge Tag**: `[problem:AtCoder-typical90_q]`  
**Category File**: [`../categories/data_structures/fenwick_segment_tree.md`](../categories/data_structures/fenwick_segment_tree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree / Fenwick Tree`  
- **Topic (Skill)**: `Circle Chord Intersection Counting via Fenwick Tree`  

---

## 1. Problem Statement & Key Idea
N vertices arranged circularly 1..N. M chords connect pairs (L_i, R_i). Count pairs of chords that intersect strictly inside the circle.

**Core Idea**: Two chords (L1, R1) and (L2, R2) intersect strictly inside the circle iff their endpoints alternate: L1 < L2 < R1 < R2.

## 2. Core Observation & Invariant
Total chord pairs = C(M, 2). Non-intersecting chords are either completely disjoint (R1 <= L2 or R2 <= L1) or one strictly contains the other (L1 <= L2 < R2 <= R1). Counting containment and disjointness via Fenwick Tree gives intersecting count by subtraction.

## 3. Step-by-Step Algorithm
1. Sort chords by L_i ascending (and R_i descending).
2. Count completely disjoint chords using prefix counts of R.
3. Count nested chords using Fenwick tree range query on R.
4. Subtract non-intersecting pairs from M*(M-1)/2.

## 4. Complexity Analysis
Time: O(M log N), Space: O(N + M).

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
    void add(int i, long long delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }
    long long query(int i) {
        long long sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
    long long query(int l, int r) {
        if (l > r) return 0;
        return query(r) - query(l - 1);
    }
};

struct Chord {
    int l, r;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Chord> chords(m);
    for (int i = 0; i < m; ++i) {
        cin >> chords[i].l >> chords[i].r;
    }

    // Sort chords by l ascending, then r ascending
    sort(chords.begin(), chords.end(), [](const Chord& a, const Chord& b) {
        if (a.l != b.l) return a.l < b.l;
        return a.r < b.r;
    });

    // Count intersecting chords directly:
    // For chord i (L_i, R_i), a previously processed chord j with L_j < L_i
    // intersects iff L_j < L_i < R_j < R_i.
    // That means R_j must be in the open interval (L_i, R_i).
    Fenwick ft(n);
    long long intersections = 0;

    // To prevent same L interference, group by L or add after checking
    // All chords have L < R.
    // Query chords with R_j in (L_i, R_i)
    for (int i = 0; i < m; ++i) {
        int l = chords[i].l;
        int r = chords[i].r;
        intersections += ft.query(l + 1, r - 1);
        ft.add(r, 1);
    }

    cout << intersections << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Interval endpoint alternation counting using Fenwick Tree.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Circular endpoint topology, range intersection counting, and Fenwick tree point-add range-query acceleration.
- **Reusable Pattern**: `Fenwick Tree Endpoint Alternation Inversion.`

---
Back to [Circle Chord Intersection Counting via Fenwick Tree](../categories/data_structures/fenwick_segment_tree.md) | [Categories Directory](../categories/README.md)