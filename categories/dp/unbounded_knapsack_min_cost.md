# Unbounded Knapsack / Minimum Cost Target Reachability

**Domain**: `Dynamic Programming`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Unbounded Knapsack / Minimum Cost Target Reachability**.

---

## Curated Problems

### [problem:AtCoder-abc153_e] — Crested Ibis vs Monster
- **Contest**: `abc153`
- **Rating / Difficulty**: 1015
- **Specific Skill**: Unbounded Knapsack / Minimum Cost Target Reachability
- **Individual Analysis**: [`../../analysis/AtCoder-abc153_e.md`](../../analysis/AtCoder-abc153_e.md)
- **Problem Statement Summary**: A monster has H health. You have N spells. Spell i deals A_i damage and costs B_i magic points. Each spell can be used any number of times. Find the minimum total magic points to deal at least H damage.
- **Core Insight**: Transitions: for each damage state h from 0 to H - 1, and for each spell (A_i, B_i): dealing damage A_i transitions to min(H, h + A_i) at cost dp[h] + B_i. Since spells can be reused, update in-place in increasing order of h.
- **Complexity**: Time: `O(N * H)` | Space: `O(H)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, n;
    if (!(cin >> h >> n)) return 0;

    vector<pair<int, int>> spells(n);
    for (int i = 0; i < n; ++i) {
        cin >> spells[i].first >> spells[i].second;
    }

    vector<long long> dp(h + 1, INF);
    dp[0] = 0;

    for (int cur = 0; cur < h; ++cur) {
        if (dp[cur] == INF) continue;
        for (const auto& [dmg, cost] : spells) {
            int nxt = min(h, cur + dmg);
            dp[nxt] = min(dp[nxt], dp[cur] + cost);
        }
    }

    cout << dp[h] << "\n";
    return 0;
}
```
