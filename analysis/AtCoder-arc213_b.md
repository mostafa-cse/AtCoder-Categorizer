# Problem Analysis: AtCoder-arc213_b — B. Hamming Distance is not 1

**Problem ID**: `AtCoder-arc213_b`  
**Contest**: `arc213`  
**Rating / Difficulty**: 2313  
**URL**: https://atcoder.jp/contests/arc213/tasks/arc213_b  
**VJudge Tag**: `[problem:AtCoder-arc213_b]`  
**Category File**: [`../categories/basics/hypercube_interval_maximum_independent_set.md`](../categories/basics/hypercube_interval_maximum_independent_set.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bitwise Thinking`  
- **Topic (Skill)**: `Bitwise Operations and Bitmasks`  

---

## 1. Problem Statement & Key Idea
Given $L$ and $R$, find the maximum size of an independent set in the induced subgraph of the hypercube graph formed by vertices $x \in [L, R]$, where edges connect integers differing by exactly one bit.

## 2. Core Observation & Invariant
The hypercube graph is bipartite partitioned by popcount parity. In an interval $[L, R]$, pairs $\{2j, 2j+1\}$ form a matching of size $(len - 2)/2$. When $L$ is odd, $R$ is even, $P(L) \neq P(R)$, and $R < L + 2^k$ (where $k = \text{MSB}(L \oplus R)$), both endpoints can be included simultaneously because no two elements differ by $2^k$.

## 3. Step-by-Step Algorithm
1. Classify $[L, R]$ by parity of endpoints. If $L$ is even or $R$ is odd, the max independent set has size $(len + 1) // 2$.
2. If $L$ is odd and $R$ is even, the size is $len // 2 + 1$ if $P(L) = P(R)$ or $R < L + 2^k$ ($k = \text{MSB}(L \oplus R)$), otherwise $len // 2$.
3. Construct $S$ by filtering on popcount parity, augmented by $P(x) \oplus ((x \gg k) \& 1)$ when $R < L + 2^k$.

## 4. Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

inline int parity(unsigned long long x) {
    return __builtin_parityll(x);
}

void solve() {
    int q;
    unsigned long long l, r;
    if (!(cin >> q >> l >> r)) return;

    unsigned long long len = r - l + 1;
    if (q == 0) {
        if (l % 2 == 0 || r % 2 == 1) {
            cout << (len + 1) / 2 << "\n";
        } else {
            if (parity(l) == parity(r)) {
                cout << len / 2 + 1 << "\n";
            } else {
                int k = 63 - __builtin_clzll(l ^ r);
                if (r < l + (1ULL << k)) {
                    cout << len / 2 + 1 << "\n";
                } else {
                    cout << len / 2 << "\n";
                }
            }
        }
    } else {
        string ans = "";
        ans.reserve(len);
        if (l % 2 == 0 || r % 2 == 1) {
            int target_p = 0;
            if (l % 2 == 0 && r % 2 == 0) target_p = parity(r);
            else if (l % 2 == 1 && r % 2 == 1) target_p = parity(l);
            else target_p = 0;

            for (unsigned long long x = l; x <= r; ++x) {
                ans.push_back(parity(x) == target_p ? '1' : '0');
            }
        } else {
            if (parity(l) == parity(r)) {
                int target_p = parity(l);
                for (unsigned long long x = l; x <= r; ++x) {
                    ans.push_back(parity(x) == target_p ? '1' : '0');
                }
            } else {
                int k = 63 - __builtin_clzll(l ^ r);
                if (r < l + (1ULL << k)) {
                    int target = parity(l) ^ ((l >> k) & 1ULL);
                    for (unsigned long long x = l; x <= r; ++x) {
                        ans.push_back((parity(x) ^ ((x >> k) & 1ULL)) == target ? '1' : '0');
                    }
                } else {
                    for (unsigned long long x = l; x <= r; ++x) {
                        ans.push_back(parity(x) == 0 ? '1' : '0');
                    }
                }
            }
        }
        cout << ans << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
