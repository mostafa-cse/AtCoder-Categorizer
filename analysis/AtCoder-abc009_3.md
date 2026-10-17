# Problem Analysis: AtCoder-abc009_3 — 辞書式順序ふたたび

**Problem ID**: `AtCoder-abc009_3`  
**Contest**: `abc009`  
**Rating / Difficulty**: 1915  
**URL**: https://atcoder.jp/contests/abc009/tasks/abc009_3  
**VJudge Tag**: `[problem:AtCoder-abc009_3]`  
**Category File**: [`../categories/basics/greedy_lexicographical_edit_budget_feasibility.md`](../categories/basics/greedy_lexicographical_edit_budget_feasibility.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Greedy Lexicographical String Construction with Feasibility Verification under Edit Budget`  

---

## 1. Problem Statement & Key Idea
Given string S of length N (N <= 100) and integer K. Find the lexicographically smallest anagram T of S such that T differs from S in at most K positions.

Construct T character by character from position 0 to N - 1. At index i, try characters c in ['a'..'z'] in alphabetical order. If character c is placed at position i, verify whether the remaining characters can be assigned to satisfy the edit budget K. The minimum extra mismatches for suffix i + 1..N - 1 is (length - sum_{ch} min(count_T(ch), count_S(ch))). If (current_diff + extra_diff <= K), greedily commit to c.

## 2. Core Observation & Invariant
Checking feasibility for each character takes O(|Sigma|) using multiset intersection, allowing exact lexicographical greedy choice.

## 3. Step-by-Step Algorithm
1. Count initial character frequencies of S.
2. For position i = 0 to N - 1:
3.   For character c = 0 to 25:
4.     If count[c] == 0 continue.
5.     Temporarily place c at T[i].
6.     Compute cur_diff = diff_so_far + (c != S[i]).
7.     Calculate max possible matches on remaining suffix: sum min(count[ch], s_rem[ch]).
8.     If cur_diff + extra_diff <= K, commit to c and break.
9. Print T.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 * 26)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    string s;
    cin >> s;

    vector<int> count(26, 0);
    for (char c : s) count[c - 'a']++;

    string t = "";
    int diff_so_far = 0;

    for (int i = 0; i < n; ++i) {
        for (int c = 0; c < 26; ++c) {
            if (count[c] == 0) continue;

            count[c]--;
            int cur_diff = diff_so_far + (c != (s[i] - 'a'));

            vector<int> s_rem(26, 0);
            for (int j = i + 1; j < n; ++j) {
                s_rem[s[j] - 'a']++;
            }

            int matches = 0;
            for (int ch = 0; ch < 26; ++ch) {
                matches += min(count[ch], s_rem[ch]);
            }
            int extra_diff = (n - 1 - i) - matches;

            if (cur_diff + extra_diff <= k) {
                t += (char)('a' + c);
                diff_so_far = cur_diff;
                break;
            }

            count[c]++;
        }
    }

    cout << t << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Greedy lexicographical construction with forward-looking multiset matchability verification.
- **Reusable Pattern**: `Greedy Anagram Prefix: Test 'a'..'z', verify if remaining character multiset can match suffix within budget K.`
