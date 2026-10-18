# Problem Analysis: AtCoder-abc442_g — G. Lightweight Knapsack

**Problem ID**: `AtCoder-abc442_g`  
**Contest**: `abc442`  
**Rating / Difficulty**: 2347  
**URL**: https://atcoder.jp/contests/abc442/tasks/abc442_g  
**VJudge Tag**: `[problem:AtCoder-abc442_g]`  
**Category File**: [`../categories/dynamic_programming/lightweight_knapsack_lcm_grouping.md`](../categories/dynamic_programming/lightweight_knapsack_lcm_grouping.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Subset Sum Optimizations`  

---

## 1. Problem Statement & Key Idea
Bounded knapsack with small weights $W_i \in \{1, 2, 3\}$ and capacity $C \le 2 \times 10^9$. Since $\text{lcm}(1, 2, 3) = 6$, all items are grouped into weight-6 super-items, leaving only 36 remainder combinations solved greedily in $O(N \log N)$.

## 2. Core Observation & Invariant
Items of each weight $w \in \{1, 2, 3\}$ are always selected in descending order of value. Because $\text{lcm}(1, 2, 3) = 6$, all remaining items of weight $w$ can be grouped into super-items of weight 6, leaving remainders $R_w = F_w \bmod (6/w)$ which take only $6 \times 3 \times 2 = 36$ total states.

## 3. Step-by-Step Algorithm
1. Sort items of each weight $w \in \{1, 2, 3\}$ descending by value.
2. Iterate over all 36 combinations of remainders $(R_1, R_2, R_3) \in [0, 5] \times [0, 2] \times [0, 1]$.
3. Take the top $R_w$ items of each weight directly; merge all remaining items into groups of size $6/w$ (each having weight 6).
4. Pool all weight-6 super-items, sort descending by value, and greedily pick the best $\lfloor (C - \sum w R_w) / 6 \rfloor$ items in $O(N \log N)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

using ll = long long;

pair<ll, vector<pair<ll, ll>>> merge_items(vector<pair<ll, ll>> ls, int ofs, int g) {
    ll top = 0;
    while (ofs && !ls.empty()) {
        auto& back = ls.back();
        ll v = back.first;
        ll k = back.second;
        if (k > ofs) {
            top += v * ofs;
            back.second -= ofs;
            break;
        }
        top += v * k;
        ofs -= k;
        ls.pop_back();
    }

    vector<pair<ll, ll>> res;
    ll cnt = 0, sum = 0;
    while (!ls.empty()) {
        auto [v, k] = ls.back();
        ls.pop_back();
        if (cnt) {
            if (cnt + k < g) {
                cnt += k;
                sum += v * k;
                continue;
            }
            k -= (g - cnt);
            sum += v * (g - cnt);
            res.emplace_back(sum, 1);
            cnt = sum = 0;
        }
        if (k >= g) {
            res.emplace_back(v * g, k / g);
        }
        cnt = k % g;
        sum = v * cnt;
    }
    return {top, res};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    ll c;
    if (!(cin >> n >> c)) return 0;

    vector<vector<pair<ll, ll>>> ls(4);
    for (int i = 0; i < n; i++) {
        ll w, v, k;
        cin >> w >> v >> k;
        ls[w].emplace_back(v, k);
    }

    for (int w = 1; w <= 3; w++) {
        sort(ls[w].begin(), ls[w].end());
    }

    ll ans = 0;

    for (int r1 = 0; r1 < 6; r1++) {
        for (int r2 = 0; r2 < 3; r2++) {
            for (int r3 = 0; r3 < 2; r3++) {
                ll rem_w = 1LL * r1 + 2LL * r2 + 3LL * r3;
                if (rem_w > c) continue;

                auto [v1, m1] = merge_items(ls[1], r1, 6);
                auto [v2, m2] = merge_items(ls[2], r2, 3);
                auto [v3, m3] = merge_items(ls[3], r3, 2);

                vector<pair<ll, ll>> all_m;
                all_m.insert(all_m.end(), m1.begin(), m1.end());
                all_m.insert(all_m.end(), m2.begin(), m2.end());
                all_m.insert(all_m.end(), m3.begin(), m3.end());

                sort(all_m.begin(), all_m.end(), greater<pair<ll, ll>>());

                ll cur_val = v1 + v2 + v3;
                ll can_take = (c - rem_w) / 6;

                for (auto [v, k] : all_m) {
                    ll take = min(can_take, k);
                    cur_val += v * take;
                    can_take -= take;
                    if (can_take == 0) break;
                }

                ans = max(ans, cur_val);
            }
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
