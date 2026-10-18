# Problem Analysis: AtCoder-arc024_4 — D - バス停

**Problem ID**: `AtCoder-arc024_4`  
**Contest**: `arc024`  
**Rating / Difficulty**: 2496  
**URL**: https://atcoder.jp/contests/arc024/tasks/arc024_4  
**VJudge Tag**: `[problem:AtCoder-arc024_4]`  
**Category File**: [`../categories/basics/bus_stops_divide_and_conquer_median_grid.md`](../categories/basics/bus_stops_divide_and_conquer_median_grid.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Divide and Conquer`  
- **Topic (Skill)**: `Divide and Conquer`  

---

## 1. Problem Statement & Key Idea
Add at most $10000 - N$ bus stops at lattice intersections so that the shortest grid route between any two bus stops equals their Manhattan distance.

## 2. Core Observation & Invariant
Using median Divide and Conquer on $x$-coordinates: for a point set $S$, let $x_{mid}$ be the median $x$-coordinate. For every point $(x, y) \in S$, we add the projection $(x_{mid}, y)$. This connects all points in $S$ to the vertical line $x = x_{mid}$ via a single horizontal edge. Points on opposite sides of $x_{mid}$ can travel monotonically $(x, y) \to (x_{mid}, y) \to (x_{mid}, y') \to (x', y')$, with total length $|x - x'| + |y - y'|$. Recursively applying this to the left and right halves achieves pairwise Manhattan connectivity in depth $\lceil \log_2 N \rceil \le 10$, adding at most $N \log_2 N \le 10,000$ points.

## 3. Step-by-Step Algorithm
1. 1. Define recursive function `dnc(sub)` for a subset of points.
2. 2. If `sub.size() <= 1`, return.
3. 3. Sort `sub` by $x$-coordinate and find median $x_{mid}$.
4. 4. For each point $(x, y) \in \text{sub}$ with $x \ne x_{mid}$, add $(x_{mid}, y)$ to the set of added stops if not already present.
5. 5. Split `sub` at the median and recursively call `dnc` on the left and right halves.
6. 6. Print the count $M$ and the coordinates of all added stops.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log^2 N)`
- **Space Complexity**: `O(N \log N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

struct Point {
    int x, y;
    bool operator<(const Point& o) const {
        if (x != o.x) return x < o.x;
        return y < o.y;
    }
    bool operator==(const Point& o) const {
        return x == o.x && y == o.y;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<Point> pts(N);
    set<Point> orig;
    for (int i = 0; i < N; ++i) {
        cin >> pts[i].x >> pts[i].y;
        orig.insert(pts[i]);
    }

    set<Point> added;

    auto dnc = [&](auto& self, vector<Point> sub) -> void {
        if (sub.size() <= 1) return;
        sort(sub.begin(), sub.end());
        int mid = sub.size() / 2;
        int x_mid = sub[mid].x;

        for (const auto& p : sub) {
            if (p.x != x_mid) {
                Point cand = {x_mid, p.y};
                if (orig.find(cand) == orig.end()) {
                    added.insert(cand);
                }
            }
        }

        vector<Point> left_sub(sub.begin(), sub.begin() + mid);
        vector<Point> right_sub(sub.begin() + mid, sub.end());
        self(self, left_sub);
        self(self, right_sub);
    };

    dnc(dnc, pts);

    cout << added.size() << "\n";
    for (const auto& p : added) {
        cout << p.x << " " << p.y << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
