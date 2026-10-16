# Two Pointers Bitwise Disjoint Subarray Counting (Sum == XOR)

**Domain**: `Basics`  
**Subtopic**: `Two Pointers`  

This workbook contains curated, high-quality competitive programming problems teaching **Two Pointers Bitwise Disjoint Subarray Counting (Sum == XOR)**.

---

## Curated Problems

### [problem:AtCoder-arc098_b] — Xor Sum 2
- **Contest**: `abc098`
- **Rating / Difficulty**: 1404
- **Specific Skill**: Two Pointers Bitwise Disjoint Subarray Counting (Sum == XOR)
- **Individual Analysis**: [`../../analysis/AtCoder-arc098_b.md`](../../analysis/AtCoder-arc098_b.md)
- **Problem Statement Summary**: Given an array A of N non-negative integers. Count the number of pairs (l, r) with 1 <= l <= r <= N such that sum_{i=l}^r A_i == XOR_{i=l}^r A_i.
- **Core Insight**: Because binary addition without carry is equivalent to XOR, the condition is monotonic: if A[l..r] has no bit collisions, any sub-interval also has no collisions. Two pointers: maintain running_xor = XOR_{i=l}^r A_i. For each l, expand r while (running_xor & A[r]) == 0. All subarrays starting at l and ending at any k in [l, r - 1] are valid (count is r - l).
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
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long ans = 0;
    long long cur_xor = 0;
    int r = 0;

    for (int l = 0; l < n; ++l) {
        while (r < n && (cur_xor & a[r]) == 0) {
            cur_xor ^= a[r];
            r++;
        }
        ans += (r - l);
        cur_xor ^= a[l];
    }

    cout << ans << "\n";
    return 0;
}
```
