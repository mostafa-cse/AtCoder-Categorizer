# Problem Analysis: AtCoder-typical90_cf — There are two types of characters

**Problem ID**: `AtCoder-typical90_cf`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 084)  
**Rating / Difficulty**: 800 (★3)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_cf  
**VJudge Tag**: `[problem:AtCoder-typical90_cf]`  
**Category File**: [`../categories/basics/complement_counting.md`](../categories/basics/complement_counting.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Complement Counting & Run-Length`  
- **Topic (Skill)**: `Complement Counting via Run-Length Encoding`  

---

## 1. Problem Statement & Key Idea
String S of length N with 'o' and 'x'. Count pairs (l, r) with 1 <= l < r <= N such that substring S[l..r] contains both 'o' and 'x'.

**Core Idea**: Complement Counting: Total pairs is N*(N - 1)/2. Count invalid substrings containing ONLY 'o' or ONLY 'x'.

## 2. Core Observation & Invariant
Substrings of identical characters are subsegments within contiguous runs. Using Run-Length Encoding, a run of length L contributes L*(L - 1)/2 invalid pairs. Subtract from total pairs in O(N).

## 3. Step-by-Step Algorithm
1. Run-length encode string into block lengths L_1, L_2, ...
2. invalid = sum L_i * (L_i - 1) / 2.
3. Output N*(N - 1)/2 - invalid.

## 4. Complexity Analysis
Time: O(N), Space: O(1).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    long long total_pairs = (long long)n * (n - 1) / 2;
    long long invalid_pairs = 0;

    int cur_len = 1;
    for (int i = 1; i < n; ++i) {
        if (s[i] == s[i - 1]) {
            cur_len++;
        } else {
            invalid_pairs += (long long)cur_len * (cur_len - 1) / 2;
            cur_len = 1;
        }
    }
    invalid_pairs += (long long)cur_len * (cur_len - 1) / 2;

    cout << total_pairs - invalid_pairs << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Complement counting subtracting contiguous monochromatic runs.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Complement Counting principle and Run-Length Encoding decomposition.
- **Reusable Pattern**: `Complement Counting with Run-Length Encoding.`

---
Back to [Complement Counting via Run-Length Encoding](../categories/basics/complement_counting.md) | [Categories Directory](../categories/README.md)