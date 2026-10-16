# Linear Congruence Equation via Extended Euclidean Algorithm

**Domain**: `Number Theory`  
**Subtopic**: `Linear Congruence`  

This workbook contains curated, high-quality competitive programming problems teaching **Linear Congruence Equation via Extended Euclidean Algorithm**.

---

## Curated Problems

### `[problem:AtCoder-abc186_e]` — Throne
- **Rating / Difficulty**: 1461
- **Contest**: `abc186`
- **Analysis**: [`analysis/AtCoder-abc186_e.md`](../../analysis/AtCoder-abc186_e.md)
- **Key Idea**: Landing on 0 is equivalent to the linear congruence K * x = -S (mod N), solved using the Extended Euclidean Algorithm.
- **Time Complexity**: `O(T * log(min(N, K)))`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>

using namespace std;

long long extGCD(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long g = extGCD(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

void solve() {
    long long n, s, k;
    cin >> n >> s >> k;

    long long b = (n - s) % n;
    long long x, y;
    long long g = extGCD(k, n, x, y);

    if (b % g != 0) {
        cout << -1 << "\n";
        return;
    }

    long long n_prime = n / g;
    long long b_prime = b / g;
    long long k_prime = k / g;

    extGCD(k_prime, n_prime, x, y);
    x = (x % n_prime + n_prime) % n_prime;

    long long ans = (__int128)x * b_prime % n_prime;
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
```
