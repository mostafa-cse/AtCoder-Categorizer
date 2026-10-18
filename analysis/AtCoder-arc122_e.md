# Problem Analysis: AtCoder-arc122_e — E. Increasing LCMs

**Problem ID**: `AtCoder-arc122_e`  
**Contest**: `arc122`  
**Rating / Difficulty**: 2535  
**URL**: https://atcoder.jp/contests/arc122/tasks/arc122_e  
**VJudge Tag**: `[problem:AtCoder-arc122_e]`  
**Category File**: [`../categories/number_theory/increasing_lcms_greedy_backward_gcd.md`](../categories/number_theory/increasing_lcms_greedy_backward_gcd.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Primes and Divisors`  
- **Topic (Skill)**: `Sieve, Prime Factorization and Divisors`  

---

## 1. Problem Statement & Key Idea
Find a permutation of $A$ such that prefix LCMs are strictly increasing, or determine that none exists.

## 2. Core Observation & Invariant
Constructing forward is hard, but constructing backwards is greedy and deterministic. Element $x$ can be placed last iff $x \nmid \text{LCM}(S \setminus \{x\}) \iff \text{LCM}_{s \in S \setminus \{x\}} \text{GCD}(x, s) < x$. Since $\text{GCD}(x, s)$ divides $x$, the LCM of these GCDs fits inside $x \le 10^{18}$, avoiding overflow.

## 3. Step-by-Step Algorithm
1. 1. While remaining set $S$ is non-empty:
2.    - Find an element $x \in S$ such that $\text{LCM}_{s \in S \setminus \{x\}} \text{GCD}(x, s) < x$.
3.    - If no such element exists, output `No`.
4.    - Otherwise, append $x$ to the sequence, remove $x$ from $S$, and repeat.
5. 2. Reverse the chosen elements and output `Yes` followed by the permutation.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 \log(\max A))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

unsigned long long gcd_ull(unsigned long long a, unsigned long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

unsigned long long lcm_ull(unsigned long long a, unsigned long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd_ull(a, b)) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<unsigned long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<unsigned long long> rem = a;
    vector<unsigned long long> ans;

    for (int step = 0; step < n; ++step) {
        bool found = false;
        for (int i = 0; i < (int)rem.size(); ++i) {
            unsigned long long x = rem[i];
            unsigned long long cur_lcm = 1;
            for (int j = 0; j < (int)rem.size(); ++j) {
                if (i == j) continue;
                unsigned long long g = gcd_ull(x, rem[j]);
                cur_lcm = lcm_ull(cur_lcm, g);
            }
            if (cur_lcm < x) {
                ans.push_back(x);
                rem.erase(rem.begin() + i);
                found = true;
                break;
            }
        }
        if (!found) {
            cout << "No\n";
            return 0;
        }
    }

    reverse(ans.begin(), ans.end());
    cout << "Yes\n";
    for (int i = 0; i < n; ++i) {
        cout << ans[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
