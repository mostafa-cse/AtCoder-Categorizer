# Divide and Conquer on Queries

**Domain**: `Miscellaneous`  
**Subtopic**: `Techniques`  

This workbook contains curated, high-quality competitive programming problems teaching **Divide and Conquer on Queries**.

---

## Curated Problems

### `[problem:AtCoder-abc426_g]` — Range Knapsack Query
- **Rating / Difficulty**: 2119
- **Contest**: `abc426`
- **Analysis**: [`analysis/AtCoder-abc426_g.md`](../../analysis/AtCoder-abc426_g.md)
- **Key Idea**: Offline Divide and Conquer over the item range [1, N]. For queries lying completely in [L, mid] or [mid+1, R], recurse on the respective halves. For queries spanning across mid (L <= mid < R), compute a suffix knapsack table from mid down to L and a prefix knapsack table from mid+1 up to R. Each spanning query with capacity C can be answered by taking max_{c} (suffix_dp[c] + prefix_dp[C - c]) in O(C) time.
- **Time Complexity**: `O(N C log N + Q C)`
- **Space Complexity**: `O(N C + Q)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Item {
    int w, v;
};

struct Query {
    int id;
    int l, r, c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Item> items(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> items[i].w >> items[i].v;
    }

    int q;
    if (!(cin >> q)) return 0;

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        queries[i].id = i;
        cin >> queries[i].l >> queries[i].r >> queries[i].c;
    }

    vector<long long> ans(q, 0);

    auto solve_dc = [&](auto& self, int l, int r, vector<Query>& q_list) -> void {
        if (q_list.empty()) return;
        if (l == r) {
            for (auto& qry : q_list) {
                if (items[l].w <= qry.c) ans[qry.id] = items[l].v;
                else ans[qry.id] = 0;
            }
            return;
        }

        int mid = (l + r) / 2;
        vector<Query> left_q, right_q, span_q;
        for (auto& qry : q_list) {
            if (qry.r <= mid) left_q.push_back(qry);
            else if (qry.l > mid) right_q.push_back(qry);
            else span_q.push_back(qry);
        }

        self(self, l, mid, left_q);
        self(self, mid + 1, r, right_q);

        if (span_q.empty()) return;

        int max_c = 0;
        for (auto& qry : span_q) max_c = max(max_c, qry.c);

        vector<vector<long long>> suff_dp(mid - l + 2, vector<long long>(max_c + 1, 0));
        for (int i = mid; i >= l; --i) {
            int idx = mid - i + 1;
            suff_dp[idx] = suff_dp[idx - 1];
            int w = items[i].w;
            int v = items[i].v;
            for (int cap = max_c; cap >= w; --cap) {
                suff_dp[idx][cap] = max(suff_dp[idx][cap], suff_dp[idx - 1][cap - w] + v);
            }
        }

        vector<vector<long long>> pref_dp(r - mid + 1, vector<long long>(max_c + 1, 0));
        for (int i = mid + 1; i <= r; ++i) {
            int idx = i - mid;
            pref_dp[idx] = pref_dp[idx - 1];
            int w = items[i].w;
            int v = items[i].v;
            for (int cap = max_c; cap >= w; --cap) {
                pref_dp[idx][cap] = max(pref_dp[idx][cap], pref_dp[idx - 1][cap - w] + v);
            }
        }

        for (auto& qry : span_q) {
            int left_idx = mid - qry.l + 1;
            int right_idx = qry.r - mid;
            long long best = 0;
            for (int cap = 0; cap <= qry.c; ++cap) {
                best = max(best, suff_dp[left_idx][cap] + pref_dp[right_idx][qry.c - cap]);
            }
            ans[qry.id] = best;
        }
    };

    solve_dc(solve_dc, 1, n, queries);

    for (int i = 0; i < q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```
