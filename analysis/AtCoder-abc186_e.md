# Problem Analysis: AtCoder-abc186_e — Throne

**Problem ID**: `AtCoder-abc186_e`  
**Contest**: `abc186`  
**Rating / Difficulty**: 1461  
**URL**: https://atcoder.jp/contests/abc186/tasks/abc186_e  
**VJudge Tag**: `[problem:AtCoder-abc186_e]`  
**Category File**: [`../categories/number_theory/linear_congruence_extended_gcd.md`](../categories/number_theory/linear_congruence_extended_gcd.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Linear Congruence`  
- **Topic (Skill)**: `Linear Congruence Equation via Extended Euclidean Algorithm`  

---

## 1. Problem Statement & Key Idea
N chairs are arranged circularly labeled 0 to N - 1 clockwise. Takahashi starts at chair S and repeatedly jumps K chairs clockwise. Find the minimum number of jumps to land on chair 0, or -1 if impossible. Process T test cases.

**Key Insight**: Landing on 0 is equivalent to the linear congruence K * x = -S (mod N), solved using the Extended Euclidean Algorithm.

## 2. Core Observation & Invariant
K * x = -S (mod N) has a solution iff gcd(K, N) divides (-S). If it does, divide K, N, -S by g = gcd(K, N) to obtain coprime K' and N'. Then x = (-S' * (K')^(-1)) mod N'.

## 3. Step-by-Step Algorithm
1. extGCD(a, b, x, y): computes gcd(a, b) and coefficients x, y such that a*x + b*y = gcd(a, b).
2. For each test case (N, S, K):
3.   Let b = (N - S) % N. We need K * x = b (mod N).
4.   Compute g = extGCD(K, N, x, y).
5.   If b % g != 0, return -1.
6.   Reduce: K' = K / g, N' = N / g, b' = b / g.
7.   extGCD(K', N', inv_k, temp).
8.   x = (inv_k % N' + N') % N'.
9.   ans = (1LL * x * b') % N'.
10.   Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(T * log(min(N, K)))`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>

using namespace std;

long long extGCD(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long g = extGCD(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

void solve() {
    long long n, s, k;
    cin >> n >> s >> k;

    long long b = (n - s) % n;
    long long x, y;
    long long g = extGCD(k, n, x, y);

    if (b % g != 0) {
        cout << -1 << "\n";
        return;
    }

    long long n_prime = n / g;
    long long b_prime = b / g;
    long long k_prime = k / g;

    extGCD(k_prime, n_prime, x, y);
    x = (x % n_prime + n_prime) % n_prime;

    long long ans = (__int128)x * b_prime % n_prime;
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Solving linear congruences a * x = b (mod m) using the Extended Euclidean Algorithm.
- **Reusable Pattern**: `Linear Congruence Solver: extGCD reduction to coprime moduli.`
