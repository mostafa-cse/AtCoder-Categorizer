# Probabilities and Expected Values

**Domain**: `Math`  
**Subtopic**: `Probabilities and Expected Values`  

This workbook contains curated, high-quality competitive programming problems teaching **Probabilities and Expected Values**.

---

## Curated Problems

### `[problem:AtCoder-abc342_f]` — Black Jack
- **Rating / Difficulty**: 2141
- **Contest**: `abc342`
- **Analysis**: [`analysis/AtCoder-abc342_f.md`](../../analysis/AtCoder-abc342_f.md)
- **Key Idea**: Phase 1: Compute the dealer's final score distribution using a sliding window sum over the transition P[i] = (1/D) * sum_{j=i-D}^{i-1} P[j] for rolls below L. Scores above N are accumulated into dealer_bust. Phase 2: Compute player's optimal stopping DP backward from score N down to 0: at score x, stopping wins with probability P_stop = dealer_bust + P(dealer < x); rolling gives P_roll = (1/D) * sum_{d=1}^D dp[x + d]. Take dp[x] = max(P_stop, P_roll). Both phases run in O(N + D) using rolling prefix windows.
- **Time Complexity**: `O(N + D)`
- **Space Complexity**: `O(N + D)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, l, d;
    if (!(cin >> n >> l >> d)) return 0;

    vector<double> P(n + d + 5, 0.0);
    P[0] = 1.0;
    double window = 0.0;

    vector<double> dealer_final(n + d + 5, 0.0);
    double dealer_bust = 0.0;

    for (int i = 1; i <= n + d; ++i) {
        if (i - 1 < l) window += P[i - 1];
        if (i - 1 - d >= 0 && i - 1 - d < l) window -= P[i - 1 - d];
        P[i] = window / d;

        if (i >= l) {
            if (i <= n) {
                dealer_final[i] = P[i];
            } else {
                dealer_bust += P[i];
            }
        }
    }

    vector<double> dealer_pref(n + 2, 0.0);
    for (int i = 0; i <= n; ++i) {
        dealer_pref[i + 1] = dealer_pref[i] + dealer_final[i];
    }

    vector<double> dp(n + d + 5, 0.0);
    double roll_window = 0.0;

    for (int x = n; x >= 0; --x) {
        double p_stop = dealer_bust + dealer_pref[x];
        double p_roll = roll_window / d;

        dp[x] = max(p_stop, p_roll);

        roll_window += dp[x];
        if (x + d <= n + d) roll_window -= dp[x + d];
    }

    cout << fixed << setprecision(10) << dp[0] << "\n";
    return 0;
}
```
