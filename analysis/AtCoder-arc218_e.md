# Problem Analysis: AtCoder-arc218_e — Reverse and Reverse

**Problem ID**: `AtCoder-arc218_e`  
**Contest**: `arc218`  
**Rating / Difficulty**: 2705  
**URL**: https://atcoder.jp/contests/arc218/tasks/arc218_e  
**VJudge Tag**: `[problem:AtCoder-arc218_e]`  
**Category File**: [`../categories/miscellaneous/reverse_and_reverse_permutation_inversions.md`](../categories/miscellaneous/reverse_and_reverse_permutation_inversions.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Inversions`  

---

## 1. Problem Statement & Key Idea
The operation 'reverse prefix of length i and suffix of length N-i' decomposes into a right-shift by i followed by a reversal. After K steps, the distribution of shift amounts modulo N is uniform except at 0 ((N-1)^K +- 1)/N, and odd K incurs a final reversal. Maintaining total inversions under adjacent swaps reduces to maintaining initial inversions I_0 and the shift moment sum S_shift = sum (k-1)(2 P_k - (N+1)), which updates in O(1) per swap query.

## 2. Core Observation & Invariant
Right-shifting P by 1 increases inversion count by 2 P_N - (N+1). Summing over all cyclic shifts yields sum I_i = N I_0 + sum_{k=1}^N (k - 1)(2 P_k - (N+1)). Swapping P_x and P_{x+1} changes this sum by exactly 2(P_x - P_{x+1}) in O(1) time.

## 3. Step-by-Step Algorithm
1. 1. Compute initial inversions I_0 using Fenwick Tree in O(N log N).
2. 2. Compute initial S_shift = sum i * (2 P[i] - (N+1)) in O(N).
3. 3. For each query (x, K):
4.    - Update I_0 (+1 if P[x] < P[x+1], else -1).
5.    - Update S_shift += 2 * (P[x] - P[x+1]).
6.    - Swap P[x] and P[x+1].
7.    - Compute sum_I = N * I_0 + S_shift.
8.    - If K is even: ans = I_0 + ((N-1)^K - 1)/N * sum_I mod MOD.
9.    - If K is odd: ans = N(N-1)/2 * (N-1)^K - (-I_0 + ((N-1)^K + 1)/N * sum_I) mod MOD.
10. 4. Print answer for each query.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + Q log K)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const long long MOD = 998244353;

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

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }
    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> P(n);
    for (int i = 0; i < n; ++i) {
        cin >> P[i];
    }

    Fenwick bit(n);
    long long I0 = 0;
    for (int i = n - 1; i >= 0; --i) {
        I0 += bit.query(P[i] - 1);
        bit.add(P[i], 1);
    }

    long long S_shift = 0;
    for (int i = 0; i < n; ++i) {
        S_shift += 1LL * i * (2LL * P[i] - (n + 1));
    }

    long long total_pairs = (1LL * n * (n - 1) / 2) % MOD;
    long long invN = modInverse(n);

    for (int q_iter = 0; q_iter < q; ++q_iter) {
        int x;
        long long K;
        cin >> x >> K;
        int idx = x - 1;
        int p_a = P[idx];
        int p_b = P[idx + 1];

        if (p_a < p_b) {
            I0++;
        } else {
            I0--;
        }

        S_shift += 2LL * (p_a - p_b);
        swap(P[idx], P[idx + 1]);

        long long sum_I = (1LL * n * (I0 % MOD) + (S_shift % MOD)) % MOD;
        if (sum_I < 0) sum_I += MOD;

        long long pow_N_minus_1 = power(n - 1, K);

        if (K % 2 == 0) {
            long long v = ((pow_N_minus_1 - 1 + MOD) % MOD) * invN % MOD;
            long long val = ((I0 % MOD) + v * sum_I) % MOD;
            if (val < 0) val += MOD;
            cout << val << "\n";
        } else {
            long long v = ((pow_N_minus_1 + 1) % MOD) * invN % MOD;
            long long val = (-(I0 % MOD) + v * sum_I) % MOD;
            long long ans = (total_pairs * pow_N_minus_1 - val) % MOD;
            if (ans < 0) ans += MOD;
            cout << ans << "\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
