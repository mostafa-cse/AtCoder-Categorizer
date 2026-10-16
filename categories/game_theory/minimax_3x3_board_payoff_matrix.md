# Minimax Search on 3x3 Game Board with Known Payoff Functions

**Domain**: `Game Theory`  
**Subtopic**: `Minimax`  

This workbook contains curated, high-quality competitive programming problems teaching **Minimax Search on 3x3 Game Board with Known Payoff Functions**.

---

## Curated Problems

### `[problem:AtCoder-abc025_c]` — Twins and Tic-Tac-Toe
- **Rating / Difficulty**: 1640
- **Contest**: `abc025`
- **Analysis**: [`analysis/AtCoder-abc025_c.md`](../../analysis/AtCoder-abc025_c.md)
- **Key Idea**: The total sum of points awarded across both players is CONSTANT (sum of all entries in B and C). Thus the game is zero-sum: maximizing Takahashi's score is equivalent to maximizing (Score_T - Score_A).
- **Time Complexity**: `O(3^9 * 9)`
- **Space Complexity**: `O(9)`
- **Verified C++ Implementation**:
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
