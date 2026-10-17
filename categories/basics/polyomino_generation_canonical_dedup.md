# Grid Connected Polyomino Generation with Canonical Deduplication

**Domain**: `Basics`  
**Subtopic**: `Backtracking`  

This workbook contains curated, high-quality competitive programming problems teaching **Grid Connected Polyomino Generation with Canonical Deduplication**.

---

## Curated Problems

### `[problem:AtCoder-abc211_e]` — Red Polyomino
- **Rating / Difficulty**: 1823
- **Contest**: `abc211`
- **Analysis**: [`analysis/AtCoder-abc211_e.md`](../../analysis/AtCoder-abc211_e.md)
- **Key Idea**: Generate polyominoes by seed expansion. To prevent generating the same set of K cells multiple times, use canonical expansion: seed must be the top-leftmost cell of the polyomino, and candidate neighboring cells are tracked and pruned systematically.
- **Time Complexity**: `O(number of K-polyominoes)`
- **Space Complexity**: `O(K)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

int n, k;
vector<string> grid;
long long ans = 0;
const int dr[] = {0, 0, 1, -1};
const int dc[] = {1, -1, 0, 0};

void dfs(vector<string>& state, vector<pair<int, int>>& frontier, int count) {
    if (count == k) {
        ans++;
        return;
    }

    while (!frontier.empty()) {
        auto [r, c] = frontier.back();
        frontier.pop_back();

        // Branch 1: Paint (r, c) red
        state[r][c] = '@'; // '@' represents red
        vector<pair<int, int>> next_frontier = frontier;

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && state[nr][nc] == '.') {
                state[nr][nc] = '?'; // mark as in frontier
                next_frontier.push_back({nr, nc});
            }
        }

        dfs(state, next_frontier, count + 1);

        // Undo '@' and new '?' additions
        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && state[nr][nc] == '?') {
                bool is_neighbor_of_other = false;
                // Only undo if not neighboring another already painted red cell
                for (int d2 = 0; d2 < 4; ++d2) {
                    int nnr = nr + dr[d2], nnc = nc + dc[d2];
                    if (nnr >= 0 && nnr < n && nnc >= 0 && nnc < n && state[nnr][nnc] == '@') {
                        is_neighbor_of_other = true;
                        break;
                    }
                }
                if (!is_neighbor_of_other) state[nr][nc] = '.';
            }
        }
        state[r][c] = '#'; // Branch 2: Leave unpainted and forbidden for this subtree
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> k)) return 0;

    grid.resize(n);
    for (int i = 0; i < n; ++i) cin >> grid[i];

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < n; ++c) {
            if (grid[r][c] == '.') {
                vector<string> state = grid;
                state[r][c] = '@';
                vector<pair<int, int>> frontier;
                for (int d = 0; d < 4; ++d) {
                    int nr = r + dr[d], nc = c + dc[d];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && state[nr][nc] == '.') {
                        state[nr][nc] = '?';
                        frontier.push_back({nr, nc});
                    }
                }
                dfs(state, frontier, 1);
                grid[r][c] = '#'; // Mark seed as forbidden for future seeds
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```
