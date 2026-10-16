# Digit DP Counting Occurrences of Digit '1'

**Domain**: `Dynamic Programming`  
**Subtopic**: `Digit DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Digit DP Counting Occurrences of Digit '1'**.

---

## Curated Problems

### [problem:AtCoder-abc029_d] — 1
- **Contest**: `abc029`
- **Rating / Difficulty**: 1393
- **Specific Skill**: Digit DP Counting Occurrences of Digit '1'
- **Individual Analysis**: [`../../analysis/AtCoder-abc029_d.md`](../../analysis/AtCoder-abc029_d.md)
- **Problem Statement Summary**: Given an integer N (1 <= N <= 10^9). Find the total number of times the digit '1' is written when writing all integers from 1 to N.
- **Core Insight**: State: (idx, count_of_ones, is_tight). At position idx with upper bound limit = (tight ? S[idx] - '0' : 9): iterate digit d from 0 to limit. Recurse on idx + 1 with count_of_ones + (d == 1) and new tight flag.
- **Complexity**: Time: `O(|S|^2 * 10)` | Space: `O(|S|^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

string s;
long long memo[15][15][2];

long long solve(int idx, int cnt, bool tight) {
    if (idx == (int)s.size()) return cnt;
    if (memo[idx][cnt][tight] != -1) return memo[idx][cnt][tight];

    int limit = (tight ? s[idx] - '0' : 9);
    long long total = 0;

    for (int d = 0; d <= limit; ++d) {
        total += solve(idx + 1, cnt + (d == 1 ? 1 : 0), tight && (d == limit));
    }

    return memo[idx][cnt][tight] = total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    s = to_string(n);
    memset(memo, -1, sizeof(memo));

    cout << solve(0, 0, true) << "\n";
    return 0;
}
```
