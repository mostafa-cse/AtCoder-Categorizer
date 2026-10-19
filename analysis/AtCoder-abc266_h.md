# Problem Analysis: AtCoder-abc266_h — Ex - Snuke Panic (2D)

**Problem ID**: `AtCoder-abc266_h`  
**Contest**: `abc266`  
**Rating / Difficulty**: 2865  
**URL**: https://atcoder.jp/contests/abc266/tasks/abc266_h  
**VJudge Tag**: `[problem:AtCoder-abc266_h]`  
**Category File**: [`../categories/miscellaneous/three_dimensional_partial_order_cdq_divide_and_conquer.md`](../categories/miscellaneous/three_dimensional_partial_order_cdq_divide_and_conquer.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `CDQ Divide and Conquer`  

---

## 1. Problem Statement & Key Idea
Takahashi starts at (0, 0) at time 0. He can move at speed <= 1 in x and speed <= 1 in positive y (y cannot decrease). N Snuke appear at times T_i, coordinates (X_i, Y_i), with sizes A_i. Maximize the total size of captured Snuke.

## 2. Core Observation & Invariant
The reachability condition |X_j - X_i| + Y_j - Y_i <= T_j - T_i with Y_j >= Y_i linearizes under coordinate transformation a = T - X - Y >= 0, b = T + X - Y >= 0, c = Y >= 0. Reachability becomes a 3D partial order: a_i <= a_j, b_i <= b_j, c_i <= c_j. This is solved by CDQ divide-and-conquer on 3D weighted DAG / LIS DP in O(N log^2 N) time.

## 3. Step-by-Step Algorithm
1. 1. Discard unreachable Snuke with a < 0, b < 0, c < 0. Add origin (0, 0, 0) with DP=0.
2. 2. Sort all points by (a, b, c) ascending.
3. 3. Discretize c for Fenwick tree updates.
4. 4. In cdq(L, R): recursively solve cdq(L, mid), sort left points as updaters and right points as queries by b, sweep and update/query max DP using Fenwick tree on c, rollback Fenwick tree, then recursively solve cdq(mid+1, R).
5. 5. Output max_i DP_i.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log^2 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Fenwick {
    int n;
    vector<long long> tree;
    Fenwick(int n) : n(n), tree(n + 1, -INF) {}

    void update(int idx, long long val) {
        for (; idx <= n; idx += idx & -idx) {
            tree[idx] = max(tree[idx], val);
        }
    }

    long long query(int idx) {
        long long res = -INF;
        for (; idx > 0; idx -= idx & -idx) {
            res = max(res, tree[idx]);
        }
        return res;
    }

    void reset(int idx) {
        for (; idx <= n; idx += idx & -idx) {
            tree[idx] = -INF;
        }
    }
};

struct Snuke {
    long long a, b, c;
    long long A;
    int c_rank;
    long long dp;
    int id;
};

vector<Snuke> P;
int max_c_rank;

void cdq(int L, int R, Fenwick& bit) {
    if (L >= R) return;
    int mid = L + (R - L) / 2;
    cdq(L, mid, bit);

    // Left points [L, mid], Right points [mid+1, R]
    // We sort both by b ascending, breaking ties so that left (updaters) come before right (queries)
    struct Event {
        long long b;
        int type; // 0: left (updater), 1: right (query)
        int idx;
        bool operator<(const Event& other) const {
            if (b != other.b) return b < other.b;
            return type < other.type;
        }
    };

    vector<Event> events;
    events.reserve(R - L + 1);
    for (int i = L; i <= mid; ++i) {
        if (P[i].dp != -INF) {
            events.push_back({P[i].b, 0, i});
        }
    }
    for (int i = mid + 1; i <= R; ++i) {
        events.push_back({P[i].b, 1, i});
    }

    sort(events.begin(), events.end());

    vector<int> updated_indices;
    for (const auto& ev : events) {
        if (ev.type == 0) {
            bit.update(P[ev.idx].c_rank, P[ev.idx].dp);
            updated_indices.push_back(P[ev.idx].c_rank);
        } else {
            long long best = bit.query(P[ev.idx].c_rank);
            if (best != -INF) {
                P[ev.idx].dp = max(P[ev.idx].dp, best + P[ev.idx].A);
            }
        }
    }

    for (int crank : updated_indices) {
        bit.reset(crank);
    }

    cdq(mid + 1, R, bit);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    // Origin: T=0, X=0, Y=0, A=0 -> a=0, b=0, c=0
    P.push_back({0, 0, 0, 0, 0, 0, 0});

    vector<long long> all_c;
    all_c.push_back(0);

    for (int i = 1; i <= N; ++i) {
        long long T, X, Y, A;
        cin >> T >> X >> Y >> A;
        long long a = T - X - Y;
        long long b = T + X - Y;
        long long c = Y;
        if (a >= 0 && b >= 0 && c >= 0) {
            P.push_back({a, b, c, A, 0, -INF, i});
            all_c.push_back(c);
        }
    }

    sort(all_c.begin(), all_c.end());
    all_c.erase(unique(all_c.begin(), all_c.end()), all_c.end());
    max_c_rank = all_c.size();

    for (auto& p : P) {
        p.c_rank = lower_bound(all_c.begin(), all_c.end(), p.c) - all_c.begin() + 1;
    }

    // Sort by a ascending, tie-break by b, then c
    sort(P.begin(), P.end(), [](const Snuke& x, const Snuke& y) {
        if (x.a != y.a) return x.a < y.a;
        if (x.b != y.b) return x.b < y.b;
        return x.c < y.c;
    });

    Fenwick bit(max_c_rank + 2);
    cdq(0, (int)P.size() - 1, bit);

    long long ans = 0;
    for (const auto& p : P) {
        ans = max(ans, p.dp);
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
