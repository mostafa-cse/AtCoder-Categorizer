# Bitmask Grid Shapes with Connectivity (DSU) and Hole-Free (Outer BFS) Checking

**Domain**: `Basics`  
**Subtopic**: `Bitmask Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Bitmask Grid Shapes with Connectivity (DSU) and Hole-Free (Outer BFS) Checking**.

---

## Curated Problems

### `[problem:AtCoder-abc219_e]` — Moat
- **Rating / Difficulty**: 1690
- **Contest**: `abc219`
- **Analysis**: [`analysis/AtCoder-abc219_e.md`](../../analysis/AtCoder-abc219_e.md)
- **Key Idea**: The grid has only 16 cells, meaning 2^16 = 65,536 subsets! Enumerate all subsets mask and check: 1) mask has all houses; 2) moat cells form 1 connected component; 3) outer white cells (padded to 6x6) form 1 connected component (guaranteeing no holes).
- **Time Complexity**: `O(2^16 * 36)`
- **Space Complexity**: `O(36)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int dr[4] = {-1, 1, 0, 0};
const int dc[4] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int house_mask = 0;
    for (int r = 0; r < 4; ++r) {
        for (int c = 0; c < 4; ++c) {
            int val;
            if (cin >> val && val == 1) {
                house_mask |= (1 << (r * 4 + c));
            }
        }
    }

    int total_masks = 1 << 16;
    int ans = 0;

    for (int mask = 1; mask < total_masks; ++mask) {
        // Condition 1: Contains all houses
        if ((mask & house_mask) != house_mask) continue;

        // Condition 2: Moat is connected
        int start_cell = __builtin_ctz(mask);
        int visited_moat = 0;
        queue<int> q;
        q.push(start_cell);
        visited_moat |= (1 << start_cell);

        while (!q.empty()) {
            int cell = q.front();
            q.pop();
            int r = cell / 4, c = cell % 4;
            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < 4 && nc >= 0 && nc < 4) {
                    int ncell = nr * 4 + nc;
                    if ((mask & (1 << ncell)) && !(visited_moat & (1 << ncell))) {
                        visited_moat |= (1 << ncell);
                        q.push(ncell);
                    }
                }
            }
        }

        if (visited_moat != mask) continue;

        // Condition 3: No holes (outer complement is connected on 6x6 grid)
        vector<vector<bool>> is_moat(6, vector<bool>(6, false));
        for (int r = 0; r < 4; ++r) {
            for (int c = 0; c < 4; ++c) {
                if (mask & (1 << (r * 4 + c))) {
                    is_moat[r + 1][c + 1] = true;
                }
            }
        }

        vector<vector<bool>> vis_outer(6, vector<bool>(6, false));
        queue<pair<int, int>> q_out;
        q_out.push({0, 0});
        vis_outer[0][0] = true;
        int outer_reach = 0;

        while (!q_out.empty()) {
            auto [r, c] = q_out.front();
            q_out.pop();
            outer_reach++;

            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < 6 && nc >= 0 && nc < 6) {
                    if (!is_moat[nr][nc] && !vis_outer[nr][nc]) {
                        vis_outer[nr][nc] = true;
                        q_out.push({nr, nc});
                    }
                }
            }
        }

        if (outer_reach == 36 - __builtin_popcount(mask)) {
            ans++;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
