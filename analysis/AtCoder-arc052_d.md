# Problem Analysis: AtCoder-arc052_d — D. 9

**Problem ID**: `AtCoder-arc052_d`  
**Contest**: `arc052`  
**Rating / Difficulty**: 2436  
**URL**: https://atcoder.jp/contests/arc052/tasks/arc052_d  
**VJudge Tag**: `[problem:AtCoder-arc052_d]`  
**Category File**: [`../categories/miscellaneous/digit_sum_modulo_meet_in_the_middle.md`](../categories/miscellaneous/digit_sum_modulo_meet_in_the_middle.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Meet in the Middle`  

---

## 1. Problem Statement & Key Idea
Count non-negative integers $N \le M \le 10^{10}$ such that $N \equiv S(N) \pmod K$. Because $N - S(N)$ is inherently divisible by 9, $N - S(N)$ must be a multiple of $L = \text{lcm}(K, 9)$. If $L \ge 10^5$, we iterate over the few multiples $X$ of $L$ and test possible digit sums $d \in [0, 90]$. If $L < 10^5$, then $K < 10^5$, and we perform Meet-in-the-Middle on the upper and lower 5 digits.

## 2. Core Observation & Invariant
Writing $N = A \times 10^5 + B$ decomposes $S(N) = S(A) + S(B)$. The congruence becomes $(A \times 10^5 - S(A)) \equiv (S(B) - B) \pmod K$. Precomputing frequencies of $(S(B) - B) \bmod K$ for $B \in [0, 10^5)$ enables $O(1)$ lookups for each $A \le \lfloor M / 10^5 \rfloor$.

## 3. Step-by-Step Algorithm
1. 1. Compute $L = \text{lcm}(K, 9) = \frac{9K}{\gcd(9, K)}$.
2. 2. If $L \ge 10^5$: loop $X$ over multiples of $L$ up to $M$. For each $d \in [0, 90]$, let $N = X + d$; if $1 \le N \le M$ and $S(N) == d$, increment answer.
3. 3. If $L < 10^5$: precompute table $freq[rem]$ for $B \in [0, 10^5)$ where $rem = (S(B) - B) \bmod K$.
4. 4. Iterate $A$ from $0$ to $\lfloor M / 10^5 \rfloor$, adding $freq[(A \times 10^5 - S(A)) \bmod K]$, and process the boundary block.
5. 5. Decrement 1 to exclude $N = 0$, and output the result.

## 4. Complexity Analysis
- **Time Complexity**: `O(M / L \cdot 90) \text{ for large } L, \; O(10^5) \text{ for small } L`
- **Space Complexity**: `O(K) \le O(10^5)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int sum_digits(long long n) {
    int s = 0;
    while (n) {
        s += n % 10;
        n /= 10;
    }
    return s;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long K, M;
    if (!(cin >> K >> M)) return 0;

    long long g = gcd(9LL, K);
    long long L = (9LL / g) * K;

    long long THRESHOLD = 100000;

    if (L >= THRESHOLD) {
        long long ans = 0;
        for (long long X = 0; X <= M; X += L) {
            for (int d = 0; d <= 90; ++d) {
                long long N = X + d;
                if (N >= 1 && N <= M) {
                    if (sum_digits(N) == d) {
                        ans++;
                    }
                }
            }
        }
        cout << ans << "\n";
    } else {
        long long B_LIMIT = 100000;
        vector<int> freq(K, 0);
        for (long long B = 0; B < B_LIMIT; ++B) {
            long long rem = (sum_digits(B) - B) % K;
            if (rem < 0) rem += K;
            freq[rem]++;
        }

        long long ans = 0;
        long long max_A = M / B_LIMIT;
        for (long long A = 0; A < max_A; ++A) {
            long long rem_A = (A * B_LIMIT - sum_digits(A)) % K;
            if (rem_A < 0) rem_A += K;
            ans += freq[rem_A];
        }

        long long rem_A = (max_A * B_LIMIT - sum_digits(max_A)) % K;
        if (rem_A < 0) rem_A += K;
        for (long long B = 0; B <= M % B_LIMIT; ++B) {
            long long rem_B = (sum_digits(B) - B) % K;
            if (rem_B < 0) rem_B += K;
            if (rem_B == rem_A) {
                ans++;
            }
        }

        ans--; // exclude N=0
        cout << ans << "\n";
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
