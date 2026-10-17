# Knapsack and Basic Dynamic Programming

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Intro to DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Knapsack and Basic Dynamic Programming**.

---

## Curated Problems

### `[problem:AtCoder-abc132_f]` — Small Products
- **Rating / Difficulty**: 2143
- **Contest**: `abc132`
- **Analysis**: [`analysis/AtCoder-abc132_f.md`](../../analysis/AtCoder-abc132_f.md)
- **Key Idea**: The condition A_{i+1} <= floor(N / A_i) implies the valid range of next elements depends solely on floor(N / A_i). The quotient floor(N / x) takes at most 2 * sqrt(N) distinct values! We partition [1, N] into O(sqrt(N)) blocks of equal quotient. DP transitions sum over valid quotient blocks using prefix sums in O(K * sqrt(N)).
- **Time Complexity**: `O(K * sqrt(N))`
- **Space Complexity**: `O(sqrt(N))`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> vals;
    for (long long l = 1; l <= n; ) {
        long long q = n / l;
        long long r = n / q;
        vals.push_back(q);
        l = r + 1;
    }
    reverse(vals.begin(), vals.end());

    int m = vals.size();
    vector<long long> count_in_block(m);
    long long prev = 0;
    for (int i = 0; i < m; ++i) {
        count_in_block[i] = (n / vals[i] - prev) % MOD;
        prev = n / vals[i];
    }

    vector<long long> dp(m, 0);
    for (int i = 0; i < m; ++i) {
        dp[i] = count_in_block[i];
    }

    for (int step = 2; step <= k; ++step) {
        vector<long long> pref(m + 1, 0);
        for (int i = 0; i < m; ++i) {
            pref[i + 1] = (pref[i] + dp[i]) % MOD;
        }

        vector<long long> next_dp(m, 0);
        for (int i = 0; i < m; ++i) {
            int opp = m - 1 - i;
            long long sum_ways = pref[opp + 1];
            next_dp[i] = (sum_ways * count_in_block[i]) % MOD;
        }
        dp = next_dp;
    }

    long long total_ans = 0;
    for (int i = 0; i < m; ++i) {
        total_ans = (total_ans + dp[i]) % MOD;
    }

    cout << total_ans << "\n";
    return 0;
}
```
