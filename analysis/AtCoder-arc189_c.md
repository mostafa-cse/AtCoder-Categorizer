# Problem Analysis: AtCoder-arc189_c — Balls and Boxes

**Problem ID**: `AtCoder-arc189_c`  
**Contest**: `arc189`  
**Rating / Difficulty**: 2239  
**URL**: https://atcoder.jp/contests/arc189/tasks/arc189_c  
**VJudge Tag**: `[problem:AtCoder-arc189_c]`  
**Category File**: [`../categories/miscellaneous/permutations_cycles_balls_and_boxes_lis.md`](../categories/miscellaneous/permutations_cycles_balls_and_boxes_lis.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Permutations`  
- **Topic (Skill)**: `Permutations and Permutation Cycles`  

---

## 1. Problem Statement & Key Idea
Move all red and blue balls from N boxes to target box X using permutations P and Q with the minimum number of box operations.

## 2. Core Observation & Invariant
Each permutation P and Q decomposes into disjoint directed cycles. A ball can reach box X iff it starts on the cycle containing X; otherwise return -1. Moving the furthest ball to X along a cycle naturally sweeps all intermediate balls to X. Thus, red balls require a sequence of operations A along cycle C_P, and blue balls require sequence B along cycle C_Q. Any valid sequence of operations contains both A and B as subsequences. Finding the shortest common supersequence of two sequences of distinct elements reduces to |A| + |B| - LCS(A, B), which is computed via Longest Increasing Subsequence (LIS) in O(N log N).

## 3. Step-by-Step Algorithm
1. 1. Trace the cycle containing X backwards in P (to find path to X) and in Q.
2. 2. Verify that all boxes with A_i > 0 belong to cycle C_P and B_i > 0 belong to C_Q; if not, output -1.
3. 3. Identify the furthest red ball and blue ball along the cycles to form required sequences seqP and seqQ.
4. 4. If seqP is empty, output |seqQ|; if seqQ is empty, output |seqP|; if both empty, output 0.
5. 5. Map elements of seqP to their indices 0, 1, ..., |seqP|-1, map matching elements of seqQ, and compute LIS of mappedQ.
6. 6. Output |seqP| + |seqQ| - LIS.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, X;
    if (!(cin >> N >> X)) return 0;

    vector<int> A(N + 1), B(N + 1);
    for (int i = 1; i <= N; ++i) cin >> A[i];
    for (int i = 1; i <= N; ++i) cin >> B[i];

    vector<int> P(N + 1), Q(N + 1);
    for (int i = 1; i <= N; ++i) cin >> P[i];
    for (int i = 1; i <= N; ++i) cin >> Q[i];

    // Build cycle for P containing X
    // In G_P, edge is i -> P_i
    // We want the reverse: from who goes to X?
    // revP[P_i] = i
    vector<int> revP(N + 1), revQ(N + 1);
    for (int i = 1; i <= N; ++i) {
        revP[P[i]] = i;
        revQ[Q[i]] = i;
    }

    // Traverse cycle backwards from X
    vector<int> cycleP;
    int curr = revP[X];
    while (curr != X) {
        cycleP.push_back(curr);
        curr = revP[curr];
    }
    // cycleP has elements in reverse order of reaching X:
    // the one closest to X is cycleP[0] (since cycleP[0] -> X)
    // the one furthest is cycleP.back()

    vector<int> cycleQ;
    curr = revQ[X];
    while (curr != X) {
        cycleQ.push_back(curr);
        curr = revQ[curr];
    }

    vector<bool> inCycleP(N + 1, false), inCycleQ(N + 1, false);
    inCycleP[X] = true;
    for (int v : cycleP) inCycleP[v] = true;
    inCycleQ[X] = true;
    for (int v : cycleQ) inCycleQ[v] = true;

    // Check if any ball is outside the cycle
    for (int i = 1; i <= N; ++i) {
        if (A[i] > 0 && !inCycleP[i]) {
            cout << -1 << "\n";
            return 0;
        }
        if (B[i] > 0 && !inCycleQ[i]) {
            cout << -1 << "\n";
            return 0;
        }
    }

    // Find furthest red ball
    // cycleP[0] is distance 1 to X, cycleP[k] is distance k+1 to X
    int maxDistP = -1;
    for (int i = 0; i < (int)cycleP.size(); ++i) {
        if (A[cycleP[i]] > 0) {
            maxDistP = max(maxDistP, i);
        }
    }

    int maxDistQ = -1;
    for (int i = 0; i < (int)cycleQ.size(); ++i) {
        if (B[cycleQ[i]] > 0) {
            maxDistQ = max(maxDistQ, i);
        }
    }

    if (maxDistP == -1 && maxDistQ == -1) {
        cout << 0 << "\n";
        return 0;
    }

    // Sequence of operations for P:
    // from cycleP[maxDistP] down to cycleP[0]
    vector<int> seqP;
    for (int i = maxDistP; i >= 0; --i) {
        seqP.push_back(cycleP[i]);
    }

    vector<int> seqQ;
    for (int i = maxDistQ; i >= 0; --i) {
        seqQ.push_back(cycleQ[i]);
    }

    if (seqP.empty()) {
        cout << seqQ.size() << "\n";
        return 0;
    }
    if (seqQ.empty()) {
        cout << seqP.size() << "\n";
        return 0;
    }

    // Now LCS of seqP and seqQ
    // Map each element in seqP to its index: 0, 1, ..., len-1
    vector<int> posP(N + 1, -1);
    for (int i = 0; i < (int)seqP.size(); ++i) {
        posP[seqP[i]] = i;
    }

    vector<int> mappedQ;
    for (int v : seqQ) {
        if (posP[v] != -1) {
            mappedQ.push_back(posP[v]);
        }
    }

    // LIS of mappedQ
    vector<int> lis;
    for (int val : mappedQ) {
        auto it = lower_bound(lis.begin(), lis.end(), val);
        if (it == lis.end()) {
            lis.push_back(val);
        } else {
            *it = val;
        }
    }

    int lcs = lis.size();
    long long ans = (long long)seqP.size() + (long long)seqQ.size() - lcs;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
