# Problem Analysis: AtCoder-abc051_c — Back and Forth

**Problem ID**: `AtCoder-abc051_c`  
**Contest**: `abc051`  
**Rating / Difficulty**: 968  
**URL**: https://atcoder.jp/contests/abc051/tasks/abc051_c  
**VJudge Tag**: `[problem:AtCoder-abc051_c]`  
**Category File**: [`../categories/basics/disjoint_grid_paths_routing.md`](../categories/basics/disjoint_grid_paths_routing.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Constructive Algorithms`  
- **Topic (Skill)**: `Disjoint Grid Paths Outer Boundary Routing`  

---

## 1. Problem Statement & Key Idea
On a 2D integer grid, construct 4 paths: S -> T, T -> S, S -> T, T -> S such that no two paths share any vertex except S and T (sx < tx, sy < ty).

**Key Idea**: The bounding box of S and T is [sx, tx] x [sy, ty]. We can route 2 paths along the inner perimeter of the bounding box, and 2 paths around the outer perimeter expanded by 1 unit.

## 2. Core Observation & Invariant
1st trip (S -> T): Right dx, Up dy. 2nd trip (T -> S): Left dx, Down dy. 3rd trip (S -> T): Down 1, Right dx+1, Up dy+1, Left 1. 4th trip (T -> S): Up 1, Left dx+1, Down dy+1, Right 1. All 4 paths are internally vertex-disjoint.

## 3. Step-by-Step Algorithm
1. Compute dx = tx - sx and dy = ty - sy.
2. Trip 1: string(dx, 'U') + string(dy, 'R') (or R then U).
3. Trip 2: string(dx, 'D') + string(dy, 'L') (or L then D).
4. Trip 3: 'D' + string(dx + 1, 'R') + string(dy + 1, 'U') + 'L'.
5. Trip 4: 'U' + string(dx + 1, 'L') + string(dy + 1, 'D') + 'R'.
6. Concatenate and output.

## 4. Complexity Analysis
- **Time Complexity**: `O(dx + dy)`
- **Space Complexity**: `O(dx + dy)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int sx, sy, tx, ty;
    if (!(cin >> sx >> sy >> tx >> ty)) return 0;

    int dx = tx - sx;
    int dy = ty - sy;

    string path = "";

    // 1st trip: S -> T
    path += string(dy, 'U');
    path += string(dx, 'R');

    // 2nd trip: T -> S
    path += string(dy, 'D');
    path += string(dx, 'L');

    // 3rd trip: S -> T (outer boundary)
    path += 'L';
    path += string(dy + 1, 'U');
    path += string(dx + 1, 'R');
    path += 'D';

    // 4th trip: T -> S (outer boundary)
    path += 'R';
    path += string(dy + 1, 'D');
    path += string(dx + 1, 'L');
    path += 'U';

    cout << path << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Vertex-disjoint grid path construction via nested bounding box boundaries.
- **Reusable Pattern**: `Disjoint round trips: route one round trip inside bounding box, second outside.`
