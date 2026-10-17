# Problem Analysis: AtCoder-arc151_d — D. Binary Representations and Queries

**Problem ID**: `AtCoder-arc151_d`  
**Contest**: `arc151`  
**Rating / Difficulty**: 2282  
**URL**: https://atcoder.jp/contests/arc151/tasks/arc151_d  
**VJudge Tag**: `[problem:AtCoder-arc151_d]`  
**Category File**: [`../categories/math/fwht_tensor_product_independent_bit_transformations.md`](../categories/math/fwht_tensor_product_independent_bit_transformations.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Convolution`  
- **Topic (Skill)**: `Fast Walsh Hadamard Transform (FWHT) and its Variations`  

---

## 1. Problem Statement & Key Idea
Given an array of size $2^N$ and $Q$ operations of the form $(x_i, y_i)$ which add $A_u$ to $A_v$ for indices whose $x_i$-th bit differs, compute the final array modulo 998244353.

## 2. Core Observation & Invariant
Each query $(X_i, Y_i)$ applies an elementary $2 \times 2$ shear matrix along dimension $X_i$ on the $N$-dimensional hypercube. Transformations acting on distinct bit dimensions commute; matrix multiplication accumulates operations per bit $X$, which are then applied via the FWHT butterfly algorithm in $O(Q + N 2^N)$.

## 3. Step-by-Step Algorithm
1. 1. For a query $(X, Y)$, pairs of indices differing only at bit $X$ are updated independently: if $Y = 0$, $\begin{pmatrix} A_u \\ A_v \end{pmatrix} \gets \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} A_u \\ A_v \end{pmatrix}$; if $Y = 1$, $\begin{pmatrix} A_u \\ A_v \end{pmatrix} \gets \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} A_u \\ A_v \end{pmatrix}$.\n2. In the hypercube tensor product representation, a transformation on bit $X_1$ and a transformation on bit $X_2$ commute whenever $X_1 \ne X_2$. Thus, queries on each bit $X \in [0, N-1]$ can be aggregated independently.\n3. For each bit $X$, multiply the sequence of $2 \times 2$ matrices in order to obtain the net transformation matrix $M_X$.\n4. Apply each $M_X$ across all $2^{N-1}$ pairs using the Fast Walsh-Hadamard Transform (FWHT) / SOS-DP butterfly sweep. Total time complexity is $O(Q + N 2^N)$, executing in ~0.03s for $N = 18$.

## 4. Complexity Analysis
- **Time Complexity**: `O(Q + 2^N \log(2^N))`
- **Space Complexity**: `O(2^N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;

struct Mat2 {
    long long a, b, c, d;
};

Mat2 mul(const Mat2& m1, const Mat2& m2) {
    return {
        (m1.a * m2.a + m1.b * m2.c) % MOD,
        (m1.a * m2.b + m1.b * m2.d) % MOD,
        (m1.c * m2.a + m1.d * m2.c) % MOD,
        (m1.c * m2.b + m1.d * m2.d) % MOD
    };
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    int sz = 1 << n;
    vector<long long> a(sz);
    for (int i = 0; i < sz; i++) cin >> a[i];

    vector<Mat2> trans(n, {1, 0, 0, 1});

    for (int i = 0; i < q; i++) {
        int x, y;
        cin >> x >> y;
        Mat2 cur;
        if (y == 0) {
            cur = {1, 0, 1, 1};
        } else {
            cur = {1, 1, 0, 1};
        }
        trans[x] = mul(cur, trans[x]);
    }

    for (int bit = 0; bit < n; bit++) {
        Mat2 m = trans[bit];
        for (int mask = 0; mask < sz; mask++) {
            if (!(mask & (1 << bit))) {
                int u = mask;
                int v = mask | (1 << bit);
                long long au = a[u];
                long long av = a[v];
                a[u] = (m.a * au + m.b * av) % MOD;
                a[v] = (m.c * au + m.d * av) % MOD;
            }
        }
    }

    for (int i = 0; i < sz; i++) {
        cout << a[i] << (i == sz - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
