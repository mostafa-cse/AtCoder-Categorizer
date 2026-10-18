# Problem Analysis: AtCoder-abl_f — F. Heights and Pairs

**Problem ID**: `AtCoder-abl_f`  
**Contest**: `abl`  
**Rating / Difficulty**: 2545  
**URL**: https://atcoder.jp/contests/abl/tasks/abl_f  
**VJudge Tag**: `[problem:AtCoder-abl_f]`  
**Category File**: [`../categories/combinatorics/heights_and_pairs_dnc_ntt_pie.md`](../categories/combinatorics/heights_and_pairs_dnc_ntt_pie.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Given $2N$ people with heights $h_i$, form $N$ disjoint pairs such that no pair contains two people of the same height. Group people by identical heights: suppose group $i$ has size $c_i$. Total unrestricted pairings of $2K$ people is $(2K - 1)!!$. By the Principle of Inclusion and Exclusion, if we choose $k$ monochromatic pairs across all groups, each group $i$ with $j$ monochromatic pairs contributes $c_i! / ((c_i - 2j)! 2^j j!) x^j$. Multiply these group polynomials using Divide and Conquer NTT.

## 2. Core Observation & Invariant
The total polynomial $Q(x) = \prod_{i} P_i(x) = \sum_{k=0}^N a_k x^k$ has coefficient $a_k$ equal to the number of ways to choose $k$ monochromatic pairs. The remaining $2N - 2k$ people are paired arbitrarily in $(2N - 2k - 1)!!$ ways. By PIE, each monochromatic pair carries weight $-1$, giving $\sum_{k=0}^N (-1)^k a_k (2N - 2k - 1)!! \pmod{998244353}$.

## 3. Step-by-Step Algorithm
1. 1. Group people by height and count frequencies $c_i$.
2. 2. For each frequency $c$, build polynomial $P(x) = \sum_{j=0}^{\lfloor c/2 \rfloor} \frac{c!}{(c - 2j)! 2^j j!} x^j$.
3. 3. Multiply all polynomials using Divide and Conquer with NTT in $O(N \log^2 N)$ time.
4. 4. Apply PIE: sum $(-1)^k a_k (2(N - k) - 1)!! \pmod{998244353}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log^2 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

static const int MOD = 998244353;

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

const int MAX = 200005;
long long fact[MAX], invFact[MAX], doubleFact[MAX];

void precompute() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAX; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAX - 1] = modInverse(fact[MAX - 1]);
    for (int i = MAX - 2; i >= 1; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
    doubleFact[0] = 1;
    doubleFact[1] = 1;
    for (int i = 2; i < MAX; ++i) {
        doubleFact[i] = (doubleFact[i - 2] * i) % MOD;
    }
}

// NTT
void ntt(vector<long long>& a, bool invert) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        long long wlen = power(3, (MOD - 1) / len);
        if (invert) wlen = modInverse(wlen);
        for (int i = 0; i < n; i += len) {
            long long w = 1;
            for (int j = 0; j < len / 2; j++) {
                long long u = a[i + j], v = (a[i + j + len / 2] * w) % MOD;
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
    vector<long long> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    int n = 1;
    while (n < (int)(a.size() + b.size())) n <<= 1;
    fa.resize(n);
    fb.resize(n);
    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < n; i++) fa[i] = (fa[i] * fb[i]) % MOD;
    ntt(fa, true);
    while (fa.size() > 1 && fa.back() == 0) fa.pop_back();
    return fa;
}

vector<long long> dnc(int l, int r, const vector<vector<long long>>& polys) {
    if (l == r) return polys[l];
    int mid = l + (r - l) / 2;
    return multiply(dnc(l, mid, polys), dnc(mid + 1, r, polys));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    precompute();

    int n;
    if (!(cin >> n)) return 0;

    map<int, int> count_map;
    for (int i = 0; i < 2 * n; ++i) {
        int h;
        cin >> h;
        count_map[h]++;
    }

    vector<vector<long long>> polys;
    for (auto const& [val, c] : count_map) {
        int max_pairs = c / 2;
        vector<long long> P(max_pairs + 1, 0);
        // c! / ((c - 2j)! * 2^j * j!)
        long long inv2 = modInverse(2);
        long long inv2_pow = 1;
        for (int j = 0; j <= max_pairs; ++j) {
            long long ways = fact[c];
            ways = (ways * invFact[c - 2 * j]) % MOD;
            ways = (ways * invFact[j]) % MOD;
            ways = (ways * inv2_pow) % MOD;
            P[j] = ways;
            inv2_pow = (inv2_pow * inv2) % MOD;
        }
        polys.push_back(P);
    }

    vector<long long> total_poly = dnc(0, polys.size() - 1, polys);

    long long ans = 0;
    for (int k = 0; k < (int)total_poly.size() && k <= n; ++k) {
        long long rem_pairs = n - k;
        long long rem_ways = 1;
        if (rem_pairs > 0) {
            rem_ways = doubleFact[2 * rem_pairs - 1];
        }
        long long term = (total_poly[k] * rem_ways) % MOD;
        if (k % 2 == 1) {
            ans = (ans - term + MOD) % MOD;
        } else {
            ans = (ans + term) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
