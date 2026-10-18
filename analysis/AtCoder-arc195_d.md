# Problem Analysis: AtCoder-arc195_d — D - Swap and Erase

**Problem ID**: `AtCoder-arc195_d`  
**Contest**: `arc195`  
**Rating / Difficulty**: 2470  
**URL**: https://atcoder.jp/contests/arc195/tasks/arc195_d  
**VJudge Tag**: `[problem:AtCoder-arc195_d]`  
**Category File**: [`../categories/dynamic_programming_dp/swap_and_erase_adjacent_swap_dp.md`](../categories/dynamic_programming_dp/swap_and_erase_adjacent_swap_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Find the minimum number of adjacent swap operations and prefix run-erase operations to make an array $A$ empty.

## 2. Core Observation & Invariant
Erasing prefix runs of identical elements can be deferred until after all swaps are complete. In any optimal solution, each element is swapped at most once, meaning all swap indices satisfy $|p_i - p_j| \ge 2$. Thus, the array $0 \dots N-1$ is partitioned into disjoint singles (unswapped elements $A_i$) and pairs (swapped elements $(A_{i+1}, A_i)$). The total cost is $1 + (\text{number of swaps}) + (\text{number of adjacent mismatches } B_i \ne B_{i+1})$, which can be minimized via linear DP.

## 3. Step-by-Step Algorithm
1. 1. Define $dp0[i]$ as the minimum cost for prefix $0 \dots i-1$ ending with a single $A_{i-1}$, and $dp1[i]$ ending with a swapped pair $(A_{i-1}, A_{i-2})$ with last element $A_{i-2}$.
2. 2. Base cases: $dp0[1] = 0$, $dp1[2] = 1 + [A_1 \ne A_0]$.
3. 3. From state at $i$, transition to $i+1$ by appending $A_i$ as a single, adding $[\text{last} \ne A_i]$.
4. 4. Transition to $i+2$ by appending $(A_i, A_{i+1})$ as a swapped pair, adding $1 + [\text{last} \ne A_{i+1}] + [A_{i+1} \ne A_i]$.
5. 5. Output $\min(dp0[N], dp1[N]) + 1$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int N;
    if (!(cin >> N)) return;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];

    if (N <= 1) {
        cout << N << "\n";
        return;
    }

    const int INF = 1e9;
    vector<int> dp0(N + 1, INF);
    vector<int> dp1(N + 1, INF);

    dp0[1] = 0;
    if (N >= 2) {
        dp1[2] = 1 + (A[1] != A[0] ? 1 : 0);
    }

    for (int i = 1; i < N; ++i) {
        for (int state = 0; state < 2; ++state) {
            int cur = (state == 0 ? dp0[i] : dp1[i]);
            if (cur >= INF) continue;
            int last_val = (state == 0 ? A[i - 1] : A[i - 2]);

            // Single element A[i]
            int cost_single = cur + (last_val != A[i] ? 1 : 0);
            if (cost_single < dp0[i + 1]) {
                dp0[i + 1] = cost_single;
            }

            // Swapped pair (A[i], A[i+1])
            if (i + 1 < N) {
                int cost_pair = cur + 1 + (last_val != A[i + 1] ? 1 : 0) + (A[i + 1] != A[i] ? 1 : 0);
                if (cost_pair < dp1[i + 2]) {
                    dp1[i + 2] = cost_pair;
                }
            }
        }
    }

    int ans = min(dp0[N], dp1[N]) + 1;
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
