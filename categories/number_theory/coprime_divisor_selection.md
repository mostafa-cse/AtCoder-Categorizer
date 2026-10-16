# Coprime Divisor Selection via Prime Factorization of GCD

**Domain**: `Number Theory`  
**Subtopic**: `Prime Factorization & GCD`  

This workbook contains curated, high-quality competitive programming problems teaching **Coprime Divisor Selection via Prime Factorization of GCD**.

---

## Curated Problems

### [problem:AtCoder-abc142_d] — Disjoint Set of Common Divisors
- **Contest**: `abc142`
- **Rating / Difficulty**: 827
- **Specific Skill**: Coprime Divisor Selection via Prime Factorization of GCD
- **Individual Analysis**: [`../../analysis/AtCoder-abc142_d.md`](../../analysis/AtCoder-abc142_d.md)
- **Problem Statement Summary**: Given two positive integers A, B <= 10^12. Select a subset of common divisors such that any two chosen divisors are mutually coprime. Maximize the number of chosen divisors.
- **Core Insight**: To maximize the number of pairwise coprime divisors, each chosen divisor > 1 should be a distinct prime factor of G! (Selecting a composite divisor p*q would prevent selecting either p or q, reducing the total count). Including 1 (which is coprime to all numbers), the maximum count is 1 + (number of distinct prime factors of G).
- **Complexity**: Time: `O(log(min(A, B)) + sqrt(gcd(A, B)))` | Space: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <numeric>

using namespace std;

long long gcd_ll(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    long long g = gcd_ll(a, b);

    long long prime_count = 0;
    for (long long d = 2; d * d <= g; ++d) {
        if (g % d == 0) {
            prime_count++;
            while (g % d == 0) {
                g /= d;
            }
        }
    }
    if (g > 1) {
        prime_count++;
    }

    cout << prime_count + 1 << "\n";
    return 0;
}
```
