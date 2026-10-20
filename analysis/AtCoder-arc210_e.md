# Problem Analysis: AtCoder-arc210_e — E - Subset Sum Gaps

**Problem ID**: `AtCoder-arc210_e`  
**Contest**: `arc210`  
**Rating / Difficulty**: 2970  
**URL**: https://atcoder.jp/contests/arc210/tasks/arc210_e  
**VJudge Tag**: `[problem:AtCoder-arc210_e]`  
**Category File**: [`../categories/miscellaneous/geometric_subset_sum_gaps_state_pruning.md`](../categories/miscellaneous/geometric_subset_sum_gaps_state_pruning.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Coordinate Compression`  

---

## 1. Problem Statement & Key Idea
Given N <= 2 * 10^5 positive integers A_i, consider all non-empty subset sums sorted in increasing order: S_1 < S_2 < ... < S_M. Count the number of indices k such that 101 S_k <= 100 S_{k+1}.

## 2. Core Observation & Invariant
A ratio gap S_{k+1} / S_k >= 1.01 indicates that no subset sum falls into (S_k, 1.01 S_k). Any two achievable sums s_1 <= s_2 with 100 s_2 < 101 s_1 cannot create a ratio gap between them because their reachable neighborhoods overlap geometrically. Thus, we prune achievable sums by merging any sums within a 1.01 factor! The number of geometrically pruned sums is bounded by O(log_{1.01}(sum A_i)) <= 3600.

## 3. Step-by-Step Algorithm
1. 1. Maintain a pruned sorted list of reachable sums, initialized with {0}.
2. 2. For each number A_i:
3.    - Form shifted list {s + A_i : s in list}.
4.    - Two-pointer merge the old list and shifted list.
5.    - Prune merged list: keep interval [s_L, s_R]; if 100 x < 101 s_L, extend s_R = x; otherwise start a new interval.
6. 3. Scan final pruned intervals and check for gaps where 101 s_R < 100 s'_L.
7. 4. Output the count of such gaps.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + K log K)`
- **Space Complexity**: `O(K)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

struct Element {
    long long val;
    long long cnt;
};

void reduce_list(const vector<Element>& merged, vector<Element>& res) {
    res.clear();
    int n = (int)merged.size();
    int i = 0;
    while (i < n) {
        int j = i;
        long long base_v = merged[i].val;
        if (base_v == 0) {
            while (j < n && merged[j].val == 0) j++;
        } else {
            // Find largest j such that 100 * merged[j].val < 101 * base_v
            // Avoid overflow using __int128_t
            while (j < n && ((__int128_t)100 * merged[j].val < (__int128_t)101 * base_v)) {
                j++;
            }
        }

        if (j - 1 >= i + 2) {
            long long add_cnt = 0;
            for (int k = i + 1; k < j - 1; ++k) {
                add_cnt = (add_cnt + merged[k].cnt) % MOD;
            }
            res.push_back({base_v, (merged[i].cnt + add_cnt) % MOD});
            i = j - 1;
        } else {
            res.push_back(merged[i]);
            i++;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<Element> cur;
    cur.push_back({0, 1});

    vector<Element> nxt;
    vector<Element> merged_raw;
    vector<Element> merged_compact;
    vector<Element> reduced;

    for (int step = 0; step < n; ++step) {
        long long ai = a[step];
        int sz = (int)cur.size();
        nxt.resize(sz);
        for (int i = 0; i < sz; ++i) {
            nxt[i] = {cur[i].val + ai, cur[i].cnt};
        }

        merged_raw.clear();
        merged_raw.reserve(2 * sz);
        int p1 = 0, p2 = 0;
        while (p1 < sz && p2 < sz) {
            if (cur[p1].val <= nxt[p2].val) {
                merged_raw.push_back(cur[p1++]);
            } else {
                merged_raw.push_back(nxt[p2++]);
            }
        }
        while (p1 < sz) merged_raw.push_back(cur[p1++]);
        while (p2 < sz) merged_raw.push_back(nxt[p2++]);

        // Compact identical values
        merged_compact.clear();
        merged_compact.reserve(merged_raw.size());
        for (const auto& elem : merged_raw) {
            if (!merged_compact.empty() && merged_compact.back().val == elem.val) {
                merged_compact.back().cnt = (merged_compact.back().cnt + elem.cnt) % MOD;
            } else {
                merged_compact.push_back(elem);
            }
        }

        // Reduce
        reduce_list(merged_compact, reduced);
        while (reduced.size() < merged_compact.size()) {
            merged_compact = move(reduced);
            reduce_list(merged_compact, reduced);
        }
        cur = move(reduced);
    }

    // Collect valid gaps
    struct Gap {
        long long v1, v2;
        long long cum;
    };
    vector<Gap> gaps;
    long long cum = 0;
    int m = (int)cur.size();
    for (int i = 0; i < m - 1; ++i) {
        cum = (cum + cur[i].cnt) % MOD;
        long long v1 = cur[i].val;
        long long v2 = cur[i + 1].val;
        if ((__int128_t)101 * v1 <= (__int128_t)100 * v2) {
            gaps.push_back({v1, v2, cum});
        }
    }

    cout << gaps.size() << "\n";
    for (const auto& g : gaps) {
        cout << g.v1 << " " << g.v2 << " " << g.cum << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
