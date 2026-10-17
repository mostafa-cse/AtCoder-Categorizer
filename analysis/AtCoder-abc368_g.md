# Problem Analysis: AtCoder-abc368_g — Add and Multiply Queries

**Problem ID**: `AtCoder-abc368_g`  
**Contest**: `abc368`  
**Rating / Difficulty**: 1841  
**URL**: https://atcoder.jp/contests/abc368/tasks/abc368_g  
**VJudge Tag**: `[problem:AtCoder-abc368_g]`  
**Category File**: [`../categories/data_structures/exponential_growth_sparse_set_skipping.md`](../categories/data_structures/exponential_growth_sparse_set_skipping.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Fenwick Tree + Set Skipping`  
- **Topic (Skill)**: `Exponential Growth Sparse Set Skipping with Fenwick Range Sum`  

---

## 1. Problem Statement & Key Idea
Given arrays A and B of length N. Process Q queries: (1) update A_i, (2) update B_i, or (3) simulate from l to r: starting with v = 1, for each i in [l, r], choose v = v + A_i or v = v * B_i to maximize v.

**Key Insight**: If B_i = 1, multiplying does nothing so we always add A_i. If B_i >= 2, multiplying doubles v. Since v <= 10^{18}, at most ~60 multiplications by B_i >= 2 can occur. Maintain indices where B_i >= 2 in a std::set.

## 2. Core Observation & Invariant
For query [l, r], skip ranges of contiguous B_k = 1 by querying the range sum of A on a Fenwick tree in O(log N), then at each sparse B_i >= 2 point choose max(v + A_i, v * B_i). At most 60 hops per query.

## 3. Step-by-Step Algorithm
1. Build Fenwick tree over A.
2. Maintain set<int> big_B containing all indices i with B_i >= 2.
3. Update A_i: Fenwick add delta.
4. Update B_i: update B_i; if new B_i >= 2, insert i into set, else erase i.
5. Query (l, r):
6.   v = 1, cur = l.
7.   While cur <= r:
8.     next_big = big_B.lower_bound(cur).
9.     if next_big > r: v += Fenwick.query(cur, r); break.
10.     v += Fenwick.query(cur, *next_big - 1);
11.     v = max(v + A[*next_big], v * B[*next_big]);
12.     cur = *next_big + 1;
13.   print v.

## 4. Complexity Analysis
- **Time Complexity**: `O((Q * 60 + N) log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

struct Fenwick {
    int sz;
    vector<long long> tree;
    Fenwick(int n) : sz(n), tree(n + 1, 0) {}
    void add(int i, long long delta) {
        for (; i <= sz; i += i & -i) tree[i] += delta;
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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1), b(n + 1);
    Fenwick ft(n);
    set<int> big_b;

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        ft.add(i, a[i]);
    }
    for (int i = 1; i <= n; ++i) {
        cin >> b[i];
        if (b[i] >= 2) big_b.insert(i);
    }

    int q;
    cin >> q;
    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int i;
            long long x;
            cin >> i >> x;
            ft.add(i, x - a[i]);
            a[i] = x;
        } else if (type == 2) {
            int i;
            long long x;
            cin >> i >> x;
            b[i] = x;
            if (b[i] >= 2) big_b.insert(i);
            else big_b.erase(i);
        } else {
            int l, r;
            cin >> l >> r;
            long long v = 1;
            int cur = l;

            while (cur <= r) {
                auto it = big_b.lower_bound(cur);
                if (it == big_b.end() || *it > r) {
                    v += ft.query(cur, r);
                    break;
                }
                int idx = *it;
                v += ft.query(cur, idx - 1);
                v = max(v + a[idx], v * b[idx]);
                cur = idx + 1;
            }
            cout << v << "\n";
        }
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Sparse point hopping for bounded exponential multipliers combined with range sum data structures.
- **Reusable Pattern**: `Multiplicative Exponential Pruning: Store B_i >= 2 in set and jump across B_i = 1 segments.`
