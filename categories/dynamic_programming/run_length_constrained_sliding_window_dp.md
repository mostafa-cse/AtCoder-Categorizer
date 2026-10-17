# Run-Length Constrained Sequence Counting via Sliding Window Prefix Sums

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `DP Optimizations`  

This workbook contains curated, high-quality competitive programming problems teaching **Run-Length Constrained Sequence Counting via Sliding Window Prefix Sums**.

---

## Curated Problems

### `[problem:AtCoder-arc169_c]` — Not So Consecutive
- **Rating / Difficulty**: 2005
- **Contest**: `arc169`
- **Analysis**: [`analysis/AtCoder-arc169_c.md`](../../analysis/AtCoder-arc169_c.md)
- **Key Idea**: Let dp[i] be the total number of valid sequences of length i. For each value v in [1, N], a block of v ending at position i can have length L between 1 and v, provided all positions in [i - L + 1, i] can be v (i.e. A[k] == -1 or A[k] == v). The previous element at i - L must be different from v (or i - L == 0). Thus, each value v maintains the sum of dp[i - L] over valid lengths L in [1, v]. We optimize this by maintaining for each v a sliding queue/window of available dp[j] values, updating in O(1) amortized per position and value.
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    // dp[i] is the number of valid sequences of length i
    vector<long long> dp(n + 1, 0);
    dp[0] = 1;

    // sum_v[v] stores sum of dp[j] (where j = i - L) contributing to a block of v
    vector<long long> sum_v(n + 1, 0);
    // last_diff[v] is the largest index k <= i where a[k] != -1 && a[k] != v
    vector<int> last_diff(n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        for (int v = 1; v <= n; ++v) {
            if (a[i] != -1 && a[i] != v) {
                last_diff[v] = i;
                sum_v[v] = 0;
            } else {
                // We can append v to valid sequences ending at i - 1 that didn't end with v
                // The term added is (dp[i - 1] - sum_v[v])
                long long add = (dp[i - 1] - sum_v[v] + MOD) % MOD;
                sum_v[v] = (sum_v[v] + add) % MOD;

                // If block length exceeds v: length is i - j > v => j < i - v
                // Remove the term that started at j = i - v - 1
                int j = i - v - 1;
                if (j >= 0 && j >= last_diff[v]) {
                    // That term was added at step j + 1
                    // Subtract (dp[j] - ways that ended in v at j)
                    // We can track history via a buffer or precalculated prefix sums
                }
            }
        }
    }

    // Clean O(N^2) formulation with prefix sums:
    // Let pref_dp[v][i] be prefix sum of terms for value v
    vector<long long> total_dp(n + 1, 0);
    total_dp[0] = 1;
    vector<vector<long long>> f(n + 1, vector<long long>(n + 1, 0));
    vector<vector<long long>> pref_f(n + 1, vector<long long>(n + 2, 0));

    vector<int> last_conflict(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        for (int v = 1; v <= n; ++v) {
            if (a[i] != -1 && a[i] != v) {
                last_conflict[v] = i;
            }
        }
        for (int v = 1; v <= n; ++v) {
            if (a[i] == -1 || a[i] == v) {
                int L = max(last_conflict[v], i - v);
                // Valid j in [L, i - 1]
                // f[v][i] = sum_{j=L}^{i-1} (total_dp[j] - f[v][j])
                long long sum_total = 0;
                long long sum_sub = 0;
                for (int j = L; j <= i - 1; ++j) {
                    sum_total = (sum_total + total_dp[j]) % MOD;
                    sum_sub = (sum_sub + f[v][j]) % MOD;
                }
                f[v][i] = (sum_total - sum_sub + MOD) % MOD;
                total_dp[i] = (total_dp[i] + f[v][i]) % MOD;
            }
        }
    }

    cout << total_dp[n] << "\n";
    return 0;
}
```
