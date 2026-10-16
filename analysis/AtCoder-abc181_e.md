# Problem Analysis: AtCoder-abc181_e — Transformable Teacher

**Problem ID**: `AtCoder-abc181_e`  
**Contest**: `abc181`  
**Rating / Difficulty**: 1193  
**URL**: https://atcoder.jp/contests/abc181/tasks/abc181_e  
**VJudge Tag**: `[problem:AtCoder-abc181_e]`  
**Category File**: [`../categories/data_structures/prefix_suffix_parity_split.md`](../categories/data_structures/prefix_suffix_parity_split.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Prefix & Suffix Arrays`  
- **Topic (Skill)**: `Prefix-Suffix Parity Split with Binary Search Insertion`  

---

## 1. Problem Statement & Key Idea
N students with heights H_1..H_N (N is odd). M transformation forms for teacher with heights W_1..W_M. Pair up all students and 1 teacher into (N+1)/2 pairs. Minimize the sum of absolute differences across pairs.

**Key Idea**: Sort student heights H_1 < H_2 < ... < H_N. When teacher with height W is inserted, they will be paired with the student H_i closest to W.

## 2. Core Observation & Invariant
If teacher pairs with student at even index i (0-indexed): elements before i pair as (H_0, H_1), (H_2, H_3)...; elements after i pair as (H_{i+1}, H_{i+2}), (H_{i+3}, H_{i+4})... Precompute prefix pair differences pref[i] and suffix pair differences suff[i]. For any teacher height W, find insertion point i via std::lower_bound in O(log N) and query pref + |H_i - W| + suff in O(1).

## 3. Step-by-Step Algorithm
1. Sort H array.
2. Compute pref array: pref[i] = pref[i-2] + (H[i-1] - H[i-2]).
3. Compute suff array: suff[i] = suff[i+2] + (H[i+2] - H[i+1]).
4. For each teacher form W: find insertion index pos = lower_bound(H) - H.begin(); if pos is odd, pair with pos - 1, else pair with pos; total = pref + |H_pair - W| + suff; minimize over all W.
5. Output minimum total difference.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + M log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> h(n);
    for (int i = 0; i < n; ++i) {
        cin >> h[i];
    }
    sort(h.begin(), h.end());

    vector<long long> pref(n, 0);
    for (int i = 2; i < n; i += 2) {
        pref[i] = pref[i - 2] + (h[i - 1] - h[i - 2]);
    }

    vector<long long> suff(n, 0);
    for (int i = n - 3; i >= 0; i -= 2) {
        suff[i] = suff[i + 2] + (h[i + 2] - h[i + 1]);
    }

    long long min_diff = 4e18;

    for (int j = 0; j < m; ++j) {
        long long w;
        cin >> w;

        int pos = lower_bound(h.begin(), h.end(), w) - h.begin();
        if (pos % 2 == 1) pos--; // pair with even index

        long long cur = pref[pos] + abs(h[pos] - w) + suff[pos];
        min_diff = min(min_diff, cur);
    }

    cout << min_diff << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Prefix and suffix pair difference splitting for single-element insertion queries.
- **Reusable Pattern**: `Odd element insertion: pref_pairs + |H[i] - W| + suff_pairs.`
