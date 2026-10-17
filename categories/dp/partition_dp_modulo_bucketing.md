# Partition DP with Modulo Remainder State Bucketing

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Partition DP with Modulo Remainder State Bucketing**.

---

## Curated Problems

### `[problem:AtCoder-abc207_e]` — Mod i
- **Rating / Difficulty**: 1820
- **Contest**: `abc207`
- **Analysis**: [`analysis/AtCoder-abc207_e.md`](../../analysis/AtCoder-abc207_e.md)
- **Key Idea**: Let dp[j][i] be the number of valid j-part partitions of prefix A[1..i]. Transitioning to j + 1 requires the next subarray sum S_i - S_p to be divisible by j + 1, which means S_p = S_i (mod j + 1). Maintain bucket[rem] summing dp[j][p] for each remainder rem mod (j + 1).
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    vector<long long> s(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        s[i] = s[i - 1] + a[i];
    }

    // dp[i]: ways to partition prefix i into current number of segments
    vector<long long> dp(n + 1, 1);
    dp[0] = 1;

    long long total_ans = dp[n];

    for (int j = 2; j <= n; ++j) {
        vector<long long> bucket(j, 0);
        vector<long long> next_dp(n + 1, 0);

        for (int i = 1; i <= n; ++i) {
            bucket[s[i - 1] % j] = (bucket[s[i - 1] % j] + dp[i - 1]) % MOD;
            next_dp[i] = bucket[s[i] % j];
        }

        total_ans = (total_ans + next_dp[n]) % MOD;
        dp = move(next_dp);
    }

    cout << total_ans << "\n";
    return 0;
}
```
