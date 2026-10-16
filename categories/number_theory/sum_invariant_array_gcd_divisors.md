# Sum-Invariant Divisor Analysis on Array GCD

**Domain**: `Number Theory`  
**Subtopic**: `Divisors`  

This workbook contains curated, high-quality competitive programming problems teaching **Sum-Invariant Divisor Analysis on Array GCD**.

---

## Curated Problems

### `[problem:AtCoder-abc136_e]` — Max GCD
- **Rating / Difficulty**: 1670
- **Contest**: `abc136`
- **Analysis**: [`analysis/AtCoder-abc136_e.md`](../../analysis/AtCoder-abc136_e.md)
- **Key Idea**: Each operation increments one element and decrements another, so the sum S = sum_{i=1}^N A_i is strictly invariant! Thus, the final GCD must divide S.
- **Time Complexity**: `O(d(S) * N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long total_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total_sum += a[i];
    }

    vector<long long> divisors;
    for (long long d = 1; d * d <= total_sum; ++d) {
        if (total_sum % d == 0) {
            divisors.push_back(d);
            if (d * d != total_sum) {
                divisors.push_back(total_sum / d);
            }
        }
    }
    sort(divisors.rbegin(), divisors.rend());

    for (long long d : divisors) {
        vector<long long> r(n);
        long long sum_rem = 0;
        for (int i = 0; i < n; ++i) {
            r[i] = a[i] % d;
            sum_rem += r[i];
        }
        sort(r.begin(), r.end());

        int p = n - (sum_rem / d);
        long long ops = 0;
        for (int i = 0; i < p; ++i) {
            ops += r[i];
        }

        if (ops <= k) {
            cout << d << "\n";
            return 0;
        }
    }

    cout << 1 << "\n";
    return 0;
}
```
