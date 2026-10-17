# Problem Analysis: AtCoder-abc222_g — 222

**Problem ID**: `AtCoder-abc222_g`  
**Contest**: `abc222`  
**Rating / Difficulty**: 2242  
**URL**: https://atcoder.jp/contests/abc222/tasks/abc222_g  
**VJudge Tag**: `[problem:AtCoder-abc222_g]`  
**Category File**: [`../categories/number_theory/multiplicative_order_repunit_divisibility.md`](../categories/number_theory/multiplicative_order_repunit_divisibility.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Modular Arithmetic`  
- **Topic (Skill)**: `Multiplicative Order and Carmichael's Lambda Function`  

---

## 1. Problem Statement & Key Idea
Find the smallest positive integer n such that the n-digit repunit 22...2 is divisible by K, or determine that no such n exists.

## 2. Core Observation & Invariant
The n-th term is 2(10^n - 1)/9. Thus 2(10^n - 1)/9 = 0 (mod K) <=> 2(10^n - 1) = 0 (mod 9K). Let M = 9K / gcd(2, 9K). The equation becomes 10^n = 1 (mod M). A solution exists iff gcd(10, M) == 1. When gcd(10, M) == 1, the smallest n is the multiplicative order of 10 modulo M, which must divide Euler's totient phi(M). We can factorize phi(M) and test its divisors.

## 3. Step-by-Step Algorithm
1. 1. Let M = 9K / gcd(2, 9K).
2. 2. If gcd(10, M) != 1, output -1 (no power of 10 can be 1 mod M).
3. 3. If M == 1, output 1.
4. 4. Compute phi(M) by finding prime factors of M in O(sqrt(M)).
5. 5. Enumerate all divisors d of phi(M) in sorted order.
6. 6. The first divisor d with 10^d = 1 (mod M) is the minimum n. Output d.

## 4. Complexity Analysis
- **Time Complexity**: `O(T * (sqrt(M) + d(phi(M)) * log(phi(M))))`
- **Space Complexity**: `O(d(phi(M)))`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

long long gcd_ll(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

long long mod_pow(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = (long long)((__int128)res * base % mod);
        base = (long long)((__int128)base * base % mod);
        exp /= 2;
    }
    return res;
}

long long get_phi(long long n) {
    long long res = n;
    for (long long p = 2; p * p <= n; ++p) {
        if (n % p == 0) {
            while (n % p == 0) n /= p;
            res -= res / p;
        }
    }
    if (n > 1) res -= res / n;
    return res;
}

void solve() {
    long long K;
    cin >> K;

    long long M = 9 * K;
    long long g = gcd_ll(2, M);
    M /= g;

    if (gcd_ll(10, M) != 1) {
        cout << -1 << "\n";
        return;
    }
    if (M == 1) {
        cout << 1 << "\n";
        return;
    }

    long long phi = get_phi(M);

    // Collect all divisors of phi
    vector<long long> divisors;
    for (long long d = 1; d * d <= phi; ++d) {
        if (phi % d == 0) {
            divisors.push_back(d);
            if (d * d != phi) divisors.push_back(phi / d);
        }
    }
    sort(divisors.begin(), divisors.end());

    for (long long d : divisors) {
        if (mod_pow(10, d, M) == 1) {
            cout << d << "\n";
            return;
        }
    }

    cout << -1 << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
