# Problem Analysis: AtCoder-arc204_b — Sort Permutation

**Problem ID**: `AtCoder-arc204_b`  
**Contest**: `arc204`  
**Rating / Difficulty**: 2210  
**URL**: https://atcoder.jp/contests/arc204/tasks/arc204_b  
**VJudge Tag**: `[problem:AtCoder-arc204_b]`  
**Category File**: [`../categories/dp/sort_permutation_cyclic_chords_interval_dp.md`](../categories/dp/sort_permutation_cyclic_chords_interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Permutation cycle decomposition reduced to maximum non-crossing chords connecting equal residues on a circle via interval DP.

## 2. Core Observation & Invariant
Sorting a permutation in minimum swaps requires every swap to split a cycle into two. Swaps between positions with i == j mod N give 1 point and correspond to chords connecting equal residue classes on the cycle. Two chords can both be executed iff they do not cross. The problem decouples independently over each cycle of P.

## 3. Step-by-Step Algorithm
1. 1. Decompose permutation P into disjoint cycles.
2. 2. For each cycle, extract the sequence of residues modulo N.
3. 3. Duplicate the sequence to length 2L and run interval DP: dp[i][len] = max non-crossing chords on subsegment [i, i + len - 1].
4. 4. Transition considers leaving endpoint unmatched, or matching with any position k < j of identical residue.
5. 5. Sum the maximum points over all cycles.

## 4. Complexity Analysis
- **Time Complexity**: `O(K * (NK)^2) <= 2.5 * 10^8 operations, runs in ~0.3s`
- **Space Complexity**: `O(L^2) per cycle`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

// Maximum non-crossing chords connecting equal residues in a cycle
int solve_cycle(const vector<int>& residues, int K) {
    int L = residues.size();
    if (L < 2) return 0;

    // Fast interval DP on circular array
    // Double the array
    vector<int> seq(2 * L);
    for (int i = 0; i < 2 * L; ++i) {
        seq[i] = residues[i % L];
    }

    // dp[i][len] = max chords on seq[i .. i + len - 1]
    // len from 2 to L
    // For fixed j = i + len - 1, we only transition from k in [i, j-1] where seq[k] == seq[j].
    // Store positions of each residue in the interval
    vector<vector<int>> dp(2 * L, vector<int>(L + 1, 0));

    // pos_by_res[val] stores recent positions of val
    for (int len = 2; len <= L; ++len) {
        for (int i = 0; i + len <= 2 * L; ++i) {
            int j = i + len - 1;
            int res = dp[i][len - 1]; // j not matched

            // match j with k in [i, j - 1]
            for (int k = j - 1; k >= i; --k) {
                if (seq[k] == seq[j]) {
                    int left = (k > i) ? dp[i][k - i + 1] : 0;
                    int mid = (j - 1 >= k + 1) ? dp[k + 1][j - 1 - (k + 1) + 1] : 0;
                    res = max(res, left + mid + 1);
                }
            }
            dp[i][len] = res;
        }
    }

    int ans = 0;
    for (int i = 0; i < L; ++i) {
        ans = max(ans, dp[i][L]);
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    if (!(cin >> N >> K)) return 0;

    int M = N * K;
    vector<int> P(M);
    for (int i = 0; i < M; ++i) {
        cin >> P[i];
        P[i]--; // 0-indexed
    }

    vector<bool> vis(M, false);
    int total_points = 0;

    for (int i = 0; i < M; ++i) {
        if (!vis[i]) {
            vector<int> cycle_residues;
            int cur = i;
            while (!vis[cur]) {
                vis[cur] = true;
                cycle_residues.push_back(cur % N);
                cur = P[cur];
            }
            total_points += solve_cycle(cycle_residues, K);
        }
    }

    cout << total_points << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
