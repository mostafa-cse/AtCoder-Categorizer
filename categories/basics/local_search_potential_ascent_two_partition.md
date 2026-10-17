# Local Search Potential Ascent for Two-Partition Intimacy Maximization

**Domain**: `Basics`  
**Subtopic**: `Constructive Algorithms`  

This workbook contains curated, high-quality competitive programming problems teaching **Local Search Potential Ascent for Two-Partition Intimacy Maximization**.

---

## Curated Problems

### `[problem:AtCoder-arc212_d]` — Two Rooms
- **Rating / Difficulty**: 2018
- **Contest**: `arc212`
- **Analysis**: [`analysis/AtCoder-arc212_d.md`](../../analysis/AtCoder-arc212_d.md)
- **Key Idea**: Represent room assignment by s_i in {-1, +1}. The potential function Phi = sum_{i < j} A_{i, j} * s_i * s_j measures total same-room intimacy minus different-room intimacy. A person i is unsatisfied iff sum_{j != i} A_{i, j} * s_i * s_j < 0. Flipping s_i <- -s_i strictly increases Phi by -2 * sum_{j != i} A_{i, j} * s_i * s_j >= 2. Because Phi is bounded by sum |A_{i, j}|, a simple local search (iteratively flipping any unsatisfied person) is guaranteed to terminate at a valid state in at most O(N^2 * max |A|) steps.
- **Time Complexity**: `O(N^3 * max |A|)`
- **Space Complexity**: `O(N^2)`
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
    if (!(cin >> n)) return 0;

    vector<vector<int>> a(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> a[i][j];
        }
    }

    // s[i] in {+1, -1}
    vector<int> s(n, 1);

    while (true) {
        bool changed = false;
        for (int i = 0; i < n; ++i) {
            int current_contribution = 0;
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                current_contribution += a[i][j] * s[i] * s[j];
            }
            if (current_contribution < 0) {
                s[i] = -s[i];
                changed = true;
                break;
            }
        }
        if (!changed) break;
    }

    string ans = "";
    for (int i = 0; i < n; ++i) {
        ans += (s[i] == 1 ? 'X' : 'Y');
    }
    cout << ans << "\n";

    return 0;
}
```
