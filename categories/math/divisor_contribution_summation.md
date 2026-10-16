# Divisor Contribution Summation / Order-of-Summation Swap

**Domain**: `Math`  
**Subtopic**: `Number Theory`  

This workbook contains curated, high-quality competitive programming problems teaching **Divisor Contribution Summation / Order-of-Summation Swap**.

---

## Curated Problems

### [problem:AtCoder-abc172_d] — Sum of Divisors
- **Contest**: `abc172`
- **Rating / Difficulty**: 963
- **Specific Skill**: Divisor Contribution Summation / Order-of-Summation Swap
- **Individual Analysis**: [`../../analysis/AtCoder-abc172_d.md`](../../analysis/AtCoder-abc172_d.md)
- **Problem Statement Summary**: Let f(K) be the number of positive divisors of K. Compute sum_{K=1}^N K * f(K) for N <= 10^7.
- **Core Insight**: A number d divides multiples d, 2d, 3d, ..., m*d where m = floor(N / d). Each multiple k*d contributes k*d to the sum. Summing over all multiples of d gives d * sum_{k=1}^m k = d * (m * (m + 1) / 2). Summing this over all d in 1..N yields exact O(N) complexity.
- **Complexity**: Time: `O(N)` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    long long total_sum = 0;
    for (long long d = 1; d <= n; ++d) {
        long long m = n / d;
        total_sum += d * (m * (m + 1) / 2);
    }

    cout << total_sum << "\n";
    return 0;
}
```
