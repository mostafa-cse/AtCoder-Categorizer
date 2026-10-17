# Problem Analysis: AtCoder-agc062_c — C. Mex of Subset Sum

**Problem ID**: `AtCoder-agc062_c`  
**Contest**: `agc062`  
**Rating / Difficulty**: 2320  
**URL**: https://atcoder.jp/contests/agc062/tasks/agc062_c  
**VJudge Tag**: `[problem:AtCoder-agc062_c]`  
**Category File**: [`../categories/basics/subset_sum_bounded_holes_expansion.md`](../categories/basics/subset_sum_bounded_holes_expansion.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Given a multiset $A$ of $N$ positive integers, find the $K$ smallest positive integers that cannot be represented as the sum of a subset of $A$.

## 2. Core Observation & Invariant
A number $z$ remains a non-representable hole after adding $A_i$ if and only if $z$ was a hole before adding $A_i$ and $z - A_i$ was also a hole before adding $A_i$. Any hole strictly smaller than $A_i$ can never be eliminated by any subsequent element $\ge A_i$.

## 3. Step-by-Step Algorithm
1. Sort $A$ in non-decreasing order.
2. Dynamically maintain the set of missing holes $H \le \text{sum}$.
3. When processing $A_i$: existing holes $z < A_i$ or $z - A_i \in H$ survive, new holes in $[\text{sum}+1, \text{sum}+A_i]$ are formed by $y + A_i$ ($y \in H$), and gaps $[\text{sum}+1, A_i-1]$ are inserted.
4. Prune $H$ to the smallest $3K$ elements at each step, achieving an $O(N K \log K)$ time complexity.

## 4. Complexity Analysis
- **Time Complexity**: `O(N K \log K)`
- **Space Complexity**: `O(K)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    set<long long> H;
    long long total_sum = 0;

    for (long long x : a) {
        set<long long> new_H;

        for (long long z : H) {
            if (z < x) {
                new_H.insert(z);
            } else if (H.count(z - x)) {
                new_H.insert(z);
            }
        }

        for (long long y : H) {
            long long z = y + x;
            if (z <= total_sum + x) {
                new_H.insert(z);
            }
        }

        if (x > total_sum + 1) {
            for (long long z = total_sum + 1; z < x; ++z) {
                new_H.insert(z);
                if ((int)new_H.size() > 3 * k) break;
            }
        }

        total_sum += x;
        H = std::move(new_H);

        if ((int)H.size() > 3 * k) {
            auto it = H.begin();
            advance(it, 3 * k);
            H.erase(it, H.end());
        }
    }

    vector<long long> ans;
    ans.reserve(k);

    for (long long h : H) {
        if ((int)ans.size() < k) {
            ans.push_back(h);
        }
    }

    long long cur = total_sum + 1;
    while ((int)ans.size() < k) {
        ans.push_back(cur++);
    }

    for (int i = 0; i < k; ++i) {
        cout << ans[i] << (i + 1 == k ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
