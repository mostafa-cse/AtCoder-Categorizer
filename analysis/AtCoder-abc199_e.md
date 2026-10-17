# Problem Analysis: AtCoder-abc199_e — Permutation

**Problem ID**: `AtCoder-abc199_e`  
**Contest**: `abc199`  
**Rating / Difficulty**: 1814  
**URL**: https://atcoder.jp/contests/abc199/tasks/abc199_e  
**VJudge Tag**: `[problem:AtCoder-abc199_e]`  
**Category File**: [`../categories/dp/subset_bitmask_dp_prefix_constraints.md`](../categories/dp/subset_bitmask_dp_prefix_constraints.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Bitmask DP`  
- **Topic (Skill)**: `Subset Bitmask DP with Prefix Count Constraints`  

---

## 1. Problem Statement & Key Idea
Count permutations of 1..N (N <= 18) satisfying M constraints: among the first X_i elements, at most Z_i elements are <= Y_i.

**Key Insight**: Standard bitmask DP over subsets: dp[mask] is the number of valid prefixes using the elements in mask. The length of the prefix is popcount(mask). Validate all constraints with X_i == popcount(mask) before transitioning.

## 2. Core Observation & Invariant
For each mask, count how many elements v in mask have v <= Y_i. If this count exceeds Z_i, mask is invalid and dp[mask] = 0.

## 3. Step-by-Step Algorithm
1. Store constraints by prefix length X.
2. Initialize dp[1 << N] = 0, dp[0] = 1.
3. For mask = 0 to (1 << N) - 1:
4.   if dp[mask] == 0: continue.
5.   k = __builtin_popcount(mask).
6.   // Validate constraints for prefix length k
7.   bool ok = true;
8.   for (auto& c : constraints[k]):
9.     count_le = count bits in mask <= Y_i.
10.     if count_le > Z_i: ok = false; break;
11.   if (!ok) { dp[mask] = 0; continue; }
12.   // Transition
13.   for v = 0 to N - 1:
14.     if (!((mask >> v) & 1)):
15.       dp[mask | (1 << v)] += dp[mask];
16. Print dp[(1 << N) - 1].

## 4. Complexity Analysis
- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(2^N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Constraint {
    int y, z;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Constraint>> cons(n + 1);
    for (int i = 0; i < m; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        cons[x].push_back({y, z});
    }

    int total_masks = 1 << n;
    vector<long long> dp(total_masks, 0);
    dp[0] = 1;

    for (int mask = 0; mask < total_masks; ++mask) {
        if (dp[mask] == 0) continue;

        int k = __builtin_popcount(mask);

        bool valid = true;
        for (auto& c : cons[k]) {
            int count_le = 0;
            for (int i = 0; i < c.y; ++i) {
                if ((mask >> i) & 1) count_le++;
            }
            if (count_le > c.z) {
                valid = false;
                break;
            }
        }

        if (!valid) {
            dp[mask] = 0;
            continue;
        }

        for (int i = 0; i < n; ++i) {
            if (!((mask >> i) & 1)) {
                dp[mask | (1 << i)] += dp[mask];
            }
        }
    }

    cout << dp[total_masks - 1] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Enforcing prefix condition filters in subset-order bitmask DP.
- **Reusable Pattern**: `Bitmask Prefix Validation: Check constraints[popcount(mask)] before pushing to transitions.`
