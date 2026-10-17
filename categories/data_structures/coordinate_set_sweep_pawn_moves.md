# Coordinate Set Row Sweep-Line with Simultaneous Block/Capture Transitions

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Sweep-Line`  

This workbook contains curated, high-quality competitive programming problems teaching **Coordinate Set Row Sweep-Line with Simultaneous Block/Capture Transitions**.

---

## Curated Problems

### `[problem:AtCoder-abc203_e]` — White Pawn
- **Rating / Difficulty**: 1750
- **Contest**: `abc203`
- **Analysis**: [`analysis/AtCoder-abc203_e.md`](../../analysis/AtCoder-abc203_e.md)
- **Key Idea**: Sort black pawns by row X. Maintain a set S of currently reachable columns. For each row X with pawns, pawns block straight movement (erased if not diagonally reachable) and allow diagonal capture (inserted if adjacent was reachable).
- **Time Complexity**: `O(M log M)`
- **Space Complexity**: `O(M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    map<int, vector<int>> row_pawns;
    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        row_pawns[x].push_back(y);
    }

    set<int> reachable;
    reachable.insert(n);

    for (auto& [row, cols] : row_pawns) {
        vector<int> to_add;
        vector<int> to_remove;

        for (int y : cols) {
            bool can_capture = (reachable.count(y - 1) || reachable.count(y + 1));
            bool is_blocked = reachable.count(y);

            if (can_capture) to_add.push_back(y);
            if (is_blocked) to_remove.push_back(y);
        }

        for (int y : to_remove) reachable.erase(y);
        for (int y : to_add) reachable.insert(y);
    }

    cout << reachable.size() << "\n";
    return 0;
}
```
