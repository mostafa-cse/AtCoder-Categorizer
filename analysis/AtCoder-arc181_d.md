# Problem Analysis: AtCoder-arc181_d — Prefix Bubble Sort

**Problem ID**: `AtCoder-arc181_d`  
**Contest**: `arc181`  
**Rating / Difficulty**: 2227  
**URL**: https://atcoder.jp/contests/arc181/tasks/arc181_d  
**VJudge Tag**: `[problem:AtCoder-arc181_d]`  
**Category File**: [`../categories/data_structures/prefix_bubble_sort_inversion_tracking_bit.md`](../categories/data_structures/prefix_bubble_sort_inversion_tracking_bit.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Binary Indexed Tree (BIT)`  
- **Topic (Skill)**: `BIT / Fenwick Tree`  

---

## 1. Problem Statement & Key Idea
Compute the inversion number of a permutation after each step in a sequence of bubble sort passes on prefixes of non-decreasing lengths A_1 <= A_2 <= ... <= A_M.

## 2. Core Observation & Invariant
For an element x = P[i], its contribution to inversions (elements greater than x to its left, inv_x) decreases by exactly 1 on every operation k that covers x (A_t >= pos(x)) until inv_x reaches 0. Since A is non-decreasing, x becomes covered at operation l_x = lower_bound(A, pos(x)) and decreases by 1 for operations in [l_x, min(M, l_x + inv_x - 1)]. A difference array over operation indices efficiently tracks cumulative inversion drops.

## 3. Step-by-Step Algorithm
1. 1. Use a Fenwick tree to compute initial inversions inv_x for each element P[i] and total inversion count.
2. 2. For each element x at initial position pos(x):
3.    - If inv_x == 0, continue.
4.    - Find first operation l_x with A_{l_x} >= pos(x) via lower_bound.
5.    - If l_x <= M, update difference array dec[l_x]++ and dec[min(M, l_x + inv_x - 1) + 1]--.
6. 3. Sweep through operations 1 to M, accumulating active decrements and subtracting from total inversions.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n);
    Fenwick bit(n);
    long long total_inv = 0;
    vector<int> inv_x(n + 1, 0);

    for (int i = 0; i < n; ++i) {
        cin >> p[i];
        int val = p[i];
        int count_le = bit.query(val);
        int inv = i - count_le;
        inv_x[val] = inv;
        total_inv += inv;
        bit.add(val, 1);
    }

    int m;
    cin >> m;
    vector<int> a(m);
    for (int i = 0; i < m; ++i) {
        cin >> a[i];
    }

    vector<int> dec(m + 2, 0);
    for (int i = 0; i < n; ++i) {
        int pos = i + 1;
        int inv = inv_x[p[i]];
        if (inv == 0) continue;

        int idx = lower_bound(a.begin(), a.end(), pos) - a.begin();
        int l_x = idx + 1;
        if (l_x <= m) {
            int r_x = min(m, l_x + inv - 1);
            dec[l_x]++;
            dec[r_x + 1]--;
        }
    }

    long long cur_dec = 0;
    long long cur_inv = total_inv;
    for (int t = 1; t <= m; ++t) {
        cur_dec += dec[t];
        cur_inv -= cur_dec;
        cout << cur_inv << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
