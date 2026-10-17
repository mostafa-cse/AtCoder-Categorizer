# Problem Analysis: AtCoder-arc039_c — 幼稚園児高橋君

**Problem ID**: `AtCoder-arc039_c`  
**Contest**: `arc039`  
**Rating / Difficulty**: 2004  
**URL**: https://atcoder.jp/contests/arc039/tasks/arc039_c  
**VJudge Tag**: `[problem:AtCoder-arc039_c]`  
**Category File**: [`../categories/data_structures/2d_4way_linked_list_grid_path_compression.md`](../categories/data_structures/2d_4way_linked_list_grid_path_compression.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `2D 4-Way Doubly Linked List Node Deletion and Grid Path Compression`  

---

## 1. Problem Statement & Key Idea
Starting at (0, 0) on an infinite 2D grid, Takahashi follows a sequence of K moves (L, R, U, D). In each move, he skips over all already visited cells in that direction and lands on the first unvisited cell, marking it visited. Find his final coordinates.

**Key Idea**: Treat visited cells as deleted nodes in a 2D doubly linked list (or 4-directional pointer hopping). When a cell (x, y) is visited, it stores pointers to its nearest unvisited neighbors in the 4 directions (L, R, D, U). When visiting (x, y), its 4 neighbors' reciprocal pointers are updated to bypass (x, y), exactly like doubly linked list node deletion extended to 4 dimensions. Dynamically allocated via std::map.

## 2. Core Observation & Invariant
Visited cell hopping on a grid is equivalent to deleting elements from horizontal and vertical linked lists simultaneously.

## 3. Step-by-Step Algorithm
1. Represent pointers using a map from pair<int,int> to array<pair<int,int>, 4>.
2. Initialize (0, 0) as visited with neighbors (0, -1) for L, (0, 1) for R, (-1, 0) for D, (1, 0) for U.
3. For each command dir in {L, R, U, D}:
4.   Move to nxt[cur][dir]. Let this be next_pos.
5.   For each direction d in {0, 1, 2, 3}, get the neighbor in direction d.
6.   Update neighbors' opposite pointers to bypass next_pos.
7.   cur = next_pos.
8. Output cur.x and cur.y.

## 4. Complexity Analysis
- **Time Complexity**: `O(K log K)`
- **Space Complexity**: `O(K)`

## 5. Core Algorithmic Skill & Learning Takeaway
2D 4-way pointer hopping / linked list deletion in sparse coordinate space.

**Reusable Pattern**: 4-Way Grid Pointer Bypass: When cell C is visited, update left neighbor's right pointer to C's right neighbor, and vice versa.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <map>
#include <string>
#include <array>

using namespace std;

// Directions: 0: L, 1: R, 2: D, 3: U
const int DX[4] = {0, 0, -1, 1};
const int DY[4] = {-1, 1, 0, 0};
const int OPP[4] = {1, 0, 3, 2};

map<pair<int, int>, array<pair<int, int>, 4>> nxt;

pair<int, int> get_ptr(pair<int, int> pos, int dir) {
    auto it = nxt.find(pos);
    if (it != nxt.end()) {
        return it->second[dir];
    }
    return {pos.first + DX[dir], pos.second + DY[dir]};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;
    string s;
    cin >> s;

    pair<int, int> cur = {0, 0};
    // Initialize (0, 0)
    array<pair<int, int>, 4> init_ptrs;
    for (int d = 0; d < 4; ++d) {
        init_ptrs[d] = {cur.first + DX[d], cur.second + DY[d]};
    }
    nxt[cur] = init_ptrs;

    for (char c : s) {
        int dir;
        if (c == 'L') dir = 0;
        else if (c == 'R') dir = 1;
        else if (c == 'D') dir = 2;
        else dir = 3;

        pair<int, int> target = get_ptr(cur, dir);

        // Target is now visited, determine its 4 neighbors
        array<pair<int, int>, 4> target_ptrs;
        for (int d = 0; d < 4; ++d) {
            target_ptrs[d] = get_ptr(target, d);
        }
        nxt[target] = target_ptrs;

        // Bypass target in all 4 neighbors
        for (int d = 0; d < 4; ++d) {
            pair<int, int> neighbor = target_ptrs[d];
            int opp_dir = OPP[d];
            // Ensure neighbor is instantiated in map
            if (nxt.find(neighbor) == nxt.end()) {
                array<pair<int, int>, 4> n_ptrs;
                for (int dd = 0; dd < 4; ++dd) {
                    n_ptrs[dd] = {neighbor.first + DX[dd], neighbor.second + DY[dd]};
                }
                nxt[neighbor] = n_ptrs;
            }
            nxt[neighbor][opp_dir] = target_ptrs[opp_dir];
        }

        cur = target;
    }

    // Problem asks for (X, Y) where X is east (second coord), Y is north (first coord)
    cout << cur.second << " " << cur.first << "\n";
    return 0;
}
```
