# Problem Analysis: AtCoder-abc110_c — String Transformation

**Problem ID**: `AtCoder-abc110_c`  
**Contest**: `abc110`  
**Rating / Difficulty**: 949  
**URL**: https://atcoder.jp/contests/abc110/tasks/abc110_c  
**VJudge Tag**: `[problem:AtCoder-abc110_c]`  
**Category File**: [`../categories/strings/alphabet_bijection_isomorphism.md`](../categories/strings/alphabet_bijection_isomorphism.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Character Bijections`  
- **Topic (Skill)**: `Alphabet Bijection / Isomorphism Verification`  

---

## 1. Problem Statement & Key Idea
Given two strings S and T of the same length. You can choose two distinct characters c_1 and c_2 and swap all occurrences of c_1 and c_2 in S. Can S be transformed into T?

**Key Idea**: Any sequence of character swaps forms a permutation on the alphabet. Thus, transformation is possible if and only if there exists a bijective (one-to-one and onto) mapping between characters of S and T.

## 2. Core Observation & Invariant
Verify two conditions: (1) each character in S maps to at most one character in T; (2) each character in T is mapped from at most one character in S.

## 3. Step-by-Step Algorithm
1. Initialize arrays s_to_t and t_to_s of size 26 to -1.
2. For each index i from 0 to |S| - 1: let u = S[i] - 'a', v = T[i] - 'a'.
3. If s_to_t[u] != -1 and s_to_t[u] != v: return 'No'.
4. If t_to_s[v] != -1 and t_to_s[v] != u: return 'No'.
5. Set s_to_t[u] = v and t_to_s[v] = u.
6. Output 'Yes' if all characters satisfy bijection.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| + |Sigma|)`
- **Space Complexity**: `O(|Sigma|)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    vector<int> s_to_t(26, -1);
    vector<int> t_to_s(26, -1);

    for (size_t i = 0; i < s.size(); ++i) {
        int u = s[i] - 'a';
        int v = t[i] - 'a';

        if (s_to_t[u] != -1 && s_to_t[u] != v) {
            cout << "No\n";
            return 0;
        }
        if (t_to_s[v] != -1 && t_to_s[v] != u) {
            cout << "No\n";
            return 0;
        }

        s_to_t[u] = v;
        t_to_s[v] = u;
    }

    cout << "Yes\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Verifying graph isomorphism / bijective mapping between character alphabets.
- **Reusable Pattern**: `Bidirectional mapping verification: check s_to_t[u] == v and t_to_s[v] == u.`
