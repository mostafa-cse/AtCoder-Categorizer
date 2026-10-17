#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

const long long NEG_INF = -1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long y, z;
    if (!(cin >> n >> m >> y >> z)) return 0;

    map<char, int> color_idx;
    vector<long long> p(m);
    for (int i = 0; i < m; ++i) {
        char c;
        long long pt;
        cin >> c >> pt;
        color_idx[c] = i;
        p[i] = pt;
    }

    string s;
    cin >> s;

    int total_masks = (1 << m);
    // last_color: 0 .. m - 1, and m means empty
    vector<vector<long long>> dp(total_masks, vector<long long>(m + 1, NEG_INF));
    dp[0][m] = 0;

    for (char ch : s) {
        int c = color_idx[ch];
        vector<vector<long long>> next_dp = dp;

        for (int mask = 0; mask < total_masks; ++mask) {
            for (int last = 0; last <= m; ++last) {
                if (dp[mask][last] == NEG_INF) continue;

                int nmask = mask | (1 << c);
                long long gain = p[c];
                if (last == c) gain += y;
                if (mask != total_masks - 1 && nmask == total_masks - 1) gain += z;

                next_dp[nmask][c] = max(next_dp[nmask][c], dp[mask][last] + gain);
            }
        }
        dp = move(next_dp);
    }

    long long ans = 0;
    for (int mask = 0; mask < total_masks; ++mask) {
        for (int last = 0; last <= m; ++last) {
            ans = max(ans, dp[mask][last]);
        }
    }

    cout << ans << "\n";
    return 0;
}
