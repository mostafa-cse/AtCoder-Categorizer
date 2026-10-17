#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct Infant {
    long long a;
    int pos;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Infant> infants(n);
    for (int i = 0; i < n; ++i) {
        cin >> infants[i].a;
        infants[i].pos = i + 1;
    }

    sort(infants.begin(), infants.end(), [](const Infant& u, const Infant& v) {
        return u.a > v.a;
    });

    // dp[l][r]
    vector<vector<long long>> dp(n + 1, vector<long long>(n + 1, 0));

    for (int k = 0; k < n; ++k) {
        long long a = infants[k].a;
        int orig_pos = infants[k].pos;

        for (int l = 0; l <= k; ++l) {
            int r = k - l;

            // Place at left: slot l + 1
            dp[l + 1][r] = max(dp[l + 1][r], dp[l][r] + a * abs(orig_pos - (l + 1)));

            // Place at right: slot n - r
            dp[l][r + 1] = max(dp[l][r + 1], dp[l][r] + a * abs(orig_pos - (n - r)));
        }
    }

    long long ans = 0;
    for (int l = 0; l <= n; ++l) {
        ans = max(ans, dp[l][n - l]);
    }

    cout << ans << "\n";
    return 0;
}
