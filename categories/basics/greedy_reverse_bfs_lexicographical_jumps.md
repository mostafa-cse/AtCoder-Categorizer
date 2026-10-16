# Greedy Reverse BFS / Range Minimum for Lexicographical Jumps

**Domain**: `Basics`  
**Subtopic**: `Greedy Algorithms`  

This workbook contains curated, high-quality competitive programming problems teaching **Greedy Reverse BFS / Range Minimum for Lexicographical Jumps**.

---

## Curated Problems

### `[problem:AtCoder-abc146_f]` — Sugoroku
- **Rating / Difficulty**: 1545
- **Contest**: `abc146`
- **Analysis**: [`analysis/AtCoder-abc146_f.md`](../../analysis/AtCoder-abc146_f.md)
- **Key Idea**: To achieve the lexicographically smallest sequence of forward jumps, work BACKWARDS from N! At each step from current position curr, jump backwards as FAR as possible (up to M steps) to a valid square.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    string s;
    if (!(cin >> n >> m >> s)) return 0;

    vector<int> rolls;
    int curr = n;

    while (curr > 0) {
        int best_prev = -1;
        int min_reach = max(0, curr - m);

        for (int prev = min_reach; prev < curr; ++prev) {
            if (s[prev] == '0') {
                best_prev = prev;
                break;
            }
        }

        if (best_prev == -1) {
            cout << -1 << "\n";
            return 0;
        }

        rolls.push_back(curr - best_prev);
        curr = best_prev;
    }

    reverse(rolls.begin(), rolls.end());
    for (size_t i = 0; i < rolls.size(); ++i) {
        cout << rolls[i] << (i + 1 == rolls.size() ? "\n" : " ");
    }

    return 0;
}
```
