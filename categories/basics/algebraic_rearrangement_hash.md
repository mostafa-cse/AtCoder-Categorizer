# Algebraic Rearrangement Hash Frequency Match

**Domain**: `Basics`  
**Subtopic**: `Hashing / Rearrangement`  

This workbook contains curated, high-quality competitive programming problems teaching **Algebraic Rearrangement Hash Frequency Match**.

---

## Curated Problems

### [problem:AtCoder-abc166_e] — This Message Will Self-Destruct in 5s
- **Contest**: `abc166`
- **Rating / Difficulty**: 1062
- **Specific Skill**: Algebraic Rearrangement Hash Frequency Match
- **Individual Analysis**: [`../../analysis/AtCoder-abc166_e.md`](../../analysis/AtCoder-abc166_e.md)
- **Problem Statement Summary**: Given N people with heights A_1, ..., A_N standing in line at positions 1..N. Count pairs (i, j) with i < j such that j - i = A_i + A_j.
- **Core Insight**: Let left_key(i) = i + A_i and right_key(j) = j - A_j. As we iterate through j from 1 to N, the number of valid pairs with j is the count of previous indices i < j such that left_key(i) == right_key(j). Maintain frequencies in a hash map.
- **Complexity**: Time: `O(N log N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    map<long long, int> cnt;
    long long ans = 0;

    for (int j = 1; j <= n; ++j) {
        long long a;
        cin >> a;
        long long target = j - a;
        if (cnt.count(target)) {
            ans += cnt[target];
        }
        cnt[j + a]++;
    }

    cout << ans << "\n";
    return 0;
}
```
