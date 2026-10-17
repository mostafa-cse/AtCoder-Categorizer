# Problem Analysis: AtCoder-arc070_b — No Need

**Problem ID**: `AtCoder-arc070_b`  
**Contest**: `abc056`  
**Rating / Difficulty**: 2015  
**URL**: https://atcoder.jp/contests/abc056/tasks/arc070_b  
**VJudge Tag**: `[problem:AtCoder-arc070_b]`  
**Category File**: [`../categories/dynamic_programming/monotone_essential_elements_knapsack_binary_search.md`](../categories/dynamic_programming/monotone_essential_elements_knapsack_binary_search.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Monotone Essential Elements via 0-1 Knapsack DP and Binary Search`  

---

## 1. Problem Statement & Key Idea
Given N positive integers a_1, ..., a_N and K. A subset is good if its sum >= K. An element a_i is 'needed' if there is some good subset that becomes not good when a_i is removed. Count how many elements are NOT needed.

**Key Idea**: An element a_i is needed iff there exists a subset of the OTHER elements with sum in [K - a_i, K - 1]. Monotonicity property: if a is sorted in ascending order, if a_i is not needed, then every a_j <= a_i is also not needed! Thus the set of not needed elements forms a prefix a_1, ..., a_m. We binary search on m. To test if a_m is needed, we run 0-1 knapsack on the other elements up to capacity K - 1 and check if any sum in [K - a_m, K - 1] is reachable in O(N K).

## 2. Core Observation & Invariant
Essentiality in bounded knapsacks is monotonic with respect to element size, reducing all-element queries to binary search.

## 3. Step-by-Step Algorithm
1. Sort a in ascending order.
2. Binary search on the boundary index m in [0, N]:
3.   Elements >= K are automatically needed.
4.   To check if a_m is needed:
5.     Run boolean 0-1 knapsack DP of capacity K using all elements except a_m.
6.     Check if any dp[s] is true for s in [max(0, K - a_m), K - 1].
7.     If yes, a_m is needed; if no, a_m is not needed.
8. The number of not needed elements is the largest m where a_m is not needed.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * K * log N)`
- **Space Complexity**: `O(K)`

## 5. Core Algorithmic Skill & Learning Takeaway
Knapsack essentiality monotonicity and binary search verification.

**Reusable Pattern**: Monotone Knapsack Essentiality: Sorted elements have a single cutoff point separating unnecessary elements from necessary ones.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    auto is_needed = [&](int idx) {
        if (a[idx] >= k) return true;

        vector<bool> dp(k, false);
        dp[0] = true;

        for (int i = 0; i < n; ++i) {
            if (i == idx) continue;
            long long val = a[i];
            if (val >= k) continue;

            for (long long s = k - 1; s >= val; --s) {
                if (dp[s - val]) dp[s] = true;
            }
        }

        long long low_bound = max(0LL, k - a[idx]);
        for (long long s = low_bound; s < k; ++s) {
            if (dp[s]) return true;
        }
        return false;
    };

    int low = 0, high = n - 1, ans = 0;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (!is_needed(mid)) {
            ans = mid + 1;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
