# First-Last Digit Pair Frequency Matrix Double Counting

**Domain**: `Math`  
**Subtopic**: `Counting & Matrices`  

This workbook contains curated, high-quality competitive programming problems teaching **First-Last Digit Pair Frequency Matrix Double Counting**.

---

## Curated Problems

### [problem:AtCoder-abc152_d] — Handstand 2
- **Contest**: `abc152`
- **Rating / Difficulty**: 1045
- **Specific Skill**: First-Last Digit Pair Frequency Matrix Double Counting
- **Individual Analysis**: [`../../analysis/AtCoder-abc152_d.md`](../../analysis/AtCoder-abc152_d.md)
- **Problem Statement Summary**: Count pairs of integers (A, B) such that 1 <= A, B <= N and the first digit of A equals the last digit of B, and the last digit of A equals the first digit of B (N <= 2 * 10^5).
- **Core Insight**: Let cnt[f][l] be the count of integers in 1..N whose first digit is f and last digit is l. If a number A has first digit f and last digit l, any valid B must have first digit l and last digit f. Therefore, the number of pairs formed by this class is cnt[f][l] * cnt[l][f]! Total answer is sum_{f=1}^9 sum_{l=1}^9 cnt[f][l] * cnt[l][f].
- **Complexity**: Time: `O(N)` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> cnt(10, vector<long long>(10, 0));

    for (int i = 1; i <= n; ++i) {
        string s = to_string(i);
        int f = s.front() - '0';
        int l = s.back() - '0';
        cnt[f][l]++;
    }

    long long ans = 0;
    for (int f = 1; f <= 9; ++f) {
        for (int l = 1; l <= 9; ++l) {
            ans += cnt[f][l] * cnt[l][f];
        }
    }

    cout << ans << "\n";
    return 0;
}
```
