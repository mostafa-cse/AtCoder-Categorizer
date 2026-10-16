# Bitwise Independent Contribution Summation modulo 10^9+7

**Domain**: `Math`  
**Subtopic**: `Bitwise Arithmetic`  

This workbook contains curated, high-quality competitive programming problems teaching **Bitwise Independent Contribution Summation modulo 10^9+7**.

---

## Curated Problems

### [problem:AtCoder-abc147_d] — Xor Sum 4
- **Contest**: `abc147`
- **Rating / Difficulty**: 1205
- **Specific Skill**: Bitwise Independent Contribution Summation modulo 10^9+7
- **Individual Analysis**: [`../../analysis/AtCoder-abc147_d.md`](../../analysis/AtCoder-abc147_d.md)
- **Problem Statement Summary**: Given an array A of N integers (A_i < 2^60). Compute sum_{i=1}^{N-1} sum_{j=i+1}^N (A_i XOR A_j) modulo 10^9 + 7.
- **Core Insight**: For each bit b: count how many elements have bit b equal to 1 (let this be c_1) and how many have bit b equal to 0 (c_0 = N - c_1). A pair (A_i, A_j) has bit b set in (A_i XOR A_j) if and only if one element has bit b = 1 and the other has bit b = 0. Thus, bit b is set in exactly c_1 * c_0 pairs! Contribution to the total sum is 2^b * c_1 * c_0.
- **Complexity**: Time: `O(60 * N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long total_ans = 0;

    for (int b = 0; b < 60; ++b) {
        long long c1 = 0;
        for (int i = 0; i < n; ++i) {
            if ((a[i] >> b) & 1) {
                c1++;
            }
        }
        long long c0 = n - c1;
        long long pairs = (c1 * c0) % MOD;
        long long weight = (1ULL << b) % MOD;
        long long term = (pairs * weight) % MOD;
        total_ans = (total_ans + term) % MOD;
    }

    cout << total_ans << "\n";
    return 0;
}
```
