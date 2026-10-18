# Problem Analysis: AtCoder-dwango2015_prelims_4 — D - タクシー

**Problem ID**: `AtCoder-dwango2015_prelims_4`  
**Contest**: `dwango2015-prelims`  
**Rating / Difficulty**: 2495  
**URL**: https://atcoder.jp/contests/dwango2015-prelims/tasks/dwango2015_prelims_4  
**VJudge Tag**: `[problem:AtCoder-dwango2015_prelims_4]`  
**Category File**: [`../categories/basics/taxi_circle_optimal_transport_weighted_median.md`](../categories/basics/taxi_circle_optimal_transport_weighted_median.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Find the minimum cost to transport participants on a circular line of length $L$ with $N$ cities so that supplies match demands.

## 2. Core Observation & Invariant
Let $d_i = b_i - c_i$ be net excess at city $i$. On a cut line, the net flow across arc $i$ of length $\Delta x_i$ is prefix sum $P_i = \sum_{j=1}^i d_j$. On a circle, adding a global circulation $F$ makes flow across arc $i$ equal $P_i + F$, with total cost $C(F) = \sum_{i=1}^N \Delta x_i |F - (-P_i)|$. Minimizing this continuous 1D convex sum is the weighted median problem with points $-P_i$ and weights $\Delta x_i$ summing to $L$. Sorting by $-P_i$ and picking the median where accumulated weight reaches $L/2$ yields the optimal circulation $F$ in $O(N \log N)$ time.

## 3. Step-by-Step Algorithm
1. 1. Compute arc lengths $\Delta x_i = a_{i+1} - a_i$ for $1 \le i < N$ and $\Delta x_N = L - a_N + a_1$.
2. 2. Compute prefix net flows $P_i = \sum_{j=1}^i (b_j - c_j)$.
3. 3. Form pairs $(-P_i, \Delta x_i)$ and sort them in ascending order of $-P_i$.
4. 4. Accumulate weights $\Delta x_i$; the first value with $2 \times \text{acc} \ge L$ is the optimal integer circulation $F$.
5. 5. Compute and print total cost $\sum_{i=1}^N \Delta x_i |P_i + F|$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long L;
    if (!(cin >> N >> L)) return 0;

    vector<long long> A(N), B(N), C(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i] >> B[i] >> C[i];
    }

    vector<long long> delta_x(N);
    for (int i = 0; i < N - 1; ++i) {
        delta_x[i] = A[i + 1] - A[i];
    }
    delta_x[N - 1] = L - A[N - 1] + A[0];

    vector<long long> P(N);
    long long cur = 0;
    for (int i = 0; i < N; ++i) {
        cur += B[i] - C[i];
        P[i] = cur;
    }

    // Weighted median of v_i = -P[i] with weight delta_x[i]
    vector<pair<long long, long long>> items(N);
    for (int i = 0; i < N; ++i) {
        items[i] = {-P[i], delta_x[i]};
    }
    sort(items.begin(), items.end());

    long long acc = 0;
    long long F = items[0].first;
    for (int i = 0; i < N; ++i) {
        acc += items[i].second;
        if (2 * acc >= L) {
            F = items[i].first;
            break;
        }
    }

    long long ans = 0;
    for (int i = 0; i < N; ++i) {
        ans += delta_x[i] * abs(P[i] + F);
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
