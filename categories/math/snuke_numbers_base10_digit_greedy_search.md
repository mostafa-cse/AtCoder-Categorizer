# Snuke Numbers via Base-10 Digit Addition and S(x) Ratio Greedy Search

**Domain**: `Math`  
**Subtopic**: `Number Theory`  

This workbook contains curated, high-quality competitive programming problems teaching **Snuke Numbers via Base-10 Digit Addition and S(x) Ratio Greedy Search**.

---

## Curated Problems

### `[problem:AtCoder-arc099_b]` — Snuke Numbers
- **Rating / Difficulty**: 2001
- **Contest**: `abc101`
- **Analysis**: [`analysis/AtCoder-arc099_b.md`](../../analysis/AtCoder-arc099_b.md)
- **Key Idea**: Between n and larger integers, the next candidate Snuke number is always obtained by incrementing some power of 10: n + 10^p. For large numbers, suffixes of 9s yield smaller ratios m / S(m). By maintaining the current Snuke number cur, we evaluate candidate numbers cur + 10^p for all 0 <= p <= 14. We pick the candidate that minimizes candidate / S(candidate). Repeating this greedily generates all Snuke numbers up to K.
- **Time Complexity**: `O(K * 15 * log10(X))`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

long long digit_sum(long long x) {
    long long s = 0;
    while (x > 0) {
        s += x % 10;
        x /= 10;
    }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    long long cur = 1;
    vector<long long> pow10(16);
    pow10[0] = 1;
    for (int i = 1; i <= 15; ++i) {
        pow10[i] = pow10[i - 1] * 10;
    }

    for (int step = 0; step < k; ++step) {
        cout << cur << "\n";
        long long best_cand = cur + 1;
        double best_val = (double)best_cand / digit_sum(best_cand);

        for (int p = 0; p <= 14; ++p) {
            long long cand = cur + pow10[p];
            double val = (double)cand / digit_sum(cand);
            if (val < best_val) {
                best_val = val;
                best_cand = cand;
            }
        }
        cur = best_cand;
    }

    return 0;
}
```
