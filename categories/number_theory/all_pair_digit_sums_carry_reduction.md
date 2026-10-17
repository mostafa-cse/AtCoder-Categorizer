# Carry Reduction Identity for All-Pair Digit Sums

**Domain**: `Number Theory`  
**Subtopic**: `Digit Sum Invariants`  

This workbook contains curated, high-quality competitive programming problems teaching **Carry Reduction Identity for All-Pair Digit Sums**.

---

## Curated Problems

### `[problem:AtCoder-arc158_c]` — All Pair Digit Sums
- **Rating / Difficulty**: 1875
- **Contest**: `arc158`
- **Analysis**: [`analysis/AtCoder-arc158_c.md`](../../analysis/AtCoder-arc158_c.md)
- **Key Idea**: The key mathematical identity is: f(A + B) = f(A) + f(B) - 9 * (number of carries when adding A and B). Summing over all N^2 pairs, the base sum is 2N * sum f(A_i). Carries at digit 10^k occur iff (A_i mod 10^k) + (A_j mod 10^k) >= 10^k.
- **Time Complexity**: `O(15 * N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long digit_sum(long long n) {
    long long s = 0;
    while (n > 0) {
        s += n % 10;
        n /= 10;
    }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    long long total_digit_sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total_digit_sum += digit_sum(a[i]);
    }

    long long base_ans = 2LL * n * total_digit_sum;
    long long total_carries = 0;

    long long pow10 = 10;
    for (int k = 1; k <= 15; ++k) {
        vector<long long> r(n);
        for (int i = 0; i < n; ++i) {
            r[i] = a[i] % pow10;
        }
        sort(r.begin(), r.end());

        int ptr = n - 1;
        long long carry_count = 0;
        for (int i = 0; i < n; ++i) {
            while (ptr >= 0 && r[i] + r[ptr] >= pow10) {
                ptr--;
            }
            carry_count += (n - 1 - ptr);
        }

        total_carries += carry_count;
        if (k < 15) pow10 *= 10;
    }

    cout << base_ans - 9LL * total_carries << "\n";
    return 0;
}
```
