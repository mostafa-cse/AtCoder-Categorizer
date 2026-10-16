# Binary Search on Positional Notation Base with Overflow Guard

**Domain**: `Math`  
**Subtopic**: `Binary Search on Answer`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Search on Positional Notation Base with Overflow Guard**.

---

## Curated Problems

### `[problem:AtCoder-abc192_d]` — Base n
- **Rating / Difficulty**: 1425
- **Contest**: `abc192`
- **Analysis**: [`analysis/AtCoder-abc192_d.md`](../../analysis/AtCoder-abc192_d.md)
- **Key Idea**: If |X| == 1, the value does not depend on base n; if int(X) <= M, answer is 1, else 0. If |X| >= 2, the value is strictly monotonically increasing with base n. Binary search for the maximum valid base n with 128-bit integer overflow protection.
- **Time Complexity**: `O(|X| * log M)`
- **Space Complexity**: `O(|X|)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool evaluate(const string& x, long long base, long long M) {
    __int128 val = 0;
    for (char c : x) {
        val = val * base + (c - '0');
        if (val > M) return false;
    }
    return val <= M;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string x;
    long long m;
    if (!(cin >> x >> m)) return 0;

    int d = 0;
    for (char c : x) {
        d = max(d, c - '0');
    }

    if (x.size() == 1) {
        cout << (d <= m ? 1 : 0) << "\n";
        return 0;
    }

    long long low = d + 1, high = m + 1;
    long long best_base = d;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (evaluate(x, mid, m)) {
            best_base = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << max(0LL, best_base - d) << "\n";
    return 0;
}
```
