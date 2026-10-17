# Problem Analysis: AtCoder-abc272_g — G. Yet Another mod M

**Problem ID**: `AtCoder-abc272_g`  
**Contest**: `abc272`  
**Rating / Difficulty**: 2187  
**URL**: https://atcoder.jp/contests/abc272/tasks/abc272_g  
**VJudge Tag**: `[problem:AtCoder-abc272_g]`  
**Category File**: [`../categories/miscellaneous/monte_carlo_majority_prime_factorization.md`](../categories/miscellaneous/monte_carlo_majority_prime_factorization.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Randomized`  
- **Topic (Skill)**: `Randomized Algorithms`  

---

## 1. Problem Statement & Key Idea
Given N <= 5000 distinct integers, find an integer M in [3, 10^9] such that some remainder modulo M occurs strictly more than N/2 times. Randomly sampling pairs and testing prime factors of their differences identifies M with high probability.

## 2. Core Observation & Invariant
If a majority remainder modulo M exists, it occupies at least floor(N/2) + 1 elements (> 50%). Two randomly selected distinct elements both belong to the majority group with probability > 1/4. When they do, M divides |A_i - A_j|. Factoring |A_i - A_j| and verifying each odd prime factor (and 4) across all N elements takes O(N) per test. Repeating for 40 random pairs reduces failure probability to (3/4)^{40} < 10^{-5}.

## 3. Step-by-Step Algorithm
1. Initialize 64-bit Mersenne Twister RNG.
2. Perform up to 40 iterations: pick random indices i != j and compute diff = |A_i - A_j|.
3. Extract prime factors of diff >= 3 (and 4 if diff is divisible by 4).
4. For each candidate modulus p: count how many k in [0, N-1] satisfy A_k % p == A_i % p. If count > N / 2, output p and terminate.
5. If no candidate satisfies the condition after 40 iterations, output -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(K * (sqrt(max_A) + N * omega(max_A)))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    mt19937_64 rng(1337);

    auto check_m = [&](long long m) {
        if (m < 3) return false;
        // Check if any residue has count > N / 2
        // To do this in O(N), we can check candidate residues
        // Or pick random elements to test their residue
        // If there is a majority residue, picking 10 random elements will hit it with prob 1 - 2^-10
        for (int rep = 0; rep < 5; ++rep) {
            long long target_rem = A[rng() % N] % m;
            int cnt = 0;
            for (int i = 0; i < N; ++i) {
                if (A[i] % m == target_rem) {
                    cnt++;
                }
            }
            if (cnt > N / 2) return true;
        }
        return false;
    };

    // Try 35 random pairs
    for (int iter = 0; iter < 40; ++iter) {
        int i = rng() % N;
        int j = rng() % N;
        while (i == j) j = rng() % N;

        long long diff = abs(A[i] - A[j]);
        if (diff == 0) continue;

        vector<long long> primes;
        long long temp = diff;

        if (temp % 4 == 0) {
            primes.push_back(4);
        }
        while (temp % 2 == 0) temp /= 2;

        for (long long p = 3; p * p <= temp; p += 2) {
            if (temp % p == 0) {
                primes.push_back(p);
                while (temp % p == 0) temp /= p;
            }
        }
        if (temp > 2) {
            primes.push_back(temp);
        }

        for (long long p : primes) {
            // Count directly with A[i] % p
            int cnt = 0;
            long long rem = A[i] % p;
            for (int k = 0; k < N; ++k) {
                if (A[k] % p == rem) cnt++;
            }
            if (cnt > N / 2) {
                cout << p << "\n";
                return 0;
            }
        }
    }

    cout << -1 << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
