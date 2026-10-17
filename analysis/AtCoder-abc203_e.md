# Problem Analysis: AtCoder-abc203_e — White Pawn

**Problem ID**: `AtCoder-abc203_e`  
**Contest**: `abc203`  
**Rating / Difficulty**: 1750  
**URL**: https://atcoder.jp/contests/abc203/tasks/abc203_e  
**VJudge Tag**: `[problem:AtCoder-abc203_e]`  
**Category File**: [`../categories/data_structures/coordinate_set_sweep_pawn_moves.md`](../categories/data_structures/coordinate_set_sweep_pawn_moves.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Sweep-Line`  
- **Topic (Skill)**: `Coordinate Set Row Sweep-Line with Simultaneous Block/Capture Transitions`  

---

## 1. Problem Statement & Key Idea
A white pawn starts at (0, N) on a (2N + 1) x (2N + 1) board. M black pawns are placed at (X_i, Y_i). White moves from row x to x + 1: moving straight to (x+1, y) requires cell to be empty; moving diagonally to (x+1, y-1) or (x+1, y+1) requires cell to contain a black pawn. Find the number of reachable column coordinates in row 2N.

**Key Insight**: Sort black pawns by row X. Maintain a set S of currently reachable columns. For each row X with pawns, pawns block straight movement (erased if not diagonally reachable) and allow diagonal capture (inserted if adjacent was reachable).

## 2. Core Observation & Invariant
Group all black pawns in the same row and perform removals and insertions simultaneously.

## 3. Step-by-Step Algorithm
1. Maintain set<int> S = {N}.
2. Sort pawns by row X.
3. For each group of pawns in row X:
4.   Collect to_add: pawn column y where y - 1 in S or y + 1 in S.
5.   Collect to_remove: pawn column y where y in S.
6.   Remove all to_remove from S.
7.   Insert all to_add into S.
8. Print S.size().

## 4. Complexity Analysis
- **Time Complexity**: `O(M log M)`
- **Space Complexity**: `O(M)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Simultaneous row sweep-line update on reachable coordinate sets.
- **Reusable Pattern**: `Row Sweep Reachability: Group by row, compute add/remove sets simultaneously, then apply.`
