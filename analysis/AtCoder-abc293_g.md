# Problem Analysis: AtCoder-abc293_g — Triple Index

**Problem ID**: `AtCoder-abc293_g`  
**Contest**: `abc293`  
**Rating / Difficulty**: 1753  
**URL**: https://atcoder.jp/contests/abc293/tasks/abc293_g  
**VJudge Tag**: `[problem:AtCoder-abc293_g]`  
**Category File**: [`../categories/data_structures/mos_algorithm_range_triples.md`](../categories/data_structures/mos_algorithm_range_triples.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Mo's Algorithm`  
- **Topic (Skill)**: `Mo's Algorithm for Range Triples C(c, 3)`  

---

## 1. Problem Statement & Key Idea
Given an array A of N integers and Q queries (l_i, r_i). For each query, find the number of index triples (i, j, k) such that l <= i < j < k <= r and A_i = A_j = A_k.

**Key Insight**: For a value occurring c times in a range, the number of triples is C(c, 3) = c * (c - 1) * (c - 2) / 6. Using Mo's Algorithm with block size B = N / sqrt(Q), update the triple count in O(1) when extending or shrinking the range.

## 2. Core Observation & Invariant
Adding an element of count c increases triples by C(c, 2) = c * (c - 1) / 2. Removing an element of count c decreases triples by C(c - 1, 2) = (c - 1) * (c - 2) / 2.

## 3. Step-by-Step Algorithm
1. Sort queries offline by (l / B, r) with Hilbert or alternating parity order.
2. Maintain current range [cur_l, cur_r], frequency array cnt[val], and cur_ans.
3. add(x): cur_ans += cnt[x] * (cnt[x] - 1) / 2; cnt[x]++;
4. remove(x): cnt[x]--; cur_ans -= cnt[x] * (cnt[x] - 1) / 2;
5. Process all queries and store answers.
6. Print answers in original order.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) * sqrt(N))`
- **Space Complexity**: `O(N + Q + max_val)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Query {
    int l, r, id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].l >> queries[i].r;
        queries[i].id = i;
    }

    int block_size = max(1, (int)(n / sqrt(q)));
    sort(queries.begin(), queries.end(), [&](const Query& x, const Query& y) {
        int b1 = x.l / block_size;
        int b2 = y.l / block_size;
        if (b1 != b2) return b1 < b2;
        return (b1 & 1) ? (x.r < y.r) : (x.r > y.r);
    });

    vector<long long> cnt(200005, 0);
    vector<long long> ans(q);
    long long cur_triples = 0;

    auto add = [&](int val) {
        cur_triples += cnt[val] * (cnt[val] - 1) / 2;
        cnt[val]++;
    };

    auto remove = [&](int val) {
        cnt[val]--;
        cur_triples -= cnt[val] * (cnt[val] - 1) / 2;
    };

    int cur_l = 1, cur_r = 0;
    for (auto& qry : queries) {
        while (cur_l > qry.l) add(a[--cur_l]);
        while (cur_r < qry.r) add(a[++cur_r]);
        while (cur_l < qry.l) remove(a[cur_l++]);
        while (cur_r > qry.r) remove(a[cur_r--]);
        ans[qry.id] = cur_triples;
    }

    for (int i = 0; i < q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Mo's Algorithm for non-invertible polynomial range combinations.
- **Reusable Pattern**: `Mo's Algorithm Range Combinations: add/remove update C(c, k) in O(1).`
