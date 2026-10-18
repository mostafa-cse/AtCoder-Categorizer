# Problem Analysis: AtCoder-arc223_e — E. Yin-Yang Two Bits Insertion

**Problem ID**: `AtCoder-arc223_e`  
**Contest**: `arc223`  
**Rating / Difficulty**: 2572  
**URL**: https://atcoder.jp/contests/arc223/tasks/arc223_e  
**VJudge Tag**: `[problem:AtCoder-arc223_e]`  
**Category File**: [`../categories/basics/yin_yang_two_bits_insertion.md`](../categories/basics/yin_yang_two_bits_insertion.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Given two binary strings S and T, determine if S can be transformed into T by repeatedly inserting two adjacent identical bits (00 or 11), and construct the minimum operations.

## 2. Core Observation & Invariant
Inserting identical adjacent bits 00 or 11 preserves the adjacent XOR parity structure of the string. By analyzing the run-length parity of adjacent XOR differences, the reachability condition reduces to a constructive matching between run-lengths of S and T.

## 3. Step-by-Step Algorithm
1. Compute the adjacent-XOR difference sequence for both S and T.
2. Decompose into blocks of alternating parity.
3. Check necessary and sufficient invariants: total parity count and prefix reachability.
4. If reachable, construct the step-by-step insertions greedily.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| + |T|)`
- **Space Complexity**: `O(|S| + |T|)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve_tc() {
    int N, M;
    if (!(cin >> N >> M)) return;
    vector<int> A(N), B(M);
    for (int i = 0; i < N; i++) cin >> A[i];
    for (int i = 0; i < M; i++) cin >> B[i];

    if (A[0] != B[0] || A.back() != B.back()) {
        cout << "No\n";
        return;
    }

    vector<int> A_diff(N - 1), B_diff(M - 1);
    int zero_a = 0, zero_b = 0;
    for (int i = 0; i < N - 1; i++) {
        A_diff[i] = (A[i] != A[i + 1] ? 1 : 0);
        if (A_diff[i] == 0) zero_a++;
    }
    for (int i = 0; i < M - 1; i++) {
        B_diff[i] = (B[i] != B[i + 1] ? 1 : 0);
        if (B_diff[i] == 0) zero_b++;
    }

    if (zero_a != zero_b) {
        cout << "No\n";
        return;
    }

    // Split at 0s to get counts of 1s
    vector<int> a_segs, b_segs;
    int cur = 0;
    for (int x : A_diff) {
        if (x == 0) {
            a_segs.push_back(cur);
            cur = 0;
        } else {
            cur++;
        }
    }
    a_segs.push_back(cur);

    cur = 0;
    for (int x : B_diff) {
        if (x == 0) {
            b_segs.push_back(cur);
            cur = 0;
        } else {
            cur++;
        }
    }
    b_segs.push_back(cur);

    int K = a_segs.size(); // number of segments = zero_a + 1

    // dp[x]: whether possible with operation 1 applied x times at boundary before current segment
    // x in {0, 1, 2}
    vector<bool> dp(3, false);
    dp[0] = true;

    for (int i = 0; i < K; i++) {
        vector<bool> next_dp(3, false);
        int a_i = a_segs[i];
        int b_i = b_segs[i];

        for (int x_prev = 0; x_prev < 3; x_prev++) {
            if (!dp[x_prev]) continue;
            int max_x_cur = (i == K - 1 ? 0 : 2);
            for (int x_cur = 0; x_cur <= max_x_cur; x_cur++) {
                int base = a_i + x_prev + x_cur;
                if (base <= b_i && (b_i - base) % 2 == 0) {
                    int diff = b_i - base;
                    if (diff == 0) {
                        next_dp[x_cur] = true;
                    } else {
                        // diff > 0 requires at least one 1 to perform +2 operation
                        if (a_i > 0 || x_prev > 0 || x_cur > 0) {
                            next_dp[x_cur] = true;
                        }
                    }
                }
            }
        }
        dp = next_dp;
    }

    if (dp[0]) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (cin >> T) {
        while (T--) solve_tc();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
