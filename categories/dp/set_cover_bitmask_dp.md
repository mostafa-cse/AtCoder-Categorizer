# Exact Set Cover Shortest Path / Bitmask Knapsack DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `Bitmask DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Exact Set Cover Shortest Path / Bitmask Knapsack DP**.

---

## Curated Problems

### [problem:AtCoder-abc142_e] — Get Everything
- **Contest**: `abc142`
- **Rating / Difficulty**: 1397
- **Specific Skill**: Exact Set Cover Shortest Path / Bitmask Knapsack DP
- **Individual Analysis**: [`../../analysis/AtCoder-abc142_e.md`](../../analysis/AtCoder-abc142_e.md)
- **Problem Statement Summary**: N treasure boxes and M keys (N <= 12). Key i costs a_i yen and unlocks a subset of boxes c_1..c_b. Find the minimum cost to unlock all N boxes (or -1 if impossible).
- **Core Insight**: Because N <= 12, the total number of states is 2^N <= 4096. Define dp[mask] = minimum cost to unlock the subset of boxes in mask. Base case: dp[0] = 0. For each key with cost a and mask key_mask: for each state s from 0 to 2^N - 1: dp[s | key_mask] = min(dp[s | key_mask], dp[s] + a).
- **Complexity**: Time: `O(M * 2^N)` | Space: `O(2^N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e15;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    int total_masks = 1 << n;
    vector<long long> dp(total_masks, INF);
    dp[0] = 0;

    for (int i = 0; i < m; ++i) {
        long long cost;
        int b;
        cin >> cost >> b;
        int key_mask = 0;
        for (int j = 0; j < b; ++j) {
            int box;
            cin >> box;
            key_mask |= (1 << (box - 1));
        }

        for (int mask = 0; mask < total_masks; ++mask) {
            if (dp[mask] == INF) continue;
            int nxt = mask | key_mask;
            dp[nxt] = min(dp[nxt], dp[mask] + cost);
        }
    }

    long long ans = dp[total_masks - 1];
    cout << (ans == INF ? -1 : ans) << "\n";
    return 0;
}
```
