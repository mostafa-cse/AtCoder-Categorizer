# Modulo-D Strided Prefix Sums

**Domain**: `Data Structures`  
**Subtopic**: `Prefix Sums`  

This workbook contains curated, high-quality competitive programming problems teaching **Modulo-D Strided Prefix Sums**.

---

## Curated Problems

### [problem:AtCoder-abc089_d] — Practical Skill Test
- **Contest**: `abc089`
- **Rating / Difficulty**: 1220
- **Specific Skill**: Modulo-D Strided Prefix Sums
- **Individual Analysis**: [`../../analysis/AtCoder-abc089_d.md`](../../analysis/AtCoder-abc089_d.md)
- **Problem Statement Summary**: An H x W grid contains numbers 1..H*W. You move from number x to x + D at cost equal to Manhattan distance between their coordinates. Answer Q queries: total cost to move from L to R (where R - L is a multiple of D).
- **Core Insight**: Precompute 1D prefix sums for each modulo class: cost[i] = cost[i - D] + dist(pos[i - D], pos[i]) for all i > D. Then the total cost to move from L to R is simply cost[R] - cost[L] in O(1) per query!
- **Complexity**: Time: `O(H * W + Q)` | Space: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

struct Coord {
    int r, c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, d;
    if (!(cin >> h >> w >> d)) return 0;

    int total_cells = h * w;
    vector<Coord> pos(total_cells + 1);

    for (int r = 1; r <= h; ++r) {
        for (int c = 1; c <= w; ++c) {
            int val;
            cin >> val;
            pos[val] = {r, c};
        }
    }

    vector<long long> cost(total_cells + 1, 0);
    for (int i = d + 1; i <= total_cells; ++i) {
        cost[i] = cost[i - d] + abs(pos[i].r - pos[i - d].r) + abs(pos[i].c - pos[i - d].c);
    }

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << cost[r] - cost[l] << "\n";
    }

    return 0;
}
```
