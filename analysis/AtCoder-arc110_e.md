# Problem Analysis: AtCoder-arc110_e — E - Shorten ABC

**Problem ID**: `AtCoder-arc110_e`  
**Contest**: `arc110`  
**Rating / Difficulty**: 2955  
**URL**: https://atcoder.jp/contests/arc110/tasks/arc110_e  
**VJudge Tag**: `[problem:AtCoder-arc110_e]`  
**Category File**: [`../categories/dynamic_programming/three_char_xor_reduction_subsequence_automaton_dp.md`](../categories/dynamic_programming/three_char_xor_reduction_subsequence_automaton_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `Substring DP`  

---

## 1. Problem Statement & Key Idea
Given a string S of length N consisting of 'A', 'B', 'C', an operation replaces two adjacent different characters with the third character. Find the number of distinct strings that can be obtained modulo 10^9+7.

## 2. Core Observation & Invariant
Mapping 'A'->1, 'B'->2, 'C'->3, replacing adjacent x != y yields x XOR y. Any contracted character represents a contiguous substring whose XOR sum is that character. Furthermore, a substring can be reduced to a single character v iff its XOR sum is v and it is not a sequence of all identical characters of length > 1. To count distinct resulting strings uniquely without duplicate derivation paths, use a subsequence automaton DP: greedily jump to the first position where the prefix XOR matches pref[i] XOR v.

## 3. Step-by-Step Algorithm
1. 1. Map string characters to {1, 2, 3} and compute prefix XOR array pref[0..N].
2. 2. Precompute next_pos[xor_val][i]: the earliest index j > i with pref[j] == xor_val.
3. 3. Identify homogeneous suffix properties to handle non-collapsible all-same substrings.
4. 4. Run DP: dp[i] is the number of ways to form valid string prefixes ending at index i.
5. 5. For each i, if the remaining suffix pref[N] XOR pref[i] != 0 and is collapsible, add dp[i] to total answer.
6. 6. Transition to next character v in {1, 2, 3}: dp[next_pos[pref[i] XOR v][i]] += dp[i].
7. 7. Output answer modulo 10^9+7.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

static const int MOD = 1000000007;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;
    string S;
    cin >> S;

    bool all_same = true;
    for (int i = 1; i < N; ++i) {
        if (S[i] != S[0]) {
            all_same = false;
            break;
        }
    }
    if (all_same) {
        cout << 1 << "\n";
        return 0;
    }

    vector<int> a(N);
    for (int i = 0; i < N; ++i) {
        if (S[i] == 'A') a[i] = 1;
        else if (S[i] == 'B') a[i] = 2;
        else if (S[i] == 'C') a[i] = 3;
    }

    vector<int> pref(N + 1, 0);
    for (int i = 0; i < N; ++i) {
        pref[i + 1] = pref[i] ^ a[i];
    }

    vector<vector<int>> next_pos(4, vector<int>(N + 2, -1));
    vector<int> last(4, -1);
    for (int i = N; i >= 0; --i) {
        for (int m = 0; m < 4; ++m) {
            next_pos[m][i] = last[m];
        }
        last[pref[i]] = i;
    }

    vector<bool> suffix_all_same(N + 1, true);
    for (int i = N - 2; i >= 0; --i) {
        if (a[i] != a[i + 1]) {
            suffix_all_same[i] = false;
        } else {
            suffix_all_same[i] = suffix_all_same[i + 1];
        }
    }

    vector<long long> dp(N + 1, 0);
    dp[0] = 1;

    long long ans = 0;

    for (int i = 0; i < N; ++i) {
        if (dp[i] == 0) continue;

        int rem_xor = pref[N] ^ pref[i];
        if (rem_xor != 0) {
            if (!(N - i > 1 && suffix_all_same[i])) {
                ans = (ans + dp[i]) % MOD;
            }
        }

        for (int v = 1; v <= 3; ++v) {
            int nxt = next_pos[pref[i] ^ v][i];
            if (nxt != -1 && nxt < N) {
                dp[nxt] = (dp[nxt] + dp[i]) % MOD;
            }
        }
    }

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
