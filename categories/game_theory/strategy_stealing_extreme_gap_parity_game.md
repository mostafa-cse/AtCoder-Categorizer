# Strategy-Stealing and Extreme Gap Parity Invariant in Subtraction Game

**Domain**: `Game Theory`  
**Subtopic**: `Combinatorial Games`  

This workbook contains curated, high-quality competitive programming problems teaching **Strategy-Stealing and Extreme Gap Parity Invariant in Subtraction Game**.

---

## Curated Problems

### `[problem:AtCoder-arc137_c]` — Distinct Numbers
- **Rating / Difficulty**: 2043
- **Contest**: `arc137`
- **Analysis**: [`analysis/AtCoder-arc137_c.md`](../../analysis/AtCoder-arc137_c.md)
- **Key Idea**: Analyze the top two elements A_N and A_{N-1}. If A_N - A_{N-1} > 1, Alice can move A_N to A_{N-1} + 1. If that resulting state is losing for the recipient, Bob loses. If it were winning for the recipient, Alice could have chosen that very winning transition directly (strategy stealing / option dominance). Thus Alice always wins if A_N - A_{N-1} > 1. If A_N - A_{N-1} == 1, neither player can leapfrog without losing, so moves strictly decrement available empty slots one by one. The total number of available slots is A_N - (N - 1), so Alice wins iff (A_N - N) is even.
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    if (a[n - 1] - a[n - 2] > 1) {
        cout << "Alice\n";
    } else {
        if ((a[n - 1] - n) % 2 != 0) {
            cout << "Bob\n";
        } else {
            cout << "Alice\n";
        }
    }

    return 0;
}
```
