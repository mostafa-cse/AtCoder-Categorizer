# Phase-Shifted Combinatorial Game with Nim Parity Inversion

**Domain**: `Game Theory`  
**Subtopic**: `Combinatorial Games`  

This workbook contains curated, high-quality competitive programming problems teaching **Phase-Shifted Combinatorial Game with Nim Parity Inversion**.

---

## Curated Problems

### `[problem:AtCoder-arc105_d]` — Let's Play Nim
- **Rating / Difficulty**: 1871
- **Contest**: `arc105`
- **Analysis**: [`analysis/AtCoder-arc105_d.md`](../../analysis/AtCoder-arc105_d.md)
- **Key Idea**: Phase 2 is normal Nim: second player wins iff XOR sum of bags is 0. If N is odd, Player 1 makes the final bag placement, so Player 2 plays first in Nim; Player 2 can always ensure non-zero XOR sum, winning Nim (First player overall wins). If N is even, Player 2 makes the final placement; Player 2 can mirror Player 1 and make all bags pairwise identical iff every coin count has even frequency.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

void solve() {
    int n;
    cin >> n;

    map<long long, int> freq;
    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        freq[a]++;
    }

    if (n % 2 == 1) {
        cout << "Second\n";
    } else {
        bool all_even = true;
        for (auto& [val, count] : freq) {
            if (count % 2 != 0) {
                all_even = false;
                break;
            }
        }
        if (all_even) cout << "Second\n";
        else cout << "First\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
```
