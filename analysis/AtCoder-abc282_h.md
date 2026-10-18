# Problem Analysis: AtCoder-abc282_h — Ex - Min + Sum

**Problem ID**: `AtCoder-abc282_h`  
**Contest**: `abc282`  
**Rating / Difficulty**: 2621  
**URL**: https://atcoder.jp/contests/abc282/tasks/abc282_h  
**VJudge Tag**: `[problem:AtCoder-abc282_h]`  
**Category File**: [`../categories/data_structures_ds/min_plus_sum_cartesian_tree.md`](../categories/data_structures_ds/min_plus_sum_cartesian_tree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `More Tree Data Structures`  
- **Topic (Skill)**: `Cartesian Tree`  

---

## 1. Problem Statement & Key Idea
Given an array A of length N and bound S, count pairs (l, r) with 1 <= l <= r <= N such that min_{l <= k <= r} A_k + sum_{k=l}^r A_k <= S.

## 2. Core Observation & Invariant
Decompose the array using Cartesian Tree / RMQ Divide and Conquer. For a subarray [L, R] with minimum at m, any pair spanning m satisfies sum_{k=l}^r A_k <= S - A_m. We iterate over the smaller side of the split (small-to-large) and binary search on prefix sums on the larger side, achieving O(N log^2 N) overall time.

## 3. Step-by-Step Algorithm
1. Build a Sparse Table for O(1) range minimum queries.
2. Recursive function solve(L, R): find minimum position m in [L, R].
3. If m - L <= R - m: iterate l in [L, m], binary search the largest r in [m, R] such that P_r - P_{l-1} <= S - A_m, and add (r - m + 1).
4. Else: iterate r in [m, R], binary search the smallest l in [L, m] such that P_r - P_{l-1} <= S - A_m, and add (m - l + 1).
5. Recurse on [L, m-1] and [m+1, R].

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log^2 N)`
- **Space Complexity**: `O(N \log N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

using ll = long long;

const int MAXN = 200005;
const int LOGN = 18;

ll A[MAXN], B[MAXN], P[MAXN];
int st[LOGN][MAXN];
int lg2[MAXN];

int query_min_idx(int L, int R) {
    int k = lg2[R - L + 1];
    int idx1 = st[k][L];
    int idx2 = st[k][R - (1 << k) + 1];
    return (A[idx1] <= A[idx2]) ? idx1 : idx2;
}

ll S_val;
ll total_ans = 0;

void rec(int L, int R) {
    if (L > R) return;
    int m = query_min_idx(L, R);
    ll rem = S_val - A[m];

    if (rem >= 0) {
        if (m - L <= R - m) {
            // Left side is smaller or equal
            for (int l = L; l <= m; ++l) {
                ll target = P[l - 1] + rem;
                // find upper_bound in P[m ... R]
                auto it = upper_bound(P + m, P + R + 1, target);
                int count = (int)(it - (P + m));
                total_ans += count;
            }
        } else {
            // Right side is smaller
            for (int r = m; r <= R; ++r) {
                ll target = P[r] - rem;
                // find lower_bound in P[L-1 ... m-1]
                auto it = lower_bound(P + (L - 1), P + m, target);
                int count = (int)((P + m) - it);
                total_ans += count;
            }
        }
    }

    rec(L, m - 1);
    rec(m + 1, R);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N >> S_val)) return 0;

    lg2[1] = 0;
    for (int i = 2; i <= N; ++i) lg2[i] = lg2[i / 2] + 1;

    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
        st[0][i] = i;
    }
    P[0] = 0;
    for (int i = 1; i <= N; ++i) {
        cin >> B[i];
        P[i] = P[i - 1] + B[i];
    }

    for (int k = 1; (1 << k) <= N; ++k) {
        for (int i = 1; i + (1 << k) - 1 <= N; ++i) {
            int idx1 = st[k - 1][i];
            int idx2 = st[k - 1][i + (1 << (k - 1))];
            st[k][i] = (A[idx1] <= A[idx2]) ? idx1 : idx2;
        }
    }

    rec(1, N);

    cout << total_ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
