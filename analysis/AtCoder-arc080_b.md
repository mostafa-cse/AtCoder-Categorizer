# Problem Analysis: AtCoder-arc080_b — Grid Coloring

**Problem ID**: `AtCoder-arc080_b`  
**Contest**: `abc069`  
**Rating / Difficulty**: 852  
**URL**: https://atcoder.jp/contests/abc069/tasks/arc080_b  
**VJudge Tag**: `[problem:AtCoder-arc080_b]`  
**Category File**: [`../categories/basics/snake_boustrophedon_fill.md`](../categories/basics/snake_boustrophedon_fill.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Grid Traversal`  
- **Topic (Skill)**: `Snake / Boustrophedon Connected Fill`  

---

## 1. Problem Statement & Key Idea
Given an H x W grid and N colors, where color i must be used exactly a_i times (sum a_i = H * W). Paint each cell such that the cells of each color form a single 4-directionally connected component.

**Key Idea**: A Hamiltonian path across the grid visits all cells such that consecutive cells are always adjacent. Painting consecutive segments along this path guarantees connectivity for every color.

## 2. Core Observation & Invariant
Boustrophedon (snake-like) traversal: visit even rows left-to-right (0 to W-1) and odd rows right-to-left (W-1 down to 0). This creates a simple continuous path through all H * W cells.

## 3. Step-by-Step Algorithm
1. Flatten the required colors into a 1D sequence of length H * W.
2. Traverse the grid row by row: for even rows traverse col 0..W-1; for odd rows traverse col W-1..0.
3. Assign the next color in the sequence to grid[r][c].
4. Print the resulting H x W grid.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, n;
    if (!(cin >> h >> w >> n)) return 0;

    vector<int> a(n);
    vector<int> stream;
    stream.reserve(h * w);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        for (int k = 0; k < a[i]; ++k) {
            stream.push_back(i + 1);
        }
    }

    vector<vector<int>> grid(h, vector<int>(w));
    int idx = 0;

    for (int r = 0; r < h; ++r) {
        if (r % 2 == 0) {
            for (int c = 0; c < w; ++c) {
                grid[r][c] = stream[idx++];
            }
        } else {
            for (int c = w - 1; c >= 0; --c) {
                grid[r][c] = stream[idx++];
            }
        }
    }

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            cout << grid[r][c] << (c + 1 == w ? '\n' : ' ');
        }
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Connected component preservation on grids using space-filling curves / snake traversal.
- **Reusable Pattern**: `Boustrophedon grid routing ensures contiguous segments are 4-connected.`
