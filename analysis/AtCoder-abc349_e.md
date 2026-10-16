# Problem Analysis: AtCoder-abc349_e — Weighted Tic-Tac-Toe

**Problem ID**: `AtCoder-abc349_e`  
**Contest**: `abc349`  
**Rating / Difficulty**: 1464  
**URL**: https://atcoder.jp/contests/abc349/tasks/abc349_e  
**VJudge Tag**: `[problem:AtCoder-abc349_e]`  
**Category File**: [`../categories/game_theory/minimax_3x3_grid_game.md`](../categories/game_theory/minimax_3x3_grid_game.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Minimax`  
- **Topic (Skill)**: `3x3 Grid Minimax Game DP with Memoization`  

---

## 1. Problem Statement & Key Idea
A 3x3 grid has point values A[i][j]. Takahashi and Aoki take turns claiming uncolored cells. If a move creates 3-in-a-row of a player's color, that player immediately wins. If all 9 cells are filled without 3-in-a-row, the player with the greater sum of cell scores wins. Determine who wins under optimal play.

**Key Insight**: Because the game board is 3x3 with at most 9 turns, the total number of reachable states is at most 3^9 = 19,683. Solve via Minimax search with memoization.

## 2. Core Observation & Invariant
State is uniquely identified by the ternary encoding of the 3x3 board. Transitions check for 3-in-a-row win; if leaf state (full board), compare score totals.

## 3. Step-by-Step Algorithm
1. Represent board state as string of length 9 or ternary integer.
2. Define minimax(state):
3.   Check if either player already has 3-in-a-row; if so, return win for that player.
4.   If all 9 cells filled, compute total scores: player with higher score wins.
5.   Whichever player's turn it is: try all uncolored cells.
6.   If any branch leads to a win, return win for the current player.
7.   Otherwise return loss.
8. Print 'Takahashi' if Takahashi wins, else 'Aoki'.

## 4. Complexity Analysis
- **Time Complexity**: `O(3^9 * 9)`
- **Space Complexity**: `O(3^9)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

long long A[3][3];
map<vector<int>, bool> memo;

bool check_line(const vector<int>& b, int p) {
    // Rows
    for (int r = 0; r < 3; ++r) {
        if (b[r * 3] == p && b[r * 3 + 1] == p && b[r * 3 + 2] == p) return true;
    }
    // Cols
    for (int c = 0; c < 3; ++c) {
        if (b[c] == p && b[3 + c] == p && b[6 + c] == p) return true;
    }
    // Diagonals
    if (b[0] == p && b[4] == p && b[8] == p) return true;
    if (b[2] == p && b[4] == p && b[6] == p) return true;
    return false;
}

// Returns true if the CURRENT player wins from this board state
bool can_win(vector<int>& b, int turn) {
    if (memo.count(b)) return memo[b];

    int prev_player = 3 - turn;
    if (check_line(b, prev_player)) {
        return memo[b] = false;
    }

    bool full = true;
    for (int x : b) if (x == 0) full = false;

    if (full) {
        long long score1 = 0, score2 = 0;
        for (int i = 0; i < 9; ++i) {
            if (b[i] == 1) score1 += A[i / 3][i % 3];
            else score2 += A[i / 3][i % 3];
        }
        if (turn == 1) return memo[b] = (score1 > score2);
        else return memo[b] = (score2 > score1);
    }

    for (int i = 0; i < 9; ++i) {
        if (b[i] == 0) {
            b[i] = turn;
            bool opp_win = can_win(b, 3 - turn);
            b[i] = 0;
            if (!opp_win) {
                return memo[b] = true;
            }
        }
    }

    return memo[b] = false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int r = 0; r < 3; ++r) {
        for (int c = 0; c < 3; ++c) {
            cin >> A[r][c];
        }
    }

    vector<int> b(9, 0);
    if (can_win(b, 1)) {
        cout << "Takahashi\n";
    } else {
        cout << "Aoki\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Game-theoretic Minimax evaluation with terminal 3-in-a-row condition check on small state spaces.
- **Reusable Pattern**: `Ternary Grid Minimax: memoized search over 3^N board states.`
