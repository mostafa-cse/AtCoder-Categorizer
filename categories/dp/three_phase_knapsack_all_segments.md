# 3-Phase Automaton Knapsack DP for All-Subsegment Subset Counting

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **3-Phase Automaton Knapsack DP for All-Subsegment Subset Counting**.

---

## Curated Problems

### `[problem:AtCoder-abc159_f]` — Knapsack for All Segments
- **Rating / Difficulty**: 1876
- **Contest**: `abc159`
- **Analysis**: [`analysis/AtCoder-abc159_f.md`](../../analysis/AtCoder-abc159_f.md)
- **Key Idea**: Each element belongs to one of three phases: Phase 0 (before L), Phase 1 (inside [L, R]), and Phase 2 (after R). Maintaining DP over the 3 phases allows simultaneous summation over all choices of L and R.
- **Time Complexity**: `O(N * S)`
- **Space Complexity**: `O(S)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, S;
    if (!(cin >> n >> S)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> dp(S + 1, 0);
    long long total_ans = 0;

    for (int v : a) {
        dp[0] = (dp[0] + 1) % MOD; // start segment here

        for (int s = S; s >= v; --s) {
            dp[s] = (dp[s] + dp[s - v]) % MOD;
        }

        total_ans = (total_ans + dp[S]) % MOD; // end segment here
    }

    cout << total_ans << "\n";
    return 0;
}
```
