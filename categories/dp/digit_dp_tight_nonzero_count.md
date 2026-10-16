# Digit DP with Tight Flag and Non-Zero Count State

**Domain**: `Dynamic Programming`  
**Subtopic**: `Digit DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Digit DP with Tight Flag and Non-Zero Count State**.

---

## Curated Problems

### [problem:AtCoder-abc154_e] — Almost Everywhere Zero
- **Contest**: `abc154`
- **Rating / Difficulty**: 1298
- **Specific Skill**: Digit DP with Tight Flag and Non-Zero Count State
- **Individual Analysis**: [`../../analysis/AtCoder-abc154_e.md`](../../analysis/AtCoder-abc154_e.md)
- **Problem Statement Summary**: Given a positive integer N (up to 100 digits) and K in {1, 2, 3}. Find the number of integers between 1 and N whose decimal representation contains exactly K non-zero digits.
- **Core Insight**: Let S be string N. dp[idx][cnt][tight]: idx is current digit position 0..|S|-1; cnt is count of non-zero digits placed so far (0..K); tight indicates if prefix matches S. If tight is true, current digit can be at most S[idx] - '0'; if false, current digit can be 0..9.
- **Complexity**: Time: `O(|S| * K * 10)` | Space: `O(|S| * K)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

string s;
int k;
long long memo[105][5][2];

long long solve(int idx, int cnt, bool tight) {
    if (cnt > k) return 0;
    if (idx == (int)s.size()) {
        return (cnt == k ? 1 : 0);
    }
    if (memo[idx][cnt][tight] != -1) {
        return memo[idx][cnt][tight];
    }

    int limit = (tight ? s[idx] - '0' : 9);
    long long ways = 0;

    for (int d = 0; d <= limit; ++d) {
        ways += solve(idx + 1, cnt + (d > 0 ? 1 : 0), tight && (d == limit));
    }

    return memo[idx][cnt][tight] = ways;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> s >> k)) return 0;

    memset(memo, -1, sizeof(memo));
    cout << solve(0, 0, true) << "\n";
    return 0;
}
```
