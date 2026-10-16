# Sliding Window Frequency Tracking / Minimum Missing Non-Negative

**Domain**: `Data Structures`  
**Subtopic**: `Sliding Window`  

This workbook contains curated, high-quality competitive programming problems teaching **Sliding Window Frequency Tracking / Minimum Missing Non-Negative**.

---

## Curated Problems

### [problem:AtCoder-abc194_e] — Mex Min
- **Contest**: `abc194`
- **Rating / Difficulty**: 1088
- **Specific Skill**: Sliding Window Frequency Tracking / Minimum Missing Non-Negative
- **Individual Analysis**: [`../../analysis/AtCoder-abc194_e.md`](../../analysis/AtCoder-abc194_e.md)
- **Problem Statement Summary**: Given an array A of length N and integer M. For each contiguous subarray of length M, compute its MEX (minimum excluded non-negative integer). Find the minimum MEX across all subarrays of length M (M <= N <= 1.5 * 10^6).
- **Core Insight**: Instead of recalculating MEX in O(M), observe that an integer x is NEVER the MEX of any length-M window if every two consecutive occurrences of x (including imaginary boundaries at index -1 and index N) are at distance <= M. Conversely, if there exists two consecutive occurrences of x separated by gap > M, then a window of length M fits completely between them without containing x, making x a valid candidate MEX! The answer is the smallest x that has a gap > M.
- **Complexity**: Time: `O(N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> pos(n + 1);
    for (int i = 0; i <= n; ++i) {
        pos[i].push_back(-1);
    }

    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        if (a <= n) {
            pos[a].push_back(i);
        }
    }

    for (int i = 0; i <= n; ++i) {
        pos[i].push_back(n);
    }

    for (int x = 0; x <= n; ++x) {
        for (size_t k = 1; k < pos[x].size(); ++k) {
            if (pos[x][k] - pos[x][k - 1] > m) {
                cout << x << "\n";
                return 0;
            }
        }
    }

    cout << n << "\n";
    return 0;
}
```
