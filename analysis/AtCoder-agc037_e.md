# Problem Analysis: AtCoder-agc037_e — Reversing and Concatenating

**Problem ID**: `AtCoder-agc037_e`  
**Contest**: `agc037`  
**Rating / Difficulty**: 2667  
**URL**: https://atcoder.jp/contests/agc037/tasks/agc037_e  
**VJudge Tag**: `[problem:AtCoder-agc037_e]`  
**Category File**: [`../categories/basics/reversing_and_concatenating_string_greedy.md`](../categories/basics/reversing_and_concatenating_string_greedy.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Given string S of length N, an operation replaces S with a length-N substring of S + S^R. Find the lexicographically smallest string after K operations. The optimal strategy identifies the minimal character c_min, uses the first operation to create the longest contiguous run of c_min at the suffix, and each subsequent operation doubles the length of this run by reversal and concatenation, rapidly saturating the string within log2(N) steps.

## 2. Core Observation & Invariant
In S + S^R, any substring of length N can be extracted. The best first move maximizes the contiguous block of minimum characters c_min ending at the suffix. On subsequent operations, appending S^R places a reversed run of c_min adjacent to the existing run, doubling the consecutive sequence of c_min with each operation (L -> 2L). After at most ceil(log2 N) operations, the entire string becomes all c_min.

## 3. Step-by-Step Algorithm
1. 1. Find minimal character c = min(S).
2. 2. In T = S + S^R, inspect all substrings of length N that maximize the trailing run of c.
3. 3. Among those with maximal trailing run of c, pick the lexicographically smallest.
4. 4. For the remaining K - 1 steps, repeatedly double the trailing run of c using the reversal-concatenation invariant, truncating to length N.
5. 5. Print the resulting string.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long K;
    if (!(cin >> N >> K)) return 0;

    string S;
    cin >> S;

    string S_rev = S;
    reverse(S_rev.begin(), S_rev.end());
    string U = S + S_rev;

    if (K == 1) {
        string best = U.substr(0, N);
        for (int i = 1; i <= N; ++i) {
            string cand = U.substr(i, N);
            if (cand < best) {
                best = cand;
            }
        }
        cout << best << "\n";
        return 0;
    }

    char c_min = 'z';
    for (char c : S) {
        if (c < c_min) c_min = c;
    }

    string best = "";
    bool has_best = false;

    for (int r = N - 1; r < 2 * N; ++r) {
        if (U[r] == c_min) {
            int L = 0;
            while (r - L >= 0 && U[r - L] == c_min) {
                L++;
            }

            string cand = "";
            if (K - 1 >= 20 || (1LL * L * (1LL << (K - 1)) >= N)) {
                cand = string(N, c_min);
            } else {
                long long M = 1LL * L * (1LL << (K - 1));
                cand.reserve(N);
                cand.append(M, c_min);

                // rest is U[r - N + 1 ... r + 1 - L] reversed
                int start = r - N + 1;
                int end = r - L; // inclusive
                for (int idx = end; idx >= start && (int)cand.size() < N; --idx) {
                    cand.push_back(U[idx]);
                }
            }

            if (!has_best || cand < best) {
                best = cand;
                has_best = true;
            }
        }
    }

    cout << best << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
