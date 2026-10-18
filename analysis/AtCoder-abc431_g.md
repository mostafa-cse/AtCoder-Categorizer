# Problem Analysis: AtCoder-abc431_g — G - One Time Swap 2

**Problem ID**: `AtCoder-abc431_g`  
**Contest**: `abc431`  
**Rating / Difficulty**: 2490  
**URL**: https://atcoder.jp/contests/abc431/tasks/abc431_g  
**VJudge Tag**: `[problem:AtCoder-abc431_g]`  
**Category File**: [`../categories/data_structures_ds/one_time_swap_2_fenwick_inversions.md`](../categories/data_structures_ds/one_time_swap_2_fenwick_inversions.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Binary Indexed Tree (BIT)`  
- **Topic (Skill)**: `BIT / Fenwick Tree`  

---

## 1. Problem Statement & Key Idea
Find the pair $(l, r)$ whose one-time swap produces the $k$-th lexicographically smallest permutation in the multiset of all $\binom{N}{2}$ swapped arrays.

## 2. Core Observation & Invariant
Comparing $f(l, r)$ to $A$: $f(l, r) < A$ if $A_l > A_r$, $f(l, r) = A$ if $A_l = A_r$, and $f(l, r) > A$ if $A_l < A_r$. For pairs with $A_l > A_r$, the lexicographical order corresponds to sorting by $(l, A_r, -r)$. By sorting queries offline, we iterate $l$ from $0$ to $N-1$ and maintain elements in a Fenwick Tree with binary lifting to identify $(A_r, r)$ in $O(\log N)$ per query. A symmetric pass handles $f(l, r) > A$.

## 3. Step-by-Step Algorithm
1. 1. Coordinate compress $A$ into $1 \dots V$.
2. 2. Sort queries $k$ descending.
3. 3. Part 1 ($B_k < A$): Sweep $l$ from $0$ to $N-1$, removing $A_l$ from a Fenwick tree of suffix counts. For queries within range, use binary lifting on the BIT to locate the $k$-th element value $v$ and index $r$.
4. 4. Part 2 ($B_k = A$): Count identical pairs $A_l = A_r$. Answer any query landing in this range with a stored identical pair.
5. 5. Part 3 ($B_k > A$): Sweep $l$ from $N-1$ down to $0$, inserting elements into a Fenwick tree to query elements greater than $A_l$.
6. 6. Output all query answers in original query order.

## 4. Complexity Analysis
- **Time Complexity**: `O(Q \log Q + (N + Q) \log N)`
- **Space Complexity**: `O(N + Q)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct BIT {
    int n;
    vector<int> tree;
    BIT(int size) : n(size), tree(size + 1, 0) {}
    void add(int idx, int val) {
        for (; idx <= n; idx += idx & -idx) tree[idx] += val;
    }
    int query(int idx) {
        int s = 0;
        for (; idx > 0; idx -= idx & -idx) s += tree[idx];
        return s;
    }
    int find_kth(int k) {
        int idx = 0;
        for (int p = 1 << 18; p > 0; p >>= 1) {
            if (idx + p <= n && tree[idx + p] <= k) {
                k -= tree[idx + p];
                idx += p;
            }
        }
        return idx + 1;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    if (!(cin >> N >> Q)) return 0;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];

    vector<int> vals = A;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    int V = vals.size();

    vector<int> c_A(N);
    for (int i = 0; i < N; ++i) {
        c_A[i] = lower_bound(vals.begin(), vals.end(), A[i]) - vals.begin() + 1;
    }

    vector<pair<long long, int>> query(Q);
    for (int i = 0; i < Q; ++i) {
        long long k;
        cin >> k;
        query[i] = {k - 1, i};
    }
    sort(query.rbegin(), query.rend());

    vector<pair<int, int>> ans(Q);

    // Part 1: B_k < A
    BIT bit1(V);
    vector<vector<int>> pos(V + 1);
    for (int i = 0; i < N; ++i) {
        bit1.add(c_A[i], 1);
        pos[c_A[i]].push_back(i);
    }

    long long cnt = 0;
    for (int l = 0; l < N; ++l) {
        bit1.add(c_A[l], -1);
        int lim = bit1.query(c_A[l] - 1);
        while (!query.empty()) {
            auto [k, qi] = query.back();
            long long k1 = k - cnt;
            if (k1 < lim) {
                int v = bit1.find_kth(k1);
                int cnt_less = bit1.query(v - 1);
                int rem = k1 - cnt_less;
                int r = pos[v][pos[v].size() - 1 - rem];
                ans[qi] = {l + 1, r + 1};
                query.pop_back();
            } else {
                break;
            }
        }
        cnt += lim;
    }

    // Part 2: B_k = A
    vector<int> C_cnt(V + 1, 0), last_idx(V + 1, -1);
    pair<int, int> p_eq = {-1, -1};
    for (int i = 0; i < N; ++i) {
        int v = c_A[i];
        if (last_idx[v] != -1) {
            p_eq = {last_idx[v] + 1, i + 1};
        }
        cnt += C_cnt[v];
        C_cnt[v]++;
        last_idx[v] = i;
    }

    while (!query.empty()) {
        auto [k, qi] = query.back();
        if (k < cnt) {
            ans[qi] = p_eq;
            query.pop_back();
        } else {
            break;
        }
    }

    // Part 3: B_k > A
    BIT bit3(V);
    vector<vector<int>> pos3(V + 1);
    int s_size = 0;

    for (int l = N - 1; l >= 0; --l) {
        int offset = bit3.query(c_A[l]);
        while (!query.empty()) {
            auto [k, qi] = query.back();
            long long k1 = k - cnt + offset;
            if (k1 < s_size) {
                int v = bit3.find_kth(k1);
                int cnt_less = bit3.query(v - 1);
                int rem = k1 - cnt_less;
                int r = pos3[v][pos3[v].size() - 1 - rem];
                ans[qi] = {l + 1, r + 1};
                query.pop_back();
            } else {
                break;
            }
        }
        cnt += s_size - offset;
        bit3.add(c_A[l], 1);
        pos3[c_A[l]].push_back(l);
        s_size++;
    }

    for (int i = 0; i < Q; ++i) {
        cout << ans[i].first << " " << ans[i].second << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
