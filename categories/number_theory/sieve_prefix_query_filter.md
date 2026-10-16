# Sieve of Eratosthenes + Prefix Sum Query Filtering

**Domain**: `Number Theory`  
**Subtopic**: `Sieve & Prefix Sums`  

This workbook contains curated, high-quality competitive programming problems teaching **Sieve of Eratosthenes + Prefix Sum Query Filtering**.

---

## Curated Problems

### [problem:AtCoder-abc084_d] — 2017-like Number
- **Contest**: `abc084`
- **Rating / Difficulty**: 980
- **Specific Skill**: Sieve of Eratosthenes + Prefix Sum Query Filtering
- **Individual Analysis**: [`../../analysis/AtCoder-abc084_d.md`](../../analysis/AtCoder-abc084_d.md)
- **Problem Statement Summary**: An odd number N is '2017-like' if both N and (N + 1) / 2 are prime. Answer Q queries: count 2017-like numbers in range [l, r] (l, r <= 10^5, Q <= 10^5).
- **Core Insight**: A number N is 2017-like if N % 2 == 1, is_prime[N], and is_prime[(N + 1) / 2]. Store a binary array is_2017[N]. Its prefix sum array pref[x] = sum_{i=1}^x is_2017[i] answers queries via pref[r] - pref[l - 1].
- **Complexity**: Time: `O(MAX log log MAX + Q)` | Space: `O(MAX)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 100000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<bool> is_prime(MAX + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p <= MAX; ++p) {
        if (is_prime[p]) {
            for (int i = p * p; i <= MAX; i += p) {
                is_prime[i] = false;
            }
        }
    }

    vector<int> is_2017(MAX + 1, 0);
    for (int i = 1; i <= MAX; ++i) {
        if (i % 2 == 1 && is_prime[i] && is_prime[(i + 1) / 2]) {
            is_2017[i] = 1;
        }
    }

    vector<int> pref(MAX + 1, 0);
    for (int i = 1; i <= MAX; ++i) {
        pref[i] = pref[i - 1] + is_2017[i];
    }

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << pref[r] - pref[l - 1] << "\n";
    }

    return 0;
}
```
