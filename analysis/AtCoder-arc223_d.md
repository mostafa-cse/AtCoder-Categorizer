# Problem Analysis: AtCoder-arc223_d — D. Xpectation of Cards in Hand with Laboratory

**Problem ID**: `AtCoder-arc223_d`  
**Contest**: `arc223`  
**Rating / Difficulty**: 2281  
**URL**: https://atcoder.jp/contests/arc223/tasks/arc223_d  
**VJudge Tag**: `[problem:AtCoder-arc223_d]`  
**Category File**: [`../categories/math/gamblers_ruin_reflection_principle_first_passage_expectation.md`](../categories/math/gamblers_ruin_reflection_principle_first_passage_expectation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Gambler's Ruin`  

---

## 1. Problem Statement & Key Idea
A grid walk starts at $(0, 0)$ and makes $A$ horizontal steps and $B$ vertical steps. Compute the number of paths that reach $(A, B)$ without the number of vertical steps ever exceeding horizontal steps by $K$ or more, modulo 998244353.

## 2. Core Observation & Invariant
Each card drawn from the deck advances a random walk in $(a, b)$ where the hand runs out of draw cards exactly when $b - a = K$ for the first time. The number of paths hitting this absorbing barrier is given by the reflection principle $\binom{a+b-1}{a} - \binom{a+b-1}{a-1}$, while paths never reaching it yield the full deck hand size $B$.

## 3. Step-by-Step Algorithm
1. 1. Drawing 2 cards and discarding 1 draw card leaves the net count of draw cards in hand as $\frac{a - b + K}{2}$. The hand runs out of draw cards iff $b = a + K$.\n2. By the reflection principle (ballot theorem), the number of card sequences where $b = a + K$ occurs for the first time at step $a + b$ is $(\binom{a+b-1}{a} - \binom{a+b-1}{a-1}) \times \binom{A-a+B-b}{A-a}$. At this moment, exactly $b$ normal cards are in hand.\n3. If the deck is exhausted before the hand runs out of draw cards (which can only happen if $B < A + K$), the path never hits the line $b - a = K$. The number of such sequences is $\binom{A+B}{A} - \binom{A+B}{A+K}$, and the final hand contains all $B$ normal cards. If $B \ge A + K$, this event has probability 0.\n4. Summing the product of final hand sizes and their corresponding path counts, then dividing by $\binom{A+B}{A}$, yields the expected hand size in $O(A + B)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(A + B)`
- **Space Complexity**: `O(A + B)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

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

const int MAX = 20000005;
long long fact[MAX];
long long invFact[MAX];

void init_fact(int limit) {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i <= limit; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[limit] = modInverse(fact[limit]);
    for (int i = limit - 1; i >= 1; i--) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

void solve_test() {
    int A, B, K;
    if (!(cin >> A >> B >> K)) return;

    long long total_arrangements = nCr(A + B, A);

    long long ways_exhausted = 0;
    if (B < A + K) {
        ways_exhausted = (nCr(A + B, A) - nCr(A + B, A + K) + MOD) % MOD;
    }
    long long sum_hand = (1LL * B * ways_exhausted) % MOD;

    int max_a = min(A, B - K);
    for (int a = 0; a <= max_a; a++) {
        int b = a + K;
        int step = a + b;
        long long ways_first = (nCr(step - 1, a) - nCr(step - 1, a - 1) + MOD) % MOD;
        long long ways_rem = nCr(A - a + B - b, A - a);
        long long ways = ways_first * ways_rem % MOD;
        sum_hand = (sum_hand + 1LL * b * ways) % MOD;
    }

    long long ans = (sum_hand * modInverse(total_arrangements)) % MOD;
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    init_fact(20000000);

    int t;
    if (cin >> t) {
        while (t--) {
            solve_test();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
