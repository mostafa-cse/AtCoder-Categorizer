# Constraint-Adaptive Knapsack (Meet-in-the-Middle vs Weight DP vs Dual Value DP)

**Domain**: `Dynamic Programming`  
**Subtopic**: `Knapsack Multi-Constraint`  

This workbook contains curated, high-quality competitive programming problems teaching **Constraint-Adaptive Knapsack (Meet-in-the-Middle vs Weight DP vs Dual Value DP)**.

---

## Curated Problems

### `[problem:AtCoder-abc032_d]` — ナップサック問題
- **Rating / Difficulty**: 1731
- **Contest**: `abc032`
- **Analysis**: [`analysis/AtCoder-abc032_d.md`](../../analysis/AtCoder-abc032_d.md)
- **Key Idea**: The ultimate knapsack master problem. Adapt algorithm based on constraints: (1) N <= 30 -> Meet-in-the-Middle O(2^{N/2}), (2) max w_i <= 1000 -> Weight DP O(N * sum w_i), (3) max v_i <= 1000 -> Dual Value DP O(N * sum v_i).
- **Time Complexity**: `Case 1: O(2^{N/2} log 2^{N/2}), Case 2: O(N * sum W), Case 3: O(N * sum V)`
- **Space Complexity**: `Case 1: O(2^{N/2}), Case 2: O(sum W), Case 3: O(sum V)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Item {
    long long v, w;
};

void solve_small_n(int n, long long W, const vector<Item>& items) {
    int n1 = n / 2;
    int n2 = n - n1;

    vector<pair<long long, long long>> part1;
    for (int mask = 0; mask < (1 << n1); ++mask) {
        long long cur_w = 0, cur_v = 0;
        for (int i = 0; i < n1; ++i) {
            if ((mask >> i) & 1) {
                cur_w += items[i].w;
                cur_v += items[i].v;
            }
        }
        if (cur_w <= W) part1.push_back({cur_w, cur_v});
    }

    vector<pair<long long, long long>> part2;
    for (int mask = 0; mask < (1 << n2); ++mask) {
        long long cur_w = 0, cur_v = 0;
        for (int i = 0; i < n2; ++i) {
            if ((mask >> i) & 1) {
                cur_w += items[n1 + i].w;
                cur_v += items[n1 + i].v;
            }
        }
        if (cur_w <= W) part2.push_back({cur_w, cur_v});
    }

    sort(part2.begin(), part2.end());
    vector<pair<long long, long long>> p2_opt;
    long long max_v = -1;
    for (auto& p : part2) {
        if (p.second > max_v) {
            max_v = p.second;
            p2_opt.push_back(p);
        }
    }

    long long ans = 0;
    for (auto& p : part1) {
        long long rem_w = W - p.first;
        auto it = upper_bound(p2_opt.begin(), p2_opt.end(), make_pair(rem_w, (long long)4e18));
        if (it != p2_opt.begin()) {
            --it;
            ans = max(ans, p.second + it->second);
        }
    }
    cout << ans << "\n";
}

void solve_small_w(int n, long long W, const vector<Item>& items) {
    int max_w = min((long long)n * 1000, W);
    vector<long long> dp(max_w + 1, 0);

    for (int i = 0; i < n; ++i) {
        for (int w = max_w; w >= items[i].w; --w) {
            dp[w] = max(dp[w], dp[w - items[i].w] + items[i].v);
        }
    }

    long long ans = 0;
    for (int w = 0; w <= max_w; ++w) ans = max(ans, dp[w]);
    cout << ans << "\n";
}

void solve_small_v(int n, long long W, const vector<Item>& items) {
    int max_v = n * 1000;
    vector<long long> dp(max_v + 1, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int v = max_v; v >= items[i].v; --v) {
            if (dp[v - items[i].v] != INF) {
                dp[v] = min(dp[v], dp[v - items[i].v] + items[i].w);
            }
        }
    }

    long long ans = 0;
    for (int v = 0; v <= max_v; ++v) {
        if (dp[v] <= W) ans = v;
    }
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    if (!(cin >> n >> W)) return 0;

    vector<Item> items(n);
    long long max_item_w = 0, max_item_v = 0;
    for (int i = 0; i < n; ++i) {
        cin >> items[i].v >> items[i].w;
        max_item_w = max(max_item_w, items[i].w);
        max_item_v = max(max_item_v, items[i].v);
    }

    if (n <= 30) {
        solve_small_n(n, W, items);
    } else if (max_item_w <= 1000) {
        solve_small_w(n, W, items);
    } else {
        solve_small_v(n, W, items);
    }

    return 0;
}
```
