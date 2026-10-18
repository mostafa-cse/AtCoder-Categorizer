# Problem Analysis: AtCoder-abc147_f — F. Sum Difference

**Problem ID**: `AtCoder-abc147_f`  
**Contest**: `abc147`  
**Rating / Difficulty**: 2393  
**URL**: https://atcoder.jp/contests/abc147/tasks/abc147_f  
**VJudge Tag**: `[problem:AtCoder-abc147_f]`  
**Category File**: [`../categories/miscellaneous/ap_subset_sums_coset_interval_union.md`](../categories/miscellaneous/ap_subset_sums_coset_interval_union.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Interval Set`  

---

## 1. Problem Statement & Key Idea
Subset sums of an arithmetic progression partition into independent cosets modulo D. For a fixed subset size k, achievable sums form a contiguous interval of multiples. Merging overlapping intervals per coset counts distinct sums in O(N log N) time.

## 2. Core Observation & Invariant
Choosing k elements from arithmetic progression A_i = X + (i-1)D yields sums S = k X + D * r, where r spans continuously across all integers in [k(k-1)/2, k(2N-k-1)/2]. Modulo D, values of S belong to independent cosets (k X) mod D. Within each coset, the set of achievable multiples q + r forms a union of integer intervals.

## 3. Step-by-Step Algorithm
1. Handle D = 0 separately (1 value if X == 0, else N + 1 values).
2. If D < 0, negate D and reflect X to X + (N - 1)D.
3. For each k in [0, N], compute rem = (k * X) % D and q = (k * X) // D.
4. Insert interval [q + k(k-1)/2, q + k(2N-k-1)/2] into the bucket for rem.
5. Sort and merge intervals within each remainder bucket, summing disjoint lengths in O(N log N) total time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll N, X, D;
    if (!(cin >> N >> X >> D)) return 0;

    if (D == 0) {
        if (X == 0) cout << 1 << "\n";
        else cout << N + 1 << "\n";
        return 0;
    }

    if (D < 0) {
        X = X + (N - 1) * D;
        D = -D;
    }

    map<ll, vector<pair<ll, ll>>> groups;
    for (ll k = 0; k <= N; k++) {
        ll rem = (k * X) % D;
        if (rem < 0) rem += D;
        ll q = (k * X - rem) / D;
        ll r_min = k * (k - 1) / 2;
        ll r_max = k * (2 * N - k - 1) / 2;
        groups[rem].push_back({q + r_min, q + r_max});
    }

    ll ans = 0;
    for (auto& [rem, intervals] : groups) {
        sort(intervals.begin(), intervals.end());
        ll cur_l = intervals[0].first;
        ll cur_r = intervals[0].second;
        for (size_t i = 1; i < intervals.size(); i++) {
            if (intervals[i].first <= cur_r) {
                cur_r = max(cur_r, intervals[i].second);
            } else {
                ans += (cur_r - cur_l + 1);
                cur_l = intervals[i].first;
                cur_r = intervals[i].second;
            }
        }
        ans += (cur_r - cur_l + 1);
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
