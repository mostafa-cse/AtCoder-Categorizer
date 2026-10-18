# Problem Analysis: AtCoder-arc095_c — E. Symmetric Grid

**Problem ID**: `AtCoder-arc095_c`  
**Contest**: `arc095`  
**Rating / Difficulty**: 2441  
**URL**: https://atcoder.jp/contests/arc095/tasks/arc095_c  
**VJudge Tag**: `[problem:AtCoder-arc095_c]`  
**Category File**: [`../categories/miscellaneous/symmetric_grid_row_column_pairing_backtracking.md`](../categories/miscellaneous/symmetric_grid_row_column_pairing_backtracking.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Backtracking`  

---

## 1. Problem Statement & Key Idea
Determine if swapping rows and columns can make an $H \times W$ grid ($H, W \le 12$) symmetric under 180-degree rotation. By transposing if necessary, assume $H \le W \le 12$. The $H$ rows must be partitioned into pairs $(u, v)$ (and at most one center row if $H$ is odd). There are at most $11!! = 10395$ such row pairings. For each fixed row pairing, check if the $W$ columns can be paired up to match symmetric signatures.

## 2. Core Observation & Invariant
For columns $c_1$ and $c_2$ to pair symmetrically, their characters across all paired rows must be reverse complements of each other ($S[u][c_1] == S[v][c_2]$ and $S[v][c_1] == S[u][c_2]$). Column signatures allow greedy matching in $O(W^2)$ time per row pairing.

## 3. Step-by-Step Algorithm
1. 1. Transpose the grid if $H > W$ to ensure $H \le 12$.
2. 2. Generate all pairings of $H$ rows via recursive backtracking (handling the center row if $H$ is odd).
3. 3. For each row pairing:
4.    - Build column signatures: $sig(c) = (S[u_k][c], S[v_k][c], \dots)$ and reverse signatures $rev(c) = (S[v_k][c], S[u_k][c], \dots)$.
5.    - Pair up columns greedily: match column $i$ with any unused $j$ having $sig(i) == rev(j)$.
6.    - If $W$ is odd, allow at most one self-symmetric column in the center ($sig(i) == rev(i)$).
7. 4. If all columns successfully pair, return YES. If no row pairing succeeds, return NO.

## 4. Complexity Analysis
- **Time Complexity**: `O(H!! \cdot W^2)`
- **Space Complexity**: `O(H W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int H, W;
vector<string> grid;
vector<pair<int, int>> current_pairs;
int center_row = -1;
bool found = false;

void check_pairing() {
    // For each column, build signature and reversed signature
    vector<string> sigs(W), rev_sigs(W);
    vector<bool> is_self(W, false);

    for (int c = 0; c < W; ++c) {
        string s = "", rs = "";
        for (auto& p : current_pairs) {
            s += grid[p.first][c];
            s += grid[p.second][c];
            rs += grid[p.second][c];
            rs += grid[p.first][c];
        }
        if (center_row != -1) {
            s += grid[center_row][c];
            rs += grid[center_row][c];
        }
        sigs[c] = s;
        rev_sigs[c] = rs;
        is_self[c] = (s == rs);
    }

    vector<bool> used(W, false);
    bool center_col_used = false;
    bool possible = true;

    for (int i = 0; i < W; ++i) {
        if (used[i]) continue;
        bool matched = false;
        for (int j = i + 1; j < W; ++j) {
            if (!used[j] && sigs[i] == rev_sigs[j]) {
                used[i] = true;
                used[j] = true;
                matched = true;
                break;
            }
        }
        if (!matched) {
            if (is_self[i] && !center_col_used && (W % 2 == 1)) {
                used[i] = true;
                center_col_used = true;
            } else {
                possible = false;
                break;
            }
        }
    }

    if (possible) {
        found = true;
    }
}

void backtrack_pair(vector<int>& rem) {
    if (found) return;
    if (rem.empty()) {
        check_pairing();
        return;
    }

    int u = rem[0];
    for (size_t i = 1; i < rem.size(); ++i) {
        int v = rem[i];
        current_pairs.push_back({u, v});
        vector<int> next_rem;
        next_rem.reserve(rem.size() - 2);
        for (size_t j = 1; j < rem.size(); ++j) {
            if (j != i) next_rem.push_back(rem[j]);
        }
        backtrack_pair(next_rem);
        current_pairs.pop_back();
        if (found) return;
    }
}

void solve_backtrack() {
    if (H % 2 == 1) {
        for (int c = 0; c < H; ++c) {
            center_row = c;
            vector<int> rem;
            for (int i = 0; i < H; ++i) {
                if (i != c) rem.push_back(i);
            }
            backtrack_pair(rem);
            if (found) return;
        }
    } else {
        center_row = -1;
        vector<int> rem(H);
        for (int i = 0; i < H; ++i) rem[i] = i;
        backtrack_pair(rem);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> H >> W)) return 0;
    grid.resize(H);
    for (int i = 0; i < H; ++i) cin >> grid[i];

    if (H > W) {
        vector<string> trans(W, string(H, ' '));
        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j) {
                trans[j][i] = grid[i][j];
            }
        }
        grid = trans;
        swap(H, W);
    }

    solve_backtrack();
    cout << (found ? "YES" : "NO") << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
