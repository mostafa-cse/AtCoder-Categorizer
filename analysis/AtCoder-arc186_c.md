# Problem Analysis: AtCoder-arc186_c — C. Ball and Box

**Problem ID**: `AtCoder-arc186_c`  
**Contest**: `arc186`  
**Rating / Difficulty**: 2451  
**URL**: https://atcoder.jp/contests/arc186/tasks/arc186_c  
**VJudge Tag**: `[problem:AtCoder-arc186_c]`  
**Category File**: [`../categories/miscellaneous/ball_and_box_exchange_arguments.md`](../categories/miscellaneous/ball_and_box_exchange_arguments.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Greedy Algorithms`  
- **Topic (Skill)**: `Exchange Arguments`  

---

## 1. Problem Statement & Key Idea
Mr. Box chooses a subset of boxes with capacities $V_i$ and prices $P_i$. If $\ge M$ boxes are bought, Mr. Ball leaves the $M-1$ largest-capacity chosen boxes empty and fills the rest to capacity. Maximize Mr. Box's profit.

## 2. Core Observation & Invariant
Sort boxes descending by capacity $V_i$. If $M > N$, Mr. Box cannot achieve positive score (output 0). If box $t$ is the $M$-th largest capacity chosen, the top $M-1$ chosen boxes must come from $\{0 \dots t-1\}$ and contribute $-(P_i - 1)$ to profit. To maximize profit, greedily select the $M-1$ smallest values of $P_i - 1$. Box $t$ yields $V_t - P_t$, and all subsequent boxes $i > t$ with $V_i > P_i$ can be freely included.

## 3. Step-by-Step Algorithm
1. 1. If $M > N$, output 0.
2. 2. Sort all boxes in descending order of $V_i$.
3. 3. Precompute suffix sums of $\max(0LL, V_i - P_i)$.
4. 4. Maintain a max-heap of size $M-1$ storing the smallest $M-1$ values of $P_i - 1$.
5. 5. For each $t \in [0, N-1]$, if the heap has size $M-1$, evaluate profit $(V_t - P_t) + \text{suff}[t+1] - \sum_{pq} (P_i - 1)$.
6. 6. Insert $P_t - 1$ into the heap.
7. 7. Output the maximum profit found.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N) per test case`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Box {
    long long v, p;
};

void solve() {
    int n, m;
    if (!(cin >> n >> m)) return;
    vector<Box> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].v >> a[i].p;

    if (m > n) {
        cout << 0 << "\n";
        return;
    }

    sort(a.begin(), a.end(), [](const Box &x, const Box &y) {
        return x.v > y.v;
    });

    vector<long long> suff(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
        suff[i] = suff[i + 1] + max(0LL, a[i].v - a[i].p);
    }

    long long ans = 0;
    priority_queue<long long> pq;
    long long sum_pq = 0;

    for (int t = 0; t < n; ++t) {
        if ((int)pq.size() == m - 1) {
            long long profit = (a[t].v - a[t].p) + suff[t + 1] - sum_pq;
            if (profit > ans) ans = profit;
        }

        if (m - 1 > 0) {
            long long cost = a[t].p - 1;
            if ((int)pq.size() < m - 1) {
                pq.push(cost);
                sum_pq += cost;
            } else if (pq.top() > cost) {
                sum_pq -= pq.top();
                pq.pop();
                pq.push(cost);
                sum_pq += cost;
            }
        }
    }

    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
