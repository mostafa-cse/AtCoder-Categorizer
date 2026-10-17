# Prime Modular Suffix Invariant for Divisible Substring Counting

**Domain**: `Number Theory`  
**Subtopic**: `Modular Invariants`  

This workbook contains curated, high-quality competitive programming problems teaching **Prime Modular Suffix Invariant for Divisible Substring Counting**.

---

## Curated Problems

### `[problem:AtCoder-abc158_e]` — Divisible Substring
- **Rating / Difficulty**: 1866
- **Contest**: `abc158`
- **Analysis**: [`analysis/AtCoder-abc158_e.md`](../../analysis/AtCoder-abc158_e.md)
- **Key Idea**: If P = 2 or P = 5: divisibility depends only on the last digit (S[r] % P == 0). If gcd(10, P) = 1: value of S[l..r] is (suf[l] - suf[r + 1]) * 10^{-(N - r)} mod P. Since 10 is invertible mod P, value = 0 (mod P) iff suf[l] = suf[r + 1] (mod P).
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(P)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, p;
    if (!(cin >> n >> p)) return 0;

    string s;
    cin >> s;

    long long ans = 0;

    if (p == 2 || p == 5) {
        for (int i = 0; i < n; ++i) {
            if ((s[i] - '0') % p == 0) {
                ans += (i + 1);
            }
        }
    } else {
        vector<long long> freq(p, 0);
        freq[0] = 1;
        long long cur_suf = 0;
        long long pow10 = 1;

        for (int i = n - 1; i >= 0; --i) {
            cur_suf = (cur_suf + (s[i] - '0') * pow10) % p;
            pow10 = (pow10 * 10) % p;
            ans += freq[cur_suf];
            freq[cur_suf]++;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
