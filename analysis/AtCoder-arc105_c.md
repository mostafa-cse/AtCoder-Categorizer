# Problem Analysis: AtCoder-arc105_c — Camels and Bridge

**Problem ID**: `AtCoder-arc105_c`  
**Contest**: `arc105`  
**Rating / Difficulty**: 1964  
**URL**: https://atcoder.jp/contests/arc105/tasks/arc105_c  
**VJudge Tag**: `[problem:AtCoder-arc105_c]`  
**Category File**: [`../categories/basics/extremal_permutation_dag_distance_dp.md`](../categories/basics/extremal_permutation_dag_distance_dp.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Permutations / DAG DP`  
- **Topic (Skill)**: `Extremal Permutation Evaluation with Segment Weight Constraints and DAG Distance DP`  

---

## 1. Problem Statement & Key Idea
N camels (N <= 8) with weights w_1..w_N must cross an M-part bridge (M <= 10^5). Part j has length l_j and weight limit v_j. Find the minimum distance between the front and rear camels so that no bridge section is overloaded.

Since N <= 8, enumerate all N! = 40320 permutations. Precompute req_dist[W]: the maximum length of any bridge section with weight capacity < W, using two-pointer/binary search on pre-sorted bridge sections. For a fixed camel order, any subsegment of camels i..j has total weight W(i..j); if W(i..j) > min(v), the distance between camel i and camel j must be >= req_dist[W(i..j)]. Compute camel positions via DAG DP: pos[j] = max_{i < j} (pos[i] + req_dist[W(i..j)]). Output the minimum pos[N] over all permutations.

## 2. Core Observation & Invariant
Small N <= 8 permits full permutation search; bridge weight constraints simplify to maximum length under weight thresholds.

## 3. Step-by-Step Algorithm
1. Check if max(w_i) > min(v_j); if so, print -1.
2. Sort bridge parts by capacity v_j ascending and build prefix maximums of length l_j.
3. Enumerate all N! permutations of camels.
4. For each permutation, evaluate pairwise distance requirements req[i][j] via binary search on weight sum.
5. Compute positions: pos[0] = 0; pos[j] = max_{i < j} (pos[i] + req[i][j]).
6. ans = min(ans, pos[N - 1]).
7. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(M log M + N! * N^2)`
- **Space Complexity**: `O(M + N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Bridge {
    long long l, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> w(n);
    long long max_w = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i];
        max_w = max(max_w, w[i]);
    }

    vector<Bridge> b(m);
    long long min_v = INF;
    for (int i = 0; i < m; ++i) {
        cin >> b[i].l >> b[i].v;
        min_v = min(min_v, b[i].v);
    }

    if (max_w > min_v) {
        cout << -1 << "\n";
        return 0;
    }

    sort(b.begin(), b.end(), [](const Bridge& x, const Bridge& y) {
        return x.v < y.v;
    });

    vector<long long> pref_max_l(m);
    pref_max_l[0] = b[0].l;
    for (int i = 1; i < m; ++i) {
        pref_max_l[i] = max(pref_max_l[i - 1], b[i].l);
    }

    auto get_min_dist = [&](long long weight) -> long long {
        // Find largest bridge with v < weight
        int low = 0, high = m - 1, best = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (b[mid].v < weight) {
                best = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        if (best == -1) return 0;
        return pref_max_l[best];
    };

    vector<int> p(n);
    iota(p.begin(), p.end(), 0);

    long long min_total_dist = INF;

    do {
        vector<long long> pos(n, 0);
        for (int j = 0; j < n; ++j) {
            long long cur_w = w[p[j]];
            for (int i = j - 1; i >= 0; --i) {
                cur_w += w[p[i]];
                long long req = get_min_dist(cur_w);
                pos[j] = max(pos[j], pos[i] + req);
            }
        }
        min_total_dist = min(min_total_dist, pos[n - 1]);
    } while (next_permutation(p.begin(), p.end()));

    cout << min_total_dist << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Permutation enumeration with weight-capacity binary search and DAG distance dynamic programming.
- **Reusable Pattern**: `Permutation Spacing DP: pos[j] = max_{i < j} (pos[i] + min_dist(i, j)), minimized over all N! permutations.`
