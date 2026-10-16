# Monotonic Subarray Product Window

**Domain**: `Basics`  
**Subtopic**: `Two Pointers`  

This workbook contains curated, high-quality competitive programming problems teaching **Monotonic Subarray Product Window**.

---

## Curated Problems

### [problem:AtCoder-abc032_c] — Columns
- **Contest**: `abc032`
- **Rating / Difficulty**: 1244
- **Specific Skill**: Monotonic Subarray Product Window
- **Individual Analysis**: [`../../analysis/AtCoder-abc032_c.md`](../../analysis/AtCoder-abc032_c.md)
- **Problem Statement Summary**: Given an array S of N positive integers. Find the maximum length of a contiguous subarray whose product of elements is at most K.
- **Core Insight**: Assuming all elements are positive (S_i >= 1), the product is monotonically increasing with the right endpoint. We can maintain a sliding window [L, R] using two pointers: multiply by S[R]; while product > K and L <= R, divide by S[L] and increment L. The window size R - L + 1 gives the maximum valid length ending at R.
- **Complexity**: Time: `O(N)` | Space: `O(N)`
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
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> s(n);
    bool has_zero = false;
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
        if (s[i] == 0) has_zero = true;
    }

    if (has_zero) {
        cout << n << "\n";
        return 0;
    }
    if (k == 0) {
        cout << 0 << "\n";
        return 0;
    }

    int max_len = 0;
    long long prod = 1;
    int l = 0;

    for (int r = 0; r < n; ++r) {
        prod *= s[r];
        while (l <= r && prod > k) {
            prod /= s[l];
            l++;
        }
        max_len = max(max_len, r - l + 1);
    }

    cout << max_len << "\n";
    return 0;
}
```
