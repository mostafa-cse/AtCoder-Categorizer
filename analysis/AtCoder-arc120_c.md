# Problem Analysis: AtCoder-arc120_c — Swaps 2

**Problem ID**: `AtCoder-arc120_c`  
**Contest**: `arc120`  
**Rating / Difficulty**: 1478  
**URL**: https://atcoder.jp/contests/arc120/tasks/arc120_c  
**VJudge Tag**: `[problem:AtCoder-arc120_c]`  
**Category File**: [`../categories/data_structures/invariant_inversion_counting_fenwick.md`](../categories/data_structures/invariant_inversion_counting_fenwick.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Fenwick Tree`  
- **Topic (Skill)**: `Invariant Value Coordinate Assignment + Fenwick Inversion Counting`  

---

## 1. Problem Statement & Key Idea
Two arrays A and B of length N. In one operation, swap adjacent elements A[i] and A[i+1], then A[i] += 1 and A[i+1] -= 1. Find the minimum operations to transform A into B, or -1 if impossible.

**Key Insight**: Notice the invariant: under swapping A[i] and A[i+1], their new values become A'[i] = A[i+1] - 1 and A'[i+1] = A[i] + 1. Thus, A[i] + i is an INVARIANT under adjacent transpositions!

## 2. Core Observation & Invariant
Let A'_i = A[i] + i and B'_i = B[i] + i. The operation becomes an ordinary adjacent swap of elements in A'. If the multisets of A' and B' match, the minimum operations equals the number of inversions to sort A' into B', computable via a Fenwick tree in O(N log N).

## 3. Step-by-Step Algorithm
1. Compute A'_i = A[i] + i and B'_i = B[i] + i for i = 0..N-1.
2. Check if sorted(A') == sorted(B'). If not, return -1.
3. Group 0-indexed positions of values in B' using a queue or vector.
4. Construct target permutation P where P[i] = next available position of A'_i in B'.
5. Count inversions in P using a Fenwick tree.
6. Print inversion count.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Discovering algebraic invariants under local transformations to reduce problems to inversion counting.
- **Reusable Pattern**: `Invariant Transposition: transform values to preserve identity under swaps + Fenwick inversion count.`
