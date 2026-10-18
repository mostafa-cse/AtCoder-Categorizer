# Problem Analysis: AtCoder-abc290_g — G. Edge Elimination

**Problem ID**: `AtCoder-abc290_g`  
**Contest**: `abc290`  
**Rating / Difficulty**: 2407  
**URL**: https://atcoder.jp/contests/abc290/tasks/abc290_g  
**VJudge Tag**: `[problem:AtCoder-abc290_g]`  
**Category File**: [`../categories/dynamic_programming/perfect_kary_tree_subtree_cut_coin_greedy.md`](../categories/dynamic_programming/perfect_kary_tree_subtree_cut_coin_greedy.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Cut edges in a perfect K-ary tree of depth D to obtain a connected component of exactly X vertices with the minimum number of cuts. Fixing the component's root at height h reduces the problem to an exact-change coin change problem with canonical tree sizes V_i.

## 2. Core Observation & Invariant
A perfect K-ary tree of height h has V_h = (K^{h+1}-1)/(K-1) vertices. To reduce it to X vertices, we must remove exactly V_h - X vertices using complete subtrees of heights 0, 1, ..., h-1. Because the subtree sizes satisfy the canonical coin system criteria, the greedy choice of the largest possible subtree is strictly optimal.

## 3. Step-by-Step Algorithm
1. 1. Precompute sizes V_i = V_{i-1} * K + 1 for i = 0 to D.
2. 2. For each candidate top-vertex height h from D down to 0 with V_h >= X:
3.    a. Calculate remaining vertices to cut: rem = V_h - X.
4.    b. Cost includes 1 cut to detach from parent (if h < D) plus greedy cuts of sizes V_{h-1}, ..., V_0.
5. 3. Return the minimum cost over all valid heights h.

## 4. Complexity Analysis
- **Time Complexity**: `O(T * D^2)`
- **Space Complexity**: `O(D)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll INF = 8e18;

ll greedy(ll rem, int p, const vector<ll>& a) {
    if (rem == 0) return 0;
    if (rem < 0) return INF;
    ll res = 0;
    for (int i = p; i >= 0; i--) {
        ll use = rem / a[i];
        res += use;
        rem -= use * a[i];
    }
    if (rem > 0) return INF;
    return res;
}

void solve() {
    ll d, k, x;
    if (!(cin >> d >> k >> x)) return;

    vector<ll> a = {1};
    for (int i = 1; i <= d; i++) {
        if (a.back() > 2e18 / k) {
            a.push_back(2e18);
        } else {
            a.push_back(a.back() * k + 1);
        }
    }

    ll ans = INF;
    for (int h = d; h >= 0; h--) {
        if (a[h] >= x) {
            ll rem = a[h] - x;
            ll up = (h == d ? 0 : 1);
            ans = min(ans, up + greedy(rem, h - 1, a));
        }
    }

    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
