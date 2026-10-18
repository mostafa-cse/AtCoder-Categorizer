# Problem Analysis: AtCoder-arc193_b — B - Broken Wheel

**Problem ID**: `AtCoder-arc193_b`  
**Contest**: `arc193`  
**Rating / Difficulty**: 2420  
**URL**: https://atcoder.jp/contests/arc193/tasks/arc193_b  
**VJudge Tag**: `[problem:AtCoder-arc193_b]`  
**Category File**: [`../categories/graph_theory/broken_wheel_cycle_matrix_scan.md`](../categories/graph_theory/broken_wheel_cycle_matrix_scan.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Cycles`  
- **Topic (Skill)**: `Cycle Detection`  

---

## 1. Problem Statement & Key Idea
Count the number of valid orientations of a wheel graph with missing rim edges such that all vertex in-degrees match given constraints.

## 2. Core Observation & Invariant
A wheel graph consists of a center hub connected to an $N$-cycle. Directing the hub edges determines the in-degree contribution to each rim vertex from the center. The remaining rim edges form a cycle of dependencies where each edge can be oriented clockwise, counterclockwise, or be absent. This defines a transfer matrix scan along the cycle of length $N$, solved via matrix multiplication or dynamic programming in $O(N)$ time.

## 3. Step-by-Step Algorithm
1. 1. Analyze in-degree constraints for each rim vertex: required degree determines the rim transitions.
2. 2. Fix the state of the initial rim edge $(0, 1)$ among the 3 possible orientations.
3. 3. Propagate transitions along the cycle $i = 1 \dots N-1$ using $3 \times 3$ state transition matrices.
4. 4. Verify that the closing edge $(N-1, 0)$ matches the initially fixed state.
5. 5. Sum valid configurations across all initial states modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;
    string s;
    cin >> s;

    // Transition matrices for s_i = 0 and s_i = 1
    int T0[3][3] = {
        {1, 1, 0},
        {1, 1, 0},
        {1, 1, 1}
    };
    int T1[3][3] = {
        {1, 1, 1},
        {1, 1, 1},
        {1, 1, 2}
    };

    long long ans = 0;
    for (int case_idx = 0; case_idx < 3; ++case_idx) {
        vector<long long> dp(3, 0);
        dp[case_idx] = 1;

        for (char ch : s) {
            vector<long long> next_dp(3, 0);
            int (*T)[3] = (ch == '1' ? T1 : T0);
            for (int u = 0; u < 3; ++u) {
                if (!dp[u]) continue;
                for (int v = 0; v < 3; ++v) {
                    next_dp[v] = (next_dp[v] + dp[u] * T[u][v]) % MOD;
                }
            }
            dp = move(next_dp);
        }
        ans = (ans + dp[case_idx]) % MOD;
    }

    ans = (ans - 2 + MOD) % MOD;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
