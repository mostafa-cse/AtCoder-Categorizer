# Problem Analysis: AtCoder-arc172_e — E. Last 9 Digits

**Problem ID**: `AtCoder-arc172_e`  
**Contest**: `arc172`  
**Rating / Difficulty**: 2358  
**URL**: https://atcoder.jp/contests/arc172/tasks/arc172_e  
**VJudge Tag**: `[problem:AtCoder-arc172_e]`  
**Category File**: [`../categories/number_theory/hensel_lifting_power_mod.md`](../categories/number_theory/hensel_lifting_power_mod.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Modular Arithmetic`  
- **Topic (Skill)**: `Chinese Remainder Theorem (CRT)`  

---

## 1. Problem Statement & Key Idea
Find the smallest positive integer $n$ such that $n^n \equiv X \pmod{10^9}$. Hensel lifting / digit-by-digit lifting uniquely extends the solution from $10^{k-1}$ to $10^k$ by testing only 10 candidates per digit in $O(L^2)$ per query.

## 2. Core Observation & Invariant
For any $X$ coprime to 10, the equation $n^n \equiv X \pmod{10^k}$ has a unique solution modulo $10^k$ for every $k \ge 2$. Furthermore, the unique solution modulo $10^k$ extends the unique solution modulo $10^{k-1}$ by testing only 10 candidates $a_{k-1} + t \cdot 10^{k-1}$ for $t \in [0, 9]$.

## 3. Step-by-Step Algorithm
1. For $k=2$, find the unique base solution $a_2 \in [1, 99]$ such that $a_2^{a_2} \equiv X \pmod{100}$ by brute force.
2. Iteratively for $k = 3, \dots, 9$, test the 10 candidate lifts $n = a_{k-1} + t \cdot 10^{k-1}$ ($0 \le t \le 9$) using binary exponentiation modulo $10^k$.
3. The unique satisfying candidate becomes $a_k$. Output $a_9$, taking $O(L^2)$ operations per query ($L = 9$ digits).

## 4. Complexity Analysis
- **Time Complexity**: `O(Q L^2)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

long long power_mod(__int128 base, __int128 exp, __int128 mod) {
    __int128 res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return (long long)res;
}

void solve() {
    long long x;
    if (!(cin >> x)) return;

    // k = 2: brute force n in [1, 99]
    long long n = -1;
    for (long long i = 1; i < 100; i++) {
        if (power_mod(i, i, 100) == x % 100) {
            n = i;
            break;
        }
    }

    if (n == -1) {
        cout << -1 << "\n";
        return;
    }

    // k = 3 .. 9: lift digit by digit
    long long cur_mod = 100;
    for (int k = 3; k <= 9; k++) {
        long long next_mod = cur_mod * 10;
        long long next_n = -1;
        for (int t = 0; t < 10; t++) {
            long long cand = n + (long long)t * cur_mod;
            if (power_mod(cand, cand, next_mod) == x % next_mod) {
                next_n = cand;
                break;
            }
        }
        n = next_n;
        cur_mod = next_mod;
    }

    cout << n << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    if (cin >> q) {
        while (q--) solve();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
