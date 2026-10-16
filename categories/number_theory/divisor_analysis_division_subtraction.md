# Number Theory Divisor Analysis on N and N-1

**Domain**: `Number Theory`  
**Subtopic**: `Divisors`  

This workbook contains curated, high-quality competitive programming problems teaching **Number Theory Divisor Analysis on N and N-1**.

---

## Curated Problems

### `[problem:AtCoder-abc161_f]` — Division or Subtraction
- **Rating / Difficulty**: 1528
- **Contest**: `abc161`
- **Analysis**: [`analysis/AtCoder-abc161_f.md`](../../analysis/AtCoder-abc161_f.md)
- **Key Idea**: Split into two cases: 1) K divides N initially; 2) K does not divide N initially.
- **Time Complexity**: `O(sqrt(N))`
- **Space Complexity**: `O(sqrt(N))`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    set<long long> valid_k;

    // Case 1: K does not divide N initially => K must divide N - 1
    long long n_minus_1 = n - 1;
    for (long long d = 1; d * d <= n_minus_1; ++d) {
        if (n_minus_1 % d == 0) {
            if (d >= 2) valid_k.insert(d);
            if (n_minus_1 / d >= 2) valid_k.insert(n_minus_1 / d);
        }
    }

    // Case 2: K divides N initially
    for (long long d = 1; d * d <= n; ++d) {
        if (n % d == 0) {
            auto test_k = [&](long long k) {
                if (k < 2) return;
                long long temp = n;
                while (temp % k == 0) temp /= k;
                if (temp % k == 1) valid_k.insert(k);
            };
            test_k(d);
            test_k(n / d);
        }
    }

    cout << valid_k.size() << "\n";
    return 0;
}
```
