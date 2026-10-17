#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> nxt(n);
    int ptr = 0;
    for (int i = 0; i < n; ++i) {
        while (ptr < n && a[ptr] < 2 * a[i]) {
            ptr++;
        }
        nxt[i] = (ptr < n ? ptr : INF);
    }

    vector<int> val(n);
    for (int i = 0; i < n; ++i) {
        val[i] = (nxt[i] == INF ? INF : nxt[i] - i);
    }

    int log_n = 0;
    while ((1 << log_n) <= n) log_n++;
    vector<vector<int>> st(log_n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        st[0][i] = val[i];
    }
    for (int k = 1; k < log_n; ++k) {
        for (int i = 0; i + (1 << k) <= n; ++i) {
            st[k][i] = max(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
        }
    }

    auto query_max = [&](int l, int r) {
        int len = r - l + 1;
        int k = 31 - __builtin_clz(len);
        return max(st[k][l], st[k][r - (1 << k) + 1]);
    };

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int l, r;
        cin >> l >> r;
        --l; --r;
        int len = r - l + 1;
        int low = 0, high = len / 2, ans = 0;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                ans = max(ans, mid);
                low = mid + 1;
                continue;
            }
            int mx = query_max(l, l + mid - 1);
            if (mx <= len - 2 * mid + 1) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        cout << ans << "\n";
    }

    return 0;
}
