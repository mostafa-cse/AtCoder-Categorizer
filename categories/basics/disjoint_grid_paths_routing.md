# Disjoint Grid Paths Outer Boundary Routing

**Domain**: `Basics`  
**Subtopic**: `Constructive Algorithms`  

This workbook contains curated, high-quality competitive programming problems teaching **Disjoint Grid Paths Outer Boundary Routing**.

---

## Curated Problems

### [problem:AtCoder-abc051_c] — Back and Forth
- **Contest**: `abc051`
- **Rating / Difficulty**: 968
- **Specific Skill**: Disjoint Grid Paths Outer Boundary Routing
- **Individual Analysis**: [`../../analysis/AtCoder-abc051_c.md`](../../analysis/AtCoder-abc051_c.md)
- **Problem Statement Summary**: On a 2D integer grid, construct 4 paths: S -> T, T -> S, S -> T, T -> S such that no two paths share any vertex except S and T (sx < tx, sy < ty).
- **Core Insight**: 1st trip (S -> T): Right dx, Up dy. 2nd trip (T -> S): Left dx, Down dy. 3rd trip (S -> T): Down 1, Right dx+1, Up dy+1, Left 1. 4th trip (T -> S): Up 1, Left dx+1, Down dy+1, Right 1. All 4 paths are internally vertex-disjoint.
- **Complexity**: Time: `O(dx + dy)` | Space: `O(dx + dy)`
- **Verified C++ Implementation**:
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
