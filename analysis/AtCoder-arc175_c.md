# Problem Analysis: AtCoder-arc175_c — Jumping Through Intervals

**Problem ID**: `AtCoder-arc175_c`  
**Contest**: `arc175`  
**Rating / Difficulty**: 2116  
**URL**: https://atcoder.jp/contests/arc175/tasks/arc175_c  
**VJudge Tag**: `[problem:AtCoder-arc175_c]`  
**Category File**: [`../categories/basics/backward_interval_clamping_greedy.md`](../categories/basics/backward_interval_clamping_greedy.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Given N intervals [L_i, R_i], choose A_i in [L_i, R_i] to minimize sum_{i=1}^{N-1} |A_i - A_{i+1}|. If multiple solutions exist, find the lexicographically smallest sequence A.

**Key Insight**: Backward pass calculates the optimal reachable interval [optL_i, optR_i] for each A_i. If [L_i, R_i] overlaps with [optL_{i+1}, optR_{i+1}], the intersection achieves zero additional transition cost. If it lies completely to the left, A_i = R_i; if to the right, A_i = L_i. A subsequent forward pass greedily selects the minimum valid A_i within [optL_i, optR_i] that matches the previous chosen value A_{i-1} as closely as possible, ensuring lexicographical minimality.

## 2. Core Observation & Invariant
Backward interval projection identifies the optimal continuous locus of points; forward greedy clamping resolves lexicographical tie-breaking.

## 3. Step-by-Step Algorithm
1. Backward sweep from N-1 down to 0:
2.   If [L_i, R_i] is disjoint to right of opt[i+1], opt[i] = [L_i, L_i].
3.   If disjoint to left, opt[i] = [R_i, R_i].
4.   Otherwise, opt[i] = [max(L_i, optL_{i+1}), min(R_i, optR_{i+1})].
5. Forward sweep from 0 to N-1:
6.   A[0] = optL[0].
7.   For i from 1 to N-1: clamp A[i-1] into [optL_i, optR_i].
8. Output sequence A.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Two-pass interval projection and lexicographical greedy forward clamping.
- **Reusable Pattern**: Minimizing transition distance between constrained intervals via backward reachability projection followed by forward tie-breaking.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> L(n), R(n);
    for (int i = 0; i < n; ++i) {
        cin >> L[i] >> R[i];
    }

    vector<long long> optL(n), optR(n);
    optL[n - 1] = L[n - 1];
    optR[n - 1] = R[n - 1];

    for (int i = n - 2; i >= 0; --i) {
        if (R[i] < optL[i + 1]) {
            optL[i] = optR[i] = R[i];
        } else if (L[i] > optR[i + 1]) {
            optL[i] = optR[i] = L[i];
        } else {
            optL[i] = max(L[i], optL[i + 1]);
            optR[i] = min(R[i], optR[i + 1]);
        }
    }

    vector<long long> A(n);
    A[0] = optL[0];

    for (int i = 1; i < n; ++i) {
        if (A[i - 1] < optL[i]) {
            A[i] = optL[i];
        } else if (A[i - 1] > optR[i]) {
            A[i] = optR[i];
        } else {
            A[i] = A[i - 1];
        }
    }

    for (int i = 0; i < n; ++i) {
        cout << A[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
