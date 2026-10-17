# Problem Analysis: AtCoder-arc104_c — Fair Elevator

**Problem ID**: `AtCoder-arc104_c`  
**Contest**: `arc104`  
**Rating / Difficulty**: 2009  
**URL**: https://atcoder.jp/contests/arc104/tasks/arc104_c  
**VJudge Tag**: `[problem:AtCoder-arc104_c]`  
**Category File**: [`../categories/dynamic_programming/non_overlapping_block_interval_partition_dp.md`](../categories/dynamic_programming/non_overlapping_block_interval_partition_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Non-Overlapping Block Interval Partition DP under Endpoint Matching Constraints`  

---

## 1. Problem Statement & Key Idea
An elevator serves floors 1 to 2N. There are N passengers with entry A_i and exit B_i (some values -1). If two passengers' intervals overlap, their traveled distances must be equal. Determine if there exists a valid full assignment.

**Key Idea**: The fairness condition implies that any overlapping passenger journeys must share the exact same length L = B_i - A_i. This forces the sequence of 2N floors to be partitioned into contiguous blocks of length 2L, where in each block, passengers enter at positions l, l+1, ..., l+L-1 and exit at l+L, l+L+1, ..., l+2L-1. A 1D DP dp[r] checks if the prefix 1 ... r can be partitioned into such valid blocks.

## 2. Core Observation & Invariant
Overlapping equality forces the interval structure into synchronized blocks [l, l+L-1] -> [l+L, l+2L-1], transforming the problem into a partition DP.

## 3. Step-by-Step Algorithm
1. Validate initial A_i, B_i inputs (no duplicates, A_i < B_i, etc.).
2. Set dp[0] = true.
3. For r from 2 to 2N step 2:
4.   For each candidate block length 2L <= r (with l = r - 2L + 1):
5.     If dp[l - 1] is true and block [l, r] is compatible with input pairs:
6.       For each k from 0 to L - 1:
7.         Check that floor l + k (as entry) and floor l + k + L (as exit) match existing passenger assignments.
8.       If valid: dp[r] = true; break.
9. If dp[2N] is true print Yes, else No.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N)`

## 5. Core Algorithmic Skill & Learning Takeaway
Interval partition DP under synchronized entry-exit block constraints.

**Reusable Pattern**: Synchronized Block Partition DP: Verifying that intervals partition into contiguous segments [l, l+L-1] paired to [l+L, l+2L-1].

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total_floors = 2 * n;
    vector<int> a(n), b(n);
    vector<int> floor_type(total_floors + 1, 0); // 1: entry, 2: exit, 0: free
    vector<int> match_floor(total_floors + 1, 0);
    vector<bool> floor_used(total_floors + 1, false);

    bool possible = true;
    for (int i = 0; i < n; ++i) {
        cin >> a[i] >> b[i];
        if (a[i] != -1 && b[i] != -1 && a[i] >= b[i]) possible = false;
        if (a[i] != -1) {
            if (floor_used[a[i]]) possible = false;
            floor_used[a[i]] = true;
            floor_type[a[i]] = 1;
        }
        if (b[i] != -1) {
            if (floor_used[b[i]]) possible = false;
            floor_used[b[i]] = true;
            floor_type[b[i]] = 2;
        }
        if (a[i] != -1 && b[i] != -1) {
            match_floor[a[i]] = b[i];
            match_floor[b[i]] = a[i];
        }
    }

    if (!possible) {
        cout << "No\n";
        return 0;
    }

    vector<bool> dp(total_floors + 1, false);
    dp[0] = true;

    for (int r = 2; r <= total_floors; r += 2) {
        for (int l = 1; l < r; l += 2) {
            if (!dp[l - 1]) continue;
            int len = r - l + 1;
            int L = len / 2;

            bool valid = true;
            for (int k = 0; k < L; ++k) {
                int enter = l + k;
                int exit_f = l + k + L;

                if (floor_type[enter] == 2 || floor_type[exit_f] == 1) {
                    valid = false;
                    break;
                }
                if (match_floor[enter] != 0 && match_floor[enter] != exit_f) {
                    valid = false;
                    break;
                }
                if (match_floor[exit_f] != 0 && match_floor[exit_f] != enter) {
                    valid = false;
                    break;
                }
            }

            if (valid) {
                dp[r] = true;
                break;
            }
        }
    }

    cout << (dp[total_floors] ? "Yes" : "No") << "\n";
    return 0;
}
```
