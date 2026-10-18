# Problem Analysis: AtCoder-abc348_g — G. Max (Sum - Max)

**Problem ID**: `AtCoder-abc348_g`  
**Contest**: `abc348`  
**Rating / Difficulty**: 2559  
**URL**: https://atcoder.jp/contests/abc348/tasks/abc348_g  
**VJudge Tag**: `[problem:AtCoder-abc348_g]`  
**Category File**: [`../categories/dynamic_programming_dp/max_sum_minus_max_dnc_persistent_segtree.md`](../categories/dynamic_programming_dp/max_sum_minus_max_dnc_persistent_segtree.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `Divide and Conquer Optimization`  

---

## 1. Problem Statement & Key Idea
For each $k = 1 \dots N$, select $k$ pairs $(A_i, B_i)$ to maximize $\sum_{i \in S} A_i - \max_{i \in S} B_i$. Sort pairs by $B_i$ ascending: $B_1 \le B_2 \le \dots \le B_N$. If the maximum $B$ in $S$ is at index $m$, we take $(A_m, B_m)$ and greedily select the $k - 1$ largest $A_i$ among prefix $1 \dots m - 1$. The optimal choice $m^*(k) = \arg\max_m f(k, m)$ is monotonically non-decreasing in $k$: $m^*(1) \le m^*(2) \le \dots \le m^*(N)$.

## 2. Core Observation & Invariant
Because $m^*(k)$ satisfies monotonicity, Divide and Conquer Optimization evaluates all $k \in [1, N]$ in $O(N \log N)$ evaluations of $f(k, m)$. Using a Persistent Segment Tree over sorted $A$-values, the sum of the $k - 1$ largest elements in prefix $m - 1$ is queried in $O(\log N)$ time, yielding total time $O(N \log^2 N)$.

## 3. Step-by-Step Algorithm
1. 1. Sort pairs by $B_i$ ascending.
2. 2. Coordinate compress $A$-values and build a Persistent Segment Tree over prefixes $0 \dots N$ maintaining count and sum.
3. 3. Implement $f(k, m) = A_m - B_m + \text{query\_k\_largest}(roots[m], k - 1)$.
4. 4. Implement `dnc(l, r, opt_l, opt_r)`:
5.    - Let $mid = (l + r) / 2$.
6.    - Find best $m \in [\max(mid - 1, opt\_l), opt\_r]$ maximizing $f(mid, m)$.
7.    - Set $ans[mid] = \max f(mid, m)$ and recurse on $(l, mid - 1, opt\_l, best\_m)$ and $(mid + 1, r, best\_m, opt\_r)$.
8. 5. Output $ans[1 \dots N]$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log^2 N)`
- **Space Complexity**: `O(N \log N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
    int cnt;
    long long sum;
    int lc, rc;
};

const int MAXNODES = 200005 * 40;
Node tree[MAXNODES];
int roots[200005];
int node_cnt = 0;

int build(int l, int r) {
    int id = ++node_cnt;
    tree[id] = {0, 0, 0, 0};
    if (l == r) return id;
    int mid = l + (r - l) / 2;
    tree[id].lc = build(l, mid);
    tree[id].rc = build(mid + 1, r);
    return id;
}

int update(int prev_id, int l, int r, int val_idx, long long val) {
    int id = ++node_cnt;
    tree[id] = tree[prev_id];
    tree[id].cnt++;
    tree[id].sum += val;
    if (l == r) return id;
    int mid = l + (r - l) / 2;
    if (val_idx <= mid) {
        tree[id].lc = update(tree[prev_id].lc, l, mid, val_idx, val);
    } else {
        tree[id].rc = update(tree[prev_id].rc, mid + 1, r, val_idx, val);
    }
    return id;
}

// Query sum of K largest values in persistent tree node
long long query_k_largest(int id, int l, int r, int k) {
    if (id == 0 || k <= 0) return 0;
    if (tree[id].cnt <= k) return tree[id].sum;
    if (l == r) {
        return (long long)k * (tree[id].sum / tree[id].cnt);
    }
    int mid = l + (r - l) / 2;
    int right_cnt = tree[tree[id].rc].cnt;
    if (k <= right_cnt) {
        return query_k_largest(tree[id].rc, mid + 1, r, k);
    } else {
        return tree[tree[id].rc].sum + query_k_largest(tree[id].lc, l, mid, k - right_cnt);
    }
}

struct Item {
    long long b, a;
    int orig_a_idx;
};

int n;
vector<Item> items;
vector<long long> ans;
int num_unique_a;
vector<long long> unique_a;

long long eval_val(int k, int m) {
    long long res = items[m].a - items[m].b;
    if (k > 1 && m > 0) {
        res += query_k_largest(roots[m], 0, num_unique_a - 1, k - 1);
    }
    return res;
}

void dnc(int l, int r, int opt_l, int opt_r) {
    if (l > r) return;
    int mid = l + (r - l) / 2;

    int best_opt = -1;
    long long best_val = -4e18;

    int search_start = max(mid - 1, opt_l);
    for (int m = search_start; m <= opt_r; ++m) {
        long long val = eval_val(mid, m);
        if (val > best_val) {
            best_val = val;
            best_opt = m;
        }
    }

    ans[mid] = best_val;
    dnc(l, mid - 1, opt_l, best_opt);
    dnc(mid + 1, r, best_opt, opt_r);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n)) return 0;

    items.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> items[i].a >> items[i].b;
        unique_a.push_back(items[i].a);
    }

    sort(unique_a.begin(), unique_a.end());
    unique_a.erase(unique(unique_a.begin(), unique_a.end()), unique_a.end());
    num_unique_a = unique_a.size();

    sort(items.begin(), items.end(), [](const Item& x, const Item& y) {
        return x.b < y.b;
    });

    roots[0] = build(0, num_unique_a - 1);
    for (int i = 0; i < n; ++i) {
        int idx = lower_bound(unique_a.begin(), unique_a.end(), items[i].a) - unique_a.begin();
        roots[i + 1] = update(roots[i], 0, num_unique_a - 1, idx, items[i].a);
    }

    ans.resize(n + 1);
    dnc(1, n, 0, n - 1);

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << "\n";
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
