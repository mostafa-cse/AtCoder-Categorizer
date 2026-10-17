# Combinatorial Game Parity Determined by Boundary Endpoints

**Domain**: `Game Theory`  
**Subtopic**: `Impartial Games`  

This workbook contains curated, high-quality competitive programming problems teaching **Combinatorial Game Parity Determined by Boundary Endpoints**.

---

## Curated Problems

### `[problem:AtCoder-arc064_b]` — An Ordinary Game
- **Rating / Difficulty**: 1814
- **Contest**: `abc048`
- **Analysis**: [`analysis/AtCoder-arc064_b.md`](../../analysis/AtCoder-arc064_b.md)
- **Key Idea**: The endpoints S[0] and S[N - 1] can never be deleted. The game must end in an alternating string c_1 c_2 c_1 c_2... If S[0] == S[N - 1], the final string must have odd length; if S[0] != S[N - 1], the final string must have even length.
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    bool same_ends = (s.front() == s.back());

    // If same_ends, final length is odd
    // If !same_ends, final length is even
    int moves_parity = same_ends ? (n % 2 == 0 ? 1 : 0) : (n % 2 == 1 ? 1 : 0);

    if (moves_parity == 1) {
        cout << "First\n";
    } else {
        cout << "Second\n";
    }

    return 0;
}
```
