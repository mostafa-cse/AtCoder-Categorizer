# Problem Analysis: AtCoder-panasonic2020_f — F - Fractal Shortest Path

**Problem ID**: `AtCoder-panasonic2020_f`  
**Contest**: `panasonic2020`  
**Rating / Difficulty**: 2834  
**URL**: https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_f  
**VJudge Tag**: `[problem:AtCoder-panasonic2020_f]`  
**Category File**: [`../categories/basics/sierpinski_carpet_fractal_shortest_path.md`](../categories/basics/sierpinski_carpet_fractal_shortest_path.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Divide and Conquer`  
- **Topic (Skill)**: `Divide and Conquer`  

---

## 1. Problem Statement & Key Idea
Given a Level 30 Sierpinski carpet fractal of size 3^30 x 3^30 where center blocks of size 3^t x 3^t are solid black obstacles, answer Q queries finding the shortest path distance through white cells between (a, b) and (c, d).

## 2. Core Observation & Invariant
On a grid without obstacles, distance is L1 Manhattan distance |x1 - x2| + |y1 - y2|. Black squares form square obstacles of size 3^t for t in 0..30. A path between two points must detour around at most one maximal blocking obstacle of size 3^t at any level. The extra detour around an obstacle of size 3^t is 2 * min(min(x1%3^t, x2%3^t) + 1, 3^t - max(x1%3^t, x2%3^t)). The exact distance equals the Manhattan distance plus 2 * max(extra_x, extra_y).

## 3. Step-by-Step Algorithm
1. 1. Convert coordinates to 0-indexed.
2. 2. Base distance is |x1 - x2| + |y1 - y2|.
3. 3. For each power of three 3^t for t in 0..34, check if an obstacle at level t lies strictly between (x1, y1) and (x2, y2) using base-3 ternary digit analysis.
4. 4. If an obstacle of size 3^t separates the coordinates along an axis, compute the minimal detour around its boundary.
5. 5. The answer is Manhattan distance + 2 * max(detour_x, detour_y).
6. 6. Answer each query in O(log_3(Grid)) = O(35) time.

## 4. Complexity Analysis
- **Time Complexity**: `O(Q * log_3(Grid))`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long ll;

bool between(ll x, ll y1, ll y2) {
    if (y1 > y2) swap(y1, y2);
    y1++;
    y2--;
    if (!(y1 <= y2)) return false;

    while (x > 0) {
        if (x % 3 == 1) {
            if (y2 - y1 > 3) return true;
            for (ll y = y1; y <= y2; ++y) {
                if (y % 3 == 1) return true;
            }
        }
        x /= 3;
        y1 /= 3;
        y2 /= 3;
    }
    return false;
}

ll get_extra(ll x1, ll y1, ll x2, ll y2) {
    ll ans = 0;
    ll three = 1;
    for (int i = 0; i < 35; ++i) {
        if (x1 / three == x2 / three && between(x1 / three, y1 / three, y2 / three)) {
            ll tmp = min(min(x1 % three, x2 % three) + 1, three - max(x1 % three, x2 % three));
            ans = max(ans, tmp);
        }
        if (three > 1e16) break;
        three *= 3;
    }
    return ans;
}

ll get_dist(ll x1, ll y1, ll x2, ll y2) {
    return abs(x1 - x2) + abs(y1 - y2) + 2 * max(get_extra(x1, y1, x2, y2), get_extra(y1, x1, y2, x2));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int q;
    if (cin >> q) {
        while (q--) {
            ll a, b, c, d;
            cin >> a >> b >> c >> d;
            // 0-based conversion
            --a; --b; --c; --d;
            cout << get_dist(a, b, c, d) << "\n";
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
