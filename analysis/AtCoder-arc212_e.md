# Problem Analysis: AtCoder-arc212_e — E. Drop Min

**Problem ID**: `AtCoder-arc212_e`  
**Contest**: `arc212`  
**Rating / Difficulty**: 2324  
**URL**: https://atcoder.jp/contests/arc212/tasks/arc212_e  
**VJudge Tag**: `[problem:AtCoder-arc212_e]`  
**Category File**: [`../categories/data_structures/drop_min_cartesian_tree_linear_extensions.md`](../categories/data_structures/drop_min_cartesian_tree_linear_extensions.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `More Tree Data Structures`  
- **Topic (Skill)**: `Cartesian Tree`  

---

## 1. Problem Statement & Key Idea
Given an array $P$ of length $N$, elements are deleted in a valid order corresponding to tree hook-length independence on the Cartesian tree. Find the expected eliminations or total valid topological orderings modulo 998244353.

## 2. Core Observation & Invariant
In the max Cartesian tree of $P$, any node $u \neq \text{root}$ can be deleted if and only if all elements of its left subtree are deleted before $u$ (if an ancestor exists to its left) or all elements of its right subtree are deleted before $u$ (if an ancestor exists to its right).

## 3. Step-by-Step Algorithm
1. Construct the Cartesian tree of $P$ using a monotonic stack in $O(N)$ time.
2. For each non-root node $u$, determine whether it has a greater ancestor to the left ($has\_L$) and right ($has\_R$).
3. By the tree hook-length independence principle, node $u$'s placement probability is $\frac{1}{sz_L+1}$, $\frac{1}{sz_R+1}$, or $\frac{1}{sz_L+1} + \frac{1}{sz_R+1} - \frac{1}{sz_L+sz_R+1}$.
4. Multiply $(N-1)!$ by all node probabilities in $O(N)$ total time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

long long modInverse(long long n) {
    long long res = 1, p = MOD - 2;
    n %= MOD;
    while (p > 0) {
        if (p & 1) res = (res * n) % MOD;
        n = (n * n) % MOD;
        p >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
    }

    vector<int> st;
    vector<int> left(n, -1), right(n, -1);

    for (int i = 0; i < n; ++i) {
        int last = -1;
        while (!st.empty() && p[st.back()] < p[i]) {
            last = st.back();
            st.pop_back();
        }
        if (!st.empty()) {
            right[st.back()] = i;
        }
        if (last != -1) {
            left[i] = last;
        }
        st.push_back(i);
    }

    int root = st[0];

    vector<int> sz(n, 0);
    function<int(int)> get_sz = [&](int u) {
        if (u == -1) return 0;
        return sz[u] = 1 + get_sz(left[u]) + get_sz(right[u]);
    };
    get_sz(root);

    vector<bool> has_L(n, false), has_R(n, false);
    vector<int> st_l;
    for (int i = 0; i < n; ++i) {
        while (!st_l.empty() && p[st_l.back()] < p[i]) {
            st_l.pop_back();
        }
        if (!st_l.empty()) has_L[i] = true;
        st_l.push_back(i);
    }
    vector<int> st_r;
    for (int i = n - 1; i >= 0; --i) {
        while (!st_r.empty() && p[st_r.back()] < p[i]) {
            st_r.pop_back();
        }
        if (!st_r.empty()) has_R[i] = true;
        st_r.push_back(i);
    }

    long long ans = 1;
    for (int i = 1; i < n; ++i) {
        ans = (ans * i) % MOD;
    }

    for (int u = 0; u < n; ++u) {
        if (u == root) continue;
        int sz_l = (left[u] != -1 ? sz[left[u]] : 0);
        int sz_r = (right[u] != -1 ? sz[right[u]] : 0);

        long long prob = 0;
        if (has_L[u] && !has_R[u]) {
            prob = modInverse(sz_l + 1);
        } else if (!has_L[u] && has_R[u]) {
            prob = modInverse(sz_r + 1);
        } else {
            long long t1 = modInverse(sz_l + 1);
            long long t2 = modInverse(sz_r + 1);
            long long t3 = modInverse(sz_l + sz_r + 1);
            prob = (t1 + t2 - t3 + MOD) % MOD;
        }

        ans = (ans * prob) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
