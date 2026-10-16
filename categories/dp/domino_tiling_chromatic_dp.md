# Domino Tiling Chromatic Transition DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `State Machine DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Domino Tiling Chromatic Transition DP**.

---

## Curated Problems

### [problem:AtCoder-arc081_b] — Coloring Dominoes
- **Contest**: `abc071`
- **Rating / Difficulty**: 1165
- **Specific Skill**: Domino Tiling Chromatic Transition DP
- **Individual Analysis**: [`../../analysis/AtCoder-arc081_b.md`](../../analysis/AtCoder-arc081_b.md)
- **Problem Statement Summary**: A 2 x N grid is tiled with dominoes (each 1x2 or 2x1). Color the dominoes using 3 colors such that adjacent dominoes have different colors. Output count modulo 10^9 + 7.
- **Core Insight**: Transitions depend strictly on the type of current domino and previous domino: (1) First block: vertical -> 3 ways; horizontal -> 3 * 2 = 6 ways. (2) vert -> vert: 2 ways. (3) vert -> horiz: 2 ways. (4) horiz -> vert: 1 way. (5) horiz -> horiz: 3 ways. Scan left-to-right multiplying factors.
- **Complexity**: Time: `O(N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s1, s2;
    if (!(cin >> n >> s1 >> s2)) return 0;

    vector<char> blocks;
    for (int i = 0; i < n; ) {
        if (s1[i] == s2[i]) {
            blocks.push_back('V');
            i += 1;
        } else {
            blocks.push_back('H');
            i += 2;
        }
    }

    long long ways = (blocks[0] == 'V' ? 3 : 6);

    for (size_t i = 1; i < blocks.size(); ++i) {
        char prev = blocks[i - 1];
        char cur = blocks[i];

        if (prev == 'V' && cur == 'V') ways = (ways * 2) % MOD;
        else if (prev == 'V' && cur == 'H') ways = (ways * 2) % MOD;
        else if (prev == 'H' && cur == 'V') ways = (ways * 1) % MOD;
        else if (prev == 'H' && cur == 'H') ways = (ways * 3) % MOD;
    }

    cout << ways << "\n";
    return 0;
}
```
