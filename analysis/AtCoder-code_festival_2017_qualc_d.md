# Problem Analysis: AtCoder-code_festival_2017_qualc_d — Yet Another Palindrome Partitioning

**Problem ID**: `AtCoder-code_festival_2017_qualc_d`  
**Contest**: `code_festival_2017_qualc`  
**Rating / Difficulty**: 2132  
**URL**: https://atcoder.jp/contests/code_festival_2017_qualc/tasks/code_festival_2017_qualc_d  
**VJudge Tag**: `[problem:AtCoder-code_festival_2017_qualc_d]`  
**Category File**: [`../categories/dynamic_programming/parity_bitmask_prefix_xor_palindrome_partitions.md`](../categories/dynamic_programming/parity_bitmask_prefix_xor_palindrome_partitions.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
Given a string S, partition it into the minimum number of substrings such that each substring can be rearranged into a palindrome.

**Key Insight**: A substring can be rearranged into a palindrome iff at most one character appears an odd number of times. Let pref[i] be the 26-bit bitmask where the c-th bit is the parity of character c in prefix S[1..i]. A substring S[j..i] can form a palindrome iff popcount(pref[i] ^ pref[j-1]) <= 1. Maintaining min_dp[mask] as the minimum partitions for any prefix with parity mask, each step checks mask itself and the 26 masks differing by 1 bit in O(26) time.

## 2. Core Observation & Invariant
Palindrome condition translates to Hamming distance <= 1 on 26-bit prefix XOR parity masks.

## 3. Step-by-Step Algorithm
1. Initialize min_dp[mask] = INF for all mask in [0, 2^26 - 1], with min_dp[0] = 0.
2. cur_mask = 0.
3. For each character c in S:
4.   cur_mask ^= (1 << (c - 'a')).
5.   cur_ans = min_dp[cur_mask] + 1.
6.   For bit b from 0 to 25:
7.     cur_ans = min(cur_ans, min_dp[cur_mask ^ (1 << b)] + 1).
8.   min_dp[cur_mask] = min(min_dp[cur_mask], cur_ans).
9. Output cur_ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(26 * |S|)`
- **Space Complexity**: `O(2^{26})`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Bitmask parity prefix XOR and O(26) shortest path transitions for palindromic substring partitioning.
- **Reusable Pattern**: Substrings rearrangeable into palindromes characterized by popcount(prefix_XOR_i ^ prefix_XOR_j) <= 1.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.size();
    int full = 1 << 26;
    vector<int> min_dp(full, 1e9);
    min_dp[0] = 0;

    int cur_mask = 0;
    int cur_ans = 0;

    for (char c : s) {
        cur_mask ^= (1 << (c - 'a'));
        int best = min_dp[cur_mask] + 1;
        for (int i = 0; i < 26; ++i) {
            best = min(best, min_dp[cur_mask ^ (1 << i)] + 1);
        }
        cur_ans = best;
        min_dp[cur_mask] = min(min_dp[cur_mask], cur_ans);
    }

    cout << cur_ans << "\n";
    return 0;
}
```
