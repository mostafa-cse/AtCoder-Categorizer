# Problem Analysis: AtCoder-typical90_f — Smallest Subsequence

**Problem ID**: `AtCoder-typical90_f`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 006)  
**Rating / Difficulty**: 1500 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_f  
**VJudge Tag**: `[problem:AtCoder-typical90_f]`  
**Category File**: [`../categories/strings/lexicographically_smallest_subsequence.md`](../categories/strings/lexicographically_smallest_subsequence.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Greedy on Strings`  
- **Topic (Skill)**: `Next-Occurrence Array / Lexicographically Smallest Subsequence`  

---

## 1. Problem Statement & Key Idea
Given string S of length N, find the lexicographically smallest subsequence of length K.

**Core Idea**: To minimize lexicographically, greedily choose the smallest possible character from left to right.

## 2. Core Observation & Invariant
A choice of character c at index pos is valid iff the remaining suffix has length >= remaining positions needed (N - pos >= K - step). Next-occurrence array enables O(26) character lookup.

## 3. Step-by-Step Algorithm
1. Precompute next_pos[i][c]: earliest index >= i where char c occurs.
2. cur = 0.
3. For step from 1 to K:
   - Loop char c from 'a' to 'z':
     - pos = next_pos[cur][c]
     - if N - pos >= K - step: append c, cur = pos + 1, break.

## 4. Complexity Analysis
Time: O(26 * N + 26 * K), Space: O(26 * N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    string s;
    if (!(cin >> n >> k >> s)) return 0;

    // next_pos[i][c]: earliest index >= i where character c occurs
    vector<vector<int>> next_pos(n + 1, vector<int>(26, n));
    for (int i = n - 1; i >= 0; --i) {
        for (int c = 0; c < 26; ++c) {
            next_pos[i][c] = next_pos[i + 1][c];
        }
        next_pos[i][s[i] - 'a'] = i;
    }

    string ans = "";
    int cur = 0;
    for (int step = 1; step <= k; ++step) {
        int rem_needed = k - step;
        for (int c = 0; c < 26; ++c) {
            int pos = next_pos[cur][c];
            if (n - pos >= rem_needed + 1) {
                ans.push_back((char)('a' + c));
                cur = pos + 1;
                break;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Next-occurrence lookup with greedy lookahead verification.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Next-character transition tables on strings and greedy lexicographical construction under length constraints.
- **Reusable Pattern**: `Next-Occurrence Array Greedy Subsequence.`

---
Back to [Next-Occurrence Array / Lexicographically Smallest Subsequence](../categories/strings/lexicographically_smallest_subsequence.md) | [Categories Directory](../categories/README.md)