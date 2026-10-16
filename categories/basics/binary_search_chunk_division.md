# Binary Search on Answer / Greedy Chunk Division

**Domain**: `Basics`  
**Subtopic**: `Binary Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Search on Answer / Greedy Chunk Division**.

---

## Curated Problems

### [problem:AtCoder-abc174_e] — Logs
- **Contest**: `abc174`
- **Rating / Difficulty**: 1227
- **Specific Skill**: Binary Search on Answer / Greedy Chunk Division
- **Individual Analysis**: [`../../analysis/AtCoder-abc174_e.md`](../../analysis/AtCoder-abc174_e.md)
- **Problem Statement Summary**: You have N logs of lengths A_1, ..., A_N. You can make at most K cuts in total. Minimize the maximum length of any piece (rounded up to nearest integer).
- **Core Insight**: To make all pieces of a log of length A have length at most L, we must cut it into ceil(A / L) pieces, which requires ceil(A / L) - 1 = (A - 1) / L cuts. The feasibility check: sum_{i=1}^N (A_i - 1) / L <= K is monotonic in L.
- **Complexity**: Time: `O(N log(max A))` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long high = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        high = max(high, a[i]);
    }

    long long low = 1, ans = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        long long cuts = 0;
        for (int i = 0; i < n; ++i) {
            cuts += (a[i] - 1) / mid;
        }

        if (cuts <= k) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
