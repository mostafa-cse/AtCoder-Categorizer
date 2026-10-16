# Central Boundary Invariant on Reversible Interval Flips

**Domain**: `Basics`  
**Subtopic**: `Ad-Hoc / Observations`  

This workbook contains curated, high-quality competitive programming problems teaching **Central Boundary Invariant on Reversible Interval Flips**.

---

## Curated Problems

### `[problem:AtCoder-arc088_b]` — Wide Flip
- **Rating / Difficulty**: 1646
- **Contest**: `abc083`
- **Analysis**: [`analysis/AtCoder-arc088_b.md`](../../analysis/AtCoder-arc088_b.md)
- **Key Idea**: Flipping substrings of length >= K can flip any prefix [0..r] or suffix [l..N-1] as long as length >= K. If adjacent characters S[i] != S[i+1], an operation must differentiate between them, which requires K <= max(i + 1, N - (i + 1)).
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    int ans = n;

    for (int i = 0; i < n - 1; ++i) {
        if (s[i] != s[i + 1]) {
            int bound = max(i + 1, n - 1 - i);
            ans = min(ans, bound);
        }
    }

    cout << ans << "\n";
    return 0;
}
```
