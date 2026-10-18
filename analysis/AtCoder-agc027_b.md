# Problem Analysis: AtCoder-agc027_b — B - Garbage Collector

**Problem ID**: `AtCoder-agc027_b`  
**Contest**: `agc027`  
**Rating / Difficulty**: 2631  
**URL**: https://atcoder.jp/contests/agc027/tasks/agc027_b  
**VJudge Tag**: `[problem:AtCoder-agc027_b]`  
**Category File**: [`../categories/miscellaneous/garbage_collector_energy_greedy.md`](../categories/miscellaneous/garbage_collector_energy_greedy.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Greedy Algorithms`  
- **Topic (Skill)**: `Exchange Arguments`  

---

## 1. Problem Statement & Key Idea
A robot collects N pieces of garbage at positions x_1 < x_2 < ... < x_N. Carrying k pieces consumes (k+1)^2 energy per unit distance, plus cost X per pickup/dropoff. Find the minimum total energy.

## 2. Core Observation & Invariant
By exchange arguments, if the robot makes K trips to the dump, it should pick up approximately ceil(N/K) pieces per trip. In each trip, pieces are collected on the way back. The furthest piece and 2nd furthest piece have energy multiplier 5; the b-th furthest piece (b >= 3) has multiplier 2b + 1. Sorting pieces and partitioning them into blocks of size K allows evaluating the cost of any K in O(N / K) time using prefix sums.

## 3. Step-by-Step Algorithm
1. Sort garbage positions x_1 ... x_N and precompute prefix sums.
2. Iterate number of trips K in [1, N].
3. For each K, fixed cost is (N + K) * X.
4. Pieces are grouped into layers of size K from right to left.
5. Layer 1: multiplier 5. Layer b >= 2: multiplier 2b + 1.
6. Sum over all layers using prefix sums in O(N / K) steps.
7. Global minimum over all K in [1, N] is the answer.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

using ll = long long;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    ll X;
    if (!(cin >> N >> X)) return 0;

    vector<ll> A(N + 1);
    vector<__int128> pref(N + 1, 0);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
        pref[i] = pref[i - 1] + A[i];
    }

    auto get_sum = [&](int l, int r) -> __int128 {
        l = max(1, l);
        if (l > r) return 0;
        return pref[r] - pref[l - 1];
    };

    __int128 best_ans = -1;

    for (int K = 1; K <= N; ++K) {
        __int128 cost = (__int128)(N + K) * X;

        // Block 1
        cost += 5 * get_sum(N - K + 1, N);
        // Block 2
        cost += 5 * get_sum(N - 2 * K + 1, N - K);

        // Block b >= 3
        int b = 3;
        while ((b - 1) * K < N) {
            int r = N - (b - 1) * K;
            int l = max(1, N - b * K + 1);
            __int128 coeff = 2 * b + 1;
            cost += coeff * get_sum(l, r);
            b++;
        }

        if (best_ans == -1 || cost < best_ans) {
            best_ans = cost;
        }
    }

    ll out_val = (ll)best_ans;
    cout << out_val << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
