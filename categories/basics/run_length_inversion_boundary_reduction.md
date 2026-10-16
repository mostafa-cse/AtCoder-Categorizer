# Run-Length Inversion / Boundary Reduction Greedy

**Domain**: `Basics`  
**Subtopic**: `Greedy / Invariants`  

This workbook contains curated, high-quality competitive programming problems teaching **Run-Length Inversion / Boundary Reduction Greedy**.

---

## Curated Problems

### [problem:AtCoder-abc140_d] — Face Produces Unhappiness
- **Contest**: `abc140`
- **Rating / Difficulty**: 1074
- **Specific Skill**: Run-Length Inversion / Boundary Reduction Greedy
- **Individual Analysis**: [`../../analysis/AtCoder-abc140_d.md`](../../analysis/AtCoder-abc140_d.md)
- **Problem Statement Summary**: N people standing in line facing 'L' or 'R'. A person at i is happy if they face someone facing the same way (person facing R has i+1 facing R; person facing L has i-1 facing L). You can reverse a contiguous subarray of people and flip their directions up to K times. Maximize happy people.
- **Core Insight**: Reversing an internal contiguous segment flips directions and merges at most 2 boundaries between different blocks, reducing block count by at most 2 per operation. Thus, each operation increases happiness by at most 2, capped at N - 1.
- **Complexity**: Time: `O(N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    string s;
    if (!(cin >> n >> k >> s)) return 0;

    int initial_happy = 0;
    for (int i = 0; i < n - 1; ++i) {
        if (s[i] == s[i + 1]) {
            initial_happy++;
        }
    }

    int ans = min(n - 1, initial_happy + 2 * k);
    cout << ans << "\n";
    return 0;
}
```
