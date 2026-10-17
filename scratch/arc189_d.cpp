#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

struct SegTree {
    int n;
    vector<long long> tree;
    SegTree(int n) : n(n), tree(4 * n, 0) {}

    void build(const vector<long long>& a, int node, int l, int r) {
        if (l == r) {
            tree[node] = a[l];
            return;
        }
        int mid = l + (r - l) / 2;
        build(a, 2 * node, l, mid);
        build(a, 2 * node + 1, mid + 1, r);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    long long query(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) return tree[node];
        if (r < ql || l > qr) return 0;
        int mid = l + (r - l) / 2;
        return max(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    vector<long long> pref(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        pref[i] = pref[i - 1] + a[i];
    }

    SegTree st(n);
    st.build(a, 1, 1, n);

    auto query_sum = [&](int l, int r) {
        return pref[r] - pref[l - 1];
    };

    vector<long long> ans(n + 1);

    for (int i = 1; i <= n; ++i) {
        int l = i, r = i;
        long long s = a[i];

        while (true) {
            bool changed = false;

            // Try to expand left
            if (l > 1 && a[l - 1] < s) {
                // Binary search leftmost index L' in [1, l - 1] such that max(L' .. l - 1) < s
                int low = 1, high = l - 1, best_l = l - 1;
                while (low <= high) {
                    int mid = low + (high - low) / 2;
                    if (st.query(1, 1, n, mid, l - 1) < s) {
                        best_l = mid;
                        high = mid - 1;
                    } else {
                        low = mid + 1;
                    }
                }
                l = best_l;
                s = query_sum(l, r);
                changed = true;
            }

            // Try to expand right
            if (r < n && a[r + 1] < s) {
                // Binary search rightmost index R' in [r + 1, n] such that max(r + 1 .. R') < s
                int low = r + 1, high = n, best_r = r + 1;
                while (low <= high) {
                    int mid = low + (high - low) / 2;
                    if (st.query(1, 1, n, r + 1, mid) < s) {
                        best_r = mid;
                        low = mid + 1;
                    } else {
                        high = mid - 1;
                    }
                }
                r = best_r;
                s = query_sum(l, r);
                changed = true;
            }

            if (!changed) break;
        }

        ans[i] = s;
    }

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
