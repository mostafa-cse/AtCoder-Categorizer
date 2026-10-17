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

    vector<vector<long long>> dp(n + 1, vector<long long>(n + 1, 0));
    dp[0][0] = 1;

    for (int i = 1; i <= n; ++i) {
        int forbidden = (i - 1) / m;
        for (int j = 1; j <= i; ++j) {
            long long choices = max(0, j - forbidden);
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] * choices) % MOD;
        }
    }

    for (int k = 1; k <= n; ++k) {
        cout << dp[n][k] << "\n";
    }

    return 0;
}
