# Problem Analysis: AtCoder-agc045_b — B - 01 Unbalanced

**Problem ID**: `AtCoder-agc045_b`  
**Contest**: `agc045`  
**Rating / Difficulty**: 2873  
**URL**: https://atcoder.jp/contests/agc045/tasks/agc045_b  
**VJudge Tag**: `[problem:AtCoder-agc045_b]`  
**Category File**: [`../categories/basics/zero_one_unbalanced_substring_prefix_balance_range.md`](../categories/basics/zero_one_unbalanced_substring_prefix_balance_range.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Given string S of 0, 1, ? of length <= 10^6, replace each ? with 0 or 1 to minimize the maximum absolute difference between the count of 0s and 1s in any substring.

## 2. Core Observation & Invariant
Mapping 0 -> -1 and 1 -> +1, the unbalancedness is max P - min P where P are prefix sums. Let Z be the minimum possible max P (achieved by setting all ? to -1). For a bound M = max P >= Z, the best minimum prefix sum f(M) is found greedily by a backward-forward pass. Furthermore, M - f(M) is convex in steps of 2, so the global minimum occurs at either M = Z or M = Z + 1.

## 3. Step-by-Step Algorithm
1. 1. Set all '?' to -1 and compute prefix sums to find Z = max P.
2. 2. Function calc_f(M): backward pass computes upper bounds R_k on P_k <= M; forward pass greedily sets '?' to +1 whenever P_{k-1} + 1 <= R_k, else -1, and returns min P.
3. 3. Compute ans1 = Z - calc_f(Z) and ans2 = (Z + 1) - calc_f(Z + 1).
4. 4. Output min(ans1, ans2).

## 4. Complexity Analysis
- **Time Complexity**: `O(|S|)`
- **Space Complexity**: `O(|S|)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int calc_f(const string& S, int N, int M) {
    vector<int> R(N + 1);
    R[N] = M;
    for (int k = N; k >= 1; --k) {
        if (S[k - 1] == '1') {
            R[k - 1] = min(M, R[k] - 1);
        } else { // '0' or '?'
            R[k - 1] = min(M, R[k] + 1);
        }
    }

    int cur_P = 0;
    int min_P = 0;
    for (int k = 1; k <= N; ++k) {
        if (S[k - 1] == '1') {
            cur_P++;
        } else if (S[k - 1] == '0') {
            cur_P--;
        } else { // '?'
            if (cur_P + 1 <= R[k]) {
                cur_P++;
            } else {
                cur_P--;
            }
        }
        min_P = min(min_P, cur_P);
    }
    return min_P;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string S;
    if (!(cin >> S)) return 0;
    int N = S.length();

    int cur_P = 0;
    int Z = 0;
    for (int i = 0; i < N; ++i) {
        if (S[i] == '1') cur_P++;
        else cur_P--; // '0' or '?'
        Z = max(Z, cur_P);
    }

    int ans1 = Z - calc_f(S, N, Z);
    int ans2 = (Z + 1) - calc_f(S, N, Z + 1);

    cout << min(ans1, ans2) << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
