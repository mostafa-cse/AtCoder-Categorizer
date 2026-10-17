# Problem Analysis: AtCoder-arc071_c — TrBBnsformBBtion

**Problem ID**: `AtCoder-arc071_c`  
**Contest**: `arc071`  
**Rating / Difficulty**: 1739  
**URL**: https://atcoder.jp/contests/arc071/tasks/arc071_c  
**VJudge Tag**: `[problem:AtCoder-arc071_c]`  
**Category File**: [`../categories/math/algebraic_invariant_mod3_string_rewriting.md`](../categories/math/algebraic_invariant_mod3_string_rewriting.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Invariants`  
- **Topic (Skill)**: `Algebraic Invariant / Value Mapping Modulo 3 on String Rewriting`  

---

## 1. Problem Statement & Key Idea
Given strings S and T of 'A' and 'B'. Allowed operations: replace 'A' with 'BB', 'BB' with 'A', 'B' with 'AA', 'AA' with 'B'. Answer Q queries: can substring S[a..b] be transformed into T[c..d]?

**Key Insight**: Map 'A' to 1 and 'B' to 2. Notice that 'A' <-> 'BB' means 1 <-> 2 + 2 = 4 = 1 (mod 3), and 'B' <-> 'AA' means 2 <-> 1 + 1 = 2 (mod 3). Thus, the sum of values modulo 3 is strictly invariant under all operations.

## 2. Core Observation & Invariant
Any string can be reduced to a single character ('A', 'B', or empty) determined uniquely by its sum mod 3. S[a..b] can transform into T[c..d] iff sum(S[a..b]) % 3 == sum(T[c..d]) % 3.

## 3. Step-by-Step Algorithm
1. Build prefix sum array for S mapping 'A'->1, 'B'->2.
2. Build prefix sum array for T mapping 'A'->1, 'B'->2.
3. For each query (a, b, c, d):
4.   sum_s = (pref_S[b] - pref_S[a - 1]) % 3.
5.   sum_t = (pref_T[d] - pref_T[c - 1]) % 3.
6.   If sum_s == sum_t, print 'YES', else 'NO'.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| + |T| + Q)`
- **Space Complexity**: `O(|S| + |T|)`

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

    int n = s.size(), m = t.size();
    vector<int> pref_s(n + 1, 0), pref_t(m + 1, 0);

    for (int i = 0; i < n; ++i) {
        pref_s[i + 1] = pref_s[i] + (s[i] == 'A' ? 1 : 2);
    }
    for (int i = 0; i < m; ++i) {
        pref_t[i + 1] = pref_t[i] + (t[i] == 'A' ? 1 : 2);
    }

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        int sum_s = (pref_s[b] - pref_s[a - 1]) % 3;
        int sum_t = (pref_t[d] - pref_t[c - 1]) % 3;
        if (sum_s == sum_t) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Discovering modular algebraic invariants in string rewriting systems.
- **Reusable Pattern**: `String Rewriting Invariant: Map characters to Z_3 values where expansions preserve modulo sum.`
