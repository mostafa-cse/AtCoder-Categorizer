# Problem Analysis: AtCoder-agc003_d — D. Anticube

**Problem ID**: `AtCoder-agc003_d`  
**Contest**: `agc003`  
**Rating / Difficulty**: 2608  
**URL**: https://atcoder.jp/contests/agc003/tasks/agc003_d  
**VJudge Tag**: `[problem:AtCoder-agc003_d]`  
**Category File**: [`../categories/number_theory/anticube_cubefree_sieve.md`](../categories/number_theory/anticube_cubefree_sieve.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Primes and Divisors`  
- **Topic (Skill)**: `Sieve, Prime Factorization and Divisors`  

---

## 1. Problem Statement & Key Idea
Given N integers s_i <= 10^{10}, find the maximum size of a subset such that no two elements multiply to a perfect cube.

## 2. Core Observation & Invariant
Remove all cubic prime factors so each s_i is cubefree modulo 3: x = prod p_j^{e_j} (e_j in {1, 2}). The unique dual partner of x is x* = prod p_j^{3 - e_j}. For each pair {x, x*}, at most one group can be chosen, so we greedily pick max(cnt(x), cnt(x*)). If x = 1, we can pick at most 1 element.

## 3. Step-by-Step Algorithm
1. Sieve primes up to 2155. Divide out small primes for each s_i.
2. For remaining cofactor rem > 2154: check if it is a perfect square (rem = r^2), a prime (Miller-Rabin), or two-prime composite. Track dual partners and greedily take max frequencies.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * (pi(2155) + log s_i))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

static const long long LIMIT = 10000000000LL;

long long mul_mod(long long a, long long b, long long m) {
    return (long long)((__int128)a * b % m);
}

long long power_mod(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = mul_mod(res, base, mod);
        base = mul_mod(base, base, mod);
        exp /= 2;
    }
    return res;
}

bool miller_rabin(long long n) {
    if (n < 2) return false;
    if (n == 2 || n == 3 || n == 5 || n == 7) return true;
    if (n % 2 == 0) return false;
    long long d = n - 1;
    int s = 0;
    while (d % 2 == 0) {
        d /= 2;
        s++;
    }
    static const long long bases[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (long long a : bases) {
        if (n <= a) break;
        long long x = power_mod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool composite = true;
        for (int r = 1; r < s; ++r) {
            x = mul_mod(x, x, n);
            if (x == n - 1) {
                composite = false;
                break;
            }
        }
        if (composite) return false;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> S(N);
    for (int i = 0; i < N; ++i) {
        cin >> S[i];
    }

    const int MAX_P = 2155;
    vector<bool> is_prime(MAX_P + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i <= MAX_P; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j <= MAX_P; j += i) {
                is_prime[j] = false;
            }
        }
    }
    vector<int> primes;
    for (int i = 2; i <= MAX_P; ++i) {
        if (is_prime[i]) primes.push_back(i);
    }

    map<long long, int> cnt;
    map<long long, long long> dual_map;

    for (int i = 0; i < N; ++i) {
        long long x = S[i];
        long long base = 1;
        long long dual = 1;
        bool overflow = false;

        for (int p : primes) {
            if ((long long)p * p * p > x) break;
            if (x % p == 0) {
                int c = 0;
                while (x % p == 0) {
                    x /= p;
                    c++;
                }
                c %= 3;
                if (c == 1) {
                    base *= p;
                    if (!overflow) {
                        if ((__int128)dual * p * p <= LIMIT) dual *= (long long)p * p;
                        else overflow = true;
                    }
                } else if (c == 2) {
                    base *= (long long)p * p;
                    if (!overflow) {
                        if ((__int128)dual * p <= LIMIT) dual *= p;
                        else overflow = true;
                    }
                }
            }
        }

        if (x > 1) {
            long long r = (long long)sqrt(x);
            while ((r + 1) * (r + 1) <= x) r++;
            while (r * r > x) r--;

            if (r * r == x) {
                base *= r * r;
                if (!overflow) {
                    if ((__int128)dual * r <= LIMIT) dual *= r;
                    else overflow = true;
                }
            } else if (miller_rabin(x)) {
                base *= x;
                if (!overflow) {
                    if ((__int128)dual * x * x <= LIMIT) dual *= x * x;
                    else overflow = true;
                }
            } else {
                base *= x;
                overflow = true;
            }
        }

        long long d_val = overflow ? -1 : dual;
        cnt[base]++;
        dual_map[base] = d_val;
    }

    int ans = 0;
    set<long long> visited;

    for (auto& entry : cnt) {
        long long base = entry.first;
        int c = entry.second;
        if (visited.count(base)) continue;
        visited.insert(base);

        if (base == 1) {
            ans += 1;
            continue;
        }

        long long d_val = dual_map[base];
        if (d_val != -1 && cnt.count(d_val)) {
            visited.insert(d_val);
            ans += max(c, cnt[d_val]);
        } else {
            ans += c;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
