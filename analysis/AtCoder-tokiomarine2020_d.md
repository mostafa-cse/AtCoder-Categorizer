# Problem Analysis: AtCoder-tokiomarine2020_d — Knapsack Queries on a tree

**Problem ID**: `AtCoder-tokiomarine2020_d`  
**Contest**: `tokiomarine2020`  
**Rating / Difficulty**: 2158  
**URL**: https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_d  
**VJudge Tag**: `[problem:AtCoder-tokiomarine2020_d]`  
**Category File**: [`../categories/miscellaneous/complete_binary_tree_depth_meet_in_the_middle.md`](../categories/miscellaneous/complete_binary_tree_depth_meet_in_the_middle.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Meet in the Middle`  

---

## 1. Problem Statement & Key Idea
Complete binary tree of depth <= 18 with 0-1 knapsack queries on paths from v to root. Sqrt decomposition / Meet-in-the-Middle on tree depth: precalculate Pareto frontiers for the top 9 levels, and enumerate 2^k subsets for the bottom <= 9 levels.

## 2. Core Observation & Invariant
Splitting the path at depth 9 limits both the top ancestor path and the bottom path to at most 9 items. For nodes u < 512, precalculating the Pareto frontier of non-dominated (weight, value) pairs takes negligible memory (< 2 MB) and O(2^9) operations per node. For any query (v, L), bottom subsets (<= 256) are combined with top Pareto pairs via binary search in O(2^k log S).

## 3. Step-by-Step Algorithm
1. For every node u < 512, compute its Pareto frontier by merging the parent's frontier with item u and filtering dominated pairs.
2. For each query (v, L), walk upwards from v until reaching ancestor u < 512, collecting the bottom items (at most 9).
3. Generate all 2^k subsets of bottom items with total weight <= L.
4. For each bottom subset, binary search node u's Pareto frontier for the largest weight <= L - w_bot and maximize v_bot + v_top.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + Q * 2^(D/2) * log(2^(D/2)))`
- **Space Complexity**: `O(2^(D/2) * 2^(D/2) + N)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Item {
    long long w, v;
};

const int TOP_LIMIT = 512;
vector<Item> top_dp[TOP_LIMIT];
long long V[300005], W[300005];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 1; i <= n; ++i) {
        cin >> V[i] >> W[i];
    }

    top_dp[1] = {{0, 0}, {W[1], V[1]}};
    if (top_dp[1][0].w == top_dp[1][1].w) {
        top_dp[1] = {{W[1], max(top_dp[1][0].v, top_dp[1][1].v)}};
    } else {
        if (top_dp[1][1].v < top_dp[1][0].v) {
            top_dp[1].pop_back();
        }
    }

    for (int u = 2; u < min(n + 1, TOP_LIMIT); ++u) {
        int p = u / 2;
        vector<Item> combined;
        for (const auto& item : top_dp[p]) {
            combined.push_back({item.w + W[u], item.v + V[u]});
        }
        for (const auto& item : top_dp[p]) {
            combined.push_back(item);
        }
        sort(combined.begin(), combined.end(), [](const Item& a, const Item& b) {
            if (a.w != b.w) return a.w < b.w;
            return a.v > b.v;
        });

        vector<Item> filtered;
        long long max_v = -1;
        for (const auto& item : combined) {
            if (item.v > max_v) {
                if (!filtered.empty() && filtered.back().w == item.w) {
                    filtered.back().v = item.v;
                } else {
                    filtered.push_back(item);
                }
                max_v = item.v;
            }
        }
        top_dp[u] = move(filtered);
    }

    int q;
    cin >> q;
    while (q--) {
        int v;
        long long L;
        cin >> v >> L;

        vector<pair<long long, long long>> bottom_items;
        int curr = v;
        while (curr >= TOP_LIMIT) {
            bottom_items.push_back({W[curr], V[curr]});
            curr /= 2;
        }

        int m = bottom_items.size();
        vector<Item> bot_subsets;
        bot_subsets.reserve(1 << m);
        bot_subsets.push_back({0, 0});
        for (int i = 0; i < m; ++i) {
            int sz = bot_subsets.size();
            for (int j = 0; j < sz; ++j) {
                long long nw = bot_subsets[j].w + bottom_items[i].first;
                long long nv = bot_subsets[j].v + bottom_items[i].second;
                if (nw <= L) {
                    bot_subsets.push_back({nw, nv});
                }
            }
        }

        long long ans = 0;
        const auto& top_list = top_dp[curr];

        for (const auto& b : bot_subsets) {
            long long rem_w = L - b.w;
            int low = 0, high = (int)top_list.size() - 1, best_idx = -1;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (top_list[mid].w <= rem_w) {
                    best_idx = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            if (best_idx != -1) {
                ans = max(ans, b.v + top_list[best_idx].v);
            }
        }

        cout << ans << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
