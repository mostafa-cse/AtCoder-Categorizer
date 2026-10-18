# Problem Analysis: AtCoder-abc385_g — G. Counting Buildings

**Problem ID**: `AtCoder-abc385_g`  
**Contest**: `abc385`  
**Rating / Difficulty**: 2492  
**URL**: https://atcoder.jp/contests/abc385/tasks/abc385_g  
**VJudge Tag**: `[problem:AtCoder-abc385_g]`  
**Category File**: [`../categories/combinatorics/counting_buildings_stirling_numbers_first_kind.md`](../categories/combinatorics/counting_buildings_stirling_numbers_first_kind.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Stirling Numbers`  
- **Topic (Skill)**: `Stirling Number of the First Kind for Fixed N`  

---

## 1. Problem Statement & Key Idea
Count permutations of $1 \dots N$ where the difference between visible buildings from the left and visible buildings from the right is $K$. When inserting element $x$ from 2 to $N$ into a permutation of $1 \dots x - 1$: placing at the left end increases $L - R$ by $+1$ (1 choice), placing at the right end decreases $L - R$ by $-1$ (1 choice), and placing in the interior leaves $L - R$ unchanged ($x - 2$ choices). The generating function is $\prod_{i=0}^{N-2} (t + t^{-1} + i)$, which expands to $\sum_{m} \left[ \begin{matrix} N-1 \\ m \end{matrix} \right] (t + t^{-1})^m$ via unsigned Stirling numbers of the first kind.

## 2. Core Observation & Invariant
The row of unsigned Stirling numbers of the first kind $\left[ \begin{matrix} N-1 \\ m \end{matrix} \right]$ is computed by expanding the polynomial $\prod_{i=0}^{N-2} (y + i)$ using divide-and-conquer NTT in $O(N \log^2 N)$. Then $(t + t^{-1})^m = \sum_{j=0}^m \binom{m}{j} t^{m - 2j}$. Extracting the coefficient of $t^K$ corresponds to summing $\left[ \begin{matrix} N-1 \\ m \end{matrix} \right] \binom{m}{(m + K)/2}$ over all $m \equiv K \pmod 2$.

## 3. Step-by-Step Algorithm
1. 1. Build polynomials $(y + i)$ for $i = 0 \dots N - 2$ and multiply them using divide-and-conquer NTT to find polynomial coefficients $C_m = \left[ \begin{matrix} N-1 \\ m \end{matrix} \right]$.
2. 2. Precompute factorials and binomial coefficients.
3. 3. For each $m$ from $|K|$ to $N - 1$ with $m \equiv K \pmod 2$:
4.    a. Compute $\binom{m}{(m + K) / 2}$.
5.    b. Accumulate $C_m \times \binom{m}{(m + K) / 2} \pmod{998244353}$.
6. 4. Output the total count.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log^2 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int MOD = 998244353;
const int G = 3;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

void ntt(vector<long long>& a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; ++i) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        long long wlen = power(G, (MOD - 1) / len);
        if (invert) wlen = modInverse(wlen);
        for (int i = 0; i < n; i += len) {
            long long w = 1;
            for (int j = 0; j < len / 2; ++j) {
                long long u = a[i + j];
                long long v = a[i + j + len / 2] * w % MOD;
                a[i + j] = (u + v < MOD ? u + v : u + v - MOD);
                a[i + j + len / 2] = (u - v >= 0 ? u - v : u - v + MOD);
                w = (w * wlen) % MOD;
            }
        }
    }
    if (invert) {
        long long n_inv = modInverse(n);
        for (long long& x : a) x = (x * n_inv) % MOD;
    }
}

vector<long long> multiply(const vector<long long>& a, const vector<long long>& b) {
    int need = a.size() + b.size() - 1;
    int n = 1;
    while (n < need) n <<= 1;
    vector<long long> fa(n, 0), fb(n, 0);
    for (size_t i = 0; i < a.size(); ++i) fa[i] = a[i];
    for (size_t i = 0; i < b.size(); ++i) fb[i] = b[i];
    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < n; ++i) fa[i] = (fa[i] * fb[i]) % MOD;
    ntt(fa, true);
    fa.resize(need);
    return fa;
}

// Compute prod_{i=l}^r (x + i)
vector<long long> get_stirling(int l, int r) {
    if (l == r) {
        return {l % MOD, 1}; // (l + x)
    }
    int mid = l + (r - l) / 2;
    return multiply(get_stirling(l, mid), get_stirling(mid + 1, r));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long K;
    if (!(cin >> N >> K)) return 0;

    if (abs(K) > N - 1) {
        cout << 0 << "\n";
        return 0;
    }

    if (N == 1) {
        cout << (K == 0 ? 1 : 0) << "\n";
        return 0;
    }

    vector<long long> s1 = get_stirling(0, N - 2);

    vector<long long> fact(N + 1), inv(N + 1);
    fact[0] = 1;
    for (int i = 1; i <= N; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv[N] = modInverse(fact[N]);
    for (int i = N - 1; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;

    auto nCr = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
    };

    long long ans = 0;
    for (int m = abs(K); m < N; ++m) {
        if ((m - K) % 2 != 0) continue;
        long long ways_s1 = (m < (int)s1.size() ? s1[m] : 0);
        int a = (m + K) / 2;
        long long ways_choose = nCr(m, a);
        ans = (ans + ways_s1 * ways_choose) % MOD;
    }

    cout << (ans % MOD + MOD) % MOD << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
