# Problem Analysis: AtCoder-abc174_f — Range Set Query

**Problem ID**: `AtCoder-abc174_f`  
**Contest**: `abc174`  
**Rating / Difficulty**: 1495  
**URL**: https://atcoder.jp/contests/abc174/tasks/abc174_f  
**VJudge Tag**: `[problem:AtCoder-abc174_f]`  
**Category File**: [`../categories/data_structures/offline_distinct_elements_fenwick.md`](../categories/data_structures/offline_distinct_elements_fenwick.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Fenwick Tree`  
- **Topic (Skill)**: `Offline Range Distinct Elements Query using Fenwick Tree`  

---

## 1. Problem Statement & Key Idea
Given an array C of length N and Q range queries [l, r]. For each query, count the number of distinct elements in the subarray C[l..r].

**Key Insight**: Process queries offline sorted by right endpoint r. Maintain a Fenwick tree where position p holds +1 iff p is the rightmost occurrence of value C[p] up to the current index r.

## 2. Core Observation & Invariant
When moving from r-1 to r, if C[r] previously occurred at last_pos[C[r]], decrement position last_pos[C[r]] in the Fenwick tree by 1. Then add +1 at position r. For any query [l, r], the distinct count is simply the range sum in [l, r].

## 3. Step-by-Step Algorithm
1. Store queries grouped by right endpoint r.
2. Initialize Fenwick tree of size N and array last_pos initialized to 0.
3. For r from 1 to N:
4.   If last_pos[C[r]] > 0, fenwick.add(last_pos[C[r]], -1).
5.   fenwick.add(r, 1).
6.   last_pos[C[r]] = r.
7.   For each query [l, r]: ans[query_id] = fenwick.query(r) - fenwick.query(l - 1).
8. Print answers for all queries in order.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N + Q)`

## 5. Complete C++ Solution
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

    int query(int i) const {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

struct Query {
    int l, r, id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> c(n + 1);
    for (int i = 1; i <= n; ++i) cin >> c[i];

    vector<vector<pair<int, int>>> queries_at(n + 1);
    for (int i = 0; i < q; ++i) {
        int l, r;
        cin >> l >> r;
        queries_at[r].push_back({l, i});
    }

    vector<int> last_pos(n + 1, 0);
    Fenwick bit(n);
    vector<int> ans(q);

    for (int r = 1; r <= n; ++r) {
        if (last_pos[c[r]] > 0) {
            bit.add(last_pos[c[r]], -1);
        }
        bit.add(r, 1);
        last_pos[c[r]] = r;

        for (const auto& qry : queries_at[r]) {
            int l = qry.first;
            int id = qry.second;
            ans[id] = bit.query(r) - bit.query(l - 1);
        }
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
- **Core Skill**: Offline Fenwick tree sweep-line for range distinct elements queries.
- **Reusable Pattern**: `Range Distinct Query Template: sweep right endpoint r, cancel last_pos, add r, query [l, r].`
