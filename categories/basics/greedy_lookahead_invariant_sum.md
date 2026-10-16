# Greedy Lookahead with Invariant Sum Constrained State

**Domain**: `Basics`  
**Subtopic**: `Greedy Algorithms`  

This workbook contains curated, high-quality competitive programming problems teaching **Greedy Lookahead with Invariant Sum Constrained State**.

---

## Curated Problems

### `[problem:AtCoder-abc166_f]` — Three Variables Game
- **Rating / Difficulty**: 1668
- **Contest**: `abc166`
- **Analysis**: [`analysis/AtCoder-abc166_f.md`](../../analysis/AtCoder-abc166_f.md)
- **Key Idea**: The sum A + B + C is strictly conserved! If sum == 0, impossible. If sum == 1: at each step, exactly one variable is positive and one is zero, leaving no choice. If sum == 2: when both variables are positive (1, 1), use 1-STEP LOOKAHEAD to increment the variable needed in the next round!
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long val[3];
    if (!(cin >> n >> val[0] >> val[1] >> val[2])) return 0;

    vector<string> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }

    vector<char> moves;

    for (int i = 0; i < n; ++i) {
        int u = s[i][0] - 'A';
        int v = s[i][1] - 'A';

        if (val[u] == 0 && val[v] == 0) {
            cout << "No\n";
            return 0;
        }

        if (val[u] == 0) {
            val[u]++;
            val[v]--;
            moves.push_back('A' + u);
        } else if (val[v] == 0) {
            val[v]++;
            val[u]--;
            moves.push_back('A' + v);
        } else {
            // Both are positive (val[u] == 1, val[v] == 1)
            // Look ahead to next query
            if (i + 1 < n && (s[i + 1][0] - 'A' == u || s[i + 1][1] - 'A' == u)) {
                val[u]++;
                val[v]--;
                moves.push_back('A' + u);
            } else {
                val[v]++;
                val[u]--;
                moves.push_back('A' + v);
            }
        }
    }

    cout << "Yes\n";
    for (char c : moves) {
        cout << c << "\n";
    }

    return 0;
}
```
