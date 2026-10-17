#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }

    int max_j = min(n + 1, m + 1);
    vector<long long> dp(max_j + 1, 0);
    dp[0] = 1;

    for (int i = 0; i < n; ++i) {
        vector<long long> next_dp(max_j + 1, 0);

        for (int j = 0; j <= max_j; ++j) {
            if (dp[j] == 0) continue;

            if (s[i] == 1) {
                // Must pick MEX
                if (j + 1 <= max_j) {
                    next_dp[j + 1] = (next_dp[j + 1] + dp[j]) % MOD;
                }
            } else {
                // Must not pick MEX
                // 1. Pick from j already used numbers
                next_dp[j] = (next_dp[j] + dp[j] * j) % MOD;

                // 2. Pick an unused number != MEX: there are max(0, M - j) choices
                if (j < m && j + 1 <= max_j) {
                    next_dp[j + 1] = (next_dp[j + 1] + dp[j] * (m - j)) % MOD;
                }
            }
        }
        dp = move(next_dp);
    }

    long long ans = 0;
    for (int j = 0; j <= max_j; ++j) {
        ans = (ans + dp[j]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
