# 3-Way Grid Rectangular Partitioning Casework

**Domain**: `Basics`  
**Subtopic**: `Complete Search`  

This workbook contains curated, high-quality competitive programming problems teaching **3-Way Grid Rectangular Partitioning Casework**.

---

## Curated Problems

### [problem:AtCoder-arc074_a] — Chocolate Bar
- **Contest**: `abc062`
- **Rating / Difficulty**: 1223
- **Specific Skill**: 3-Way Grid Rectangular Partitioning Casework
- **Individual Analysis**: [`../../analysis/AtCoder-arc074_a.md`](../../analysis/AtCoder-arc074_a.md)
- **Problem Statement Summary**: Divide an H x W grid into 3 non-empty rectangles using at most 2 straight cuts. Minimize the difference between the maximum and minimum area among the 3 rectangles.
- **Core Insight**: If H % 3 == 0 or W % 3 == 0, the difference is 0. Otherwise, iterate over all possible cut positions for the first piece (length 1 to H-1 or 1 to W-1). For the remaining rectangle, dividing it in half as equally as possible gives optimal sub-rectangles.
- **Complexity**: Time: `O(H + W)` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <algorithm>

using namespace std;

long long solve(long long h, long long w) {
    if (h % 3 == 0 || w % 3 == 0) return 0;

    long long min_diff = h * w;

    // Horizontal first cut at height i
    for (long long i = 1; i < h; ++i) {
        long long s1 = i * w;

        // Subcase 1: remaining (h - i) x w split horizontally
        long long rem_h = h - i;
        long long s2a = (rem_h / 2) * w;
        long long s3a = (rem_h - rem_h / 2) * w;
        long long diff_a = max({s1, s2a, s3a}) - min({s1, s2a, s3a});
        min_diff = min(min_diff, diff_a);

        // Subcase 2: remaining (h - i) x w split vertically
        long long s2b = rem_h * (w / 2);
        long long s3b = rem_h * (w - w / 2);
        long long diff_b = max({s1, s2b, s3b}) - min({s1, s2b, s3b});
        min_diff = min(min_diff, diff_b);
    }

    return min_diff;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long h, w;
    if (!(cin >> h >> w)) return 0;

    cout << min(solve(h, w), solve(w, h)) << "\n";
    return 0;
}
```
