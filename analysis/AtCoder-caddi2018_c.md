# Problem Analysis: AtCoder-caddi2018_c — E. Negative Doubling

**Problem ID**: `AtCoder-caddi2018_c`  
**Contest**: `caddi2018`  
**Rating / Difficulty**: 2327  
**URL**: https://atcoder.jp/contests/caddi2018/tasks/caddi2018_c  
**VJudge Tag**: `[problem:AtCoder-caddi2018_c]`  
**Category File**: [`../categories/dynamic_programming/sign_partition_monotonic_stack_scaling_dp.md`](../categories/dynamic_programming/sign_partition_monotonic_stack_scaling_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Given array $A$ of length $N$, find the minimum number of operations (multiplying an element by 4 or dividing by 4) to make $A$ non-decreasing, allowing negative values via optimal sign assignment.

## 2. Core Observation & Invariant
In any sorted array, all negative elements (requiring $2c_i + 1$ operations) must precede all positive elements (requiring $2d_i$ operations). For a fixed suffix, the required powers satisfy $d_j = P_j - \min_{k=i}^j P_k$ where $P_k$ is the prefix sum of relative scale adjustments.

## 3. Step-by-Step Algorithm
1. Partition the array into $m$ negative elements and $N - m$ positive elements.
2. Calculate relative scale adjustments $diff_i = \lceil \log_4(A_i / A_{i+1}) \rceil$.
3. Compute the suffix sums of running minimums using a monotonic stack in $O(N)$ time for the positive suffix and reversed negative prefix.
4. Iterate over all $m \in [0, N]$ to find the global minimum in $O(N)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

long long calc_diff(long long x, long long y) {
    if (x <= y) {
        long long s = 0;
        while (x <= y / 4) {
            y /= 4;
            s++;
        }
        return -s;
    } else {
        long long s = 0;
        while (x > y) {
            y *= 4;
            s++;
        }
        return s;
    }
}

vector<long long> compute_costs(int n, const vector<long long>& arr) {
    vector<long long> cost(n + 1, 0);
    if (n <= 1) return cost;

    vector<long long> diff(n - 1);
    for (int i = 0; i < n - 1; ++i) {
        diff[i] = calc_diff(arr[i], arr[i + 1]);
    }

    vector<long long> pref(n, 0);
    for (int i = 0; i < n - 1; ++i) {
        pref[i + 1] = pref[i] + diff[i];
    }

    vector<long long> suf_pref(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
        suf_pref[i] = suf_pref[i + 1] + pref[i];
    }

    vector<pair<long long, long long>> st;
    long long stack_sum = 0;

    for (int i = n - 1; i >= 0; --i) {
        long long cnt = 1;
        long long val = pref[i];
        while (!st.empty() && st.back().first >= val) {
            long long v = st.back().first;
            long long c = st.back().second;
            st.pop_back();
            stack_sum -= v * c;
            cnt += c;
        }
        st.push_back({val, cnt});
        stack_sum += val * cnt;
        cost[i] = suf_pref[i] - stack_sum;
    }

    return cost;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> pos_cost = compute_costs(n, a);

    vector<long long> a_rev = a;
    reverse(a_rev.begin(), a_rev.end());
    vector<long long> neg_rev_cost = compute_costs(n, a_rev);

    long long ans = -1;

    for (int m = 0; m <= n; ++m) {
        long long c_neg = (m > 0 ? m + 2 * neg_rev_cost[n - m] : 0);
        long long c_pos = (m < n ? 2 * pos_cost[m] : 0);
        long long cur = c_neg + c_pos;
        if (ans == -1 || cur < ans) {
            ans = cur;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
