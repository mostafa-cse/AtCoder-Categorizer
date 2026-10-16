# Independent X/Y Coordinate Subset Sum Knapsack DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `Bitset DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Independent X/Y Coordinate Subset Sum Knapsack DP**.

---

## Curated Problems

### `[problem:AtCoder-arc087_b]` — FT Robot
- **Rating / Difficulty**: 1508
- **Contest**: `abc082`
- **Analysis**: [`analysis/AtCoder-arc087_b.md`](../../analysis/AtCoder-arc087_b.md)
- **Key Idea**: Turns alternate between moving along the X-axis and Y-axis! The first segment of 'F's must move +X. All subsequent segments can move in either positive or negative direction, independently for X and Y.
- **Time Complexity**: `O(|S|^2 / 64)`
- **Space Complexity**: `O(|S|)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <bitset>
#include <cmath>

using namespace std;

const int OFFSET = 8000;

bool can_reach(const vector<int>& moves, int target) {
    bitset<16005> dp;
    dp[OFFSET] = 1;

    for (int d : moves) {
        dp = (dp << d) | (dp >> d);
    }

    if (abs(target) > 8000) return false;
    return dp[target + OFFSET];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int target_x, target_y;
    if (!(cin >> s >> target_x >> target_y)) return 0;

    vector<int> segments;
    int cur = 0;
    for (char c : s) {
        if (c == 'F') {
            cur++;
        } else {
            segments.push_back(cur);
            cur = 0;
        }
    }
    segments.push_back(cur);

    // First segment is fixed along +X
    target_x -= segments[0];

    vector<int> moves_x, moves_y;
    for (size_t i = 1; i < segments.size(); ++i) {
        if (segments[i] == 0) continue;
        if (i % 2 == 1) {
            moves_y.push_back(segments[i]);
        } else {
            moves_x.push_back(segments[i]);
        }
    }

    if (can_reach(moves_x, target_x) && can_reach(moves_y, target_y)) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
```
