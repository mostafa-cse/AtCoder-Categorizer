# Interval Grundy Decomposition under Alternating Parity Boundary Constraints

**Domain**: `Game Theory`  
**Subtopic**: `Sprague-Grundy Theorem`  

This workbook contains curated, high-quality competitive programming problems teaching **Interval Grundy Decomposition under Alternating Parity Boundary Constraints**.

---

## Curated Problems

### `[problem:AtCoder-arc151_c]` — 01 Game
- **Rating / Difficulty**: 1940
- **Contest**: `arc151`
- **Analysis**: [`analysis/AtCoder-arc151_c.md`](../../analysis/AtCoder-arc151_c.md)
- **Key Idea**: The board decomposes into independent intervals of empty cells. By Sprague-Grundy theorem, the total game is the XOR sum of segment Grundy values. For an open end of length L, G(L) = L. For an internal segment of length L between matching values (0...0 or 1...1), G(L) = 1 if L is odd, 0 if L is even (i.e. 1 for odd, 0 for even). Between opposite values (0...1 or 1...0), G(L) = 0 for all L! If M = 0, G = N mod 2.
- **Time Complexity**: `O(M log M)`
- **Space Complexity**: `O(M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Clue {
    long long pos;
    int val;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int m;
    if (!(cin >> n >> m)) return 0;

    if (m == 0) {
        cout << (n % 2 == 1 ? "Takahashi" : "Aoki") << "\n";
        return 0;
    }

    vector<Clue> clues(m);
    for (int i = 0; i < m; ++i) {
        cin >> clues[i].pos >> clues[i].val;
    }

    sort(clues.begin(), clues.end(), [](const Clue& a, const Clue& b) {
        return a.pos < b.pos;
    });

    long long xor_sum = 0;

    xor_sum ^= (clues[0].pos - 1);

    for (int i = 0; i < m - 1; ++i) {
        if (clues[i].val == clues[i + 1].val) {
            xor_sum ^= 1;
        } else {
            xor_sum ^= 0;
        }
    }

    xor_sum ^= (n - clues[m - 1].pos);

    cout << (xor_sum != 0 ? "Takahashi" : "Aoki") << "\n";
    return 0;
}
```
