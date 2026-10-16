# 3x3 Grid Minimax Game DP with Memoization

**Domain**: `Game Theory`  
**Subtopic**: `Minimax`  

This workbook contains curated, high-quality competitive programming problems teaching **3x3 Grid Minimax Game DP with Memoization**.

---

## Curated Problems

### `[problem:AtCoder-abc349_e]` — Weighted Tic-Tac-Toe
- **Rating / Difficulty**: 1464
- **Contest**: `abc349`
- **Analysis**: [`analysis/AtCoder-abc349_e.md`](../../analysis/AtCoder-abc349_e.md)
- **Key Idea**: Because the game board is 3x3 with at most 9 turns, the total number of reachable states is at most 3^9 = 19,683. Solve via Minimax search with memoization.
- **Time Complexity**: `O(3^9 * 9)`
- **Space Complexity**: `O(3^9)`
- **Verified C++ Implementation**:
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
