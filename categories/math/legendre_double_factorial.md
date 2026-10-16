# Legendre's Formula on Double Factorial / p-adic Valuation

**Domain**: `Math`  
**Subtopic**: `Number Theory`  

This workbook contains curated, high-quality competitive programming problems teaching **Legendre's Formula on Double Factorial / p-adic Valuation**.

---

## Curated Problems

### [problem:AtCoder-abc148_e] — Double Factorial
- **Contest**: `abc148`
- **Rating / Difficulty**: 818
- **Specific Skill**: Legendre's Formula on Double Factorial / p-adic Valuation
- **Individual Analysis**: [`../../analysis/AtCoder-abc148_e.md`](../../analysis/AtCoder-abc148_e.md)
- **Problem Statement Summary**: Given N <= 10^18. Calculate the number of trailing zeros in the decimal representation of N!! = N * (N - 2) * (N - 4) ...
- **Core Insight**: For even N, N!! = 2^(N/2) * (N/2)!. The factors of 5 come from even multiples of 5, which are multiples of 10: 10, 20, 30... Dividing N by 2 maps each number 2k to k, giving exact Legendre formula v_5((N/2)!) = sum_{k >= 1} floor((N/2) / 5^k) = sum_{k >= 1} floor(N / (2 * 5^k)).
- **Complexity**: Time: `O(log_5 N)` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    if (n % 2 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    long long ans = 0;
    long long div = 10;
    while (n >= div) {
        ans += n / div;
        if (n / 5 < div) break; // prevent overflow
        div *= 5;
    }

    cout << ans << "\n";
    return 0;
}
```
