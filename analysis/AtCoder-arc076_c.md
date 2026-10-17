# Problem Analysis: AtCoder-arc076_c — E. Connected?

**Problem ID**: `AtCoder-arc076_c`  
**Contest**: `arc076`  
**Rating / Difficulty**: 2180  
**URL**: https://atcoder.jp/contests/arc076/tasks/arc076_c  
**VJudge Tag**: `[problem:AtCoder-arc076_c]`  
**Category File**: [`../categories/basics/perimeter_mapping_stack_bracket_matching.md`](../categories/basics/perimeter_mapping_stack_bracket_matching.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Standard Template Library (STL)`  
- **Topic (Skill)**: `Stack`  

---

## 1. Problem Statement & Key Idea
Determine if N pairs of numbered points in an R x C rectangle can be connected by non-intersecting continuous curves inside the rectangle. Only pairs where both endpoints lie on the boundary can partition the rectangle; internal points can always be routed freely.

## 2. Core Observation & Invariant
Curves with at least one internal endpoint never form boundary-to-boundary cuts and can always be routed around each other in 2D space. Boundary-to-boundary curves form chords of the rectangle disk. Two chords intersect if and only if their endpoints alternate along the perimeter. Mapping perimeter coordinates clockwise to 1D and checking matching pairs via a stack resolves the question in O(N log N) time.

## 3. Step-by-Step Algorithm
1. Filter pairs: keep only pairs i where both (x_{i,1}, y_{i,1}) and (x_{i,2}, y_{i,2}) lie on the boundary (x in {0, R} or y in {0, C}).
2. Map each boundary point (x, y) to a 1D perimeter coordinate t in [0, 2(R+C)) by walking the perimeter clockwise: bottom (y=0) -> right (x=R) -> top (y=C) -> left (x=0).
3. Store events (t, pair_id) for all kept endpoints and sort them by coordinate t.
4. Traverse the sorted events maintaining a stack: if the top of the stack equals pair_id, pop it; otherwise push pair_id.
5. If the stack is empty after processing all events, print YES; otherwise print NO.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long R, C;
    int N;
    if (!(cin >> R >> C >> N)) return 0;

    auto on_boundary = [&](long long x, long long y) {
        return (x == 0 || x == R || y == 0 || y == C);
    };

    auto get_pos = [&](long long x, long long y) -> long long {
        if (y == 0) return x;
        if (x == R) return R + y;
        if (y == C) return R + C + (R - x);
        if (x == 0) return 2 * R + C + (C - y);
        return -1;
    };

    vector<pair<long long, int>> events;
    events.reserve(2 * N);

    for (int i = 1; i <= N; ++i) {
        long long x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        if (on_boundary(x1, y1) && on_boundary(x2, y2)) {
            events.push_back({get_pos(x1, y1), i});
            events.push_back({get_pos(x2, y2), i});
        }
    }

    sort(events.begin(), events.end());

    vector<int> st;
    st.reserve(events.size());

    for (auto const& ev : events) {
        int id = ev.second;
        if (!st.empty() && st.back() == id) {
            st.pop_back();
        } else {
            st.push_back(id);
        }
    }

    if (st.empty()) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
