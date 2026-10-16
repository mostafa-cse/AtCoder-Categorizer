# Pairwise Coprime via Smallest Prime Factor (SPF) Sieve

**Domain**: `Number Theory`  
**Subtopic**: `Prime Factorization`  

This workbook contains curated, high-quality competitive programming problems teaching **Pairwise Coprime via Smallest Prime Factor (SPF) Sieve**.

---

## Curated Problems

### [problem:AtCoder-abc177_e] — Coprime
- **Contest**: `abc177`
- **Rating / Difficulty**: 1057
- **Specific Skill**: Pairwise Coprime via Smallest Prime Factor (SPF) Sieve
- **Individual Analysis**: [`../../analysis/AtCoder-abc177_e.md`](../../analysis/AtCoder-abc177_e.md)
- **Problem Statement Summary**: Given an array A of N positive integers. Determine if they are 'pairwise coprime' (gcd(A_i, A_j) = 1 for all i < j), 'setwise coprime' (gcd(A_1, ..., A_N) = 1), or 'not coprime'.
- **Core Insight**: Precompute the Smallest Prime Factor (SPF) for all numbers up to MAX = 10^6 using linear sieve. For each element A_i, factorize it in O(log A_i) using SPF, tracking prime factors in a global frequency array prime_cnt[p]. If any prime has prime_cnt[p] >= 2, the array is NOT pairwise coprime.
- **Complexity**: Time: `O(MAX log log MAX + N log MAX)` | Space: `O(MAX)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

const int MAX = 1000000;

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

    int n;
    if (!(cin >> n)) return 0;

    vector<int> spf(MAX + 1);
    for (int i = 0; i <= MAX; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAX; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAX; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }

    vector<int> a(n);
    long long overall_gcd = 0;
    vector<int> prime_count(MAX + 1, 0);
    bool pairwise = true;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        overall_gcd = gcd_ll(overall_gcd, a[i]);

        int temp = a[i];
        while (temp > 1) {
            int p = spf[temp];
            prime_count[p]++;
            if (prime_count[p] > 1) pairwise = false;
            while (temp % p == 0) temp /= p;
        }
    }

    if (pairwise) {
        cout << "pairwise coprime\n";
    } else if (overall_gcd == 1) {
        cout << "setwise coprime\n";
    } else {
        cout << "not coprime\n";
    }

    return 0;
}
```
