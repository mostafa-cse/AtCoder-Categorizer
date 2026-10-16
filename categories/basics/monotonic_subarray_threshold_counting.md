# Monotonic Subarray Sum Threshold Counting

**Domain**: `Basics`  
**Subtopic**: `Two Pointers`  

This workbook contains curated, high-quality competitive programming problems teaching **Monotonic Subarray Sum Threshold Counting**.

---

## Curated Problems

### [problem:AtCoder-abc130_d] — Enough Array
- **Contest**: `abc130`
- **Rating / Difficulty**: 865
- **Specific Skill**: Monotonic Subarray Sum Threshold Counting
- **Individual Analysis**: [`../../analysis/AtCoder-abc130_d.md`](../../analysis/AtCoder-abc130_d.md)
- **Problem Statement Summary**: Given an array A of N positive integers and an integer K. Count the number of contiguous subarrays whose sum is >= K.
- **Core Insight**: For each left index L, find the smallest right index R such that sum(A[L .. R]) >= K. Because elements are positive, all subarrays extending from L to R' (for R <= R' < N) also have sum >= K, contributing exactly N - R subarrays. As L increases, R never decreases (monotonicity), allowing O(N) two pointers traversal.
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
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long ans = 0;
    long long current_sum = 0;
    int r = 0;

    for (int l = 0; l < n; ++l) {
        while (r < n && current_sum < k) {
            current_sum += a[r];
            r++;
        }
        if (current_sum >= k) {
            ans += (n - r + 1);
        }
        current_sum -= a[l];
    }

    cout << ans << "\n";
    return 0;
}
```
