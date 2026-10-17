# Basic Greedy Algorithms

**Domain**: `Basics`  
**Subtopic**: `Greedy and Constructive`  

This workbook contains curated, high-quality competitive programming problems teaching **Basic Greedy Algorithms**.

---

## Curated Problems

### `[problem:AtCoder-arc175_c]` — Jumping Through Intervals
- **Rating / Difficulty**: 2116
- **Contest**: `arc175`
- **Analysis**: [`analysis/AtCoder-arc175_c.md`](../../analysis/AtCoder-arc175_c.md)
- **Key Idea**: Backward pass calculates the optimal reachable interval [optL_i, optR_i] for each A_i. If [L_i, R_i] overlaps with [optL_{i+1}, optR_{i+1}], the intersection achieves zero additional transition cost. If it lies completely to the left, A_i = R_i; if to the right, A_i = L_i. A subsequent forward pass greedily selects the minimum valid A_i within [optL_i, optR_i] that matches the previous chosen value A_{i-1} as closely as possible, ensuring lexicographical minimality.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
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

    vector<long long> L(n), R(n);
    for (int i = 0; i < n; ++i) {
        cin >> L[i] >> R[i];
    }

    vector<long long> optL(n), optR(n);
    optL[n - 1] = L[n - 1];
    optR[n - 1] = R[n - 1];

    for (int i = n - 2; i >= 0; --i) {
        if (R[i] < optL[i + 1]) {
            optL[i] = optR[i] = R[i];
        } else if (L[i] > optR[i + 1]) {
            optL[i] = optR[i] = L[i];
        } else {
            optL[i] = max(L[i], optL[i + 1]);
            optR[i] = min(R[i], optR[i + 1]);
        }
    }

    vector<long long> A(n);
    A[0] = optL[0];

    for (int i = 1; i < n; ++i) {
        if (A[i - 1] < optL[i]) {
            A[i] = optL[i];
        } else if (A[i - 1] > optR[i]) {
            A[i] = optR[i];
        } else {
            A[i] = A[i - 1];
        }
    }

    for (int i = 0; i < n; ++i) {
        cout << A[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
