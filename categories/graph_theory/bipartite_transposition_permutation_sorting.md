# Bipartite Transposition Permutation Sorting via Permutation Cycle Decomposition

**Domain**: `Graph Theory`  
**Subtopic**: `Directed Graphs`  

This workbook contains curated, high-quality competitive programming problems teaching **Bipartite Transposition Permutation Sorting via Permutation Cycle Decomposition**.

---

## Curated Problems

### `[problem:AtCoder-arc124_d]` — Yet Another Sorting Problem
- **Rating / Difficulty**: 2008
- **Contest**: `arc124`
- **Analysis**: [`analysis/AtCoder-arc124_d.md`](../../analysis/AtCoder-arc124_d.md)
- **Key Idea**: Decompose the permutation into disjoint cycles. Normally, sorting a cycle of length S takes S - 1 swaps. With bipartite swap restrictions, a mixed cycle containing both white and black positions can still be resolved in S - 1 swaps. A monochromatic cycle cannot be resolved alone: it requires borrowing a node of the opposite color. Pairing one white-only cycle with one black-only cycle resolves both in S_W + S_B swaps. Unpaired monochromatic cycles take S + 1 swaps. Total answer is sum_{cycles} (S - 1) + 2 * max(cnt_white_only, cnt_black_only).
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    int total = n + m;
    vector<int> p(total + 1);
    for (int i = 1; i <= total; ++i) {
        cin >> p[i];
    }

    vector<bool> visited(total + 1, false);
    int c_white = 0, c_black = 0;
    int base_swaps = 0;

    for (int i = 1; i <= total; ++i) {
        if (!visited[i]) {
            int cur = i;
            int len = 0;
            int white_cnt = 0, black_cnt = 0;

            while (!visited[cur]) {
                visited[cur] = true;
                len++;
                if (cur <= n) white_cnt++;
                else black_cnt++;
                cur = p[cur];
            }

            if (len > 1) {
                base_swaps += (len - 1);
                if (white_cnt > 0 && black_cnt == 0) c_white++;
                else if (black_cnt > 0 && white_cnt == 0) c_black++;
            }
        }
    }

    int ans = base_swaps + 2 * max(c_white, c_black);
    cout << ans << "\n";

    return 0;
}
```
