# Bitmask Partition Enumeration / Contiguous Splitting

**Domain**: `Basics`  
**Subtopic**: `Bitmask Brute Force`  

This workbook contains curated, high-quality competitive programming problems teaching **Bitmask Partition Enumeration / Contiguous Splitting**.

---

## Curated Problems

### [problem:AtCoder-abc197_c] — ORXOR
- **Contest**: `abc197`
- **Rating / Difficulty**: 809
- **Specific Skill**: Bitmask Partition Enumeration / Contiguous Splitting
- **Individual Analysis**: [`../../analysis/AtCoder-abc197_c.md`](../../analysis/AtCoder-abc197_c.md)
- **Problem Statement Summary**: Given an array A of N integers (N <= 20). Partition A into non-empty contiguous subarrays. For each subarray, compute the bitwise OR. Compute the bitwise XOR of all resulting subarray ORs. Find the minimum possible XOR sum across all valid partitions.
- **Core Insight**: Each partition corresponds 1-to-1 with a bitmask of length N - 1, where the i-th bit indicates whether to split between A[i] and A[i+1]. We can evaluate each partition in O(N).
- **Complexity**: Time: `O(N * 2^(N-1))` | Space: `O(N)`
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

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long min_xor = -1;
    int total_masks = 1 << (n - 1);

    for (int mask = 0; mask < total_masks; ++mask) {
        long long current_xor = 0;
        long long current_or = a[0];

        for (int i = 0; i < n - 1; ++i) {
            if ((mask >> i) & 1) {
                current_xor ^= current_or;
                current_or = a[i + 1];
            } else {
                current_or |= a[i + 1];
            }
        }
        current_xor ^= current_or;

        if (min_xor == -1 || current_xor < min_xor) {
            min_xor = current_xor;
        }
    }

    cout << min_xor << "\n";
    return 0;
}
```
