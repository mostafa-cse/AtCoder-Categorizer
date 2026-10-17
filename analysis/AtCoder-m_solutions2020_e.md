# Problem Analysis: AtCoder-m_solutions2020_e — E. M's Solution

**Problem ID**: `AtCoder-m_solutions2020_e`  
**Contest**: `m-solutions2020`  
**Rating / Difficulty**: 2268  
**URL**: https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_e  
**VJudge Tag**: `[problem:AtCoder-m_solutions2020_e]`  
**Category File**: [`../categories/dynamic_programming_dp/bitmask_dp_ternary_state_railway.md`](../categories/dynamic_programming_dp/bitmask_dp_ternary_state_railway.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
A grid city has initial railways along $x=0$ and $y=0$. There are $N \le 15$ towns with positions $(X_i, Y_i)$ and populations $P_i$. For each $K = 0, 1, \dots, N$, find the minimum weighted walking distance to railways if we build $K$ new horizontal or vertical railways.

## 2. Core Observation & Invariant
Any optimal railway line passes directly through at least one town ($x = X_i$ or $y = Y_i$). Moreover, among at most $N$ lines, each chosen line can be injectively associated with a distinct town. Hence, each town $i$ is assigned one of 3 states: (1) build vertical line $x = X_i$, (2) build horizontal line $y = Y_i$, or (0) build no line. There are $3^N = 3^{15} \approx 1.43 \times 10^7$ assignments. A ternary branch-and-bound DFS maintaining running distances for all $N$ towns evaluates all combinations in $\approx 140$ ms.

## 3. Step-by-Step Algorithm
1. Store town coordinates and populations in fixed arrays.
2. Initialize answer array `ans[K] = inf` for $0 \le K \le N$.
3. Run ternary DFS `dfs(idx, count_lines, d0, ..., d14)` from `idx = 0`.
4. Branch 0: town `idx` builds no line, passing distances unchanged.
5. Branch 1: town `idx` builds $x = X_{idx}$, updating each $d_j = \min(d_j, |X_j - X_{idx}|)$ and incrementing `count_lines`.
6. Branch 2: town `idx` builds $y = Y_{idx}$, updating each $d_j = \min(d_j, |Y_j - Y_{idx}|)$ and incrementing `count_lines`.
7. At leaf `idx == N`, sum $P_j \times d_j$ and update `ans[count_lines]`.
8. Apply prefix minima `ans[K] = min(ans[K], ans[K-1])` and print answers.

## 4. Complexity Analysis
- **Time Complexity**: `O(3^N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int n;
long long x[15], y[15], p[15];
long long ans[16];

void dfs(int idx, int count_lines, long long d0, long long d1, long long d2, long long d3,
         long long d4, long long d5, long long d6, long long d7,
         long long d8, long long d9, long long d10, long long d11,
         long long d12, long long d13, long long d14) {
    if (idx == n) {
        long long total = 0;
        if (0 < n) total += p[0] * d0;
        if (1 < n) total += p[1] * d1;
        if (2 < n) total += p[2] * d2;
        if (3 < n) total += p[3] * d3;
        if (4 < n) total += p[4] * d4;
        if (5 < n) total += p[5] * d5;
        if (6 < n) total += p[6] * d6;
        if (7 < n) total += p[7] * d7;
        if (8 < n) total += p[8] * d8;
        if (9 < n) total += p[9] * d9;
        if (10 < n) total += p[10] * d10;
        if (11 < n) total += p[11] * d11;
        if (12 < n) total += p[12] * d12;
        if (13 < n) total += p[13] * d13;
        if (14 < n) total += p[14] * d14;
        if (total < ans[count_lines]) ans[count_lines] = total;
        return;
    }

    // 0: no line
    dfs(idx + 1, count_lines, d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14);

    // 1: vertical line at x[idx]
    dfs(idx + 1, count_lines + 1,
        min(d0, llabs(x[0] - x[idx])),
        min(d1, llabs(x[1] - x[idx])),
        min(d2, llabs(x[2] - x[idx])),
        min(d3, llabs(x[3] - x[idx])),
        min(d4, llabs(x[4] - x[idx])),
        min(d5, llabs(x[5] - x[idx])),
        min(d6, llabs(x[6] - x[idx])),
        min(d7, llabs(x[7] - x[idx])),
        min(d8, llabs(x[8] - x[idx])),
        min(d9, llabs(x[9] - x[idx])),
        min(d10, llabs(x[10] - x[idx])),
        min(d11, llabs(x[11] - x[idx])),
        min(d12, llabs(x[12] - x[idx])),
        min(d13, llabs(x[13] - x[idx])),
        min(d14, llabs(x[14] - x[idx])));

    // 2: horizontal line at y[idx]
    dfs(idx + 1, count_lines + 1,
        min(d0, llabs(y[0] - y[idx])),
        min(d1, llabs(y[1] - y[idx])),
        min(d2, llabs(y[2] - y[idx])),
        min(d3, llabs(y[3] - y[idx])),
        min(d4, llabs(y[4] - y[idx])),
        min(d5, llabs(y[5] - y[idx])),
        min(d6, llabs(y[6] - y[idx])),
        min(d7, llabs(y[7] - y[idx])),
        min(d8, llabs(y[8] - y[idx])),
        min(d9, llabs(y[9] - y[idx])),
        min(d10, llabs(y[10] - y[idx])),
        min(d11, llabs(y[11] - y[idx])),
        min(d12, llabs(y[12] - y[idx])),
        min(d13, llabs(y[13] - y[idx])),
        min(d14, llabs(y[14] - y[idx])));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n)) return 0;
    for (int i = 0; i < n; ++i) {
        cin >> x[i] >> y[i] >> p[i];
    }
    for (int i = 0; i <= n; ++i) ans[i] = 2e18;

    dfs(0, 0,
        min(llabs(x[0]), llabs(y[0])), min(llabs(x[1]), llabs(y[1])), min(llabs(x[2]), llabs(y[2])),
        min(llabs(x[3]), llabs(y[3])), min(llabs(x[4]), llabs(y[4])), min(llabs(x[5]), llabs(y[5])),
        min(llabs(x[6]), llabs(y[6])), min(llabs(x[7]), llabs(y[7])), min(llabs(x[8]), llabs(y[8])),
        min(llabs(x[9]), llabs(y[9])), min(llabs(x[10]), llabs(y[10])), min(llabs(x[11]), llabs(y[11])),
        min(llabs(x[12]), llabs(y[12])), min(llabs(x[13]), llabs(y[13])), min(llabs(x[14]), llabs(y[14])));

    for (int k = 1; k <= n; ++k) {
        ans[k] = min(ans[k], ans[k - 1]);
    }

    for (int k = 0; k <= n; ++k) {
        cout << ans[k] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
