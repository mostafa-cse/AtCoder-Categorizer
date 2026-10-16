# Dual Binary Search on Middle Anchor / Triplet Counting

**Domain**: `Basics`  
**Subtopic**: `Binary Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Dual Binary Search on Middle Anchor / Triplet Counting**.

---

## Curated Problems

### [problem:AtCoder-arc084_a] — Snuke Festival
- **Contest**: `abc077`
- **Rating / Difficulty**: 1096
- **Specific Skill**: Dual Binary Search on Middle Anchor / Triplet Counting
- **Individual Analysis**: [`../../analysis/AtCoder-arc084_a.md`](../../analysis/AtCoder-arc084_a.md)
- **Problem Statement Summary**: You have three parts of altars: top parts A, middle parts B, bottom parts C (each size N). An altar consists of a < b < c (a in A, b in B, c in C). Count valid altars.
- **Core Insight**: Sort A and C. For a fixed b, valid a are those with a < b (count is std::lower_bound(A) - A.begin()). Valid c are those with c > b (count is C.end() - std::upper_bound(C)). Total altars for this b is count_A * count_C.
- **Complexity**: Time: `O(N log N)` | Space: `O(N)`
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
    if (!(cin >> n)) return 0;

    vector<long long> a(n), b(n), c(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[i];
    for (int i = 0; i < n; ++i) cin >> c[i];

    sort(a.begin(), a.end());
    sort(c.begin(), c.end());

    long long total = 0;
    for (int i = 0; i < n; ++i) {
        long long val_b = b[i];
        long long cnt_a = lower_bound(a.begin(), a.end(), val_b) - a.begin();
        long long cnt_c = c.end() - upper_bound(c.begin(), c.end(), val_b);
        total += cnt_a * cnt_c;
    }

    cout << total << "\n";
    return 0;
}
```
