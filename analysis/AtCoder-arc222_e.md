# Problem Analysis: AtCoder-arc222_e — E - XOR Matching

**Problem ID**: `AtCoder-arc222_e`  
**Contest**: `arc222`  
**Rating / Difficulty**: 2423  
**URL**: https://atcoder.jp/contests/arc222/tasks/arc222_e  
**VJudge Tag**: `[problem:AtCoder-arc222_e]`  
**Category File**: [`../categories/math/xor_matching_fwht_autocorrelation.md`](../categories/math/xor_matching_fwht_autocorrelation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Convolution`  
- **Topic (Skill)**: `Fast Walsh Hadamard Transform (FWHT) and its Variations`  

---

## 1. Problem Statement & Key Idea
For each $X \in [0, 2^M - 1]$, find the maximum number of disjoint pairs of cards with bitwise XOR equal to $X$, and output $\sum_{X} f(X) 10^X \pmod{998244353}$.

## 2. Core Observation & Invariant
For $X = 0$, $f(0) = \sum \lfloor C[i] / 2 \rfloor$. For $X > 0$, values partition into independent pairs $\{i, i \oplus X\}$, so $f(X) = \frac{1}{2} \sum_i \min(C[i], C[i \oplus X])$. Using $\min(a, b) = \sum_{x \ge 1} [a \ge x][b \ge x]$, the sum decomposes into XOR convolutions of indicator vectors $S_x[i] = [C[i] \ge x]$ with themselves. By setting a threshold $K \approx 20$, the first $K$ terms are summed via FWHT in $O(K M 2^M)$ time, and remaining heavy pairs ($C[i] > K$) are corrected directly in $O((N/K)^2)$ time.

## 3. Step-by-Step Algorithm
1. 1. Compute frequency array $C[i]$ of values $0 \le i < 2^M$.
2. 2. For $X = 0$, $f(0) = \sum C[i] / 2$.
3. 3. Choose threshold $K = 20$. For $x = 1, \dots, K$, form boolean array $S_x[i] = [C[i] \ge x]$, apply FWHT, and accumulate pointwise squares into $\hat{T}$.
4. 4. Apply inverse FWHT to $\hat{T}$. For $X > 0$, add $T[X] / 2$ to $f(X)$.
5. 5. Collect all heavy values with $C[i] > K$. Iterate over all pairs $(i, j)$ of heavy values and add $\min(C[i], C[j]) - K$ to $f(i \oplus j)$.
6. 6. Compute the final answer $\sum f(X) 10^X \pmod{998244353}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(K M 2^M + (N/K)^2) = O((N M 2^M)^{2/3})`
- **Space Complexity**: `O(2^M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

void fwht(vector<long long> &a) {
    int n = a.size();
    for (int step = 1; step < n; step *= 2) {
        for (int i = 0; i < n; i += 2 * step) {
            for (int j = i; j < i + step; ++j) {
                long long u = a[j];
                long long v = a[j + step];
                a[j] = u + v;
                a[j + step] = u - v;
            }
        }
    }
}

void ifwht(vector<long long> &a) {
    int n = a.size();
    for (int step = 1; step < n; step *= 2) {
        for (int i = 0; i < n; i += 2 * step) {
            for (int j = i; j < i + step; ++j) {
                long long u = a[j];
                long long v = a[j + step];
                a[j] = (u + v) / 2;
                a[j + step] = (u - v) / 2;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    int sz = 1 << M;
    vector<int> C(sz, 0);
    int max_c = 0;
    for (int i = 0; i < N; ++i) {
        int a;
        cin >> a;
        C[a]++;
        if (C[a] > max_c) max_c = C[a];
    }

    vector<long long> ans(sz, 0);
    long long pairs0 = 0;
    for (int c : C) pairs0 += c / 2;
    ans[0] = pairs0;

    int K = 20;
    int actual_K = min(K, max_c);

    vector<long long> sum_hat(sz, 0);
    vector<long long> S(sz);
    for (int x = 1; x <= actual_K; ++x) {
        for (int i = 0; i < sz; ++i) {
            S[i] = (C[i] >= x ? 1 : 0);
        }
        fwht(S);
        for (int i = 0; i < sz; ++i) {
            sum_hat[i] += S[i] * S[i];
        }
    }

    ifwht(sum_hat);
    for (int X = 1; X < sz; ++X) {
        ans[X] += sum_hat[X] / 2;
    }

    vector<int> heavy;
    for (int i = 0; i < sz; ++i) {
        if (C[i] > actual_K) heavy.push_back(i);
    }

    int num_h = heavy.size();
    for (int idx1 = 0; idx1 < num_h; ++idx1) {
        int i = heavy[idx1];
        for (int idx2 = idx1 + 1; idx2 < num_h; ++idx2) {
            int j = heavy[idx2];
            int X = i ^ j;
            ans[X] += min(C[i], C[j]) - actual_K;
        }
    }

    long long total = 0;
    long long p10 = 1;
    for (int X = 0; X < sz; ++X) {
        total = (total + (ans[X] % MOD) * p10) % MOD;
        p10 = (p10 * 10) % MOD;
    }

    cout << total << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
