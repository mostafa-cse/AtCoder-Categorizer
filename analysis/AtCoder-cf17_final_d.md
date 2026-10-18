# Problem Analysis: AtCoder-cf17_final_d — D. Zabuton

**Problem ID**: `AtCoder-cf17_final_d`  
**Contest**: `cf17-final`  
**Rating / Difficulty**: 2509  
**URL**: https://atcoder.jp/contests/cf17-final/tasks/cf17_final_d  
**VJudge Tag**: `[problem:AtCoder-cf17_final_d]`  
**Category File**: [`../categories/dynamic_programming_dp/zabuton_cushion_stacking_exchange_argument_knapsack.md`](../categories/dynamic_programming_dp/zabuton_cushion_stacking_exchange_argument_knapsack.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Maximize participants who can stack cushions. Participant $i$ can stack $P_i$ cushions if the current stack has at most $H_i$ cushions. By exchange argument, consider participants $i$ and $j$ stacked adjacent. For both to succeed in order $(i, j)$, initial stack $S \le \min(H_i, H_j - P_i)$. Swapping to $(j, i)$ requires $S \le \min(H_j, H_i - P_j)$. Order $(i, j)$ is weakly superior if $H_j - P_i \ge H_i - P_j \iff H_i + P_i \le H_j + P_j$. Sorting participants by $H_i + P_i$ ascending establishes the canonical order, after which a 1D Knapsack DP computes the maximum count.

## 2. Core Observation & Invariant
After sorting by $H_i + P_i$, let $DP[j]$ be the minimum total cushions stacked by a subset of $j$ participants. For each participant $(H_i, P_i)$, if $DP[j] \le H_i$, transition $DP[j + 1] = \min(DP[j + 1], DP[j] + P_i)$ in reverse order.

## 3. Step-by-Step Algorithm
1. 1. Read $N$ participants $(H_i, P_i)$.
2. 2. Sort participants in ascending order of $H_i + P_i$.
3. 3. Initialize $DP$ array of size $N + 1$ with $\infty$, setting $DP[0] = 0$.
4. 4. Maintain current maximum participants $ans = 0$.
5. 5. For each participant $i$:
6.    a. For $j$ from $ans$ down to 0:
7.       if $DP[j] \le H_i$, relax $DP[j + 1] = \min(DP[j + 1], DP[j] + P_i)$ and update $ans = \max(ans, j + 1)$.
8. 6. Output $ans$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Participant {
    long long h, p;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<Participant> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].h >> a[i].p;
    }

    sort(a.begin(), a.end(), [](const Participant& x, const Participant& y) {
        return (x.h + x.p) < (y.h + y.p);
    });

    vector<long long> dp(n + 1, -1);
    dp[0] = 0;
    int ans = 0;

    for (int i = 0; i < n; ++i) {
        long long h = a[i].h;
        long long p = a[i].p;
        for (int j = ans; j >= 0; --j) {
            if (dp[j] != -1 && dp[j] <= h) {
                long long nxt = dp[j] + p;
                if (dp[j + 1] == -1 || nxt < dp[j + 1]) {
                    dp[j + 1] = nxt;
                    if (j + 1 > ans) {
                        ans = j + 1;
                    }
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
