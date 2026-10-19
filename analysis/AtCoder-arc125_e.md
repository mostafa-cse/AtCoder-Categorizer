# Problem Analysis: AtCoder-arc125_e — E - Snack

**Problem ID**: `AtCoder-arc125_e`  
**Contest**: `arc125`  
**Rating / Difficulty**: 2874  
**URL**: https://atcoder.jp/contests/arc125/tasks/arc125_e  
**VJudge Tag**: `[problem:AtCoder-arc125_e]`  
**Category File**: [`../categories/graph_theory/snack_distribution_bipartite_min_cut_optimization.md`](../categories/graph_theory/snack_distribution_bipartite_min_cut_optimization.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Maximum Flow / Minimum Cut`  

---

## 1. Problem Statement & Key Idea
Distribute N kinds of snacks (kind i has A_i pieces) to M children, where child j can receive at most B_j pieces of any single snack and at most C_j pieces in total. Find the maximum total pieces distributed.

## 2. Core Observation & Invariant
By max-flow min-cut duality, the min-cut capacity when selecting the k largest snack capacities in S is sum_{i=1}^{N-k} A_{(i)} + sum_{j=1}^M min(C_j, k B_j). For each child j, the threshold where k B_j exceeds C_j is t_j = floor(C_j / B_j). Sorting snacks A and grouping children by threshold t_j allows evaluating all cuts k in [0, N] via a single linear sweep in O(N log N + M log M) time.

## 3. Step-by-Step Algorithm
1. 1. Sort A ascending and compute prefix sums.
2. 2. For each child j, compute transition point t_j = floor(C_j / B_j) and bucket into events[t_j].
3. 3. Maintain running sum_B (for children with t_j >= k) and sum_C (for children with t_j < k).
4. 4. Sweep k from 0 to N, evaluating cut(k) = pref[N - k] + k * sum_B + sum_C, then updating sums for children with t_j = k.
5. 5. Output the minimum cut.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + M log M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }
    vector<long long> B(M);
    for (int j = 0; j < M; ++j) {
        cin >> B[j];
    }
    vector<long long> C(M);
    for (int j = 0; j < M; ++j) {
        cin >> C[j];
    }

    sort(A.begin(), A.end());
    vector<long long> pref(N + 1, 0);
    for (int i = 0; i < N; ++i) {
        pref[i + 1] = pref[i] + A[i];
    }

    vector<vector<pair<long long, long long>>> events(N + 2);
    long long sum_B = 0;
    long long sum_C = 0;

    for (int j = 0; j < M; ++j) {
        sum_B += B[j];
        long long t = C[j] / B[j];
        if (t <= N) {
            events[t].push_back({B[j], C[j]});
        }
    }

    long long min_cut = -1;

    for (int k = 0; k <= N; ++k) {
        long long cut = pref[N - k] + 1LL * k * sum_B + sum_C;
        if (min_cut == -1 || cut < min_cut) {
            min_cut = cut;
        }

        for (const auto& pr : events[k]) {
            sum_B -= pr.first;
            sum_C += pr.second;
        }
    }

    cout << min_cut << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
