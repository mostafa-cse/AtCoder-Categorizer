# Problem Analysis: AtCoder-abc191_f — F. GCD or MIN

**Problem ID**: `AtCoder-abc191_f`  
**Contest**: `abc191`  
**Rating / Difficulty**: 2333  
**URL**: https://atcoder.jp/contests/abc191/tasks/abc191_f  
**VJudge Tag**: `[problem:AtCoder-abc191_f]`  
**Category File**: [`../categories/number_theory/gcd_divisor_closure_reachability.md`](../categories/number_theory/gcd_divisor_closure_reachability.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Primes and Divisors`  
- **Topic (Skill)**: `Sieve, Prime Factorization and Divisors`  

---

## 1. Problem Statement & Key Idea
Repeatedly replacing $(x, y)$ with $\gcd(x, y)$ or $\min(x, y)$ can achieve any divisor $d \le \min(A)$ if and only if the GCD of all array elements divisible by $d$ is exactly $d$. Evaluated by factorizing all elements in $O(N \sqrt{\max A})$.

## 2. Core Observation & Invariant
Operation $x \leftarrow \gcd(x, y)$ can only reduce values, so the final single remaining value cannot exceed $m = \min(A)$. Any integer $d \le m$ is reachable as a final value if and only if the GCD of all array elements that are multiples of $d$ is exactly $d$.

## 3. Step-by-Step Algorithm
1. Find $m = \min(A)$. For each $A_i$, enumerate all of its divisors $d \le m$ in $O(\sqrt{A_i})$ time.
2. Maintain a hash map `g[d]` storing the running GCD of all array elements divisible by $d$.
3. Count all divisors $d$ for which $g[d] == d$, plus 1 for the identity $m$ itself.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \sqrt{\max A})`
- **Space Complexity**: `O(N \cdot d(\max A))`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    long long m = 2e9;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        m = min(m, a[i]);
    }

    unordered_map<long long, long long> g;
    g.reserve(100000);

    for (long long x : a) {
        for (long long d = 1; d * d <= x; ++d) {
            if (x % d == 0) {
                if (d <= m) {
                    auto it = g.find(d);
                    if (it == g.end()) {
                        g[d] = x;
                    } else {
                        it->second = gcd(it->second, x);
                    }
                }
                long long d2 = x / d;
                if (d2 <= m) {
                    auto it = g.find(d2);
                    if (it == g.end()) {
                        g[d2] = x;
                    } else {
                        it->second = gcd(it->second, x);
                    }
                }
            }
        }
    }

    int ans = 0;
    for (auto &pair : g) {
        if (pair.first == pair.second) {
            ans++;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
