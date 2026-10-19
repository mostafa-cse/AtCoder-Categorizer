# Problem Analysis: AtCoder-arc114_d — D - Moving Pieces on Line

**Problem ID**: `AtCoder-arc114_d`  
**Contest**: `arc114`  
**Rating / Difficulty**: 2723  
**URL**: https://atcoder.jp/contests/arc114/tasks/arc114_d  
**VJudge Tag**: `[problem:AtCoder-arc114_d]`  
**Category File**: [`../categories/dynamic_programming_dp/moving_pieces_slope_trick.md`](../categories/dynamic_programming_dp/moving_pieces_slope_trick.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `More Tricks`  
- **Topic (Skill)**: `Slope Trick`  

---

## 1. Problem Statement & Key Idea
Given N pieces at positions a_1..a_N on an infinite line graph with all edges initially red. Moving a piece flips the color of traversed edges. We want to achieve a target pattern of blue intervals [t_1, t_2], ..., [t_{K-1}, t_K] with minimum total piece movements.

## 2. Core Observation & Invariant
The total movement cost depends only on the final piece positions b_1 <= b_2 <= ... <= b_N: cost = sum |a_i - b_i|. In the multiset union {a_1..a_N} U {b_1..b_N}, the odd-multiplicity vertices must match {t_1..t_K}. Thus, the multiset of odd-multiplicity elements of b is uniquely determined as C = odd(a) XOR {t_1..t_K}. The remaining N - |C| elements of b can appear with even multiplicity, which corresponds to pairing up the remaining pieces of a to move to the same point at cost a_{v} - a_{u}. We sort a and C and use DP: dp[j][f] is the minimum cost after matching j elements of C, where f in {0, 1} indicates whether an element of a is currently waiting to close a pair.

## 3. Step-by-Step Algorithm
1. 1. Sort array A and array T.
2. 2. Compute frequency counts of all values in A and T to find the set C of values with odd total multiplicity.
3. 3. Let l = |C|. If l > N or (N - l) % 2 != 0, return -1.
4. 4. Initialize DP table dp[j][f] = INF for 0 <= j <= l and f in {0, 1}, with dp[0][0] = 0.
5. 5. For each element a in sorted A, update rolling DP table:
6.    - Match a with C[j] (if j < l): transition to (j + 1, f) with cost +|a - C[j]|.
7.    - Pair a: if f == 0, transition to (j, 1) with cost -a; if f == 1, transition to (j, 0) with cost +a.
8. 6. Output dp[l][0] if < INF, else -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * |C|)`
- **Space Complexity**: `O(|C|)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

const long long INF = 1e18;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    if (!(cin >> N >> K)) return 0;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    vector<long long> T(K);
    for (int i = 0; i < K; ++i) {
        cin >> T[i];
    }

    sort(A.begin(), A.end());
    sort(T.begin(), T.end());

    map<long long, int> cnt;
    for (long long x : A) cnt[x]++;
    for (long long x : T) cnt[x]++;

    vector<long long> C;
    for (const auto& kv : cnt) {
        if (kv.second % 2 == 1) {
            C.push_back(kv.first);
        }
    }

    int l = C.size();
    if (l > N || (N - l) % 2 != 0) {
        cout << -1 << "\n";
        return 0;
    }

    vector<vector<long long>> dp(l + 1, vector<long long>(2, INF));
    dp[0][0] = 0;

    for (int i = 0; i < N; ++i) {
        long long a = A[i];
        vector<vector<long long>> ndp(l + 1, vector<long long>(2, INF));
        for (int j = 0; j <= l; ++j) {
            for (int f = 0; f < 2; ++f) {
                long long val = dp[j][f];
                if (val >= INF) continue;

                // Match with C[j]
                if (j < l) {
                    long long cost = abs(a - C[j]);
                    if (val + cost < ndp[j + 1][f]) {
                        ndp[j + 1][f] = val + cost;
                    }
                }

                // Pair up
                if (f == 0) {
                    if (val - a < ndp[j][1]) {
                        ndp[j][1] = val - a;
                    }
                } else {
                    if (val + a < ndp[j][0]) {
                        ndp[j][0] = val + a;
                    }
                }
            }
        }
        dp = move(ndp);
    }

    long long ans = dp[l][0];
    if (ans >= INF) {
        cout << -1 << "\n";
    } else {
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
