# Euler's Totient Function / Phi Function

**Domain**: `Number Theory`  
**Subtopic**: `Multiplicative Functions`  

This workbook contains curated, high-quality competitive programming problems teaching **Euler's Totient Function / Phi Function**.

---

## Curated Problems

### `[problem:AtCoder-abc212_g]` — Power Pair
- **Rating / Difficulty**: 2150
- **Contest**: `abc212`
- **Analysis**: [`analysis/AtCoder-abc212_g.md`](../../analysis/AtCoder-abc212_g.md)
- **Key Idea**: The pair (0, 0) gives 1 valid solution. For non-zero elements x in Z_P^*, the generated cyclic subgroup <x> has size equal to its multiplicative order d = ord_P(x), which divides P - 1. Any element of order d generates all d elements of the unique cyclic subgroup of order d. In Z_P^*, the number of elements with multiplicative order d is phi(d). Each such element can reach exactly d distinct values y. Therefore, the total number of non-zero pairs is sum_{d | P-1} phi(d) * d.
- **Time Complexity**: `O(sqrt(P) + divisors(P - 1) log P)`
- **Space Complexity**: `O(divisors(P - 1))`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

long long phi(long long n) {
    long long result = n;
    for (long long p = 2; p * p <= n; ++p) {
        if (n % p == 0) {
            while (n % p == 0) n /= p;
            result -= result / p;
        }
    }
    if (n > 1) result -= result / n;
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long p;
    if (!(cin >> p)) return 0;

    long long num = p - 1;
    vector<long long> divisors;
    for (long long d = 1; d * d <= num; ++d) {
        if (num % d == 0) {
            divisors.push_back(d);
            if (d * d != num) {
                divisors.push_back(num / d);
            }
        }
    }

    sort(divisors.begin(), divisors.end());

    long long total_pairs = 1;
    for (long long d : divisors) {
        long long count_elements = phi(d) % MOD;
        long long contribution = (count_elements * (d % MOD)) % MOD;
        total_pairs = (total_pairs + contribution) % MOD;
    }

    cout << total_pairs << "\n";
    return 0;
}
```
