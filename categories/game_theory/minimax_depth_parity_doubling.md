# Binary Tree Game Theory Minimax Depth Parity

**Domain**: `Game Theory`  
**Subtopic**: `Minimax`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Tree Game Theory Minimax Depth Parity**.

---

## Curated Problems

### `[problem:AtCoder-abc027_c]` — Doubling Game
- **Rating / Difficulty**: 1539
- **Contest**: `abc027`
- **Analysis**: [`analysis/AtCoder-abc027_c.md`](../../analysis/AtCoder-abc027_c.md)
- **Key Idea**: The game takes place on a complete binary tree where leaves exceed N. The player who wants to win should force the game to a depth where the opponent is compelled to exceed N.
- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    int depth = 0;
    for (long long temp = n; temp > 0; temp /= 2) {
        depth++;
    }

    long long x = 1;
    bool takahashi_turn = true;

    while (x <= n) {
        if (depth % 2 == 1) {
            // Takahashi minimizes, Aoki maximizes
            if (takahashi_turn) x = 2 * x + 1;
            else x = 2 * x;
        } else {
            // Takahashi maximizes, Aoki minimizes
            if (takahashi_turn) x = 2 * x;
            else x = 2 * x + 1;
        }
        takahashi_turn = !takahashi_turn;
    }

    // The player whose turn it is now won, because the previous player exceeded N
    if (takahashi_turn) {
        cout << "Takahashi\n";
    } else {
        cout << "Aoki\n";
    }

    return 0;
}
```
