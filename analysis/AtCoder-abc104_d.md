# Problem Analysis: AtCoder-abc104_d — We Love ABC

**Problem ID**: `AtCoder-abc104_d`  
**Contest**: `abc104`  
**Rating / Difficulty**: 1739  
**URL**: https://atcoder.jp/contests/abc104/tasks/abc104_d  
**VJudge Tag**: `[problem:AtCoder-abc104_d]`  
**Category File**: [`../categories/dp/subsequence_automaton_wildcards_dp.md`](../categories/dp/subsequence_automaton_wildcards_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Automaton DP`  
- **Topic (Skill)**: `Subsequence Pattern Matching Expectation / DP on Automaton with Wildcards`  

---

## 1. Problem Statement & Key Idea
Given string S containing 'A', 'B', 'C', and '?'. Replace each '?' with 'A', 'B', or 'C' in 3^Q ways. Find the sum over all 3^Q strings of the number of subsequences equal to 'ABC', modulo 10^9 + 7.

**Key Insight**: Maintain a 4-state vector [cnt, a, ab, abc] representing the total ways to form prefixes of 'ABC'. Each character updates the state vector linearly.

## 2. Core Observation & Invariant
For 'A' or '?', 'A' counts increase by cnt. For 'B' or '?', 'AB' counts increase by a. For 'C' or '?', 'ABC' counts increase by ab. When '?' appears, every existing state is multiplied by 3 because of the 3 choices.

## 3. Step-by-Step Algorithm
1. Initialize cnt = 1, a = 0, ab = 0, abc = 0.
2. For each char c in S:
3.   If c == 'A': a = (a + cnt) % MOD.
4.   If c == 'B': ab = (ab + a) % MOD.
5.   If c == 'C': abc = (abc + ab) % MOD.
6.   If c == '?':
7.     new_abc = (3 * abc + ab) % MOD.
8.     new_ab = (3 * ab + a) % MOD.
9.     new_a = (3 * a + cnt) % MOD.
10.     new_cnt = (3 * cnt) % MOD.
11.     update state variables.
12. Print abc.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    long long cnt = 1; // 3^(number of '?')
    long long a = 0;   // ways to form "A"
    long long ab = 0;  // ways to form "AB"
    long long abc = 0; // ways to form "ABC"

    for (char c : s) {
        if (c == 'A') {
            a = (a + cnt) % MOD;
        } else if (c == 'B') {
            ab = (ab + a) % MOD;
        } else if (c == 'C') {
            abc = (abc + ab) % MOD;
        } else if (c == '?') {
            long long next_abc = (3 * abc + ab) % MOD;
            long long next_ab = (3 * ab + a) % MOD;
            long long next_a = (3 * a + cnt) % MOD;
            long long next_cnt = (3 * cnt) % MOD;

            abc = next_abc;
            ab = next_ab;
            a = next_a;
            cnt = next_cnt;
        }
    }

    cout << abc << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: DP on small finite state automaton tracking subsequence matches under wildcard branches.
- **Reusable Pattern**: `Wildcard Subsequence DP: Maintain linear combination of partial matches multiplied by branch factor.`
