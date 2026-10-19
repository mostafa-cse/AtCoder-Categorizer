# Problem Analysis: AtCoder-abc244_h — Ex. Linear Maximization

**Problem ID**: `AtCoder-abc244_h`  
**Contest**: `abc244`  
**Rating / Difficulty**: 2878  
**URL**: https://atcoder.jp/contests/abc244/tasks/abc244_h  
**VJudge Tag**: `[problem:AtCoder-abc244_h]`  
**Category File**: [`../categories/geometry/dynamic_convex_hull_offline_cdq.md`](../categories/geometry/dynamic_convex_hull_offline_cdq.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Convex Polygon`  
- **Topic (Skill)**: `Dynamic Convex Hull`  

---

## 1. Problem Statement & Key Idea
Process Q operations online: add point (X_i, Y_i) to set S, or query max_{(x, y) in S} (A_i x + B_i y).

## 2. Core Observation & Invariant
Maximizing a linear function A x + B y over a set of points corresponds to finding extreme vertices on the upper/lower convex hull. Because points are added dynamically, offline CDQ divide-and-conquer can process insertions in the left half and answer queries in the right half via ternary search / two pointers on the static convex hull in O(Q log^2 Q) time.

## 3. Step-by-Step Algorithm
1. 1. Read all Q queries offline.
2. 2. Apply CDQ divide-and-conquer on query index range [L, R].
3. 3. Recursively solve left half [L, M].
4. 4. Collect points inserted in [L, M] and construct their upper and lower convex hulls via Graham scan.
5. 5. For each query in [M+1, R], find optimal point on hull via ternary search.
6. 6. Recursively solve right half [M+1, R].

## 4. Complexity Analysis
- **Time Complexity**: `O(Q log^2 Q)`
- **Space Complexity**: `O(Q)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    long long x, y;
    bool operator<(const Point& other) const {
        if (x != other.x) return x < other.x;
        return y < other.y;
    }
    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
};

struct Query {
    long long x, y, a, b;
};

long long cross_product(const Point& o, const Point& a, const Point& b) {
    __int128 x1 = a.x - o.x;
    __int128 y1 = a.y - o.y;
    __int128 x2 = b.x - o.x;
    __int128 y2 = b.y - o.y;
    __int128 cp = x1 * y2 - y1 * x2;
    if (cp > 0) return 1;
    if (cp < 0) return -1;
    return 0;
}

long long dot(const Point& p, long long a, long long b) {
    return p.x * a + p.y * b;
}

long long ternary_search_chain(const vector<Point>& chain, long long a, long long b) {
    if (chain.empty()) return -4e18;
    int low = 0, high = (int)chain.size() - 1;
    while (high - low > 3) {
        int m1 = low + (high - low) / 3;
        int m2 = high - (high - low) / 3;
        if (dot(chain[m1], a, b) < dot(chain[m2], a, b)) {
            low = m1;
        } else {
            high = m2;
        }
    }
    long long best = dot(chain[low], a, b);
    for (int i = low + 1; i <= high; ++i) {
        best = max(best, dot(chain[i], a, b));
    }
    return best;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int q;
    if (!(cin >> q)) return 0;

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].x >> queries[i].y >> queries[i].a >> queries[i].b;
    }

    vector<long long> ans(q, -4e18);

    auto cdq = [&](auto& self, int L, int R) -> void {
        if (L == R) {
            ans[L] = max(ans[L], queries[L].a * queries[L].x + queries[L].b * queries[L].y);
            return;
        }

        int mid = L + (R - L) / 2;
        self(self, L, mid);

        // Build hull of points in L..mid
        vector<Point> pts;
        pts.reserve(mid - L + 1);
        for (int i = L; i <= mid; ++i) {
            pts.push_back({queries[i].x, queries[i].y});
        }
        sort(pts.begin(), pts.end());
        pts.erase(unique(pts.begin(), pts.end()), pts.end());

        vector<Point> lower, upper;
        for (const auto& p : pts) {
            while (lower.size() >= 2 && cross_product(lower[lower.size() - 2], lower.back(), p) <= 0) {
                lower.pop_back();
            }
            lower.push_back(p);
        }
        for (int i = (int)pts.size() - 1; i >= 0; --i) {
            const auto& p = pts[i];
            while (upper.size() >= 2 && cross_product(upper[upper.size() - 2], upper.back(), p) <= 0) {
                upper.pop_back();
            }
            upper.push_back(p);
        }

        for (int i = mid + 1; i <= R; ++i) {
            long long a = queries[i].a;
            long long b = queries[i].b;
            long long best = max(ternary_search_chain(lower, a, b), ternary_search_chain(upper, a, b));
            ans[i] = max(ans[i], best);
        }

        self(self, mid + 1, R);
    };

    cdq(cdq, 0, q - 1);

    for (int i = 0; i < q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
