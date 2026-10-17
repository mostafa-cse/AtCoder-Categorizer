# Digit DP

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Digit DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Digit DP**.

---

## Curated Problems

### `[problem:AtCoder-abc182_f]` — Valid payments
- **Rating / Difficulty**: 2121
- **Contest**: `abc182`
- **Analysis**: [`analysis/AtCoder-abc182_f.md`](../../analysis/AtCoder-abc182_f.md)
- **Key Idea**: Let c_i = A_{i+1} / A_i. Any amount in greedy canonical representation has digit at A_i in [0, c_i - 1]. In base A, X has unique greedy digits d_i. When paying, for denomination A_i, we can either pay exactly d_i + carry coins (no carry forward), or pay d_i + carry + 1 coins (giving 1 carry forward to A_{i+1} and receiving c_i - (d_i + carry + 1) change, provided d_i + carry > 0). This is a clean 2-state DP over carry in {0, 1}.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long X;
    if (!(cin >> n >> X)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> c(n);
    for (int i = 0; i < n - 1; ++i) {
        c[i] = a[i + 1] / a[i];
    }

    vector<long long> d(n);
    long long rem = X;
    for (int i = n - 1; i >= 0; --i) {
        d[i] = rem / a[i];
        rem %= a[i];
    }

    map<long long, long long> dp;
    dp[0] = 1;

    for (int i = 0; i < n - 1; ++i) {
        map<long long, long long> next_dp;
        for (auto& entry : dp) {
            long long carry = entry.first;
            long long ways = entry.second;

            long long cur_d = d[i] + carry;

            long long pay1 = cur_d % c[i];
            long long next_carry1 = cur_d / c[i];
            next_dp[next_carry1] += ways;

            if (pay1 > 0) {
                long long next_carry2 = next_carry1 + 1;
                next_dp[next_carry2] += ways;
            }
        }
        dp = next_dp;
    }

    long long ans = 0;
    for (auto& entry : dp) {
        ans += entry.second;
    }

    cout << ans << "\n";
    return 0;
}
```
