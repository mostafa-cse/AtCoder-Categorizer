# Problem Analysis: AtCoder-panasonic2020_e — E. Three Substrings

**Problem ID**: `AtCoder-panasonic2020_e`  
**Contest**: `panasonic2020`  
**Rating / Difficulty**: 2309  
**URL**: https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_e  
**VJudge Tag**: `[problem:AtCoder-panasonic2020_e]`  
**Category File**: [`../categories/strings/pairwise_wildcard_alignment_filtering_span.md`](../categories/strings/pairwise_wildcard_alignment_filtering_span.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `String Matching`  
- **Topic (Skill)**: `String Matching using Bitsets`  

---

## 1. Problem Statement & Key Idea
Given three strings $a, b, c$ with wildcards '?', find the minimum length of a string containing all three as substrings.

## 2. Core Observation & Invariant
Three strings $a, b, c$ can be embedded at relative offsets $(0, i, j)$ if and only if all three pairwise overlaps $(a, b)$ at $i$, $(a, c)$ at $j$, and $(b, c)$ at $j - i$ are mutually consistent.

## 3. Step-by-Step Algorithm
1. Precompute compatibility tables for each pair of strings over all relative shifts in $[-4000, 4000]$ in $O(|a||b| + |b||c| + |a||c|)$ time.
2. Iterate over valid shift offsets $(i, j) \in [-2000, 2000]^2$, pruning incompatible pairs in $O(1)$ via the precomputed table.
3. Compute the span $\max(|a|, i+|b|, j+|c|) - \min(0, i, j)$ and output the global minimum.

## 4. Complexity Analysis
- **Time Complexity**: `O(|a||b| + |a||c| + |b||c| + L^2)`
- **Space Complexity**: `O(L)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int OFFSET = 4005;
const int MAX_SPAN = 8010;

bool ok_ab[MAX_SPAN];
bool ok_ac[MAX_SPAN];
bool ok_bc[MAX_SPAN];

void compute_match(const string& x, const string& y, bool ok[]) {
    int lx = x.size(), ly = y.size();
    for (int offset = -4000; offset <= 4000; ++offset) {
        bool match = true;
        for (int i = 0; i < ly; ++i) {
            int pos_x = offset + i;
            if (pos_x >= 0 && pos_x < lx) {
                if (x[pos_x] != '?' && y[i] != '?' && x[pos_x] != y[i]) {
                    match = false;
                    break;
                }
            }
        }
        ok[offset + OFFSET] = match;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b, c;
    if (!(cin >> a >> b >> c)) return 0;

    int la = a.size(), lb = b.size(), lc = c.size();

    compute_match(a, b, ok_ab);
    compute_match(a, c, ok_ac);
    compute_match(b, c, ok_bc);

    int ans = la + lb + lc;

    for (int i = -2000; i <= 2000; ++i) {
        if (!ok_ab[i + OFFSET]) continue;
        for (int j = -2000; j <= 2000; ++j) {
            if (!ok_ac[j + OFFSET]) continue;
            if (!ok_bc[j - i + OFFSET]) continue;

            int left = min(0, min(i, j));
            int right = max(la, max(i + lb, j + lc));
            ans = min(ans, right - left);
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
