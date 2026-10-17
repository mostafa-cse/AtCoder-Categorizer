# Problem Analysis: AtCoder-arc192_c — Range Sums 2

**Problem ID**: `AtCoder-arc192_c`  
**Contest**: `arc192`  
**Rating / Difficulty**: 2158  
**URL**: https://atcoder.jp/contests/arc192/tasks/arc192_c  
**VJudge Tag**: `[problem:AtCoder-arc192_c]`  
**Category File**: [`../categories/miscellaneous/interactive_range_sums_extremal_reconstruction.md`](../categories/miscellaneous/interactive_range_sums_extremal_reconstruction.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Interactive Problems`  
- **Topic (Skill)**: `Interactive Problems`  

---

## 1. Problem Statement & Key Idea
Interactive reconstruction of a permutation P and positive array A from at most 2N range sum queries sum_{i=min(P_s, P_t)}^{max(P_s, P_t)} A_i with P_1 < P_2 guaranteed.

## 2. Core Observation & Invariant
Because all A_i > 0, querying (1, i) for all i >= 2 identifies an extreme endpoint m with maximal range sum (so P_m = 1 or P_m = N). Assuming P_m = 1, querying (m, i) sorts elements along the line, yielding P and differences A_3..A_N. One boundary query finds A_1 and A_2. If P_1 > P_2, invert P_i <- N + 1 - P_i and reverse A.

## 3. Step-by-Step Algorithm
1. Query (1, i) for i = 2..N. Let m be the index with the maximal returned sum. Assume P_m = 1.
2. Query (m, i) for all i != m (reusing query (1, m) from step 1).
3. Sort remaining vertices by their (m, i) responses to assign P_{x_1} = 2, ..., P_{x_{N-1}} = N.
4. Compute adjacent differences to find A_3..A_N.
5. Query (x_1, x_{N-1}) to get total sum minus A_1, determining A_1 and A_2.
6. If P_1 > P_2, replace P_i with N + 1 - P_i and reverse A. Output answer with !.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N) with <= 2N - 2 queries`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

long long query(int s, int t) {
    cout << "? " << s << " " << t << "\n";
    cout.flush();
    long long ret;
    cin >> ret;
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    pair<long long, int> mx = {-1, -1};
    vector<long long> from1(n + 1, 0);

    for (int i = 2; i <= n; ++i) {
        long long val = query(1, i);
        from1[i] = val;
        mx = max(mx, {val, i});
    }

    int m = mx.second;
    vector<pair<long long, int>> resps;
    for (int i = 1; i <= n; ++i) {
        if (i == m) continue;
        long long val;
        if (i == 1) {
            val = from1[m];
        } else {
            val = query(m, i);
        }
        resps.push_back({val, i});
    }

    sort(resps.begin(), resps.end());

    vector<int> P(n + 1, 0);
    vector<long long> A(n + 1, 0);

    P[m] = 1;
    for (int i = 0; i < n - 1; ++i) {
        P[resps[i].second] = i + 2;
    }

    for (int i = 1; i < n - 1; ++i) {
        A[i + 2] = resps[i].first - resps[i - 1].first;
    }

    long long q_ends = query(resps[0].second, resps.back().second);
    long long total = resps.back().first;
    A[1] = total - q_ends;

    long long sum_known = 0;
    for (int i = 1; i <= n; ++i) {
        if (i != 2) sum_known += A[i];
    }
    A[2] = total - sum_known;

    if (P[1] > P[2]) {
        for (int i = 1; i <= n; ++i) {
            P[i] = n + 1 - P[i];
        }
        reverse(A.begin() + 1, A.end());
    }

    cout << "!";
    for (int i = 1; i <= n; ++i) cout << " " << P[i];
    for (int i = 1; i <= n; ++i) cout << " " << A[i];
    cout << "\n";
    cout.flush();

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
