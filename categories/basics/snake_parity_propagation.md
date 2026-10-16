# Snake Path Parity Propagation

**Domain**: `Basics`  
**Subtopic**: `Constructive Algorithms`  

This workbook contains curated, high-quality competitive programming problems teaching **Snake Path Parity Propagation**.

---

## Curated Problems

### [problem:AtCoder-abc109_d] — Make Them Even
- **Contest**: `abc109`
- **Rating / Difficulty**: 1172
- **Specific Skill**: Snake Path Parity Propagation
- **Individual Analysis**: [`../../analysis/AtCoder-abc109_d.md`](../../analysis/AtCoder-abc109_d.md)
- **Problem Statement Summary**: An H x W grid has coins. You can move 1 coin from (r, c) to an adjacent cell. Maximize the number of cells with an even number of coins.
- **Core Insight**: Traverse cells along the snake path: if the current cell has an odd number of coins, push 1 coin to the next cell in the path! The current cell immediately becomes even. The odd parity propagates forward, leaving every cell even except possibly the very last cell in the path.
- **Complexity**: Time: `O(H * W)` | Space: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Move {
    int r1, c1, r2, c2;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<vector<int>> a(h, vector<int>(w));
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            cin >> a[i][j];
        }
    }

    vector<pair<int, int>> path;
    for (int r = 0; r < h; ++r) {
        if (r % 2 == 0) {
            for (int c = 0; c < w; ++c) path.push_back({r, c});
        } else {
            for (int c = w - 1; c >= 0; --c) path.push_back({r, c});
        }
    }

    vector<Move> moves;
    for (size_t i = 0; i < path.size() - 1; ++i) {
        auto [r, c] = path[i];
        if (a[r][c] % 2 == 1) {
            auto [nr, nc] = path[i + 1];
            a[r][c]--;
            a[nr][nc]++;
            moves.push_back({r + 1, c + 1, nr + 1, nc + 1});
        }
    }

    cout << moves.size() << "\n";
    for (const auto& m : moves) {
        cout << m.r1 << " " << m.c1 << " " << m.r2 << " " << m.c2 << "\n";
    }

    return 0;
}
```
