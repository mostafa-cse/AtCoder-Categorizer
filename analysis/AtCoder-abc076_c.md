# Problem Analysis: AtCoder-abc076_c — Dubious Document 2

**Problem ID**: `AtCoder-abc076_c`  
**Contest**: `abc076`  
**Rating / Difficulty**: 846  
**URL**: https://atcoder.jp/contests/abc076/tasks/abc076_c  
**VJudge Tag**: `[problem:AtCoder-abc076_c]`  
**Category File**: [`../categories/strings/rightmost_match_lexicographical.md`](../categories/strings/rightmost_match_lexicographical.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `String Matching & Greedy`  
- **Topic (Skill)**: `Rightmost Match Lexicographical Minimization`  

---

## 1. Problem Statement & Key Idea
Given string S containing lowercase letters and '?', and string T. Replace all '?' such that T appears as a contiguous substring of S and the resulting string is lexicographically smallest. If impossible, output UNRESTORABLE.

**Key Idea**: To make the restored string lexicographically smallest, early characters in S should be 'a' as much as possible. Placing T as far to the right as possible minimizes its impact on earlier positions.

## 2. Core Observation & Invariant
Iterate backwards over all possible start positions i for T in S. The first (rightmost) index i where T matches S[i .. i + |T| - 1] (allowing '?' to match any char) gives the optimal placement. All remaining '?' in S become 'a'.

## 3. Step-by-Step Algorithm
1. Scan i from |S| - |T| down to 0.
2. Check if T can match substring S[i .. i + |T| - 1].
3. If valid, build candidate string: S[0..i-1] with '?' replaced by 'a', then T, then S[i+|T|..|S|-1] with '?' replaced by 'a'.
4. Output the candidate string. If no valid i exists, output UNRESTORABLE.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| * |T|)`
- **Space Complexity**: `O(|S|)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size();
    int m = t.size();

    int best_pos = -1;
    for (int i = n - m; i >= 0; --i) {
        bool match = true;
        for (int j = 0; j < m; ++j) {
            if (s[i + j] != '?' && s[i + j] != t[j]) {
                match = false;
                break;
            }
        }
        if (match) {
            best_pos = i;
            break;
        }
    }

    if (best_pos == -1) {
        cout << "UNRESTORABLE\n";
    } else {
        string res = s;
        for (int j = 0; j < m; ++j) {
            res[best_pos + j] = t[j];
        }
        for (int i = 0; i < n; ++i) {
            if (res[i] == '?') res[i] = 'a';
        }
        cout << res << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Reverse greedy placement for lexicographical string minimization.
- **Reusable Pattern**: `Place required non-'a' substring at rightmost valid position, fill remaining wildcards with 'a'.`
