# Problem Analysis: AtCoder-abc233_h — Ex. Manhattan Christmas Tree

**Problem ID**: `AtCoder-abc233_h`  
**Contest**: `abc233`  
**Rating / Difficulty**: 2530  
**URL**: https://atcoder.jp/contests/abc233/tasks/abc233_h  
**VJudge Tag**: `[problem:AtCoder-abc233_h]`  
**Category File**: [`../categories/data_structures_ds/manhattan_christmas_tree_parallel_binary_search_fenwick.md`](../categories/data_structures_ds/manhattan_christmas_tree_parallel_binary_search_fenwick.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Persistent Segment Tree`  

---

## 1. Problem Statement & Key Idea
Given $N$ points $(x_i, y_i)$, answer $Q$ queries: for query point $(x, y)$ and integer $K$, find the $K$-th smallest Manhattan distance $|x - x_i| + |y - y_i|$ to any of the $N$ points. Rotate coordinates by $45^\circ$: let $u = x + y, v = x - y$. The Manhattan metric becomes Chebyshev metric $\max(|u - u_i|, |v - v_i|)$. The condition $\max(|u - u_i|, |v - v_i|) \le D$ translates to a 2D axis-aligned bounding box $[u - D, u + D] \times [v - D, v + D]$.

## 2. Core Observation & Invariant
The number of points in $[u - D, u + D] \times [v - D, v + D]$ is monotonic with respect to $D \in [0, 4 \times 10^5]$. We can binary search $D$ for all $Q$ queries simultaneously using Parallel Binary Search. In each round, testing if box contains $\ge K$ points is equivalent to 2D range counting, solved by a sweep-line with a Fenwick Tree in $O((N + Q) \log(\max V))$ time.

## 3. Step-by-Step Algorithm
1. 1. Transform all points: $u_i = x_i + y_i, v_i = x_i - y_i + 2 \times 10^5$ (offset to ensure $v_i \ge 1$).
2. 2. Transform queries $(x, y, K)$: $u_q = x + y, v_q = x - y + 2 \times 10^5$, search range $[L_q, R_q] = [0, 4 \times 10^5]$.
3. 3. Run Parallel Binary Search for $\lceil \log_2(4 \times 10^5) \rceil \approx 19$ rounds:
4.    a. Assign each query to $mid = (L_q + R_q) / 2$.
5.    b. Generate 2D sweep-line events: add points at $u_i$, and for query boxes $[u_q - mid, u_q + mid] \times [v_{min}, v_{max}]$, generate query events at $u_q - mid - 1$ (subtract) and $u_q + mid$ (add).
6.    c. Sort events by $u$-coordinate and process with a Fenwick Tree over $v$.
7.    d. If count in box $\ge K$, update $ans_q = mid, R_q = mid - 1$; else $L_q = mid + 1$.
8. 4. Output $ans_q$ for each query.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) \log(V) \log(\max D))`
- **Space Complexity**: `O(N + Q)`

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
        if (i <= 0) return 0;
        if (i > n) i = n;
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
    int query(int l, int r) {
        if (l > r) return 0;
        return query(r) - query(l - 1);
    }
};

struct Point {
    int u, v;
};

struct Query {
    int u, v, k;
    int id;
};

struct Event {
    int u;
    int type; // 0 = point, 1 = query
    int id;
    int sign;
    int v1, v2;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    const int OFFSET = 100000;
    const int MAX_COORD = 400005;

    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        pts[i].u = x + y + 1;
        pts[i].v = x - y + OFFSET + 1;
    }

    int q;
    if (!(cin >> q)) return 0;

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        int a, b, k;
        cin >> a >> b >> k;
        queries[i].u = a + b + 1;
        queries[i].v = a - b + OFFSET + 1;
        queries[i].k = k;
        queries[i].id = i;
    }

    vector<int> L(q, 0), R(q, 200000), ans(q, 200000);

    for (int iter = 0; iter < 19; ++iter) {
        bool active = false;
        vector<Event> events;
        events.reserve(n + 2 * q);

        for (int i = 0; i < n; ++i) {
            events.push_back({pts[i].u, 0, i, 0, pts[i].v, 0});
        }

        for (int i = 0; i < q; ++i) {
            if (L[i] <= R[i]) {
                active = true;
                int mid = L[i] + (R[i] - L[i]) / 2;
                int u1 = max(1, queries[i].u - mid);
                int u2 = min(MAX_COORD, queries[i].u + mid);
                int v1 = max(1, queries[i].v - mid);
                int v2 = min(MAX_COORD, queries[i].v + mid);

                events.push_back({u1 - 1, 1, i, -1, v1, v2});
                events.push_back({u2, 1, i, +1, v1, v2});
            }
        }

        if (!active) break;

        sort(events.begin(), events.end(), [](const Event& a, const Event& b) {
            if (a.u != b.u) return a.u < b.u;
            return a.type < b.type;
        });

        Fenwick ft(MAX_COORD);
        vector<int> cnt(q, 0);

        for (const auto& ev : events) {
            if (ev.type == 0) {
                ft.add(ev.v1, 1);
            } else {
                int count = ft.query(ev.v1, ev.v2);
                cnt[ev.id] += ev.sign * count;
            }
        }

        for (int i = 0; i < q; ++i) {
            if (L[i] <= R[i]) {
                int mid = L[i] + (R[i] - L[i]) / 2;
                if (cnt[i] >= queries[i].k) {
                    ans[i] = mid;
                    R[i] = mid - 1;
                } else {
                    L[i] = mid + 1;
                }
            }
        }
    }

    for (int i = 0; i < q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
