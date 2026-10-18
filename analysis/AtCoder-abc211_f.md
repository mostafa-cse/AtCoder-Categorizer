# Problem Analysis: AtCoder-abc211_f — F. Rectilinear Polygons

**Problem ID**: `AtCoder-abc211_f`  
**Contest**: `abc211`  
**Rating / Difficulty**: 2350  
**URL**: https://atcoder.jp/contests/abc211/tasks/abc211_f  
**VJudge Tag**: `[problem:AtCoder-abc211_f]`  
**Category File**: [`../categories/geometry/rectilinear_polygons_sweep_line.md`](../categories/geometry/rectilinear_polygons_sweep_line.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Sweep Line`  
- **Topic (Skill)**: `Sweep Line Algorithm and Radial Sweep`  

---

## 1. Problem Statement & Key Idea
Answer point location queries in $N$ rectilinear polygons. CCW orientation determines whether vertical edges enter (+1) or exit (-1) the interior, evaluated by sweeping $x$ with a difference-array Fenwick tree in $O((M + Q) \log (\max Y))$.

## 2. Core Observation & Invariant
In any rectilinear polygon, when oriented counter-clockwise, vertical edges going downward enter the polygon interior (adding $+1$ to the $y$-interval), while vertical edges going upward exit the interior (adding $-1$). Point location for $(X + 0.5, Y + 0.5)$ reduces to a 1D point query on the accumulated interval status at $x \le X$ via sweep-line.

## 3. Step-by-Step Algorithm
1. Normalize each polygon to CCW orientation using signed polygon area.
2. For each vertical edge at $x$: downward edges add $+1$ on interval $[y_{\min} + 1, y_{\max}]$, upward edges add $-1$ on the same interval.
3. Sort vertical edge updates and point queries by $x$-coordinate.
4. Sweep along $x$, applying range additions/subtractions in a difference-array Fenwick tree and answering queries in $O((M + Q) \log(\max Y))$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O((M + Q) \log (\max Y))`
- **Space Complexity**: `O(M + Q + \max Y)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_Y = 100005;

struct Fenwick {
    int tree[MAX_Y + 5];
    void add(int i, int v) {
        for (; i <= MAX_Y; i += i & -i) {
            tree[i] += v;
        }
    }
    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) {
            sum += tree[i];
        }
        return sum;
    }
};

Fenwick fenw;

struct Event {
    int x;
    int type; // 0 for segment update, 1 for query
    int y1, y2; // for segment: y1 to y2-1
    int val; // +1 or -1
    int q_id; // for query
    int q_y; // for query
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<Event> events;

    for (int i = 0; i < N; ++i) {
        int M;
        cin >> M;
        vector<pair<long long, long long>> pts(M);
        for (int j = 0; j < M; ++j) {
            cin >> pts[j].first >> pts[j].second;
        }

        // Compute signed area
        long long area2 = 0;
        for (int j = 0; j < M; ++j) {
            int nxt = (j + 1) % M;
            area2 += pts[j].first * pts[nxt].second - pts[nxt].first * pts[j].second;
        }

        // If clockwise, reverse to make counter-clockwise
        if (area2 < 0) {
            reverse(pts.begin(), pts.end());
        }

        // Now process vertical segments
        for (int j = 0; j < M; ++j) {
            int nxt = (j + 1) % M;
            if (pts[j].first == pts[nxt].first) {
                int x = pts[j].first;
                int y_from = pts[j].second;
                int y_to = pts[nxt].second;

                if (y_from > y_to) {
                    // Downward edge: Enter (+1) for [y_to, y_from - 1]
                    // 1-based indexing for Fenwick: y + 1
                    events.push_back({x, 0, y_to + 1, y_from, +1, -1, -1});
                } else {
                    // Upward edge: Exit (-1) for [y_from, y_to - 1]
                    events.push_back({x, 0, y_from + 1, y_to, -1, -1, -1});
                }
            }
        }
    }

    int Q;
    if (!(cin >> Q)) return 0;
    for (int q = 0; q < Q; ++q) {
        int x, y;
        cin >> x >> y;
        events.push_back({x, 1, 0, 0, 0, q, y + 1});
    }

    sort(events.begin(), events.end(), [](const Event& a, const Event& b) {
        if (a.x != b.x) return a.x < b.x;
        return a.type < b.type; // segments first, then queries
    });

    vector<int> ans(Q);
    for (const auto& ev : events) {
        if (ev.type == 0) {
            // Range update: [y1, y2]
            fenw.add(ev.y1, ev.val);
            fenw.add(ev.y2 + 1, -ev.val);
        } else {
            ans[ev.q_id] = fenw.query(ev.q_y);
        }
    }

    for (int q = 0; q < Q; ++q) {
        cout << ans[q] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
