#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    auto is_needed = [&](int idx) {
        if (a[idx] >= k) return true;

        vector<bool> dp(k, false);
        dp[0] = true;

        for (int i = 0; i < n; ++i) {
            if (i == idx) continue;
            long long val = a[i];
            if (val >= k) continue;

            for (long long s = k - 1; s >= val; --s) {
                if (dp[s - val]) dp[s] = true;
            }
        }

        long long low_bound = max(0LL, k - a[idx]);
        for (long long s = low_bound; s < k; ++s) {
            if (dp[s]) return true;
        }
        return false;
    };

    int low = 0, high = n - 1, ans = 0;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (!is_needed(mid)) {
            ans = mid + 1;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
