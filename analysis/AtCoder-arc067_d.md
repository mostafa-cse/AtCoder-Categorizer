# Problem Analysis: AtCoder-arc067_d — F - Yakiniku Restaurants

**Problem ID**: `AtCoder-arc067_d`  
**Contest**: `arc067`  
**Rating / Difficulty**: 2729  
**URL**: https://atcoder.jp/contests/arc067/tasks/arc067_d  
**VJudge Tag**: `[problem:AtCoder-arc067_d]`  
**Category File**: [`../categories/dynamic_programming_dp/yakiniku_restaurants_dnc_optimization.md`](../categories/dynamic_programming_dp/yakiniku_restaurants_dnc_optimization.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `Divide and Conquer Optimization`  

---

## 1. Problem Statement & Key Idea
There are N restaurants on a line with distances A_i between adjacent restaurants, and M meal tickets. Restaurant i gives deliciousness B_{i, j} for ticket j. Find the maximum happiness sum_{j=1}^M max_{k in [L, R]} B_{k, j} - dist(L, R) over all intervals 1 <= L <= R <= N.

## 2. Core Observation & Invariant
For each ticket type j, restaurant i provides the maximum deliciousness B_{i, j} over a maximal interval [L_i, R_i], computable using a monotonic stack. Thus, restaurant i contributes B_{i, j} to all query intervals [l, r] satisfying L_i <= l <= i and i <= r <= R_i. This contribution is a 2D rectangle in the (l, r) plane. Applying 2D difference array updates for all N * M rectangles across all tickets takes O(N * M) time. Computing the 2D prefix sums takes O(N^2) time, immediately yielding the optimal interval in O(N * M + N^2) total time.

## 3. Step-by-Step Algorithm
1. 1. Compute prefix sums of distances A to obtain dist(l, r) in O(1).
2. 2. Initialize a 2D difference array diff of size (N + 2) x (N + 2).
3. 3. For each ticket type j from 1 to M:
4.    a. Use monotonic stacks to find left boundary L_i and right boundary R_i for each restaurant i.
5.    b. Apply 2D difference updates: add B_{i, j} to rectangle [L_i, i] x [i, R_i].
6. 4. Compute 2D prefix sums of diff in O(N^2).
7. 5. For each 1 <= l <= r <= N, compute net profit = diff[l][r] - (dist[r] - dist[l]) and take the maximum.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M + N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> A(n);
    vector<long long> dist_prefix(n + 1, 0);
    for (int i = 1; i < n; ++i) {
        cin >> A[i];
        dist_prefix[i + 1] = dist_prefix[i] + A[i];
    }

    vector<vector<long long>> B(n + 1, vector<long long>(m + 1));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            cin >> B[i][j];
        }
    }

    // 2D difference array
    vector<vector<long long>> diff(n + 2, vector<long long>(n + 2, 0));
    vector<int> stk(n + 2);
    vector<int> L(n + 1), R(n + 1);

    for (int j = 1; j <= m; ++j) {
        // Monotonic stack left
        int top = 0;
        for (int i = 1; i <= n; ++i) {
            while (top > 0 && B[stk[top]][j] < B[i][j]) {
                top--;
            }
            L[i] = (top == 0 ? 1 : stk[top] + 1);
            stk[++top] = i;
        }

        // Monotonic stack right
        top = 0;
        for (int i = n; i >= 1; --i) {
            while (top > 0 && B[stk[top]][j] <= B[i][j]) {
                top--;
            }
            R[i] = (top == 0 ? n : stk[top] - 1);
            stk[++top] = i;
        }

        // Apply 2D difference updates
        for (int i = 1; i <= n; ++i) {
            int l_b = L[i];
            int r_b = R[i];
            long long val = B[i][j];

            diff[l_b][i] += val;
            diff[i + 1][i] -= val;
            diff[l_b][r_b + 1] -= val;
            diff[i + 1][r_b + 1] += val;
        }
    }

    long long max_profit = 0;

    for (int l = 1; l <= n; ++l) {
        for (int r = 1; r <= n; ++r) {
            diff[l][r] += diff[l - 1][r] + diff[l][r - 1] - diff[l - 1][r - 1];
            if (r >= l) {
                long long travel_cost = dist_prefix[r] - dist_prefix[l];
                long long net_profit = diff[l][r] - travel_cost;
                if (net_profit > max_profit) {
                    max_profit = net_profit;
                }
            }
        }
    }

    cout << max_profit << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
