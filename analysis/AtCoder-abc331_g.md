# Problem Analysis: AtCoder-abc331_g — Collect Them All

**Problem ID**: `AtCoder-abc331_g`  
**Contest**: `abc331`  
**Rating / Difficulty**: 2668  
**URL**: https://atcoder.jp/contests/abc331/tasks/abc331_g  
**VJudge Tag**: `[problem:AtCoder-abc331_g]`  
**Category File**: [`../categories/combinatorics/collect_them_all_min_max_pie.md`](../categories/combinatorics/collect_them_all_min_max_pie.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Bags contain C_i items of color i. Items are drawn with replacement proportional to count. By Min-Max Inclusion-Exclusion, the expected time to see all N colors is sum_{empty != S} (-1)^{|S|+1} * (sum C_j) / (sum_{i in S} C_i). The polynomial generating function prod_{i=1}^N (1 - x^{C_i}) computes the coefficients of x^W in O(M log^2 M) via divide-and-conquer NTT.

## 2. Core Observation & Invariant
The term (-1)^{|S|} * x^{sum_{i in S} C_i} corresponds to the expansion of prod_{i=1}^N (1 - x^{C_i}). The coefficient of x^k in -P(x) directly yields sum_{S: sum C_i = k} (-1)^{|S|+1}. Multiplying by M / k where M = sum C_i produces the exact expected value.

## 3. Step-by-Step Algorithm
1. 1. Compute total count M = sum_{i=1}^N C_i.
2. 2. Construct polynomials P_i(x) = 1 - x^{C_i}.
3. 3. Multiply all N polynomials using divide-and-conquer NTT in O(M log^2 M).
4. 4. For each degree k in [1, M], add contribution -[x^k]P(x) * (M / k) mod 998244353.
5. 5. Output total sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(M log^2 M)`
- **Space Complexity**: `O(M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

static const long long MOD = 998244353;
static const long long G = 3;

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
    for (int i = 1, j = 0; i < n; i++) {
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
            for (int j = 0; j < len / 2; j++) {
                long long u = a[i + j];
                long long v = (a[i + j + len / 2] * w) % MOD;
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
    int deg_a = a.size() - 1;
    int deg_b = b.size() - 1;
    if (deg_a < 0 || deg_b < 0) return {};
    int n = 1;
    while (n < deg_a + deg_b + 1) n <<= 1;
    vector<long long> fa(n, 0), fb(n, 0);
    for (size_t i = 0; i < a.size(); ++i) fa[i] = a[i];
    for (size_t i = 0; i < b.size(); ++i) fb[i] = b[i];
    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < n; ++i) fa[i] = (fa[i] * fb[i]) % MOD;
    ntt(fa, true);
    fa.resize(deg_a + deg_b + 1);
    return fa;
}

struct PolyCompare {
    bool operator()(const vector<long long>& a, const vector<long long>& b) const {
        return a.size() > b.size();
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    priority_queue<vector<long long>, vector<vector<long long>>, PolyCompare> pq;

    for (int i = 0; i < M; ++i) {
        int c;
        cin >> c;
        vector<long long> p(c + 1, 0);
        p[0] = 1;
        p[c] = (MOD - 1);
        pq.push(p);
    }

    while (pq.size() > 1) {
        auto p1 = pq.top(); pq.pop();
        auto p2 = pq.top(); pq.pop();
        pq.push(multiply(p1, p2));
    }

    auto poly = pq.top();

    long long ans = 0;
    for (int k = 1; k <= N && k < (int)poly.size(); ++k) {
        long long coef = poly[k];
        if (coef != 0) {
            long long term = (MOD - coef) % MOD * modInverse(k) % MOD;
            ans = (ans + term) % MOD;
        }
    }

    ans = (ans * N) % MOD;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
