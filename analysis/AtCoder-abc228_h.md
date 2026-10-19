# Problem Analysis: AtCoder-abc228_h — H - Histogram

**Problem ID**: `AtCoder-abc228_h`  
**Contest**: `abc228`  
**Rating / Difficulty**: 2729  
**URL**: https://atcoder.jp/contests/abc228/tasks/abc228_h  
**VJudge Tag**: `[problem:AtCoder-abc228_h]`  
**Category File**: [`../categories/dynamic_programming_dp/histogram_cht_optimization.md`](../categories/dynamic_programming_dp/histogram_cht_optimization.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Convex Hull Trick (CHT)`  
- **Topic (Skill)**: `Convex Hull Trick (CHT) and Dynamic CHT`  

---

## 1. Problem Statement & Key Idea
Given N pairs (A_i, C_i). Each element A_i can be incremented at cost C_i per unit. If K distinct values remain in A, pay additional K * X. Find the minimum total cost.

## 2. Core Observation & Invariant
Sort and group distinct values: a_1 < a_2 < ... < a_M with accumulated weights c_k = sum C_i for A_i = a_k. In any optimal solution, a prefix of values is raised to a_i. The DP transition to cover the first i values with the last group being [j+1, i] raised to a_i is: dp[i] = min_{j < i} (dp[j] + S_{ac}[j] - S_c[j] * a_i) + X + a_i * S_c[i] - S_{ac}[i], where S_c and S_{ac} are prefix sums of c_k and a_k * c_k. This is of the form min(m_j * x + k_j) where query x = a_i is strictly increasing and slope m_j = -S_c[j] is strictly decreasing. Hence, the Convex Hull Trick (CHT) with a deque computes all transitions in O(M) time.

## 3. Step-by-Step Algorithm
1. 1. Sort pairs (A_i, C_i) and compress identical values of A_i by summing their costs.
2. 2. Compute prefix sums S_c[i] = sum_{k=1}^i c_k and S_{ac}[i] = sum_{k=1}^i a_k * c_k.
3. 3. Initialize CHT deque with line (m = 0, k = 0).
4. 4. For each i from 1 to M:
5.    a. Query the minimum value at x = a_i using the CHT deque in amortized O(1).
6.    b. Compute dp[i] = min_val + X + a_i * S_c[i] - S_{ac}[i].
7.    c. Add line (m = -S_c[i], k = dp[i] + S_{ac}[i]) to the CHT deque, maintaining convexity.
8. 5. Output dp[M].

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

struct Line {
    long long m, k;
    long long eval(long long x) const {
        return m * x + k;
    }
};

// Check if l2 is redundant between l1 and l3
// intersection(l1, l2) >= intersection(l2, l3)
// (l2.k - l1.k) / (l1.m - l2.m) >= (l3.k - l2.k) / (l2.m - l3.m)
// Cross multiply: (l2.k - l1.k) * (l2.m - l3.m) >= (l3.k - l2.k) * (l1.m - l2.m)
bool check_redundant(const Line& l1, const Line& l2, const Line& l3) {
    __int128 left = (__int128)(l2.k - l1.k) * (l2.m - l3.m);
    __int128 right = (__int128)(l3.k - l2.k) * (l1.m - l2.m);
    return left >= right;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long X;
    if (!(cin >> N >> X)) return 0;

    vector<pair<long long, long long>> items(N);
    for (int i = 0; i < N; ++i) {
        cin >> items[i].first >> items[i].second;
    }

    sort(items.begin(), items.end());

    vector<long long> A_vals = {0};
    vector<long long> C_vals = {0};

    for (int i = 0; i < N; ) {
        int j = i;
        long long sum_c = 0;
        while (j < N && items[j].first == items[i].first) {
            sum_c += items[j].second;
            j++;
        }
        A_vals.push_back(items[i].first);
        C_vals.push_back(sum_c);
        i = j;
    }

    int M = (int)A_vals.size() - 1;

    vector<long long> Sc(M + 1, 0), Sac(M + 1, 0);
    for (int i = 1; i <= M; ++i) {
        Sc[i] = Sc[i - 1] + C_vals[i];
        Sac[i] = Sac[i - 1] + A_vals[i] * C_vals[i];
    }

    vector<long long> dp(M + 1, 0);
    deque<Line> dq;

    auto add_line = [&](long long m, long long k) {
        Line l = {m, k};
        while (dq.size() >= 2 && check_redundant(dq[dq.size() - 2], dq.back(), l)) {
            dq.pop_back();
        }
        dq.push_back(l);
    };

    auto query = [&](long long x) {
        while (dq.size() >= 2 && dq[0].eval(x) >= dq[1].eval(x)) {
            dq.pop_front();
        }
        return dq.front().eval(x);
    };

    // Base line j = 0: m = 0, k = 0
    add_line(0, 0);

    for (int i = 1; i <= M; ++i) {
        long long min_val = query(A_vals[i]);
        dp[i] = min_val + X + A_vals[i] * Sc[i] - Sac[i];
        add_line(-Sc[i], dp[i] + Sac[i]);
    }

    cout << dp[M] << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
