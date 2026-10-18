# Problem Analysis: AtCoder-arc150_d — D. Removing Gacha

**Problem ID**: `AtCoder-arc150_d`  
**Contest**: `arc150`  
**Rating / Difficulty**: 2407  
**URL**: https://atcoder.jp/contests/arc150/tasks/arc150_d  
**VJudge Tag**: `[problem:AtCoder-arc150_d]`  
**Category File**: [`../categories/combinatorics/coupon_collector_tree_depth_harmonic_linearity_expectation.md`](../categories/combinatorics/coupon_collector_tree_depth_harmonic_linearity_expectation.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Contribution Technique`  

---

## 1. Problem Statement & Key Idea
Compute the expected number of operations to turn all vertices good by repeatedly selecting bad vertices uniformly at random. By Linearity of Expectation, sum the expected selection count of each individual vertex, which reduces to the classic Coupon Collector's Problem.

## 2. Core Observation & Invariant
For any vertex v at depth d_v (root has depth 1), operations choosing vertices outside the 1-to-v path do not affect v's state. On the path of length d_v, all nodes are chosen uniformly until all d_v nodes are collected. By symmetry, the expected number of times vertex v is selected is exactly the d_v-th harmonic number H_{d_v} = sum_{i=1}^{d_v} 1/i.

## 3. Step-by-Step Algorithm
1. 1. Compute depth d_v for every vertex v from parent pointers.
2. 2. Precompute modular inverses and harmonic numbers H_k = sum_{i=1}^k 1/i mod 998244353.
3. 3. Total expected operations is sum_{v=1}^N H_{d_v} mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> depth(n + 1, 0);
    depth[1] = 1;
    for (int i = 2; i <= n; i++) {
        int p;
        cin >> p;
        depth[i] = depth[p] + 1;
    }

    vector<ll> inv(n + 1, 1), H(n + 1, 0);
    for (int i = 2; i <= n; i++) {
        inv[i] = (MOD - MOD / i) * inv[MOD % i] % MOD;
    }
    for (int i = 1; i <= n; i++) {
        H[i] = (H[i - 1] + inv[i]) % MOD;
    }

    ll ans = 0;
    for (int i = 1; i <= n; i++) {
        ans = (ans + H[depth[i]]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
