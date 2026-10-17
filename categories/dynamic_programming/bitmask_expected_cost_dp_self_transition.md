# Bitmask DP

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Bit Related DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Bitmask DP**.

---

## Curated Problems

### `[problem:AtCoder-arc016_3]` — Gacha
- **Rating / Difficulty**: 2087
- **Contest**: `arc016`
- **Analysis**: [`analysis/AtCoder-arc016_3.md`](../../analysis/AtCoder-arc016_3.md)
- **Key Idea**: Let dp[mask] be the minimum expected cost to collect all remaining prizes when the currently collected set of prizes is mask. From state mask, if we decide to roll gacha j, some prize we roll might already be in mask (a self-loop occurring with probability p_stay = sum_{k in mask} P_{j,k} / 100), or it might yield a new prize k not in mask. Setting up the Bellman expectation equation: E_j[mask] = C_j + p_stay * E_j[mask] + sum_{k not in mask} (P_{j,k} / 100) * dp[mask | (1 << k)]. Solving for E_j[mask]: E_j[mask] = (C_j + sum_{k not in mask} (P_{j,k}/100) * dp[mask | (1 << k)]) / (1 - p_stay). Then dp[mask] = min_j E_j[mask].
- **Time Complexity**: `O(M * N * 2^N)`
- **Space Complexity**: `O(2^N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

struct Gacha {
    double cost;
    vector<pair<int, double>> prizes; // (id, prob)
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Gacha> gachas(m);
    for (int j = 0; j < m; ++j) {
        int c, cost;
        cin >> c >> cost;
        gachas[j].cost = cost;
        for (int i = 0; i < c; ++i) {
            int prize;
            double p;
            cin >> prize >> p;
            gachas[j].prizes.push_back({prize - 1, p / 100.0});
        }
    }

    int full = 1 << n;
    vector<double> dp(full, 1e18);
    dp[full - 1] = 0.0;

    for (int mask = full - 2; mask >= 0; --mask) {
        for (int j = 0; j < m; ++j) {
            double p_stay = 0.0;
            double next_exp = 0.0;
            for (auto& item : gachas[j].prizes) {
                int prize = item.first;
                double prob = item.second;
                if ((mask >> prize) & 1) {
                    p_stay += prob;
                } else {
                    next_exp += prob * dp[mask | (1 << prize)];
                }
            }
            if (p_stay >= 1.0 - 1e-9) continue;
            double cost = (gachas[j].cost + next_exp) / (1.0 - p_stay);
            dp[mask] = min(dp[mask], cost);
        }
    }

    cout << fixed << setprecision(10) << dp[0] << "\n";
    return 0;
}
```
