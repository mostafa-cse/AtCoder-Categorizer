# Digit Transformation Graph via Floyd-Warshall

**Domain**: `Graph Theory`  
**Subtopic**: `All-Pairs Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Digit Transformation Graph via Floyd-Warshall**.

---

## Curated Problems

### [problem:AtCoder-abc079_d] — Wall
- **Contest**: `abc079`
- **Rating / Difficulty**: 949
- **Specific Skill**: Digit Transformation Graph via Floyd-Warshall
- **Individual Analysis**: [`../../analysis/AtCoder-abc079_d.md`](../../analysis/AtCoder-abc079_d.md)
- **Problem Statement Summary**: An H x W wall contains digits 0..9 and -1. Transforming digit i to j costs c_{i, j}. Find the minimum total cost to transform every digit on the wall into 1.
- **Core Insight**: Run Floyd-Warshall on the 10 x 10 cost matrix in 10^3 = 1000 operations. Then for each cell on the wall containing digit d != -1, add the optimal cost dist[d][1].
- **Complexity**: Time: `O(10^3 + H * W)` | Space: `O(10^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<vector<int>> c(10, vector<int>(10));
    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < 10; ++j) {
            cin >> c[i][j];
        }
    }

    for (int k = 0; k < 10; ++k) {
        for (int i = 0; i < 10; ++i) {
            for (int j = 0; j < 10; ++j) {
                c[i][j] = min(c[i][j], c[i][k] + c[k][j]);
            }
        }
    }

    long long total_cost = 0;
    for (int r = 0; r < h; ++r) {
        for (int col = 0; col < w; ++col) {
            int d;
            cin >> d;
            if (d != -1 && d != 1) {
                total_cost += c[d][1];
            }
        }
    }

    cout << total_cost << "\n";
    return 0;
}
```
