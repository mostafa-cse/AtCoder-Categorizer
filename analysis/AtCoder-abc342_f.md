# Problem Analysis: AtCoder-abc342_f — Black Jack

**Problem ID**: `AtCoder-abc342_f`  
**Contest**: `abc342`  
**Rating / Difficulty**: 2141  
**URL**: https://atcoder.jp/contests/abc342/tasks/abc342_f  
**VJudge Tag**: `[problem:AtCoder-abc342_f]`  
**Category File**: [`../categories/math/rolling_window_probability_dp_optimal_stopping.md`](../categories/math/rolling_window_probability_dp_optimal_stopping.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Player and Dealer play a modified Blackjack with dice rolls in 1..D. Bust threshold is N. Dealer rolls until score >= L. Player rolls to maximize probability of beating Dealer.

**Key Insight**: Phase 1: Compute the dealer's final score distribution using a sliding window sum over the transition P[i] = (1/D) * sum_{j=i-D}^{i-1} P[j] for rolls below L. Scores above N are accumulated into dealer_bust. Phase 2: Compute player's optimal stopping DP backward from score N down to 0: at score x, stopping wins with probability P_stop = dealer_bust + P(dealer < x); rolling gives P_roll = (1/D) * sum_{d=1}^D dp[x + d]. Take dp[x] = max(P_stop, P_roll). Both phases run in O(N + D) using rolling prefix windows.

## 2. Core Observation & Invariant
Independent dealer distribution precomputation followed by backward sliding-window DP finds the optimal stopping boundary in linear time.

## 3. Step-by-Step Algorithm
1. Compute dealer score distribution using rolling window of length D.
2. Aggregate dealer bust probability and prefix sum of dealer scores.
3. Backward sweep for player score x from N down to 0:
4.   p_stop = dealer_bust + dealer_pref[x].
5.   p_roll = roll_window / D.
6.   dp[x] = max(p_stop, p_roll), update roll_window.
7. Output dp[0].

## 4. Complexity Analysis
- **Time Complexity**: `O(N + D)`
- **Space Complexity**: `O(N + D)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Optimal stopping game theory and sliding window probability DP.
- **Reusable Pattern**: Dice-based sequential games resolved via dealer distribution precomputation and backward player DP with rolling window transitions.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
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
