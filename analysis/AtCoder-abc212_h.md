# Problem Analysis: AtCoder-abc212_h — H - Nim Counting

**Problem ID**: `AtCoder-abc212_h`  
**Contest**: `abc212`  
**Rating / Difficulty**: 2741  
**URL**: https://atcoder.jp/contests/abc212/tasks/abc212_h  
**VJudge Tag**: `[problem:AtCoder-abc212_h]`  
**Category File**: [`../categories/math/nim_counting_xor_fwht.md`](../categories/math/nim_counting_xor_fwht.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Convolution`  
- **Topic (Skill)**: `Fast Walsh Hadamard Transform (FWHT) and its Variations`  

---

## 1. Problem Statement & Key Idea
There are K integers A_1, ..., A_K. We choose an integer M between 1 and N, and then choose a sequence of M integers from the A_i. A game of Nim is played with M heaps of sizes corresponding to the chosen sequence. Find the number of ways to choose the sequence such that Takahashi (the first player) has a winning strategy, modulo 998244353.

## 2. Core Observation & Invariant
In Nim, the first player has a winning strategy if and only if the XOR sum of the heap sizes is non-zero. The total number of sequences of length M is K^M, so the total number of sequences of length 1 <= M <= N is sum_{M=1}^N K^M. To find the number of losing sequences, we must count the number of sequences of length M whose XOR sum is exactly 0. Let P be the indicator vector of the K allowed integers in the group (Z_2)^16 (since A_i < 2^16). The XOR convolution power P^{(*M)} gives the distribution of XOR sums of M choices. By applying the Fast Walsh-Hadamard Transform (FWHT), convolution becomes pointwise multiplication: FWHT(P^{(*M)}) = FWHT(P)^M. Summing over 1 <= M <= N in the frequency domain yields sum_{M=1}^N v^M = v(v^N - 1)/(v - 1) if v != 1, or N if v = 1. Applying inverse FWHT yields the exact number of zero-XOR configurations in O(V log V) time where V = 2^16.

## 3. Step-by-Step Algorithm
1. 1. Initialize vector P of size V = 2^16 with the counts of each A_i.
2. 2. Compute FWHT(P) using the standard Walsh-Hadamard butterfly transform.
3. 3. In the transform domain, replace each value v with the geometric sum S(v) = sum_{M=1}^N v^M mod 998244353.
4. 4. Apply inverse FWHT to S to recover the distribution of XOR sums.
5. 5. The number of losing sequences is S_final[0].
6. 6. The answer is (sum_{M=1}^N K^M - S_final[0]) mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(V log V + K) where V = 2^16`
- **Space Complexity**: `O(V)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

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

void fwht(vector<long long>& a, bool inv = false) {
    int n = a.size();
    for (int len = 1; 2 * len <= n; len <<= 1) {
        for (int i = 0; i < n; i += 2 * len) {
            for (int j = 0; j < len; j++) {
                long long u = a[i + j];
                long long v = a[i + len + j];
                a[i + j] = (u + v) % MOD;
                a[i + len + j] = (u - v + MOD) % MOD;
            }
        }
    }
    if (inv) {
        long long inv_n = modInverse(n);
        for (int i = 0; i < n; i++) {
            a[i] = (a[i] * inv_n) % MOD;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    const int SIZE = 1 << 16;
    vector<long long> a(SIZE, 0);
    for (int i = 0; i < k; i++) {
        int val;
        cin >> val;
        a[val] = 1;
    }

    fwht(a, false);

    // For each frequency x in 0..SIZE-1:
    // sum_{m=1}^n v^m
    vector<long long> s(SIZE, 0);
    for (int i = 0; i < SIZE; i++) {
        long long v = a[i];
        if (v == 1) {
            s[i] = n % MOD;
        } else {
            long long num = (v * (power(v, n) - 1 + MOD)) % MOD;
            long long den = modInverse((v - 1 + MOD) % MOD);
            s[i] = (num * den) % MOD;
        }
    }

    fwht(s, true);

    long long zero_xor = s[0];

    // Total arrangements = sum_{m=1}^n k^m
    long long total = 0;
    if (k == 1) {
        total = n % MOD;
    } else {
        long long num = (k * (power(k, n) - 1 + MOD)) % MOD;
        long long den = modInverse(k - 1);
        total = (num * den) % MOD;
    }

    long long win = (total - zero_xor + MOD) % MOD;
    cout << win << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
