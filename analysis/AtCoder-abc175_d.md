# Problem Analysis: AtCoder-abc175_d — Moving Piece

**Problem ID**: `AtCoder-abc175_d`  
**Contest**: `abc175`  
**Rating / Difficulty**: 1491  
**URL**: https://atcoder.jp/contests/abc175/tasks/abc175_d  
**VJudge Tag**: `[problem:AtCoder-abc175_d]`  
**Category File**: [`../categories/basics/functional_graph_cycle_round_trips.md`](../categories/basics/functional_graph_cycle_round_trips.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Functional Graphs`  
- **Topic (Skill)**: `Functional Graph Permutation Cycle Decomposition with Round Trips`  

---

## 1. Problem Statement & Key Idea
Given a permutation P of 1..N and score array C. Takahashi starts at square s, makes between 1 and K moves along P, adding C[current] at each step. Maximize total score over all starting squares and move counts.

**Key Insight**: The permutation graph consists of disjoint cycles. For each cycle of length L and total score S: if S > 0 and K >= L, taking full cycles is beneficial; remaining steps (up to 2*L) can be simulated.

## 2. Core Observation & Invariant
If cycle sum S <= 0, we should only test up to min(K, L) moves. If S > 0, we can take m = max(0LL, K / L - 1) full cycles, and test the remaining K - m * L moves (at most 2*L steps).

## 3. Step-by-Step Algorithm
1. Find all cycles in the permutation P.
2. ans = -INF.
3. For each starting square s from 1 to N:
4.   Trace cycle from s, recording prefix sums pref[step].
5.   Let L = cycle length, S = pref[L].
6.   For step from 1 to min((long long)L, K):
7.     score = pref[step].
8.     If S > 0:
9.       full_cycles = (K - step) / L;
10.       score += full_cycles * S;
11.     ans = max(ans, score).
12. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
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

    vector<int> p(n + 1);
    vector<long long> c(n + 1);

    for (int i = 1; i <= n; ++i) cin >> p[i];
    for (int i = 1; i <= n; ++i) cin >> c[i];

    long long max_score = -2e18;

    for (int start = 1; start <= n; ++start) {
        vector<long long> cycle_scores;
        int curr = p[start];
        cycle_scores.push_back(c[curr]);

        while (curr != start) {
            curr = p[curr];
            cycle_scores.push_back(c[curr]);
        }

        int L = cycle_scores.size();
        vector<long long> pref(L + 1, 0);
        for (int i = 0; i < L; ++i) {
            pref[i + 1] = pref[i] + cycle_scores[i];
        }

        long long cycle_sum = pref[L];

        for (int step = 1; step <= min((long long)L, k); ++step) {
            long long score = pref[step];
            if (cycle_sum > 0) {
                long long full_cycles = (k - step) / L;
                score += full_cycles * cycle_sum;
            }
            max_score = max(max_score, score);
        }
    }

    cout << max_score << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Permutation cycle decomposition with full-cycle acceleration and bounded step simulation.
- **Reusable Pattern**: `Permutation Cycle Round-Trip: test all 1..min(K, L) steps + floor((K - step)/L) * cycle_sum.`
