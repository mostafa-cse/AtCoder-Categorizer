# Interactive Tree Diameter via 2-Query BFS/DFS

**Domain**: `Graph Theory`  
**Subtopic**: `Tree Diameter`  

This workbook contains curated, high-quality competitive programming problems teaching **Interactive Tree Diameter via 2-Query BFS/DFS**.

---

## Curated Problems

### [problem:AtCoder-abc019_4] — Takahashi and Tree
- **Contest**: `abc019`
- **Rating / Difficulty**: 1378
- **Specific Skill**: Interactive Tree Diameter via 2-Query BFS/DFS
- **Individual Analysis**: [`../../analysis/AtCoder-abc019_4.md`](../../analysis/AtCoder-abc019_4.md)
- **Problem Statement Summary**: An unweighted tree with N vertices (N <= 50). You can ask at most 2N distance queries '? u v' to get the distance between u and v. Find the diameter of the tree.
- **Core Insight**: Pass 1: ask '? 1 i' for all i in 2..N (N - 1 queries). Let u be the vertex maximizing dist(1, u). Pass 2: ask '? u i' for all i != u (N - 1 queries). The maximum distance found is the exact diameter of the tree! Total queries: 2N - 2 <= 2N.
- **Complexity**: Time: `O(N) queries` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int farthest_node = 1;
    long long max_d1 = -1;

    for (int i = 2; i <= n; ++i) {
        cout << "? 1 " << i << endl;
        long long dist;
        cin >> dist;
        if (dist > max_d1) {
            max_d1 = dist;
            farthest_node = i;
        }
    }

    long long diameter = 0;
    for (int i = 1; i <= n; ++i) {
        if (i == farthest_node) continue;
        cout << "? " << farthest_node << " " << i << endl;
        long long dist;
        cin >> dist;
        diameter = max(diameter, dist);
    }

    cout << "! " << diameter << endl;
    return 0;
}
```
