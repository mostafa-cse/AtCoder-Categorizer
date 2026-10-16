# Sign Flip Parity Invariant

**Domain**: `Math`  
**Subtopic**: `Invariants & Parity`  

This workbook contains curated, high-quality competitive programming problems teaching **Sign Flip Parity Invariant**.

---

## Curated Problems

### [problem:AtCoder-abc125_d] — Flipping Signs
- **Contest**: `abc125`
- **Rating / Difficulty**: 833
- **Specific Skill**: Sign Flip Parity Invariant
- **Individual Analysis**: [`../../analysis/AtCoder-abc125_d.md`](../../analysis/AtCoder-abc125_d.md)
- **Problem Statement Summary**: Given an array A of N integers. You can choose adjacent elements A[i] and A[i+1] and multiply both by -1 any number of times. Maximize the sum of elements of A.
- **Core Insight**: Moreover, because negative signs can be moved along adjacent pairs to any two arbitrary positions, we can flip any pair of elements (i, j). If the total number of negative numbers is even, ALL elements can be made non-negative (sum = sum |A_i|). If odd, exactly one element must remain negative; to maximize the sum, we choose the element with minimum absolute value (sum = sum |A_i| - 2 * min |A_i|).
- **Complexity**: Time: `O(N)` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long sum_abs = 0;
    long long min_abs = 2e9 + 7;
    int neg_count = 0;

    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        if (a < 0) neg_count++;
        long long abs_val = abs(a);
        sum_abs += abs_val;
        min_abs = min(min_abs, abs_val);
    }

    if (neg_count % 2 == 0) {
        cout << sum_abs << "\n";
    } else {
        cout << sum_abs - 2 * min_abs << "\n";
    }

    return 0;
}
```
