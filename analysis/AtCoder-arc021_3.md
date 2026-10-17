# Problem Analysis: AtCoder-arc021_3 — C. 増築王高橋君

**Problem ID**: `AtCoder-arc021_3`  
**Contest**: `arc021`  
**Rating / Difficulty**: 2164  
**URL**: https://atcoder.jp/contests/arc021/tasks/arc021_3  
**VJudge Tag**: `[problem:AtCoder-arc021_3]`  
**Category File**: [`../categories/basics/binary_search_marginal_cost_threshold.md`](../categories/basics/binary_search_marginal_cost_threshold.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Binary Search`  

---

## 1. Problem Statement & Key Idea
Find the minimum cost to perform K building upgrades where building i starts at price A_i and increases by D_i per upgrade. The upgrade costs for building i form an arithmetic progression A_i + m*D_i. Binary search on the marginal upgrade cost threshold X. Upgrades with cost strictly below X are unconditionally taken, and the remaining upgrades needed to reach K are purchased at price exactly X.

## 2. Core Observation & Invariant
As marginal cost X increases, the number of available upgrades costing <= X is monotonically non-decreasing: sum_i max(0, (X - A_i)/D_i + 1). Binary searching for the smallest integer X where the total count is >= K isolates the K-th cheapest upgrade. Summing the closed-form arithmetic progressions c_i*A_i + c_i*(c_i-1)/2*D_i for all c_i upgrades with cost < X takes O(N) time.

## 3. Step-by-Step Algorithm
1. Binary search on the marginal cost threshold X in the range [1, 2*10^14].
2. In the predicate, count total upgrades costing <= X: count(X) = sum_i max(0LL, (X - A_i) / D_i + 1). If count >= K, set best_X = X and search lower.
3. After finding best_X, count and sum costs of all upgrades strictly less than best_X using the arithmetic progression sum for each building.
4. Add (K - taken_upgrades) * best_X to account for the remaining upgrades at cost exactly best_X.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log(max_cost))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long K;
    int N;
    if (!(cin >> K >> N)) return 0;

    vector<long long> A(N), D(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i] >> D[i];
    }

    long long low = 1, high = 2e14, best_X = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        long long cnt = 0;
        for (int i = 0; i < N; ++i) {
            if (mid >= A[i]) {
                cnt += (mid - A[i]) / D[i] + 1;
                if (cnt >= K) break;
            }
        }
        if (cnt >= K) {
            best_X = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    long long total_cost = 0;
    long long total_upgrades = 0;
    for (int i = 0; i < N; ++i) {
        if (best_X - 1 >= A[i]) {
            long long c = (best_X - 1 - A[i]) / D[i] + 1;
            total_upgrades += c;
            total_cost += c * A[i] + (c * (c - 1) / 2) * D[i];
        }
    }

    total_cost += (K - total_upgrades) * best_X;
    cout << total_cost << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
