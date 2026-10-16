# Problem Analysis: AtCoder-abc025_c — Twins and Tic-Tac-Toe

**Problem ID**: `AtCoder-abc025_c`  
**Contest**: `abc025`  
**Rating / Difficulty**: 1640  
**URL**: https://atcoder.jp/contests/abc025/tasks/abc025_c  
**VJudge Tag**: `[problem:AtCoder-abc025_c]`  
**Category File**: [`../categories/game_theory/minimax_3x3_board_payoff_matrix.md`](../categories/game_theory/minimax_3x3_board_payoff_matrix.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Minimax`  
- **Topic (Skill)**: `Minimax Search on 3x3 Game Board with Known Payoff Functions`  

---

## 1. Problem Statement & Key Idea
A 3x3 grid game between Takahashi and Aoki. They alternate filling empty cells with 'o' (Takahashi) and 'x' (Aoki). Final scores are determined by given reward matrices B (adjacent horizontal cells) and C (adjacent vertical cells): if adjacent cells match, Takahashi gets points; if they differ, Aoki gets points. Both play optimally to maximize their own final score. Output both final scores.

**Key Insight**: The total sum of points awarded across both players is CONSTANT (sum of all entries in B and C). Thus the game is zero-sum: maximizing Takahashi's score is equivalent to maximizing (Score_T - Score_A).

## 2. Core Observation & Invariant
There are only 9 turns on a 3x3 grid, with at most 3^9 = 19,683 reachable states. Solve via recursive Minimax: Takahashi maximizes (Score_T - Score_A), Aoki minimizes it.

## 3. Step-by-Step Algorithm
1. Read reward matrices B (2x3) and C (3x2). Calculate total_points.
2. Define evaluate(board): compute Score_T - Score_A based on matching adjacent cells.
3. Define minimax(board, turn):
4.   If board is full (turn == 9), return evaluate(board).
5.   If turn % 2 == 0 (Takahashi): max over empty cells of minimax(board with cell filled, turn + 1).
6.   If turn % 2 == 1 (Aoki): min over empty cells of minimax(board with cell filled, turn + 1).
7. Let diff = minimax(empty_board, 0).
8. Score_T = (total_points + diff) / 2, Score_A = (total_points - diff) / 2.
9. Print Score_T and Score_A.

## 4. Complexity Analysis
- **Time Complexity**: `O(3^9 * 9)`
- **Space Complexity**: `O(9)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int B[2][3];
int C[3][2];
int total_sum = 0;

int evaluate(const vector<vector<int>>& b) {
    int diff = 0;
    // Horizontal (vertical adjacency in problem notation B[2][3])
    for (int r = 0; r < 2; ++r) {
        for (int c = 0; c < 3; ++c) {
            if (b[r][c] == b[r + 1][c]) diff += B[r][c];
            else diff -= B[r][c];
        }
    }
    // Vertical (horizontal adjacency C[3][2])
    for (int r = 0; r < 3; ++r) {
        for (int c = 0; c < 2; ++c) {
            if (b[r][c] == b[r][c + 1]) diff += C[r][c];
            else diff -= C[r][c];
        }
    }
    return diff;
}

int minimax(vector<vector<int>>& b, int turn) {
    if (turn == 9) {
        return evaluate(b);
    }

    if (turn % 2 == 0) {
        // Takahashi maximizes
        int best = -1e9;
        for (int r = 0; r < 3; ++r) {
            for (int c = 0; c < 3; ++c) {
                if (b[r][c] == 0) {
                    b[r][c] = 1; // 'o'
                    best = max(best, minimax(b, turn + 1));
                    b[r][c] = 0;
                }
            }
        }
        return best;
    } else {
        // Aoki minimizes
        int best = 1e9;
        for (int r = 0; r < 3; ++r) {
            for (int c = 0; c < 3; ++c) {
                if (b[r][c] == 0) {
                    b[r][c] = 2; // 'x'
                    best = min(best, minimax(b, turn + 1));
                    b[r][c] = 0;
                }
            }
        }
        return best;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int r = 0; r < 2; ++r) {
        for (int c = 0; c < 3; ++c) {
            cin >> B[r][c];
            total_sum += B[r][c];
        }
    }

    for (int r = 0; r < 3; ++r) {
        for (int c = 0; c < 2; ++c) {
            cin >> C[r][c];
            total_sum += C[r][c];
        }
    }

    vector<vector<int>> board(3, vector<int>(3, 0));
    int diff = minimax(board, 0);

    int score_T = (total_sum + diff) / 2;
    int score_A = (total_sum - diff) / 2;

    cout << score_T << "\n" << score_A << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Zero-sum reduction of constant-sum game trees with exhaustive Minimax search.
- **Reusable Pattern**: `Constant Sum Minimax: diff = Score_A - Score_B; ans_A = (total + diff)/2.`
