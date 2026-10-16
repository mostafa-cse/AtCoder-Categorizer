# Game Theory Minimax 1-Step Lookahead / Card Draw Reduction

**Domain**: `Game Theory`  
**Subtopic**: `Minimax`  

This workbook contains curated, high-quality competitive programming problems teaching **Game Theory Minimax 1-Step Lookahead / Card Draw Reduction**.

---

## Curated Problems

### `[problem:AtCoder-arc085_b]` — ABS
- **Rating / Difficulty**: 1550
- **Contest**: `abc078`
- **Analysis**: [`analysis/AtCoder-arc085_b.md`](../../analysis/AtCoder-arc085_b.md)
- **Key Idea**: By backward induction, Y will always choose to take all remaining cards up to N to achieve |X's chosen card - A_N|. Knowing this, X only needs to choose between taking all cards up to N (score |A_N - W|) or taking all cards up to N - 1 (score |A_{N-1} - A_N|).
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long z, w;
    if (!(cin >> n >> z >> w)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    if (n == 1) {
        cout << abs(a[0] - w) << "\n";
    } else {
        long long ans = max(abs(a[n - 1] - w), abs(a[n - 2] - a[n - 1]));
        cout << ans << "\n";
    }

    return 0;
}
```
