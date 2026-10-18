# Problem Analysis: AtCoder-arc043_c — C. 転倒距離

**Problem ID**: `AtCoder-arc043_c`  
**Contest**: `arc043`  
**Rating / Difficulty**: 2409  
**URL**: https://atcoder.jp/contests/arc043/tasks/arc043_c  
**VJudge Tag**: `[problem:AtCoder-arc043_c]`  
**Category File**: [`../categories/miscellaneous/inversion_distance_cayley_midpoint_fenwick.md`](../categories/miscellaneous/inversion_distance_cayley_midpoint_fenwick.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Inversions`  

---

## 1. Problem Statement & Key Idea
Given permutations A and B, find a permutation C equidistant from both in terms of inversion distance. Parity requires total inversion count I(A, B) to be even, and C is constructed on the Cayley shortest path with distance I/2 using a Fenwick Tree.

## 2. Core Observation & Invariant
Renumbering elements so A = (1, 2, ..., N), the distance dist(A, B) is the standard inversion count of B. If I is odd, no midpoint exists. If I is even, any permutation on the shortest path from A to B with I/2 inversions relative to A satisfies dist(A, C) = dist(B, C) = I/2.

## 3. Step-by-Step Algorithm
1. 1. Map elements so that A becomes identity (1, 2, ..., N).
2. 2. Count inversions in mapped B using a Fenwick tree, recording the contribution c_i of each element.
3. 3. If total inversions I is odd, output -1.
4. 4. Greedily take prefix elements of B while target T = I/2 >= c_i, and position the critical boundary element to cross exactly the remaining T inversions among unplaced elements.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, int delta) {
        while (i <= n) {
            tree[i] += delta;
            i += i & (-i);
        }
    }
    int query(int i) {
        int s = 0;
        while (i > 0) {
            s += tree[i];
            i -= i & (-i);
        }
        return s;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n), b(n);
    vector<int> pos_in_a(n + 1), orig_val(n + 1);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        pos_in_a[a[i]] = i + 1;
        orig_val[i + 1] = a[i];
    }
    for (int i = 0; i < n; i++) cin >> b[i];

    vector<int> b_mapped(n);
    for (int i = 0; i < n; i++) b_mapped[i] = pos_in_a[b[i]];

    Fenwick ft(n);
    vector<int> c(n);
    ll total_inv = 0;
    for (int i = n - 1; i >= 0; i--) {
        int val = b_mapped[i];
        int cnt = ft.query(val - 1);
        c[i] = cnt;
        total_inv += cnt;
        ft.add(val, 1);
    }

    if (total_inv % 2 != 0) {
        cout << -1 << "\n";
        return 0;
    }

    ll T = total_inv / 2;
    vector<int> prefix_b;
    vector<bool> used(n + 1, false);
    int stop_idx = n;
    ll rem_T = 0;

    for (int i = 0; i < n; i++) {
        if (T >= c[i]) {
            prefix_b.push_back(b_mapped[i]);
            used[b_mapped[i]] = true;
            T -= c[i];
        } else {
            stop_idx = i;
            rem_T = T;
            break;
        }
    }

    vector<int> rem_a;
    for (int x = 1; x <= n; x++) {
        if (!used[x]) rem_a.push_back(x);
    }

    if (stop_idx < n) {
        int val = b_mapped[stop_idx];
        vector<int> smaller_idx;
        for (size_t i = 0; i < rem_a.size(); i++) {
            if (rem_a[i] < val) smaller_idx.push_back(i);
        }
        int k = smaller_idx.size();
        int target_pos = smaller_idx[k - rem_T];
        rem_a.erase(remove(rem_a.begin(), rem_a.end(), val), rem_a.end());
        rem_a.insert(rem_a.begin() + target_pos, val);
    }

    vector<int> ans_mapped = prefix_b;
    ans_mapped.insert(ans_mapped.end(), rem_a.begin(), rem_a.end());

    for (int i = 0; i < n; i++) {
        cout << orig_val[ans_mapped[i]] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
