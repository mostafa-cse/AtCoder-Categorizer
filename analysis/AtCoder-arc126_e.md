# Problem Analysis: AtCoder-arc126_e — E - Infinite Operations

**Problem ID**: `AtCoder-arc126_e`  
**Contest**: `arc126`  
**Rating / Difficulty**: 2766  
**URL**: https://atcoder.jp/contests/arc126/tasks/arc126_e  
**VJudge Tag**: `[problem:AtCoder-arc126_e]`  
**Category File**: [`../categories/data_structures_ds/infinite_operations_potential_segment_tree.md`](../categories/data_structures_ds/infinite_operations_potential_segment_tree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree (Point Update Range Query)`  

---

## 1. Problem Statement & Key Idea
Given sequence A of length N and Q point-update queries. For each query, let f(n) be the maximum points gained by choosing A_i <= A_j and moving them x closer while gaining x points. Find lim_{n -> inf} f(n) modulo 998244353 after each update.

## 2. Core Observation & Invariant
Let F(A) = sum_{i < j} |A_i - A_j|. Any valid operation gaining x points reduces F(A) by at least 2x, and a 'good' operation on adjacent elements in sorted order reduces F(A) by exactly 2x. Thus, the infinite limit is exactly F(A) / 2! When an element A_pos changes from old_val to new_val, the change in F(A) depends on sum_{a in A \ {old_val}} (|new_val - a| - |old_val - a|). This can be dynamically maintained using coordinate compression and a Fenwick tree (or Segment Tree) storing counts and prefix sums in O(log(N + Q)) per query.

## 3. Step-by-Step Algorithm
1. 1. Collect all initial values and query values to build a coordinate compression map of size M <= N + Q.
2. 2. Compute initial F(A) / 2 = (sum_{i=0}^{N-1} (2i - N + 1) * sorted_A[i]) / 2 mod 998244353.
3. 3. Initialize a Fenwick tree with counts and values of elements in A.
4. 4. For each update (pos, new_val):
5.    a. Query and remove old_val, subtracting its contribution from the current answer.
6.    b. Query and insert new_val, adding its contribution to the current answer.
7.    c. Update A[pos] = new_val and output the current answer modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log(N + Q))`
- **Space Complexity**: `O(N + Q)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;
const long long INV2 = 499122177;

struct BIT {
    int n;
    vector<long long> tree_cnt;
    vector<long long> tree_sum;

    BIT(int n) : n(n), tree_cnt(n + 1, 0), tree_sum(n + 1, 0) {}

    void add(int i, long long val, long long cnt) {
        while (i <= n) {
            tree_cnt[i] += cnt;
            tree_sum[i] = (tree_sum[i] + val) % MOD;
            if (tree_sum[i] < 0) tree_sum[i] += MOD;
            i += i & -i;
        }
    }

    pair<long long, long long> query(int i) {
        long long s = 0, c = 0;
        while (i > 0) {
            s = (s + tree_sum[i]) % MOD;
            c += tree_cnt[i];
            i -= i & -i;
        }
        return {s, c};
    }
};

struct Query {
    int pos;
    long long new_val;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> A(n);
    vector<long long> all_vals;
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
        all_vals.push_back(A[i]);
    }

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].pos >> queries[i].new_val;
        --queries[i].pos;
        all_vals.push_back(queries[i].new_val);
    }

    sort(all_vals.begin(), all_vals.end());
    all_vals.erase(unique(all_vals.begin(), all_vals.end()), all_vals.end());

    auto get_rank = [&](long long v) -> int {
        return (int)(lower_bound(all_vals.begin(), all_vals.end(), v) - all_vals.begin()) + 1;
    };

    int M = (int)all_vals.size();
    BIT bit(M);

    vector<long long> sorted_A = A;
    sort(sorted_A.begin(), sorted_A.end());

    long long cur_ans = 0;
    for (int i = 0; i < n; ++i) {
        long long coef = (2LL * i - n + 1) % MOD;
        if (coef < 0) coef += MOD;
        cur_ans = (cur_ans + coef * (sorted_A[i] % MOD)) % MOD;
    }
    cur_ans = (cur_ans * INV2) % MOD;

    for (int i = 0; i < n; ++i) {
        bit.add(get_rank(A[i]), A[i], 1);
    }

    for (int i = 0; i < q; ++i) {
        int pos = queries[i].pos;
        long long old_val = A[pos];
        long long new_val = queries[i].new_val;

        // 1. Remove old_val
        int r_old = get_rank(old_val);
        bit.add(r_old, (MOD - (old_val % MOD)) % MOD, -1);

        auto [sum_less_old, cnt_less_old] = bit.query(r_old);
        auto [total_sum, total_cnt] = bit.query(M);
        long long sum_ge_old = (total_sum - sum_less_old) % MOD;
        if (sum_ge_old < 0) sum_ge_old += MOD;
        long long cnt_ge_old = total_cnt - cnt_less_old;

        long long diff_old = ((cnt_less_old % MOD) * (old_val % MOD) - sum_less_old) % MOD;
        diff_old = (diff_old + (sum_ge_old - (cnt_ge_old % MOD) * (old_val % MOD))) % MOD;
        if (diff_old < 0) diff_old += MOD;
        diff_old = (diff_old * INV2) % MOD;
        cur_ans = (cur_ans - diff_old) % MOD;
        if (cur_ans < 0) cur_ans += MOD;

        // 2. Add new_val
        int r_new = get_rank(new_val);
        auto [sum_less_new, cnt_less_new] = bit.query(r_new);
        long long sum_ge_new = (total_sum - sum_less_new) % MOD;
        if (sum_ge_new < 0) sum_ge_new += MOD;
        long long cnt_ge_new = total_cnt - cnt_less_new;

        long long diff_new = ((cnt_less_new % MOD) * (new_val % MOD) - sum_less_new) % MOD;
        diff_new = (diff_new + (sum_ge_new - (cnt_ge_new % MOD) * (new_val % MOD))) % MOD;
        if (diff_new < 0) diff_new += MOD;
        diff_new = (diff_new * INV2) % MOD;
        cur_ans = (cur_ans + diff_new) % MOD;

        bit.add(r_new, new_val % MOD, 1);
        A[pos] = new_val;

        cout << cur_ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
