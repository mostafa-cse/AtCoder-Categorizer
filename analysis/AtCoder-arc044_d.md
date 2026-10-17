# Problem Analysis: AtCoder-arc044_d — D. suffix array

**Problem ID**: `AtCoder-arc044_d`  
**Contest**: `arc044`  
**Rating / Difficulty**: 2335  
**URL**: https://atcoder.jp/contests/arc044/tasks/arc044_d  
**VJudge Tag**: `[problem:AtCoder-arc044_d]`  
**Category File**: [`../categories/strings/suffix_array_inverse_construction.md`](../categories/strings/suffix_array_inverse_construction.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Suffix Structures`  
- **Topic (Skill)**: `Suffix Array`  

---

## 1. Problem Statement & Key Idea
Invert a given suffix array $A$ into the lexicographically smallest uppercase string $S$. Characters are determined greedily by comparing next-suffix ranks $rank[A_i + 1] < rank[A_{i+1} + 1]$ in $O(N)$ time.

## 2. Core Observation & Invariant
For adjacent suffixes $A_i$ and $A_{i+1}$ in the suffix array, $S[A_i] \le S[A_{i+1}]$. If $rank[A_i + 1] < rank[A_{i+1} + 1]$, equality $S[A_{i+1}] = S[A_i]$ preserves suffix order; otherwise, a strict character increment $S[A_{i+1}] = S[A_i] + 1$ is strictly required.

## 3. Step-by-Step Algorithm
1. Compute suffix ranks $rank[x]$ from the given permutation $A$, setting $rank[N+1] = 0$ for the empty suffix.
2. Greedily assign $S[A_0] = 'A'$. For each $i$ from 0 to $N-2$, set $S[A_{i+1}] = S[A_i]$ if $rank[A_i + 1] < rank[A_{i+1} + 1]$, else $S[A_{i+1}] = S[A_i] + 1$.
3. If the maximum character exceeds 'Z', output -1; otherwise, output $S$ in $O(N)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    vector<int> rank_s(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        --a[i]; // 0-indexed
        rank_s[a[i]] = i + 1;
    }
    rank_s[n] = 0; // empty suffix

    string s(n, '?');
    int cur_char = 0;
    s[a[0]] = (char)('A' + cur_char);

    for (int i = 0; i < n - 1; ++i) {
        if (rank_s[a[i] + 1] < rank_s[a[i + 1] + 1]) {
            // keep cur_char
        } else {
            cur_char++;
        }
        if (cur_char >= 26) {
            cout << -1 << "\n";
            return 0;
        }
        s[a[i + 1]] = (char)('A' + cur_char);
    }

    cout << s << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
