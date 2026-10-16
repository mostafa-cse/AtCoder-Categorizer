# Adjacent Pair Overlap Forward Greedy Reduction

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Adjacent Pair Overlap Forward Greedy Reduction**.

---

## Curated Problems

### [problem:AtCoder-arc064_a] — Boxes and Candies
- **Contest**: `abc048`
- **Rating / Difficulty**: 1164
- **Specific Skill**: Adjacent Pair Overlap Forward Greedy Reduction
- **Individual Analysis**: [`../../analysis/AtCoder-arc064_a.md`](../../analysis/AtCoder-arc064_a.md)
- **Problem Statement Summary**: Given array a_1..a_n. In one operation, eat a candy from box i. Make every adjacent pair sum a_i + a_{i+1} <= x. Minimize candies eaten.
- **Core Insight**: Reducing candies from a_{i+1} fixes the current pair (a_i, a_{i+1}) AND simultaneously helps the next pair (a_{i+1}, a_{i+2})! If a_i itself exceeds x, first reduce a_i to x.
- **Complexity**: Time: `O(N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long x;
    if (!(cin >> n >> x)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long eaten = 0;
    if (a[0] > x) {
        eaten += a[0] - x;
        a[0] = x;
    }

    for (int i = 0; i < n - 1; ++i) {
        long long sum = a[i] + a[i + 1];
        if (sum > x) {
            long long excess = sum - x;
            eaten += excess;
            a[i + 1] -= excess;
        }
    }

    cout << eaten << "\n";
    return 0;
}
```
