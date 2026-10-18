# Problem Analysis: AtCoder-abc230_g — G. GCD Permutation

**Problem ID**: `AtCoder-abc230_g`  
**Contest**: `abc230`  
**Rating / Difficulty**: 2516  
**URL**: https://atcoder.jp/contests/abc230/tasks/abc230_g  
**VJudge Tag**: `[problem:AtCoder-abc230_g]`  
**Category File**: [`../categories/number_theory/gcd_permutation_square_free_sieve.md`](../categories/number_theory/gcd_permutation_square_free_sieve.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Primes and Divisors`  
- **Topic (Skill)**: `Sieve, Prime Factorization and Divisors`  

---

## 1. Problem Statement & Key Idea
Count pairs $(i, j)$ with $1 \le i \le j \le N$ such that $\gcd(i, j) > 1$ and $\gcd(P_i, P_j) > 1$. Condition $[\gcd > 1] = 1 - [\gcd = 1] = - \sum_{g > 1} \mu(g) [g \mid \gcd]$. Applying Mobius inversion to both indices and values expresses the condition as double Mobius inversion: $\sum_{g > 1, h > 1} \mu(g) \mu(h) \binom{cnt(g, h) + 1}{2}$, where $cnt(g, h)$ is the number of indices $i$ such that $g \mid i$ and $h \mid P_i$.

## 2. Core Observation & Invariant
Only square-free integers $g, h > 1$ with $\mu \ne 0$ need to be considered. For a fixed square-free $g > 1$, consider all indices $i$ that are multiples of $g$ ($i = c \cdot g$). For each such index, factorize $P_i$ into its square-free divisors $h > 1$ and count occurrences in a frequency array. The sum of divisor counts over all multiples of $g$ across all $g$ is $\sum_{g} \sum_{c=1}^{N/g} d(P_{cg}) \approx O(N \log^2 N)$, which requires $\le 7 \times 10^6$ operations.

## 3. Step-by-Step Algorithm
1. 1. Precompute primes, Mobius function $\mu$, and square-free divisors for each number up to $N$.
2. 2. Iterate over each square-free $g \in [2, N]$:
3.    a. For each multiple $i = g, 2g, \dots \le N$, retrieve square-free divisors $h > 1$ of $P_i$.
4.    b. Increment a local frequency table $freq[h]++$ and record visited $h$.
5.    c. For each unique $h$, compute pair count $\binom{freq[h] + 1}{2}$ and add $\mu(g) \cdot \mu(h) \cdot \binom{freq[h] + 1}{2}$ to total.
6.    d. Reset frequency table entries for visited $h$.
7. 3. Output total pairs.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log^2 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> p[i];
    }

    vector<int> mu(n + 1, 0);
    vector<bool> is_prime(n + 1, true);
    vector<int> primes;
    mu[1] = 1;

    for (int i = 2; i <= n; ++i) {
        if (is_prime[i]) {
            primes.push_back(i);
            mu[i] = -1;
        }
        for (int pr : primes) {
            if (i * pr > n) break;
            is_prime[i * pr] = false;
            if (i % pr == 0) {
                mu[i * pr] = 0;
                break;
            } else {
                mu[i * pr] = -mu[i];
            }
        }
    }

    vector<vector<int>> divs(n + 1);
    for (int i = 1; i <= n; ++i) {
        if (mu[i] != 0) {
            for (int j = i; j <= n; j += i) {
                divs[j].push_back(i);
            }
        }
    }

    vector<int> cnt(n + 1, 0);
    vector<int> touched;
    touched.reserve(n);

    long long ans = 0;

    for (int g = 2; g <= n; ++g) {
        if (mu[g] == 0) continue;
        touched.clear();

        for (int k = g; k <= n; k += g) {
            int val = p[k];
            for (int h : divs[val]) {
                if (h > 1) {
                    if (cnt[h] == 0) {
                        touched.push_back(h);
                    }
                    cnt[h]++;
                }
            }
        }

        for (int h : touched) {
            long long c = cnt[h];
            long long pairs = c * (c + 1) / 2;
            ans += (long long)mu[g] * mu[h] * pairs;
            cnt[h] = 0;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
