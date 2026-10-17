# Problem Analysis: AtCoder-abc163_e — Active Infants

**Problem ID**: `AtCoder-abc163_e`  
**Contest**: `abc163`  
**Rating / Difficulty**: 2037  
**URL**: https://atcoder.jp/contests/abc163/tasks/abc163_e  
**VJudge Tag**: `[problem:AtCoder-abc163_e]`  
**Category File**: [`../categories/dynamic_programming/greedy_descending_deque_interval_dp.md`](../categories/dynamic_programming/greedy_descending_deque_interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Greedy Descending Sort with Deque Extreme-Slot Interval DP`  

---

## 1. Problem Statement & Key Idea
N infants have activity levels A_i and start at positions 1 ... N. Rearrange them into a permutation of 1 ... N to maximize total happiness sum A_i * |i - p_i|.

**Key Idea**: Infants with larger A_i gain the most happiness from being placed as far away as possible, meaning at the extremal ends of the remaining available positions (1, N, 2, N-1, ...). Sort infants in descending order of A_i. When placing the k-th infant (1-indexed), the remaining extremal slots are l + 1 on the left and N - r on the right, where l + r = k - 1. DP state: dp[l][r] = max happiness when l infants have been placed on the leftmost positions and r infants on the rightmost positions.

## 2. Core Observation & Invariant
Sorting by weight ensures that the remaining available slot choice is restricted to the two endpoints of an expanding prefix/suffix deque.

## 3. Step-by-Step Algorithm
1. Sort infants as pairs (A_i, orig_pos) in descending order of A_i.
2. Initialize dp[N + 1][N + 1] with 0.
3. For k from 0 to N - 1 (current infant idx = k):
4.   For l from 0 to k:
5.     r = k - l.
6.     Infant pos = sorted_infants[k].orig_pos, val = sorted_infants[k].val.
7.     // Option 1: place at leftmost slot (l + 1)
8.     dp[l + 1][r] = max(dp[l + 1][r], dp[l][r] + val * abs(pos - (l + 1)));
9.     // Option 2: place at rightmost slot (N - r)
10.     dp[l][r + 1] = max(dp[l][r + 1], dp[l][r] + val * abs(pos - (N - r)));
11. Find max over all dp[l][r] with l + r == N.
12. Print max value.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. Core Algorithmic Skill & Learning Takeaway
Greedy descending sort with deque boundary placement interval DP.

**Reusable Pattern**: Extremal Deque DP: Sort descending by multiplier; assign elements greedily to available ends via dp[left][right].

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct Infant {
    long long a;
    int pos;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Infant> infants(n);
    for (int i = 0; i < n; ++i) {
        cin >> infants[i].a;
        infants[i].pos = i + 1;
    }

    sort(infants.begin(), infants.end(), [](const Infant& u, const Infant& v) {
        return u.a > v.a;
    });

    // dp[l][r]
    vector<vector<long long>> dp(n + 1, vector<long long>(n + 1, 0));

    for (int k = 0; k < n; ++k) {
        long long a = infants[k].a;
        int orig_pos = infants[k].pos;

        for (int l = 0; l <= k; ++l) {
            int r = k - l;

            // Place at left: slot l + 1
            dp[l + 1][r] = max(dp[l + 1][r], dp[l][r] + a * abs(orig_pos - (l + 1)));

            // Place at right: slot n - r
            dp[l][r + 1] = max(dp[l][r + 1], dp[l][r] + a * abs(orig_pos - (n - r)));
        }
    }

    long long ans = 0;
    for (int l = 0; l <= n; ++l) {
        ans = max(ans, dp[l][n - l]);
    }

    cout << ans << "\n";
    return 0;
}
```
