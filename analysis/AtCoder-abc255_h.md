# Problem Analysis: AtCoder-abc255_h — Ex. Range Harvest Query

**Problem ID**: `AtCoder-abc255_h`  
**Contest**: `abc255`  
**Rating / Difficulty**: 2430  
**URL**: https://atcoder.jp/contests/abc255/tasks/abc255_h  
**VJudge Tag**: `[problem:AtCoder-abc255_h]`  
**Category File**: [`../categories/miscellaneous/range_harvest_tree_fruit_interval_set_odt.md`](../categories/miscellaneous/range_harvest_tree_fruit_interval_set_odt.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Interval Set`  

---

## 1. Problem Statement & Key Idea
Maintain trees' last harvest dates using an interval set (ODT) in std::set, computing harvested fruits via arithmetic progression formulas and consolidating queried ranges into single intervals in amortized O(Q log Q) time.

## 2. Core Observation & Invariant
Because every harvest query overwrites the range [L, R] with the current day D, intervals of identical harvest dates are consolidated. Each query creates at most 2 new interval fragments, ensuring an amortized O(1) deletions per query.

## 3. Step-by-Step Algorithm
1. 1. Initialize the interval set with a single range [1, N] harvested on day 0.
2. 2. For each query (D, L, R), split intervals at boundary points L and R + 1.
3. 3. For each sub-interval [l, r] with previous harvest day d within [L, R], accumulate (D - d) * sum_{i=l}^r i modulo 998244353.
4. 4. Erase the covered intervals and insert the consolidated interval [L, R] with day D.
5. 5. Output the collected fruits for each query.

## 4. Complexity Analysis
- **Time Complexity**: `O(Q log Q)`
- **Space Complexity**: `O(Q)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MOD = 998244353;
const ll INV2 = (MOD + 1) / 2;

struct Node {
    ll l, r, d;
    bool operator<(const Node& o) const {
        return l < o.l;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll N;
    int Q;
    if (!(cin >> N >> Q)) return 0;

    set<Node> odt;
    odt.insert({1, N, 0});

    auto split = [&](ll x) -> set<Node>::iterator {
        if (x > N) return odt.end();
        auto it = --odt.upper_bound({x, 0, 0});
        if (it->l == x) return it;
        ll l = it->l, r = it->r, d = it->d;
        odt.erase(it);
        odt.insert({l, x - 1, d});
        return odt.insert({x, r, d}).first;
    };

    while (Q--) {
        ll D, L, R;
        cin >> D >> L >> R;

        auto itr = split(R + 1);
        auto itl = split(L);

        ll total = 0;
        for (auto it = itl; it != itr; ++it) {
            ll l = it->l, r = it->r, d = it->d;
            ll cnt = (r - l + 1) % MOD;
            ll sum_idx = (l + r) % MOD * cnt % MOD * INV2 % MOD;
            ll fruits = (D - d) % MOD * sum_idx % MOD;
            total = (total + fruits) % MOD;
        }

        odt.erase(itl, itr);
        odt.insert({L, R, D});

        cout << (total % MOD + MOD) % MOD << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
