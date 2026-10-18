# Problem Analysis: AtCoder-arc120_e — 1D Party

**Problem ID**: `AtCoder-arc120_e`  
**Contest**: `arc120`  
**Rating / Difficulty**: 2653  
**URL**: https://atcoder.jp/contests/arc120/tasks/arc120_e  
**VJudge Tag**: `[problem:AtCoder-arc120_e]`  
**Category File**: [`../categories/dynamic_programming_dp/party_1d_convex_hull_trick.md`](../categories/dynamic_programming_dp/party_1d_convex_hull_trick.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Convex Hull Trick (CHT)`  
- **Topic (Skill)**: `Convex Hull Trick (CHT) and Dynamic CHT`  

---

## 1. Problem Statement & Key Idea
Finding the minimum time for all N people on a line to meet reduces via binary search on time v to checking whether an interval-chain dynamic programming transition can connect person 1 to person N.

## 2. Core Observation & Invariant
Binary search on time v. Person i and person j can meet within time v iff their initial distance is at most 2v. In optimal movement, people meet in contiguous pair or triplet groups. Transitioning from i to j requires A[j] - A[i+1] <= 2v. A difference array or prefix-sum DP verifies feasibility in O(N) time per binary search iteration.

## 3. Step-by-Step Algorithm
1. 1. Binary search the answer v in range [0, 10^9].
2. 2. For a fixed v, compute for each i the furthest j such that A[j] - A[i+1] <= 2v.
3. 3. Check feasibility using a difference array / BFS reachability across people.
4. 4. Adjust binary search boundaries until exact minimum v is found.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(max A))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool ok(int N, const vector<long long>& A, long long v) {
    vector<int> diff(N + 5, 0);
    diff[0] += 1;
    diff[1] -= 1;
    int cur = 0;
    int x = 0; // two pointers

    for (int i = 0; i < N - 1; ++i) {
        cur += diff[i];
        if (cur == 0) continue;

        while (x < N && A[x] <= A[i] + 2 * v) {
            x++;
        }
        int max_reach = x - 1;

        if (max_reach == N - 1) return true;

        if (i == 0) {
            if (max_reach >= 1) {
                diff[1] += 1;
                diff[max_reach] -= 1;
            }
        } else if (max_reach > i + 2) {
            diff[i + 2] += 1;
            diff[max_reach] -= 1;
        }
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    long long low = 0;
    long long high = (A[N - 1] - A[0]) / 2;
    long long ans = high;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (ok(N, A, mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
